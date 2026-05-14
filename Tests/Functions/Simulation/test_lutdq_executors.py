from importlib import import_module
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
import pytest

from pyleecan.Classes.ElecLUTdq import ElecLUTdq
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.LUT import LUT
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.OutElec import OutElec
from pyleecan.Classes.OutLoss import OutLoss
from pyleecan.Classes.OutLossModel import OutLossModel
from pyleecan.Classes.Output import Output
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.XOutput import XOutput
from pyleecan.Functions.Simulation.LUTdq import (
    LOSS_SERIES_KEYS,
    extract_control_surface,
    extract_loss_series,
    load_efficiency_map_cache,
    load_inductance_map_cache,
    run_drive_cycle_lut,
    run_efficiency_map_lut,
    run_inductance_map_lut,
    save_efficiency_map_cache,
    save_inductance_map_cache,
)
from pyleecan.Functions.Simulation.LUTdq.plot_efficiency_map import (
    _build_region_segments,
)
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


pytestmark = pytest.mark.star


def _build_test_simu():
    return Simu1(
        input=InputCurrent(OP=OPdq(N0=1000.0, Id_ref=0.0, Iq_ref=0.0)),
        elec=ElecLUTdq(Urms_max=300.0, Irms_max=200.0),
        var_simu=VarLoadCurrent(is_keep_all_output=True),
    )


def _fake_run(self):
    if self.elec.LUT_enforced is None:
        self.elec.LUT_enforced = LUT()

    outputs = []
    for op in self.var_simu.OP_matrix.get_OP_list():
        torque = op.Tem_av_ref
        if torque is None:
            torque = self.elec.load_rate * op.N0 * 0.01

        power_out = torque * 2 * np.pi * op.N0 / 60.0
        power_in = power_out / 0.9 if power_out != 0 else 0.0

        op_result = op.copy()
        op_result.efficiency = 0.9
        if op_result.Id_ref is None or op_result.Iq_ref is None:
            op_result.set_Id_Iq(0.0, torque / 10.0)
        if op_result.Ud_ref is None or op_result.Uq_ref is None:
            op_result.set_Ud_Uq(0.0, torque / 5.0)

        outputs.append(
            Output(
                elec=OutElec(
                    OP=op_result,
                    Tem_av=torque,
                    P_out=power_out,
                    P_in=power_in,
                )
            )
        )

    return XOutput(simu=self, output_list=outputs)


def _build_loss_outlossv(power_W, name):
    """Return an OutLossModel pre-loaded with a scalar value."""
    return OutLossModel(name=name, scalar_value=float(power_W))


def _fake_run_with_losses(self):
    """Variant of _fake_run that attaches a synthetic OutLoss to each step."""
    if self.elec.LUT_enforced is None:
        self.elec.LUT_enforced = LUT()

    outputs = []
    for op in self.var_simu.OP_matrix.get_OP_list():
        torque = op.Tem_av_ref
        if torque is None:
            torque = self.elec.load_rate * op.N0 * 0.01

        power_out = torque * 2 * np.pi * op.N0 / 60.0
        power_in = power_out / 0.9 if power_out != 0 else 0.0

        op_result = op.copy()
        op_result.efficiency = 0.9
        if op_result.Id_ref is None or op_result.Iq_ref is None:
            op_result.set_Id_Iq(0.0, torque / 10.0)
        if op_result.Ud_ref is None or op_result.Uq_ref is None:
            op_result.set_Ud_Uq(0.0, torque / 5.0)

        # Synthetic loss budget scaled by mechanical power.
        Pmech = abs(power_out)
        loss_dict = {
            "stator winding Joule": _build_loss_outlossv(
                0.02 * Pmech, "stator winding Joule"
            ),
            "rotor cage Joule": _build_loss_outlossv(0.01 * Pmech, "rotor cage Joule"),
            "stator core": _build_loss_outlossv(0.015 * Pmech, "stator core iron"),
            "rotor core": _build_loss_outlossv(0.005 * Pmech, "rotor core iron"),
            "magnet eddy": _build_loss_outlossv(0.003 * Pmech, "magnet eddy"),
            "mech friction": _build_loss_outlossv(0.002 * Pmech, "mech friction"),
            "stray": _build_loss_outlossv(0.001 * Pmech, "stray"),
        }

        outputs.append(
            Output(
                elec=OutElec(
                    OP=op_result,
                    Tem_av=torque,
                    P_out=power_out,
                    P_in=power_in,
                ),
                loss=OutLoss(loss_dict=loss_dict),
            )
        )

    return XOutput(simu=self, output_list=outputs)


