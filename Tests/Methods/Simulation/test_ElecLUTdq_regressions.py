from types import SimpleNamespace

import numpy as np
import pytest

from pyleecan.Methods.Simulation.ElecLUTdq.run import run
from pyleecan.Methods.Simulation.ElecLUTdq.solve_MTPA import solve_MTPA
from pyleecan.Methods.Simulation.ElecLUTdq.solve_power import solve_power
from pyleecan.Methods.Simulation.ElecLUTdq.solve_torque import solve_torque


class DummyLogger:
    def info(self, *_args, **_kwargs):
        return None

    def warning(self, *_args, **_kwargs):
        return None


class DummyLUT:
    def __init__(self, iq_values, phid=1.0, joule_losses=None, is_loss_model=False):
        self.iq_values = np.asarray(iq_values, dtype=float)
        self.phid = phid
        self.joule_losses = np.asarray(joule_losses, dtype=float)
        self.simu = SimpleNamespace(loss=object() if is_loss_model else None)

    def interp_Phi_dqh(self, Id, Iq):
        shape = np.asarray(Id).shape
        return (
            np.full(shape, self.phid, dtype=float),
            np.zeros(shape, dtype=float),
            np.zeros(shape, dtype=float),
        )

    def interp_Ploss_dqh(self, Id, Iq, N0=None, exclude_models=None):
        iq = np.asarray(Iq, dtype=float)
        losses = np.zeros((iq.size, 5), dtype=float)
        losses[:, 0] = self.joule_losses
        return losses

    def get_Phi_dqh_mag_mean(self):
        return np.array([self.phid, 0.0])

    def interp_Tem_rip_dqh(self, Id, Iq):
        return None

    def get_OP_array(self, *args):
        return np.array([[1000.0, -10.0, 20.0], [1000.0, 0.0, 30.0]])


def _build_machine():
    conductor = SimpleNamespace(comp_surface_active=lambda: 2.0)
    winding = SimpleNamespace(qs=1, Npcp=2, Ntcoil=6, conductor=conductor)
    stator = SimpleNamespace(
        winding=winding,
        comp_resistance_wind=lambda T: 0.5,
        get_Zs=lambda: 12,
        Rint=0.1,
    )
    return SimpleNamespace(stator=stator)


def test_run_preserves_explicit_Irms_max():
    machine = _build_machine()
    op = SimpleNamespace(
        N0=1000.0,
        Pem_av_ref=None,
        Pem_av_in=None,
        efficiency=None,
        Id_ref=None,
        Iq_ref=None,
        Ud_ref=None,
        Uq_ref=None,
    )
    out_elec = SimpleNamespace(OP=op, get_Jrms=lambda: None)
    simu = SimpleNamespace(
        machine=machine,
        input=SimpleNamespace(Irms_max=12.0, is_generator=False),
        elec=None,
    )
    output = SimpleNamespace(simu=simu, elec=out_elec, mag=SimpleNamespace(), loss=None)
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Irms_max=42.0,
        Jrms_max=None,
        LUT_enforced=DummyLUT(iq_values=[0.0, 1.0], joule_losses=[0.0, 0.0]),
        type_skin_effect=0,
        Tsta=20.0,
        Trot=20.0,
        n_Id=1,
        n_Iq=1,
        get_logger=lambda: DummyLogger(),
        solve_MTPA=lambda LUT, Rs: {
            "P_in": 100.0,
            "P_out": 90.0,
            "efficiency": 0.9,
            "Tem_av": 50.0,
            "Id": 0.0,
            "Iq": 1.0,
            "Ud": 0.0,
            "Uq": 10.0,
            "Phid": 1.0,
            "Phiq": 0.0,
            "Phid_mag": 1.0,
            "Phiq_mag": 0.0,
            "Pjoule": 10.0,
            "Erms": 20.0,
        },
        solve_power=None,
        comp_LUTdq=None,
    )
    simu.elec = self

    run(self)

    assert self.Irms_max == pytest.approx(42.0)
    assert simu.input.Irms_max == pytest.approx(12.0)


def test_solve_power_uses_input_power_fallback():
    op = SimpleNamespace(Pem_av_ref=None, Pem_av_in=6.5, N0=1000.0, efficiency=None)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1))
            ),
            input=SimpleNamespace(is_generator=False),
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=10.0,
        Irms_max=10.0,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=0.8,
        Iq_max=1.0,
        n_Id=1,
        n_Iq=2,
        n_interp=4,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(
        iq_values=[0.8, 1.0],
        joule_losses=[0.1, 1.5],
        is_loss_model=True,
    )

    out_dict = solve_power(self, lut, Rs=0.0)

    assert out_dict["Iq"] == pytest.approx(1.0)
    assert out_dict["P_in"] == pytest.approx(2 * np.pi)
    assert out_dict["control_region"] == "MTPA"


def test_solve_power_accepts_missing_voltage_limit():
    op = SimpleNamespace(Pem_av_ref=None, Pem_av_in=6.5, N0=1000.0, efficiency=None)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1))
            ),
            input=SimpleNamespace(is_generator=False),
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=None,
        Irms_max=10.0,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=0.8,
        Iq_max=1.0,
        n_Id=1,
        n_Iq=2,
        n_interp=4,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(
        iq_values=[0.8, 1.0],
        joule_losses=[0.1, 1.5],
        is_loss_model=True,
    )

    out_dict = solve_power(self, lut, Rs=0.0)

    assert out_dict["Iq"] == pytest.approx(1.0)
    assert out_dict["control_region"] == "MTPA"


