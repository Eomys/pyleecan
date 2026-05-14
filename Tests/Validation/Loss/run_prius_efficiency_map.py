from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Tests.Validation.Loss.prius_validation_preflight import (
    PriusValidationPreflightError,
    find_first_available_executable,
    require_existing_files,
    require_python_modules,
)


CASE_NAME = "prius2004_full_validation"
MACHINE_PATH = (
    REPO_ROOT / "SimulationModels" / "Toyota_Prius_2004" / "IPMSM_Toyota_Prius_2004.json"
)
OUTPUT_ROOT = REPO_ROOT / ".local" / "verification" / CASE_NAME
CACHE_ROOT = OUTPUT_ROOT / "results" / "efficiency_map" / "prius2004_loss_efficiency_map"
PLOT_DIR = OUTPUT_ROOT / "plots"
SUMMARY_PATH = OUTPUT_ROOT / "summary.json"

REQUIRED_MODULES = ["SciDataTool", "gmsh", "femm"]
KNOWN_FEMM_PATHS = [
    Path("C:/femm42/bin/femm.exe"),
    Path("C:/Program Files/femm42/bin/femm.exe"),
    Path("C:/Program Files (x86)/femm42/bin/femm.exe"),
]


def require_prius_efficiency_map_runtime(machine_path, check_femm=True):
    """Validate local inputs before launching a long FEMM-backed map run."""

    require_existing_files(
        required_files={"Prius machine model": machine_path},
        purpose="Toyota Prius 2004 efficiency-map validation",
        repo_root=REPO_ROOT,
        recovery_steps=[
            "Restore SimulationModels\\Toyota_Prius_2004\\IPMSM_Toyota_Prius_2004.json before running the validation.",
        ],
    )
    require_python_modules(
        module_names=REQUIRED_MODULES,
        purpose="Toyota Prius 2004 efficiency-map validation",
        recovery_steps=[
            "Run python -m pip install -e \".[test]\" or use the prepared .local\\envs\\Exenv interpreter.",
            "The default conda/base interpreter may not contain the optional FEMM/Gmsh validation stack.",
        ],
    )

    if check_femm and find_first_available_executable(["femm"], KNOWN_FEMM_PATHS) is None:
        raise PriusValidationPreflightError(
            "Toyota Prius 2004 efficiency-map validation cannot start because FEMM was not found.\n"
            "Recovery steps:\n"
            "- Install FEMM, or add femm.exe to PATH.\n"
            "- On Windows the expected local path is C:\\femm42\\bin\\femm.exe."
        )


def build_prius_efficiency_map_simu(machine, args):
    """Create the FEMM-backed LUT workflow used for Prius efficiency maps."""

    from pyleecan.Classes.ElecLUTdq import ElecLUTdq
    from pyleecan.Classes.InputCurrent import InputCurrent
    from pyleecan.Classes.Loss import Loss
    from pyleecan.Classes.LossModelJoule import LossModelJoule
    from pyleecan.Classes.LossModelMagnet import LossModelMagnet
    from pyleecan.Classes.LossModelProximity import LossModelProximity
    from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
    from pyleecan.Classes.MagFEMM import MagFEMM
    from pyleecan.Classes.OPdq import OPdq
    from pyleecan.Classes.Simu1 import Simu1
    from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent

    return Simu1(
        name=CASE_NAME,
        machine=machine,
        input=InputCurrent(
            OP=OPdq(N0=float(args.speed_min), Id_ref=0, Iq_ref=0),
            Nt_tot=int(args.nt_tot),
            Na_tot=int(args.na_tot),
            is_periodicity_a=True,
            is_periodicity_t=True,
        ),
        elec=ElecLUTdq(
            Urms_max=float(args.urms_max),
            Jrms_max=float(args.jrms_max),
            n_interp=int(args.n_interp),
            n_Id=int(args.n_id),
            n_Iq=int(args.n_iq),
            Id_max=0,
            Iq_min=0,
            is_grid_dq=True,
            Tsta=float(args.tsta),
            type_skin_effect=1,
            LUT_simu=Simu1(
                input=InputCurrent(
                    OP=OPdq(),
                    Nt_tot=int(args.lut_nt_tot),
                    Na_tot=int(args.na_tot),
                    is_periodicity_a=True,
                    is_periodicity_t=True,
                ),
                var_simu=VarLoadCurrent(is_keep_all_output=True),
                mag=MagFEMM(
                    is_periodicity_a=True,
                    is_periodicity_t=True,
                    nb_worker=int(args.nb_worker),
                    is_get_meshsolution=True,
                    is_fast_draw=True,
                    is_calc_torque_energy=False,
                ),
                loss=Loss(
                    is_get_meshsolution=False,
                    Tsta=float(args.loss_tsta),
                    model_dict={
                        "stator core": LossModelSteinmetz(group="stator core"),
                        "rotor core": LossModelSteinmetz(group="rotor core"),
                        "joule": LossModelJoule(group="stator winding"),
                        "proximity": LossModelProximity(group="stator winding"),
                        "magnets": LossModelMagnet(group="rotor magnets"),
                    },
                ),
            ),
        ),
        var_simu=VarLoadCurrent(is_keep_all_output=True),
    )


