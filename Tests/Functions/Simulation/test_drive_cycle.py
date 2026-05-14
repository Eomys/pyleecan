from pathlib import Path

import numpy as np
import pytest

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.OutElec import OutElec
from pyleecan.Classes.OutLoss import OutLoss
from pyleecan.Classes.OutLossModel import OutLossModel
from pyleecan.Classes.Output import Output
from pyleecan.Classes.XOutput import XOutput
from pyleecan.Functions.Simulation.DriveCycle import (
    build_drive_cycle_op_matrix,
    list_standard_drive_cycles,
    read_drive_cycle_csv,
    read_standard_drive_cycle,
    summarize_drive_cycle_outputs,
)
from pyleecan.definitions import DATA_DIR


def test_read_drive_cycle_csv_and_build_torque_op_matrix(tmp_path):
    csv_path = Path(tmp_path) / "drive_cycle.csv"
    csv_path.write_text(
        "time_s,speed_rpm,torque_nm,Udc_V\n"
        "0.0,1000,10,350\n"
        "0.5,1200,20,350\n"
        "1.0,1400,15,350\n",
        encoding="utf-8",
    )

    trajectory = read_drive_cycle_csv(
        str(csv_path),
        column_map={
            "time": "time_s",
            "N0": "speed_rpm",
            "Tem_av": "torque_nm",
            "Udc": "Udc_V",
        },
    )
    op_matrix, metadata = build_drive_cycle_op_matrix(trajectory, target="torque")

    assert np.allclose(op_matrix.N0, [1000.0, 1200.0, 1400.0])
    assert np.allclose(op_matrix.Tem_av_ref, [10.0, 20.0, 15.0])
    assert metadata["duration"] == pytest.approx(1.0)
    assert np.allclose(metadata["Udc"], [350.0, 350.0, 350.0])


def test_build_drive_cycle_power_input_matrix_sets_flag():
    trajectory = {
        "time": np.array([0.0, 0.5, 1.0]),
        "N0": np.array([1500.0, 1600.0, 1700.0]),
        "Pem_av": np.array([5e3, 6e3, 7e3]),
    }

    op_matrix, metadata = build_drive_cycle_op_matrix(trajectory, target="power_in")

    assert np.allclose(op_matrix.Pem_av_ref, trajectory["Pem_av"])
    assert op_matrix.is_output_power is False
    assert metadata["target"] == "power_in"


def test_summarize_drive_cycle_outputs_returns_cycle_metrics():
    time = np.array([0.0, 1.0, 2.0])
    outputs = []

    for speed in [1000.0, 1500.0, 2000.0]:
        op = OPdq(N0=speed, efficiency=0.8)
        op.set_Id_Iq(3.0, 4.0)
        op.set_Ud_Uq(6.0, 8.0)
        outputs.append(
            Output(
                elec=OutElec(
                    OP=op,
                    Tem_av=50.0,
                    P_out=100.0,
                    P_in=125.0,
                )
            )
        )

    summary = summarize_drive_cycle_outputs(XOutput(output_list=outputs), time)

    assert summary["step_count"] == 3
    assert summary["duration"] == pytest.approx(2.0)
    assert summary["energy_out_J"] == pytest.approx(200.0)
    assert summary["energy_in_J"] == pytest.approx(250.0)
    assert summary["energy_loss_J"] == pytest.approx(50.0)
    assert summary["eta_cycle"] == pytest.approx(0.8)
    assert summary["max_I_rms_A"] == pytest.approx(5.0)
    assert summary["max_U_rms_V"] == pytest.approx(10.0)


def test_summarize_drive_cycle_outputs_integrates_loss_breakdown():
    time = np.array([0.0, 1.0, 2.0])
    outputs = []

    for speed in [1000.0, 1500.0, 2000.0]:
        op = OPdq(N0=speed, efficiency=100.0 / 110.0)
        op.set_Id_Iq(3.0, 4.0)
        op.set_Ud_Uq(6.0, 8.0)
        outputs.append(
            Output(
                elec=OutElec(
                    OP=op,
                    Tem_av=50.0,
                    P_out=100.0,
                    P_in=110.0,
                ),
                loss=OutLoss(
                    loss_dict={
                        "stator winding Joule": OutLossModel(
                            name="stator winding Joule", scalar_value=5.0
                        ),
                        "stator core iron": OutLossModel(
                            name="stator core iron", scalar_value=3.0
                        ),
                        "magnet eddy": OutLossModel(
                            name="magnet eddy", scalar_value=2.0
                        ),
                    }
                ),
            )
        )

    summary = summarize_drive_cycle_outputs(XOutput(output_list=outputs), time)

    assert np.allclose(summary["P_loss"], [10.0, 10.0, 10.0])
    assert np.allclose(summary["P_loss_total"], [10.0, 10.0, 10.0])
    assert summary["energy_loss_J"] == pytest.approx(20.0)
    assert summary["energy_loss_breakdown_J"]["P_jl"] == pytest.approx(10.0)
    assert summary["energy_loss_breakdown_J"]["P_fe"] == pytest.approx(6.0)
    assert summary["energy_loss_breakdown_J"]["P_mag"] == pytest.approx(4.0)
    assert summary["energy_loss_breakdown_J"]["P_loss_total"] == pytest.approx(20.0)


def test_read_standard_drive_cycle_segments():
    assert "nedc" in list_standard_drive_cycles()
    assert "wltp_class3" in list_standard_drive_cycles()

    for name in ("nedc", "wltp_class3"):
        trajectory = read_standard_drive_cycle(name)
        op_matrix, metadata = build_drive_cycle_op_matrix(trajectory, target="torque")

        assert trajectory["time"].size >= 10
        assert trajectory["time"].size == trajectory["N0"].size
        assert trajectory["Tem_av"].size == trajectory["N0"].size
        assert metadata["target"] == "torque"
        assert op_matrix.get_N_OP() == trajectory["time"].size

    data_dir = Path(DATA_DIR) / "DriveCycle"
    assert (data_dir / "NEDC_segment.csv").stat().st_size < 50_000
    assert (data_dir / "WLTP_class3_segment.csv").stat().st_size < 50_000
