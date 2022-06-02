from os.path import join

import pytest

import numpy as np
from numpy.testing import assert_almost_equal

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEMM import LossFEMM
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.OutLoss import OutLoss

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D 


is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
def test_FEMM_Loss_SPMSM():
    """Test to calculate losses in SPMSM using LossFEMM model from https://www.femm.info/wiki/SPMLoss """

    machine = load(join(DATA_DIR, "Machine", "SPMSM_18s16p_loss.json"))

    Cprox = 4.1018  # sigma_w * cond.Hwire * cond.Wwire
    k_hy = 0.00844 / 0.453592
    k_ed = 31.2e-6 / 0.453592
    alpha_f = 1
    alpha_B = 2

    rho = machine.stator.mat_type.struct.rho

    # Check hysteresis loss coefficient [W/(m^3*T^2*Hz)]
    assert_almost_equal(k_hy * rho, 143, decimal=0)
    # Check eddy current loss coefficient [W/(m^3*T^2*Hz^2)]
    assert_almost_equal(k_ed * rho, 0.53, decimal=3)

    loss_model = LossModelSteinmetz(
        k_hy=k_hy, k_ed=k_ed, alpha_f=alpha_f, alpha_B=alpha_B
    )

    assert (k_hy == loss_model.k_hy and
        k_ed == loss_model.k_ed and
        alpha_f == loss_model.alpha_f and
        alpha_B == loss_model.alpha_B), (
        "As we provided the coefficients, the loss model should not change them")

    simu = Simu1(name="test_FEMM_Loss_SPMSM", machine=machine)

    simu.input = InputCurrent(
        Nt_tot=16 * 20,
        Na_tot=1000 * 2,
        OP=OPdq(N0=4000, Id_ref=0, Iq_ref=np.sqrt(2)),
        is_periodicity_t=True,
        is_periodicity_a=True,
    )

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=4,
        is_get_meshsolution=True,
        FEMM_dict_enforced={
            "mesh": {
                "meshsize_airgap": 0.00014,
                "elementsize_airgap": 0.00014,
                "smart_mesh": 0,
            },
        },
        is_fast_draw=True,
        is_periodicity_rotor=True,
        is_calc_torque_energy=False,
        # is_close_femm=False,
    )

    simu.loss = LossFEMM(
        Cp=Cprox,
        is_get_meshsolution=True,
        Tsta=120,
        type_skin_effect=0,
        model_dict={"stator core": loss_model, "rotor core": loss_model},
    )

    out = simu.run()

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()
    outloss_list = list()
    OP = out.elec.OP.copy()
    for speed in speed_array:
        OP.felec = speed / 60 * p
        out_dict = {"coeff_dict": out.loss.coeff_dict}
        outloss = OutLoss()
        outloss.store(out_dict, lam=machine.stator, OP=OP, type_skin_effect=0, Tsta=120)
        outloss_list.append(outloss)

    joule_list = [o.Pjoule for o in outloss_list]
    sc_list = [o.Pstator for o in outloss_list]
    rc_list = [o.Protor for o in outloss_list]
    prox_list = [o.Pprox for o in outloss_list]
    mag_list = [o.Pmagnet for o in outloss_list]
    ovl_list = [o.get_loss_overall() for o in outloss_list]

    power_dict = {
        "total_power": out.mag.Pem_av,
        "overall_losses": out.loss.get_loss_overall(),
        "stator_loss": out.loss.Pstator,
        "copper_loss": out.loss.Pjoule,
        "rotor_loss": out.loss.Protor,
        "magnet_loss": out.loss.Pmagnet,
        "proximity_loss": out.loss.Pprox,
    }
    print(power_dict)

    power_val_ref = [61.87, 9.10, 3.32, 4.38, 0.04, 1.29, 0.05]

    assert_almost_equal(list(power_dict.values()), power_val_ref, decimal=2)

    if is_show_fig:
        out.loss.meshsol_list[0].plot_contour(
            "freqs=sum",
            label="Loss",
            group_names=[
                "stator core",
                "stator winding",
                "rotor core",
                "rotor magnets",
            ],
            # clim=[1e4, 1e7],
        )

        plot_2D(
            [speed_array],
            [ovl_list, joule_list, sc_list, rc_list, prox_list, mag_list],
            xlabel="Speed [rpm]",
            ylabel="Losses [W]",
            legend_list=[
                "Overall",
                "Winding Joule",
                "Stator core",
                "Rotor core",
                "Winding proximity",
                "Magnets",
            ],
        )

    return out