def _finite_float(value):
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return None
    return numeric if np.isfinite(numeric) else None


def _nearest_finite_index(values, target):
    values = np.asarray(values, dtype=float)
    finite_index = np.where(np.isfinite(values))[0]
    if finite_index.size == 0:
        return None
    nearest = int(np.argmin(np.abs(values[finite_index] - float(target))))
    return int(finite_index[nearest])


def validate_prius_efficiency_args(args):
    """Validate command-line sampling options before launching FEMM."""

    if args.speed_count < 2:
        raise PriusValidationPreflightError("speed-count must be at least 2")
    if args.load_count < 2:
        raise PriusValidationPreflightError("load-count must be at least 2")
    if args.n_id < 2 or args.n_iq < 2:
        raise PriusValidationPreflightError("n-id and n-iq must be at least 2")
    if args.nt_tot < 16 or args.lut_nt_tot < 16:
        raise PriusValidationPreflightError(
            "Toyota Prius 2004 efficiency-map validation requires nt-tot and "
            "lut-nt-tot to be at least 16. Lower values can collapse the "
            "periodic time axis to one sample and make loss post-processing fail."
        )


def build_summary(result, args, machine_path):
    """Build an Elmer-compatible summary for the generated efficiency map."""

    cache_paths = result.get("cache_paths", {})
    plot_paths = result.get("plot_paths", {})
    full_load = result.get("full_load", {})
    full_load_speed = np.asarray(full_load.get("N0", result["speed"]), dtype=float)
    static_index = _nearest_finite_index(full_load_speed, args.static_speed_rpm)
    if static_index is None:
        fallback_speed = np.asarray(result["speed"], dtype=float)
        static_index = _nearest_finite_index(fallback_speed, args.static_speed_rpm)
        full_load_speed = fallback_speed

    speed_rpm = None if static_index is None else _finite_float(full_load_speed[static_index])
    model_torque = (
        None if static_index is None else _finite_float(np.asarray(full_load["Tem_av"])[static_index])
    )
    model_power = (
        None
        if static_index is None
        else _finite_float(np.asarray(full_load["P_out"])[static_index] * 1e-3)
    )
    reference_power = float(args.reference_power_kw)
    reference_torque = float(args.reference_torque_nm)

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "case_name": CASE_NAME,
        "machine_file": str(Path(machine_path).resolve()),
        "output_root": str(Path(args.output_root).resolve()),
        "settings": {
            "speed_min": float(args.speed_min),
            "speed_max": float(args.speed_max),
            "speed_count": int(args.speed_count),
            "load_min": float(args.load_min),
            "load_max": float(args.load_max),
            "load_count": int(args.load_count),
            "nt_tot": int(args.nt_tot),
            "lut_nt_tot": int(args.lut_nt_tot),
            "na_tot": int(args.na_tot),
            "n_Id": int(args.n_id),
            "n_Iq": int(args.n_iq),
            "nb_worker": int(args.nb_worker),
        },
        "results": {
            "efficiency_map": {
                "npz_path": cache_paths.get("npz_path"),
                "json_path": cache_paths.get("json_path"),
                "plot_paths": plot_paths,
                "base_speed_rpm": _finite_float(result.get("base_speed_rpm")),
                "speed_count": int(np.asarray(result["speed"]).size),
                "load_count": int(np.asarray(result["load"]).size),
            }
        },
        "comparison": {
            "static_vs_published": {
                "requested_speed_rpm": float(args.static_speed_rpm),
                "speed_rpm": speed_rpm,
                "reference_power_kW": reference_power,
                "reference_torque_Nm": reference_torque,
                "model_power_kW": model_power,
                "model_torque_Nm": model_torque,
                "power_delta_pct": (
                    None
                    if model_power is None or reference_power == 0
                    else (model_power - reference_power) / reference_power * 100.0
                ),
                "torque_delta_pct": (
                    None
                    if model_torque is None or reference_torque == 0
                    else (model_torque - reference_torque) / reference_torque * 100.0
                ),
            }
        },
    }