class _FakeInductanceLUT(LUT):
    def __init__(self):
        super().__init__()

    def get_OP_array(self, *_args):
        id_axis = np.array([-20.0, 0.0, 20.0])
        iq_axis = np.array([-10.0, 0.0, 10.0])
        Id, Iq = np.meshgrid(id_axis, iq_axis)
        return np.column_stack(
            [
                np.full(Id.size, 1200.0),
                Id.ravel(),
                Iq.ravel(),
            ]
        )

    def interp_Phi_dqh(self, Id, Iq):
        Id = np.asarray(Id, dtype=float)
        Iq = np.asarray(Iq, dtype=float)
        return np.vstack(
            [
                0.6 + 0.01 * Id,
                0.02 * Iq,
                np.zeros_like(Id),
            ]
        )

    def get_Phi_dqh_mag_mean(self):
        return np.array([0.6, 0.0, 0.0])


class _AnalyticEfficiencyLUT(LUT):
    Id_axis = np.linspace(-140.0, 20.0, 7)
    Iq_axis = np.linspace(0.0, 150.0, 8)
    Phi_mag = 0.075
    Ld = 0.00032
    Lq = 0.00056

    def __init__(self, **kwargs):
        kwargs.setdefault("simu", Simu1(loss=None))
        super().__init__(**kwargs)

    def get_OP_array(self, *_args):
        Id, Iq = np.meshgrid(self.Id_axis, self.Iq_axis)
        return np.column_stack(
            [
                np.full(Id.size, 1000.0),
                Id.ravel(),
                Iq.ravel(),
            ]
        )

    def interp_Phi_dqh(self, Id, Iq):
        Id = np.asarray(Id, dtype=float)
        Iq = np.asarray(Iq, dtype=float)
        return (
            self.Phi_mag + self.Ld * Id,
            self.Lq * Iq,
            np.zeros_like(Id),
        )

    def get_Phi_dqh_mag_mean(self):
        return np.array([self.Phi_mag, 0.0, 0.0])

    def interp_Tem_rip_dqh(self, Id, Iq):
        return None


def _build_real_lutdq_simu():
    machine = load(str(Path(DATA_DIR) / "Machine" / "Toyota_Prius.json"))
    return Simu1(
        machine=machine,
        input=InputCurrent(
            OP=OPdq(N0=1000.0, Id_ref=0.0, Iq_ref=0.0),
            Nt_tot=16,
            Nrev=1,
        ),
        elec=ElecLUTdq(
            LUT_enforced=_AnalyticEfficiencyLUT(),
            Urms_max=220.0,
            Irms_max=150.0,
            n_Id=7,
            n_Iq=8,
            n_interp=48,
            type_skin_effect=0,
        ),
        var_simu=VarLoadCurrent(is_keep_all_output=True),
    )


def test_run_drive_cycle_lut_returns_summary(monkeypatch):
    monkeypatch.setattr(Simu1, "run", _fake_run)

    simu = _build_test_simu()
    trajectory = {
        "time": np.array([0.0, 1.0, 2.0]),
        "N0": np.array([1000.0, 1200.0, 800.0]),
        "Tem_av": np.array([10.0, -5.0, 15.0]),
    }

    result = run_drive_cycle_lut(simu, trajectory, target="torque")

    assert np.allclose(result["OP_matrix"].Tem_av_ref, trajectory["Tem_av"])
    assert result["summary"]["step_count"] == 3
    assert result["summary"]["eta_cycle"] == pytest.approx(0.9)
    assert result["summary"]["duration"] == 2.0


def test_run_drive_cycle_lut_integrates_m1_loss_breakdown(monkeypatch):
    monkeypatch.setattr(Simu1, "run", _fake_run_with_losses)

    simu = _build_test_simu()
    trajectory = {
        "time": np.array([0.0, 1.0, 2.0]),
        "N0": np.array([1000.0, 1000.0, 1000.0]),
        "Tem_av": np.array([10.0, 10.0, 10.0]),
    }

    result = run_drive_cycle_lut(simu, trajectory, target="torque")
    summary = result["summary"]
    Pmech = abs(summary["P_out"][0])

    assert np.allclose(summary["P_loss_total"], 0.056 * Pmech)
    assert summary["energy_loss_J"] == pytest.approx(2.0 * 0.056 * Pmech)
    assert summary["energy_loss_breakdown_J"]["P_jl"] == pytest.approx(
        2.0 * 0.03 * Pmech
    )
    assert summary["energy_loss_breakdown_J"]["P_fe"] == pytest.approx(
        2.0 * 0.02 * Pmech
    )
    assert summary["energy_loss_breakdown_J"]["P_mag"] == pytest.approx(
        2.0 * 0.003 * Pmech
    )


