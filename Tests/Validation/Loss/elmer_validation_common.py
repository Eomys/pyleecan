from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from math import pi
from pathlib import Path

import numpy as np

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagElmer import MagElmer
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Functions.ParaView import launch_paraview, render_vtu_screenshot
from pyleecan.Functions.load import load


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SIMULATION_THREADS = 8


@dataclass(frozen=True)
class ElmerPointRequest:
    tag: str
    speed_rpm: float
    screenshot: bool = False


def to_builtin(value):
    if isinstance(value, dict):
        return {str(key): to_builtin(val) for key, val in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_builtin(val) for val in value]
    if isinstance(value, np.ndarray):
        return to_builtin(value.tolist())
    if isinstance(value, np.generic):
        return to_builtin(value.item())
    if isinstance(value, float):
        if not np.isfinite(value):
            return None
        return value
    if isinstance(value, Path):
        return str(value)
    return value


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def resolve_validation_machine_path(machine_path, baseline_summary):
    """Return the machine file that should be used for Elmer/FEMM comparisons.

    Validation summaries may reference a geometry snapshot that differs from the
    repository's canonical SimulationModels entry. When that snapshot exists, it
    is the authoritative machine definition for apples-to-apples replay of the
    stored FEMM baseline.
    """

    requested_path = Path(machine_path).resolve() if machine_path is not None else None

    baseline_machine = baseline_summary.get("machine_file")
    if baseline_machine:
        baseline_path = Path(baseline_machine)
        if baseline_path.exists():
            return baseline_path.resolve(), requested_path

    if requested_path is None:
        raise FileNotFoundError(
            "Validation machine path is missing and the baseline summary does not "
            "reference an existing machine snapshot."
        )

    return requested_path, requested_path


def save_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(to_builtin(payload), ensure_ascii=False, indent=2, allow_nan=False),
        encoding="utf-8",
    )
    return path


def write_csv(path, headers, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)
    return path


def load_npz_dict(path):
    with np.load(path, allow_pickle=True) as npz_file:
        return {key: npz_file[key] for key in npz_file.files}


def relative_to_repo(path):
    try:
        return str(Path(path).resolve().relative_to(REPO_ROOT))
    except Exception:
        return str(path)


def format_metric(value, fmt="{:.3f}"):
    if value is None:
        return "n/a"
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return str(value)
    if not np.isfinite(numeric):
        return "n/a"
    return fmt.format(numeric)


def format_percent(value):
    return format_metric(value, "{:.2f}%")


def markdown_table(headers, rows):
    table = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    table.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(table)


def percent_delta(model_value, reference_value):
    if reference_value in [None, 0]:
        return np.nan
    if not np.isfinite(model_value) or not np.isfinite(reference_value):
        return np.nan
    return (float(model_value) - float(reference_value)) / float(reference_value) * 100.0


def select_full_load_point(npz_dict, request):
    speed_vect = np.asarray(npz_dict["full_load__N0"], dtype=float)
    index = int(np.argmin(np.abs(speed_vect - float(request.speed_rpm))))

    return {
        "tag": request.tag,
        "speed_rpm": float(speed_vect[index]),
        "load_fraction": 1.0,
        "Id_ref_A": float(np.asarray(npz_dict["full_load__Id"], dtype=float)[index]),
        "Iq_ref_A": float(np.asarray(npz_dict["full_load__Iq"], dtype=float)[index]),
        "Tem_av_Nm": float(np.asarray(npz_dict["full_load__Tem_av"], dtype=float)[index]),
        "P_out_W": float(np.asarray(npz_dict["full_load__P_out"], dtype=float)[index]),
        "I_rms_A": float(np.asarray(npz_dict["full_load__I_rms"], dtype=float)[index]),
        "U_rms_V": float(np.asarray(npz_dict["full_load__U_rms"], dtype=float)[index]),
        "control_region": str(np.asarray(npz_dict["full_load_control_region"])[index]),
    }


def build_elmer_simu(
    machine,
    case_name,
    point,
    path_result,
    import_file="",
    nt_tot=12,
    na_tot=720,
    kmesh_fineness=1.0,
):
    return Simu1(
        name=f"{case_name}_{point['tag']}",
        machine=machine.copy(),
        path_result=str(path_result),
        input=InputCurrent(
            Nt_tot=int(nt_tot),
            Na_tot=int(na_tot),
            OP=OPdq(
                N0=float(point["speed_rpm"]),
                Id_ref=float(point["Id_ref_A"]),
                Iq_ref=float(point["Iq_ref_A"]),
            ),
            is_periodicity_t=True,
            is_periodicity_a=True,
        ),
        mag=MagElmer(
            is_periodicity_a=True,
            is_periodicity_t=False,
            nb_worker=DEFAULT_SIMULATION_THREADS,
            is_get_mesh=False,
            is_save_FEA=True,
            import_file=str(import_file),
            Kmesh_fineness=float(kmesh_fineness),
        ),
    )