@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_Loss_Prius():
    """Test to calculate losses in Toyota_Prius using LossFEMM model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius_loss.json"))

    simu = Simu1(name="test_FEMM_Loss_Prius", machine=machine)
    
    Cprox=1

    # Current for MTPA
    Ic = 230 * np.exp(1j * 140 * np.pi / 180)

    simu.input = InputCurrent(
        Nt_tot=40 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=1200, Id_ref=Ic.real, Iq_ref=Ic.imag),
        is_periodicity_t=True,
        is_periodicity_a=True,
    )

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=4,
        is_get_meshsolution=True,
        is_fast_draw=True,
        is_calc_torque_energy=False,
    )


    loss_model = LossModelSteinmetz()
    simu.loss = LossFEMM(
        Cp=Cprox,
        is_get_meshsolution=True,
        Tsta=100,
        type_skin_effect=0,
        model_dict={"stator core": loss_model, "rotor core": loss_model},
    )

    out = simu.run()

    power_dict = {
        "total_power": out.mag.Pem_av,
        "overall_losses": out.loss.get_loss_overall(),
        "stator_loss": out.loss.Pstator,
        "copper_loss": out.loss.Pjoule,
        "rotor_loss": out.loss.Protor,
        "magnet_loss": out.loss.Pmagnet,
        "proximity_loss": out.loss.Pprox,
    }
    print(power_dict)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()
    outloss_list = list()
    OP = out.elec.OP.copy()
    for speed in speed_array:
        OP.felec = speed / 60 * p
        out_dict = {"coeff_dict": out.loss.coeff_dict}
        outloss = OutLoss()
        outloss.store(out_dict, lam=machine.stator, OP=OP, type_skin_effect=0, Tsta=120)
        outloss_list.append(outloss)

    joule_list = [o.Pjoule for o in outloss_list]
    sc_list = [o.Pstator for o in outloss_list]
    rc_list = [o.Protor for o in outloss_list]
    prox_list = [o.Pprox for o in outloss_list]
    mag_list = [o.Pmagnet for o in outloss_list]
    ovl_list = [o.get_loss_overall() for o in outloss_list]

    if is_show_fig:
        out.loss.meshsol_list[0].plot_contour(
            "freqs=sum",
            label="Loss",
            group_names=[
                "stator core",
                # "stator winding",
                "rotor core",
                "rotor magnets",
            ],
            # clim=[2e4, 2e7],
        )

        plot_2D(
            [speed_array],
            [ovl_list, joule_list, sc_list, rc_list, prox_list, mag_list],
            xlabel="Speed [rpm]",
            ylabel="Losses [W]",
            legend_list=[
                "Overall",
                "Winding Joule",
                "Stator core",
                "Rotor core",
                "Winding proximity",
                "Magnets",
            ],
        )

    # out.loss.meshsol_list[0].plot_contour(
    #     "freqs=sum",
    #     label="Loss",
    #     group_names=["stator core", "stator winding"],
    #     # clim=[2e4, 2e7],
    # )

    # out.loss.meshsol_list[0].plot_contour(
    #     "freqs=sum",
    #     label="Loss",
    #     group_names=["rotor core", "rotor magnets"],
    #     # clim=[2e4, 2e7],
    # )

    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_FEMM_Loss_SPMSM()

    out = test_FEMM_Loss_Prius() 