def test_lut_default_simulation_uses_eight_femm_workers():
    machine = load(str(Path(DATA_DIR) / "Machine" / "Toyota_Prius.json"))
    lut = LUT()

    lut.set_default_simulation(machine)

    assert lut.simu.mag.nb_worker == 8


def test_run_efficiency_map_lut_builds_torque_grid(monkeypatch):
    monkeypatch.setattr(Simu1, "run", _fake_run)

    simu = _build_test_simu()
    result = run_efficiency_map_lut(
        simu,
        speed_vect=np.array([1000.0, 2000.0]),
        load_vect=np.array([0.25, 1.0]),
    )

    assert np.allclose(result["Tem_max"], [10.0, 20.0])
    assert np.allclose(result["Tem_av_ref"], [[2.5, 10.0], [5.0, 20.0]])
    assert np.allclose(result["Tem_av"], result["Tem_av_ref"])
    assert np.allclose(result["efficiency"], 0.9)


def test_run_efficiency_map_lut_reports_mtpv_region(monkeypatch):
    monkeypatch.setattr(Simu1, "run", _fake_run)

    simu = _build_test_simu()
    simu.elec.Urms_max = 3.0
    simu.elec.Irms_max = 100.0
    result = run_efficiency_map_lut(
        simu,
        speed_vect=np.array([1000.0, 2000.0]),
        load_vect=np.array([0.5, 1.0]),
    )

    assert result["full_load_control_region"].tolist() == ["MTPA", "MTPV"]
    assert result["base_speed_rpm"] == pytest.approx(2000.0)
    assert result["control_region"][1, 1] == "MTPV"
    assert result["control_region_code"][1, 1] == 2


def test_run_efficiency_map_lut_reports_fw_region(monkeypatch):
    monkeypatch.setattr(Simu1, "run", _fake_run)

    simu = _build_test_simu()
    simu.elec.Urms_max = 3.0
    simu.elec.Irms_max = 2.0
    result = run_efficiency_map_lut(
        simu,
        speed_vect=np.array([1000.0, 2000.0]),
        load_vect=np.array([0.5, 1.0]),
    )

    assert result["full_load_control_region"].tolist() == ["MTPA", "FW"]
    assert result["control_region"][1, 1] == "FW"
    assert result["control_region_code"][1, 1] == 1


def test_save_and_load_efficiency_map_cache(monkeypatch, tmp_path):
    monkeypatch.setattr(Simu1, "run", _fake_run)

    simu = _build_test_simu()
    result = run_efficiency_map_lut(
        simu,
        speed_vect=np.array([1000.0, 2000.0]),
        load_vect=np.array([0.25, 1.0]),
    )

    cache_paths = save_efficiency_map_cache(result, str(tmp_path / "eff_map"))
    loaded = load_efficiency_map_cache(cache_paths["npz_path"])

    assert Path(cache_paths["npz_path"]).is_file()
    assert Path(cache_paths["json_path"]).is_file()
    assert np.allclose(loaded["Tem_av"], result["Tem_av"])
    assert np.allclose(loaded["efficiency"], result["efficiency"])
    assert np.allclose(loaded["full_load"]["Tem_av"], result["full_load"]["Tem_av"])


def test_run_inductance_map_lut_returns_ld_lq_maps():
    simu = _build_test_simu()
    simu.elec.LUT_enforced = _FakeInductanceLUT()

    result = run_inductance_map_lut(simu, n_Id_interp=3, n_Iq_interp=3)

    assert result["speed_rpm"] == pytest.approx(1200.0)
    assert result["Ld"].shape == (3, 3)
    assert result["Lq"].shape == (3, 3)
    assert np.allclose(result["Ld"][result["Id_grid"] != 0], 0.01)
    assert np.allclose(result["Lq"][result["Iq_grid"] != 0], 0.02)


def test_save_and_load_inductance_map_cache(tmp_path):
    simu = _build_test_simu()
    simu.elec.LUT_enforced = _FakeInductanceLUT()
    result = run_inductance_map_lut(simu, n_Id_interp=3, n_Iq_interp=3)

    cache_paths = save_inductance_map_cache(result, str(tmp_path / "inductance_map"))
    loaded = load_inductance_map_cache(cache_paths["npz_path"])

    assert Path(cache_paths["npz_path"]).is_file()
    assert Path(cache_paths["json_path"]).is_file()
    assert np.allclose(loaded["Ld"], result["Ld"], equal_nan=True)
    assert np.allclose(loaded["Lq"], result["Lq"], equal_nan=True)