def build_femm_simu(
    machine,
    case_name,
    point,
    path_result,
    nt_tot=12,
    na_tot=720,
):
    return Simu1(
        name=f"{case_name}_{point['tag']}_femm",
        machine=machine.copy(),
        path_result=str(path_result),
        input=InputCurrent(
            Nt_tot=int(nt_tot),
            Na_tot=int(na_tot),
            OP=OPdq(
                N0=float(point["speed_rpm"]),
                Id_ref=float(point["Id_ref_A"]),
                Iq_ref=float(point["Iq_ref_A"]),
            ),
            is_periodicity_t=True,
            is_periodicity_a=True,
        ),
        mag=MagFEMM(
            is_periodicity_a=True,
            is_periodicity_t=True,
            nb_worker=DEFAULT_SIMULATION_THREADS,
            is_get_meshsolution=False,
            is_fast_draw=True,
            is_calc_torque_energy=False,
        ),
    )


def summarize_elmer_output(output):
    torque = float(getattr(output.mag, "Tem_av", np.nan))
    speed_rpm = float(output.elec.OP.N0)
    u_rms = np.nan
    i_rms = np.nan

    try:
        u_rms = float(output.elec.OP.get_U0_UPhi0()["U0"])
    except Exception:
        pass

    try:
        i_rms = float(output.elec.OP.get_I0_Phi0()["I0"])
    except Exception:
        pass

    return {
        "speed_rpm": speed_rpm,
        "Tem_av_Nm": torque,
        "P_out_W": torque * 2.0 * pi * speed_rpm / 60.0,
        "I_rms_A": i_rms,
        "U_rms_V": u_rms,
        "path_result": str(output.get_path_result()),
        "elmer_mesh_dir": str(Path(output.get_path_result()) / "Elmer" / "ELMER_simulation"),
    }


def summarize_femm_output(output):
    torque = float(getattr(output.mag, "Tem_av", np.nan))
    speed_rpm = float(output.elec.OP.N0)
    u_rms = np.nan
    i_rms = np.nan

    try:
        u_rms = float(output.elec.OP.get_U0_UPhi0()["U0"])
    except Exception:
        pass

    try:
        i_rms = float(output.elec.OP.get_I0_Phi0()["I0"])
    except Exception:
        pass

    return {
        "speed_rpm": speed_rpm,
        "Tem_av_Nm": torque,
        "P_out_W": torque * 2.0 * pi * speed_rpm / 60.0,
        "I_rms_A": i_rms,
        "U_rms_V": u_rms,
        "path_result": str(output.get_path_result()),
    }


def compare_point(elmer_metrics, femm_metrics):
    return {
        "speed_delta_pct": percent_delta(
            elmer_metrics["speed_rpm"], femm_metrics["speed_rpm"]
        ),
        "torque_delta_pct": percent_delta(
            elmer_metrics["Tem_av_Nm"], femm_metrics["Tem_av_Nm"]
        ),
        "power_delta_pct": percent_delta(
            elmer_metrics["P_out_W"], femm_metrics["P_out_W"]
        ),
        "current_delta_pct": percent_delta(
            elmer_metrics["I_rms_A"], femm_metrics["I_rms_A"]
        ),
        "voltage_delta_pct": percent_delta(
            elmer_metrics["U_rms_V"], femm_metrics["U_rms_V"]
        ),
    }


def maybe_render_paraview(point_result, screenshot_path, open_gui=False):
    artifact = {
        "screenshot": None,
        "screenshot_error": None,
        "paraview_opened": False,
        "paraview_error": None,
    }
    elmer_mesh_dir = point_result["elmer"]["elmer_mesh_dir"]

    try:
        artifact["screenshot"] = str(
            render_vtu_screenshot(
                result_path=elmer_mesh_dir,
                array_name=None,
                output_path=screenshot_path,
            )
        )
    except Exception as error:
        artifact["screenshot_error"] = str(error)

    if open_gui:
        try:
            launch_paraview(elmer_mesh_dir)
            artifact["paraview_opened"] = True
        except Exception as error:
            artifact["paraview_error"] = str(error)

    return artifact


def build_point_rows(point_result_list):
    rows = []
    for point_result in point_result_list:
        femm = point_result["femm_baseline"]
        elmer = point_result["elmer"]
        cmp = point_result["compare_to_femm"]
        rows.append(
            [
                point_result["tag"],
                format_metric(femm["speed_rpm"], "{:.0f}"),
                femm["control_region"],
                format_metric(femm["Tem_av_Nm"]),
                format_metric(elmer["Tem_av_Nm"]),
                format_percent(cmp["torque_delta_pct"]),
                format_metric(femm["P_out_W"] * 1e-3),
                format_metric(elmer["P_out_W"] * 1e-3),
                format_percent(cmp["power_delta_pct"]),
                format_metric(femm["I_rms_A"]),
                format_metric(elmer["I_rms_A"]),
                format_metric(femm["U_rms_V"]),
                format_metric(elmer["U_rms_V"]),
            ]
        )
    return rows