def test_solve_MTPA_raises_clear_error_when_no_feasible_point():
    op = SimpleNamespace(N0=1000.0)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1)),
                get_pole_pair_number=lambda: 1,
            )
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=0.1,
        Irms_max=0.1,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=1.0,
        Iq_max=1.0,
        n_Id=1,
        n_Iq=1,
        n_interp=2,
        load_rate=1.0,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(iq_values=[1.0], joule_losses=[0.0], is_loss_model=False)

    with pytest.raises(ValueError, match="No feasible dq operating point"):
        solve_MTPA(self, lut, Rs=0.0)


def test_solve_MTPA_accepts_missing_voltage_limit():
    op = SimpleNamespace(N0=1000.0)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1)),
                get_pole_pair_number=lambda: 1,
            )
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=None,
        Irms_max=10.0,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=1.0,
        Iq_max=1.0,
        n_Id=1,
        n_Iq=1,
        n_interp=2,
        load_rate=1.0,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(iq_values=[1.0], joule_losses=[0.0], is_loss_model=False)

    out_dict = solve_MTPA(self, lut, Rs=0.0)

    assert out_dict["Iq"] == pytest.approx(1.0)
    assert out_dict["control_region"] == "MTPA"


def test_solve_torque_tracks_positive_torque_reference():
    op = SimpleNamespace(Tem_av_ref=0.9, N0=1000.0, efficiency=None)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1)),
                get_pole_pair_number=lambda: 1,
            )
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=10.0,
        Irms_max=10.0,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=0.0,
        Iq_max=1.0,
        n_Id=1,
        n_Iq=2,
        n_interp=60,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(iq_values=[0.0, 1.0], joule_losses=[0.0, 0.0], is_loss_model=False)

    out_dict = solve_torque(self, lut, Rs=0.0)

    assert out_dict["Tem_av"] == pytest.approx(0.9, abs=0.05)
    assert out_dict["Iq"] == pytest.approx(0.9, abs=0.05)
    assert out_dict["control_region"] == "MTPA"


def test_solve_torque_supports_negative_torque_reference():
    op = SimpleNamespace(Tem_av_ref=-0.6, N0=1000.0, efficiency=None)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1)),
                get_pole_pair_number=lambda: 1,
            )
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=10.0,
        Irms_max=10.0,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=-1.0,
        Iq_max=0.0,
        n_Id=1,
        n_Iq=2,
        n_interp=60,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(iq_values=[-1.0, 0.0], joule_losses=[0.0, 0.0], is_loss_model=False)

    out_dict = solve_torque(self, lut, Rs=0.0)

    assert out_dict["Tem_av"] == pytest.approx(-0.6, abs=0.05)
    assert out_dict["Iq"] == pytest.approx(-0.6, abs=0.05)
    assert out_dict["control_region"] == "MTPA"


def test_solve_torque_accepts_missing_voltage_limit():
    op = SimpleNamespace(Tem_av_ref=0.9, N0=1000.0, efficiency=None)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1)),
                get_pole_pair_number=lambda: 1,
            )
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=None,
        Irms_max=10.0,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=0.0,
        Iq_max=1.0,
        n_Id=1,
        n_Iq=2,
        n_interp=60,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(iq_values=[0.0, 1.0], joule_losses=[0.0, 0.0], is_loss_model=False)

    out_dict = solve_torque(self, lut, Rs=0.0)

    assert out_dict["Tem_av"] == pytest.approx(0.9, abs=0.05)
    assert out_dict["control_region"] == "MTPA"


def test_solve_torque_unreachable_target_prefers_fully_feasible_point():
    op = SimpleNamespace(Tem_av_ref=2.0, N0=1000.0, efficiency=None)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1)),
                get_pole_pair_number=lambda: 1,
            )
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=10.0,
        Irms_max=0.5,
        Id_min=0.0,
        Id_max=0.0,
        Iq_min=0.0,
        Iq_max=1.0,
        n_Id=1,
        n_Iq=2,
        n_interp=60,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(iq_values=[0.0, 1.0], joule_losses=[0.0, 0.0], is_loss_model=False)

    out_dict = solve_torque(self, lut, Rs=0.0)

    i_rms = np.sqrt(out_dict["Id"] ** 2 + out_dict["Iq"] ** 2)
    u_rms = np.sqrt(out_dict["Ud"] ** 2 + out_dict["Uq"] ** 2)
    assert i_rms <= self.Irms_max + 1e-9
    assert u_rms <= self.Urms_max + 1e-9
    assert out_dict["Tem_av"] < op.Tem_av_ref
    assert out_dict["Tem_av"] == pytest.approx(self.Irms_max, abs=0.05)


def test_solve_torque_low_interp_count_keeps_non_singleton_axes():
    op = SimpleNamespace(Tem_av_ref=0.5, N0=1000.0, efficiency=None)
    op.get_felec = lambda: 1.0
    output = SimpleNamespace(
        simu=SimpleNamespace(
            machine=SimpleNamespace(
                stator=SimpleNamespace(winding=SimpleNamespace(qs=1)),
                get_pole_pair_number=lambda: 1,
            )
        ),
        elec=SimpleNamespace(OP=op),
    )
    self = SimpleNamespace(
        parent=SimpleNamespace(parent=output),
        Urms_max=10.0,
        Irms_max=10.0,
        Id_min=0.0,
        Id_max=1.0,
        Iq_min=0.0,
        Iq_max=1.0,
        n_Id=2,
        n_Iq=2,
        n_interp=1,
        get_logger=lambda: DummyLogger(),
    )
    lut = DummyLUT(iq_values=[0.0, 1.0], joule_losses=[0.0, 0.0], is_loss_model=False)

    out_dict = solve_torque(self, lut, Rs=0.0)

    assert np.isfinite(out_dict["Tem_av"])
    assert np.isfinite(out_dict["Id"])
    assert np.isfinite(out_dict["Iq"])