def test_run_efficiency_map_lut_writes_cache_and_plot_outputs(monkeypatch, tmp_path):
    monkeypatch.setattr(Simu1, "run", _fake_run)

    def _fake_plot_efficiency_map(
        _result, save_dir, file_prefix="efficiency_map", **_kwargs
    ):
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)
        paths = {
            "efficiency_map": save_dir / f"{file_prefix}_efficiency_map.png",
            "torque_envelope": save_dir / f"{file_prefix}_torque_envelope.png",
        }
        for path in paths.values():
            path.write_text("plot", encoding="utf-8")
        return {key: str(value) for key, value in paths.items()}

    plot_module = import_module(
        "pyleecan.Functions.Simulation.LUTdq.plot_efficiency_map"
    )

    monkeypatch.setattr(plot_module, "plot_efficiency_map", _fake_plot_efficiency_map)

    simu = _build_test_simu()
    result = run_efficiency_map_lut(
        simu,
        speed_vect=np.array([1000.0, 2000.0]),
        load_vect=np.array([0.25, 1.0]),
        cache_path=str(tmp_path / "cache" / "efficiency_map"),
        plot_dir=str(tmp_path / "plots"),
        file_prefix="toyota_prius",
    )

    assert Path(result["cache_paths"]["npz_path"]).is_file()
    assert Path(result["cache_paths"]["json_path"]).is_file()
    assert Path(result["plot_paths"]["efficiency_map"]).is_file()
    assert Path(result["plot_paths"]["torque_envelope"]).is_file()


def test_run_efficiency_map_lut_real_varload_cache_and_plots(tmp_path):
    simu = _build_real_lutdq_simu()
    result = run_efficiency_map_lut(
        simu,
        speed_vect=np.array([800.0, 1800.0, 3200.0]),
        load_vect=np.array([0.5, 1.0]),
        cache_path=str(tmp_path / "cache" / "analytic_efficiency_map"),
        plot_dir=str(tmp_path / "plots"),
        file_prefix="analytic",
    )

    assert result["Tem_av"].shape == (3, 2)
    assert result["efficiency"].shape == (3, 2)
    assert np.all(np.isfinite(result["Tem_av"]))
    assert np.all(np.isfinite(result["efficiency"]))
    assert result["xoutput"].output_list is not None
    assert len(result["xoutput"].output_list) == result["OP_matrix"].get_N_OP()
    assert Path(result["cache_paths"]["npz_path"]).is_file()
    assert Path(result["cache_paths"]["json_path"]).is_file()
    assert Path(result["plot_paths"]["efficiency_map"]).is_file()
    assert Path(result["plot_paths"]["control_region_map"]).is_file()


def test_lutdq_efficiency_map_demo_script_smoke(tmp_path):
    project_root = Path(__file__).resolve().parents[3]
    script_path = project_root / "Tutorials" / "run_lutdq_efficiency_map_demo.py"
    output_dir = tmp_path / "demo"

    completed = subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--output-dir",
            str(output_dir),
            "--speed-count",
            "3",
            "--load-count",
            "2",
            "--file-prefix",
            "smoke",
        ],
        cwd=str(project_root),
        capture_output=True,
        text=True,
        check=True,
        timeout=120,
    )

    summary_path = output_dir / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert "LUTdq efficiency-map demo complete" in completed.stdout
    assert (output_dir / "smoke.npz").is_file()
    assert (output_dir / "smoke.json").is_file()
    assert (output_dir / "smoke_efficiency_map.png").is_file()
    assert (output_dir / "smoke_control_region_map.png").is_file()
    assert summary["speed_count"] == 3
    assert summary["load_count"] == 2
    assert summary["max_efficiency"] is not None