def save_summary(summary, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False),
        encoding="utf-8",
    )
    return path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a Toyota Prius 2004 FEMM-backed LUT efficiency map"
    )
    parser.add_argument("--machine-path", type=Path, default=MACHINE_PATH)
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    parser.add_argument("--cache-root", type=Path, default=CACHE_ROOT)
    parser.add_argument("--plot-dir", type=Path, default=PLOT_DIR)
    parser.add_argument("--check-inputs", action="store_true")
    parser.add_argument("--skip-femm-check", action="store_true")
    parser.add_argument("--speed-min", type=float, default=500.0)
    parser.add_argument("--speed-max", type=float, default=6000.0)
    parser.add_argument("--speed-count", type=int, default=30)
    parser.add_argument("--load-min", type=float, default=0.1)
    parser.add_argument("--load-max", type=float, default=1.0)
    parser.add_argument("--load-count", type=int, default=7)
    parser.add_argument("--nt-tot", type=int, default=80)
    parser.add_argument("--lut-nt-tot", type=int, default=40)
    parser.add_argument("--na-tot", type=int, default=1600)
    parser.add_argument("--n-id", type=int, default=5)
    parser.add_argument("--n-iq", type=int, default=5)
    parser.add_argument("--n-interp", type=int, default=100)
    parser.add_argument("--nb-worker", type=int, default=8)
    parser.add_argument("--urms-max", type=float, default=153.0)
    parser.add_argument("--jrms-max", type=float, default=27e6)
    parser.add_argument("--tsta", type=float, default=120.0)
    parser.add_argument("--loss-tsta", type=float, default=100.0)
    parser.add_argument("--static-speed-rpm", type=float, default=1200.0)
    parser.add_argument("--reference-power-kw", type=float, default=50.0)
    parser.add_argument("--reference-torque-nm", type=float, default=400.0)
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        validate_prius_efficiency_args(args)
        require_prius_efficiency_map_runtime(
            args.machine_path,
            check_femm=not args.skip_femm_check,
        )
    except PriusValidationPreflightError as error:
        raise SystemExit(str(error))

    if args.check_inputs:
        print("Prius efficiency-map validation inputs are available.")
        return

    from pyleecan.Functions.load import load
    from pyleecan.Functions.Simulation.LUTdq import run_efficiency_map_lut

    machine = load(str(args.machine_path))
    simu = build_prius_efficiency_map_simu(machine, args)
    speed_vect = np.linspace(args.speed_min, args.speed_max, args.speed_count)
    load_vect = np.linspace(args.load_min, args.load_max, args.load_count)

    result = run_efficiency_map_lut(
        simu,
        speed_vect=speed_vect,
        load_vect=load_vect,
        cache_path=str(args.cache_root),
        plot_dir=str(args.plot_dir),
        file_prefix=Path(args.cache_root).name,
        is_show_fig=False,
    )
    args.output_root.mkdir(parents=True, exist_ok=True)
    summary = build_summary(result, args, args.machine_path)
    summary_path = save_summary(summary, args.output_root / "summary.json")

    print("Wrote Prius efficiency-map summary to " + str(summary_path))
    print("Wrote Prius efficiency-map cache to " + result["cache_paths"]["npz_path"])


if __name__ == "__main__":
    main()