def run_elmer_validation_case(
    *,
    case_name,
    machine_path,
    baseline_summary_path,
    baseline_npz_path,
    output_root,
    point_request_list,
    nt_tot=12,
    na_tot=720,
    kmesh_fineness=1.0,
    open_paraview_gui=False,
):
    output_root = Path(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    baseline_summary = load_json(baseline_summary_path)
    resolved_machine_path, requested_machine_path = resolve_validation_machine_path(
        machine_path,
        baseline_summary,
    )
    machine = load(str(resolved_machine_path))
    baseline_npz = load_npz_dict(baseline_npz_path)

    point_result_list = []
    reusable_msh = ""

    for index, request in enumerate(point_request_list):
        point_seed = select_full_load_point(baseline_npz, request)
        point_dir = output_root / "runs" / request.tag

        femm_output = build_femm_simu(
            machine=machine,
            case_name=case_name,
            point=point_seed,
            path_result=point_dir / "FEMM",
            nt_tot=nt_tot,
            na_tot=na_tot,
        ).run()
        femm_point = point_seed.copy()
        femm_metrics = summarize_femm_output(femm_output)
        for key, value in femm_metrics.items():
            if key in {"I_rms_A", "U_rms_V"} and not np.isfinite(value):
                continue
            femm_point[key] = value

        simu = build_elmer_simu(
            machine=machine,
            case_name=case_name,
            point=point_seed,
            path_result=point_dir,
            import_file=reusable_msh if index > 0 else "",
            nt_tot=nt_tot,
            na_tot=na_tot,
            kmesh_fineness=kmesh_fineness,
        )
        output = simu.run()
        elmer_metrics = summarize_elmer_output(output)

        if index == 0:
            reusable_msh = (
                Path(output.get_path_result()) / "Elmer" / "ELMER_simulation.msh"
            ).resolve()

        point_result = {
            "tag": request.tag,
            "point_seed": point_seed,
            "femm_baseline": femm_point,
            "elmer": elmer_metrics,
            "compare_to_femm": compare_point(elmer_metrics, femm_point),
            "artifacts": {},
        }

        if request.screenshot:
            point_result["artifacts"] = maybe_render_paraview(
                point_result,
                screenshot_path=output_root / "artifacts" / f"{case_name}_{request.tag}.png",
                open_gui=open_paraview_gui,
            )

        point_result_list.append(point_result)

    summary = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "case_name": case_name,
        "machine_file": str(resolved_machine_path),
        "requested_machine_file": (
            str(requested_machine_path) if requested_machine_path is not None else None
        ),
        "baseline_summary_file": str(Path(baseline_summary_path).resolve()),
        "baseline_npz_file": str(Path(baseline_npz_path).resolve()),
        "output_root": str(output_root.resolve()),
        "settings": {
            "nt_tot": int(nt_tot),
            "na_tot": int(na_tot),
            "kmesh_fineness": float(kmesh_fineness),
            "open_paraview_gui": bool(open_paraview_gui),
        },
        "reused_reference_msh": str(reusable_msh) if reusable_msh else None,
        "points": point_result_list,
    }

    csv_rows = []
    for point_result in point_result_list:
        femm = point_result["femm_baseline"]
        elmer = point_result["elmer"]
        cmp = point_result["compare_to_femm"]
        csv_rows.append(
            [
                point_result["tag"],
                femm["speed_rpm"],
                femm["control_region"],
                femm["Tem_av_Nm"],
                elmer["Tem_av_Nm"],
                cmp["torque_delta_pct"],
                femm["P_out_W"],
                elmer["P_out_W"],
                cmp["power_delta_pct"],
                femm["I_rms_A"],
                elmer["I_rms_A"],
                cmp["current_delta_pct"],
                femm["U_rms_V"],
                elmer["U_rms_V"],
                cmp["voltage_delta_pct"],
                relative_to_repo(elmer["path_result"]),
                relative_to_repo(point_result["artifacts"].get("screenshot")),
                point_result["artifacts"].get("screenshot_error"),
            ]
        )

    save_json(output_root / "summary.json", summary)
    write_csv(
        output_root / "point_comparison.csv",
        [
            "tag",
            "speed_rpm",
            "control_region",
            "femm_torque_Nm",
            "elmer_torque_Nm",
            "torque_delta_pct",
            "femm_power_W",
            "elmer_power_W",
            "power_delta_pct",
            "femm_current_A",
            "elmer_current_A",
            "current_delta_pct",
            "femm_voltage_V",
            "elmer_voltage_V",
            "voltage_delta_pct",
            "result_path",
            "screenshot_path",
            "screenshot_error",
        ],
        csv_rows,
    )

    return summary, baseline_summary