def test_build_region_segments_keeps_single_point_transitions_visible():
    speed = np.array([300.0, 600.0, 1200.0, 1540.0, 1750.0, 2500.0])
    values = np.array([40.0, 55.0, 78.0, 94.0, 102.0, 93.0])
    regions = np.array(["MTPA", "MTPA", "MTPA", "MTPA", "FW", "MTPV"])

    segments = _build_region_segments(speed, values, regions)

    assert len(segments["MTPA"]) == 1
    assert len(segments["FW"]) == 1
    assert len(segments["MTPV"]) == 1
    assert np.allclose(segments["MTPA"][0][0], np.array([300.0, 600.0, 1200.0, 1540.0]))
    assert np.allclose(segments["FW"][0][0], np.array([1750.0]))
    assert np.allclose(segments["FW"][0][1], np.array([102.0]))
    assert np.allclose(segments["MTPV"][0][0], np.array([2500.0]))


# ---------------------------------------------------------------------------
# M1 — LUT loss aggregation regression (perf-roadmap-phase1)
# ---------------------------------------------------------------------------


def test_extract_loss_series_returns_canonical_buckets():
    from pyleecan.Classes.OPMatrix import OPMatrix

    monkeypatched_simu = _build_test_simu()
    monkeypatched_simu.var_simu.set_OP_array(
        OPMatrix(N0=np.array([1000.0]), col_names=["N0"]),
        is_update_input=True,
        input_index=0,
    )
    xoutput = _fake_run_with_losses(monkeypatched_simu)

    series = extract_loss_series(xoutput)

    for key in LOSS_SERIES_KEYS:
        assert key in series
        assert series[key].shape == (1,)

    # Synthetic budget: Pmech is the mechanical power for the single OP.
    Pmech = abs(xoutput.output_list[0].elec.P_out)
    assert series["P_jl_s"][0] == pytest.approx(0.02 * Pmech)
    assert series["P_jl_r"][0] == pytest.approx(0.01 * Pmech)
    assert series["P_jl"][0] == pytest.approx(0.03 * Pmech)
    assert series["P_fe_s"][0] == pytest.approx(0.015 * Pmech)
    assert series["P_fe_r"][0] == pytest.approx(0.005 * Pmech)
    assert series["P_fe"][0] == pytest.approx(0.02 * Pmech)
    assert series["P_mag"][0] == pytest.approx(0.003 * Pmech)
    assert series["P_mech"][0] == pytest.approx(0.002 * Pmech)
    assert series["P_loss_other"][0] == pytest.approx(0.001 * Pmech)
    assert series["P_loss_total"][0] == pytest.approx(
        (0.02 + 0.01 + 0.015 + 0.005 + 0.003 + 0.002 + 0.001) * Pmech
    )


def test_extract_loss_series_returns_nan_without_outloss():
    from pyleecan.Classes.OPMatrix import OPMatrix

    monkeypatched_simu = _build_test_simu()
    monkeypatched_simu.var_simu.set_OP_array(
        OPMatrix(N0=np.array([1000.0]), col_names=["N0"]),
        is_update_input=True,
        input_index=0,
    )
    xoutput = _fake_run(monkeypatched_simu)

    series = extract_loss_series(xoutput)
    for key in LOSS_SERIES_KEYS:
        assert np.all(np.isnan(series[key]))


def test_run_efficiency_map_lut_emits_loss_maps(monkeypatch):
    monkeypatch.setattr(Simu1, "run", _fake_run_with_losses)

    simu = _build_test_simu()
    speeds = np.array([1000.0, 2000.0])
    loads = np.array([0.5, 1.0])
    result = run_efficiency_map_lut(simu, speed_vect=speeds, load_vect=loads)

    assert "loss_maps" in result
    for key in ("P_jl", "P_fe", "P_mag", "P_mech", "P_loss_total"):
        assert key in result["loss_maps"]
        assert result["loss_maps"][key].shape == (speeds.size, loads.size)
        assert np.all(np.isfinite(result["loss_maps"][key]))
        # Top-level alias must mirror loss_maps payload.
        assert np.array_equal(result[key], result["loss_maps"][key])

    # Loss budget must be strictly positive for non-zero torque cells.
    assert np.all(result["P_loss_total"] > 0)
    # Stator + rotor parts must sum to the aggregated bucket.
    assert np.allclose(
        result["loss_maps"]["P_jl"],
        result["loss_maps"]["P_jl_s"] + result["loss_maps"]["P_jl_r"],
    )
    assert np.allclose(
        result["loss_maps"]["P_fe"],
        result["loss_maps"]["P_fe_s"] + result["loss_maps"]["P_fe_r"],
    )


def test_run_efficiency_map_lut_skips_loss_maps_without_outloss(monkeypatch):
    monkeypatch.setattr(Simu1, "run", _fake_run)

    simu = _build_test_simu()
    result = run_efficiency_map_lut(
        simu,
        speed_vect=np.array([1000.0, 2000.0]),
        load_vect=np.array([0.5, 1.0]),
    )

    assert "loss_maps" not in result
    for key in LOSS_SERIES_KEYS:
        assert key not in result


