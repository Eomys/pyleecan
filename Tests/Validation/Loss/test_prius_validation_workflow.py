from argparse import Namespace
import json
from os import name as os_name
from pathlib import Path

import numpy as np
import pytest

from Tests.Validation.Loss.prius_validation_preflight import (
    PriusValidationPreflightError,
    find_first_available_executable,
    require_executables,
    require_existing_files,
    require_python_modules,
)
from Tests.Validation.Loss.elmer_validation_common import save_json
from Tests.Validation.Loss.run_prius_efficiency_map import (
    build_prius_efficiency_map_simu,
    build_summary,
    validate_prius_efficiency_args,
)
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


def test_missing_required_files_message_is_actionable(tmp_path):
    missing_summary = tmp_path / "missing" / "summary.json"

    with pytest.raises(PriusValidationPreflightError) as error:
        require_existing_files(
            required_files={"Prius baseline summary": missing_summary},
            purpose="Prius validation",
            repo_root=tmp_path,
            recovery_steps=["Generate the Prius efficiency-map cache first."],
        )

    message = str(error.value)
    assert "Prius validation cannot start" in message
    assert "missing\\summary.json" in message or "missing/summary.json" in message
    assert "Generate the Prius efficiency-map cache first." in message


def test_python_module_preflight_reports_missing_module():
    with pytest.raises(PriusValidationPreflightError) as error:
        require_python_modules(
            module_names=["pyleecan_missing_prius_dependency"],
            purpose="Prius efficiency map",
            recovery_steps=["Install validation dependencies."],
        )

    message = str(error.value)
    assert "pyleecan_missing_prius_dependency" in message
    assert "Install validation dependencies." in message


def test_executable_preflight_reports_missing_solver(tmp_path):
    with pytest.raises(PriusValidationPreflightError) as error:
        require_executables(
            requirements=[
                (
                    "ElmerSolver executable",
                    ["pyleecan_missing_elmer_solver"],
                    [tmp_path / "missing" / "ElmerSolver.exe"],
                )
            ],
            purpose="Prius Elmer validation",
            recovery_steps=["Install Elmer or add it to PATH."],
        )

    message = str(error.value)
    assert "ElmerSolver executable" in message
    assert "Install Elmer or add it to PATH." in message


def test_executable_preflight_uses_elmer_home(monkeypatch, tmp_path):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    executable_name = "ElmerSolver.exe" if os_name == "nt" else "ElmerSolver"
    executable_path = bin_dir / executable_name
    executable_path.write_text("", encoding="utf-8")
    monkeypatch.setenv("ELMER_HOME", str(tmp_path))

    assert find_first_available_executable(["ElmerSolver"]) == executable_path


def test_elmer_summary_json_is_strict(tmp_path):
    summary_path = save_json(
        tmp_path / "summary.json",
        {
            "missing_voltage": np.nan,
            "nonfinite_array": np.array([1.0, np.inf, -np.inf]),
        },
    )

    raw_summary = summary_path.read_text(encoding="utf-8")
    assert "NaN" not in raw_summary
    assert "Infinity" not in raw_summary
    assert json.loads(raw_summary) == {
        "missing_voltage": None,
        "nonfinite_array": [1.0, None, None],
    }


def test_efficiency_map_summary_is_elmer_compatible(tmp_path):
    args = Namespace(
        output_root=tmp_path,
        speed_min=500.0,
        speed_max=6000.0,
        speed_count=2,
        load_min=0.1,
        load_max=1.0,
        load_count=2,
        nt_tot=80,
        lut_nt_tot=40,
        na_tot=720,
        n_id=5,
        n_iq=5,
        nb_worker=8,
        static_speed_rpm=1200.0,
        reference_power_kw=50.0,
        reference_torque_nm=400.0,
    )
    result = {
        "speed": np.array([1200.0, 2000.0]),
        "load": np.array([0.1, 1.0]),
        "base_speed_rpm": 2000.0,
        "cache_paths": {
            "npz_path": str(tmp_path / "eff_map.npz"),
            "json_path": str(tmp_path / "eff_map.json"),
        },
        "plot_paths": {"efficiency_map": str(tmp_path / "eff_map.png")},
        "full_load": {
            "N0": np.array([1200.0, 2000.0]),
            "Tem_av": np.array([410.0, 380.0]),
            "P_out": np.array([51_500.0, 79_600.0]),
        },
    }

    summary = build_summary(result, args, Path("machine.json"))

    static = summary["comparison"]["static_vs_published"]
    assert summary["results"]["efficiency_map"]["npz_path"].endswith("eff_map.npz")
    assert static["reference_power_kW"] == 50.0
    assert static["reference_torque_Nm"] == 400.0
    assert static["model_power_kW"] == pytest.approx(51.5)
    assert static["model_torque_Nm"] == pytest.approx(410.0)


def test_efficiency_map_summary_uses_nearest_finite_full_load_point(tmp_path):
    args = Namespace(
        output_root=tmp_path,
        speed_min=500.0,
        speed_max=6000.0,
        speed_count=2,
        load_min=0.1,
        load_max=1.0,
        load_count=2,
        nt_tot=16,
        lut_nt_tot=16,
        na_tot=64,
        n_id=2,
        n_iq=2,
        nb_worker=1,
        static_speed_rpm=1200.0,
        reference_power_kw=50.0,
        reference_torque_nm=400.0,
    )
    result = {
        "speed": np.array([500.0, 6000.0]),
        "load": np.array([0.1, 1.0]),
        "base_speed_rpm": np.nan,
        "cache_paths": {},
        "plot_paths": {},
        "full_load": {
            "N0": np.array([500.0, np.nan]),
            "Tem_av": np.array([120.0, np.nan]),
            "P_out": np.array([6_283.0, np.nan]),
        },
    }

    summary = build_summary(result, args, Path("machine.json"))
    static = summary["comparison"]["static_vs_published"]

    assert static["speed_rpm"] == pytest.approx(500.0)
    assert static["model_torque_Nm"] == pytest.approx(120.0)
    assert static["model_power_kW"] == pytest.approx(6.283)


def test_prius_efficiency_map_rejects_too_few_time_steps():
    args = Namespace(
        speed_count=2,
        load_count=2,
        n_id=2,
        n_iq=2,
        nt_tot=8,
        lut_nt_tot=16,
    )

    with pytest.raises(PriusValidationPreflightError) as error:
        validate_prius_efficiency_args(args)

    assert "at least 16" in str(error.value)


def test_prius_efficiency_map_loss_simu_keeps_meshsolution():
    machine = load(str(Path(DATA_DIR) / "Machine" / "Toyota_Prius.json"))
    args = Namespace(
        speed_min=500.0,
        nt_tot=8,
        lut_nt_tot=8,
        na_tot=16,
        urms_max=153.0,
        jrms_max=27e6,
        n_interp=20,
        n_id=2,
        n_iq=2,
        tsta=120.0,
        loss_tsta=100.0,
        nb_worker=1,
    )

    simu = build_prius_efficiency_map_simu(machine, args)

    assert simu.elec.LUT_simu.loss is not None
    assert simu.elec.LUT_simu.mag.is_get_meshsolution is True