# ---------------------------------------------------------------------------
# M2 — LUT control-surface extraction (perf-roadmap-phase1)
# ---------------------------------------------------------------------------


def _build_control_surface_fixture():
    speed = np.array([1000.0, 3000.0])
    load = np.array([0.25, 0.50, 1.00])
    N0 = speed[:, None] * np.ones((1, load.size))
    load_grid = np.ones((speed.size, 1)) * load[None, :]
    Tem_av = np.array(
        [
            [20.0, 42.0, 72.0],
            [18.0, 48.0, 70.0],
        ]
    )
    I_rms = np.array(
        [
            [40.0, 70.0, 140.0],
            [32.0, 82.0, 132.0],
        ]
    )
    U_rms = np.array(
        [
            [60.0, 150.0, 294.0],
            [120.0, 292.0, 298.0],
        ]
    )
    control_region = np.array(
        [
            ["MTPA", "MTPA", "FW"],
            ["MTPA", "FW", "MTPV"],
        ]
    )

    return {
        "speed": speed,
        "load": load,
        "N0": N0,
        "load_grid": load_grid,
        "Tem_av": Tem_av,
        "Id": -0.2 * I_rms,
        "Iq": 0.98 * I_rms,
        "I_rms": I_rms,
        "Ud": np.zeros_like(U_rms),
        "Uq": U_rms,
        "U_rms": U_rms,
        "efficiency": np.array([[0.88, 0.91, 0.89], [0.86, 0.90, 0.87]]),
        "P_loss_total": np.array([[120.0, 140.0, 260.0], [110.0, 180.0, 330.0]]),
        "P_jl": np.array([[60.0, 70.0, 120.0], [50.0, 88.0, 150.0]]),
        "control_region": control_region,
        "voltage_limited_mask": U_rms >= 0.98 * 300.0,
        "current_limited_mask": I_rms >= 0.98 * 150.0,
        "base_speed_rpm": 3000.0,
    }


def test_extract_control_surface_selects_mtpa_mtpv_and_fw_boundary():
    result = _build_control_surface_fixture()

    surface = extract_control_surface(result, Irms_max=150.0, Urms_max=300.0)

    assert np.array_equal(
        surface["control_region_code"], np.array([[0, 0, 1], [0, 1, 2]])
    )
    assert surface["base_speed_rpm"] == pytest.approx(3000.0)

    # MTPA maximizes Tem / Irms within MTPA cells for each speed row.
    assert np.array_equal(surface["mtpa"]["index"], np.array([1, 0]))
    assert np.allclose(surface["mtpa"]["Tem_av"], np.array([42.0, 18.0]))
    assert np.allclose(surface["mtpa"]["P_loss_total"], np.array([140.0, 110.0]))

    # MTPV only exists on the second speed row in this fixture.
    assert np.array_equal(surface["mtpv"]["index"], np.array([-1, 2]))
    assert np.isnan(surface["mtpv"]["Tem_av"][0])
    assert surface["mtpv"]["Tem_av"][1] == pytest.approx(70.0)
    assert surface["mtpv"]["control_region"][1] == "MTPV"

    # Field weakening starts at the first voltage-limited or non-MTPA point.
    assert np.array_equal(surface["fw_boundary"]["index"], np.array([2, 1]))
    assert np.allclose(surface["fw_boundary"]["load"], np.array([1.0, 0.5]))
    assert np.allclose(
        surface["fw_boundary"]["voltage_margin"],
        np.array([(300.0 - 294.0) / 300.0, (300.0 - 292.0) / 300.0]),
    )


def test_extract_control_surface_uses_nested_loss_maps():
    result = _build_control_surface_fixture()
    result["loss_maps"] = {"P_loss_total": result.pop("P_loss_total")}

    surface = extract_control_surface(result, Irms_max=150.0, Urms_max=300.0)

    assert np.allclose(surface["mtpa"]["P_loss_total"], np.array([140.0, 110.0]))
    assert np.allclose(
        surface["fw_boundary"]["loss_per_torque"],
        np.array([260.0 / 72.0, 180.0 / 48.0]),
    )


def test_extract_control_surface_raises_on_missing_required_map():
    result = _build_control_surface_fixture()
    result.pop("Tem_av")

    with pytest.raises(KeyError, match="Tem_av"):
        extract_control_surface(result)
