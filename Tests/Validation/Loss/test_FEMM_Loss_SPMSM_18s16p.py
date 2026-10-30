from multiprocessing import cpu_count
from os.path import join

import numpy as np
import pytest

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.LossFEA import LossFEA
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.OutLoss import OutLoss
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load

is_show_fig = False


@pytest.mark.Loss
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.long_10m
def test_LossFEA_SPMSM():
    """Test to calculate losses in SPMSM using LossFEA model from https://www.femm.info/wiki/SPMLoss"""

    machine = load(join(DATA_DIR, "Machine", "SPMSM_18s16p_loss.json"))

    Ce = 0.530 / 7700
    Ch = 143 / 7700
    Cprox = 4.1018  # sigma_w * cond.Hwire * cond.Wwire

    simu = Simu1(name="test_FEMM_Loss_SPMSM", machine=machine)

    simu.input = InputCurrent(
        Nt_tot=16 * 10 * 2,
        Na_tot=1000 * 2,
        OP=OPdq(N0=4000, Id_ref=0, Iq_ref=np.sqrt(2)),
        is_periodicity_t=True,
        is_periodicity_a=True,
    )

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
        is_get_meshsolution=True,
        FEMM_dict_enforced={
            "mesh": {
                "meshsize_airgap": 0.00014,
                "elementsize_airgap": 0.00014,
                "smart_mesh": 0,
            },
        },
        is_calc_torque_energy=False,
    )

    simu.loss = LossFEA(
        k_hy_enforced=Ch,
        k_ed_enforced=Ce,
        k_p_enforced=Cprox,
        is_get_meshsolution=True,
        Tsta=120,
        type_skin_effect=0,
        type_loss_model_core="Steinmetz",
        alpha_f_enforced=1,
        alpha_B_enforced=2,
        is_stacking_factor=True,
    )

    out = simu.run()

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    # Check Power Dict
    power_dict = out.loss.get_power_dict()
    exp_power_dict = {
        "stator core": np.float64(3.3278595306143064),
        "stator joule": np.float64(4.385847766901312),
        "stator proximity": np.float64(0.05525019341272971),
        "rotor core": np.float64(0.04407322797220236),
        "rotor magnets": np.float64(1.2951002420384434),
        "stator core + stator joule + stator proximity + rotor core + rotor magnets": np.float64(
            9.108130960938993
        ),
        "total_power": np.float64(61.900931327124255),
    }
    assert len(power_dict.keys()) == len(exp_power_dict.keys())
    for key in power_dict:
        assert power_dict[key] == pytest.approx(exp_power_dict[key], rel=1e-2)

    # Same with temporal approach
    out_time = out.copy()
    out_time.simu.loss = LossFEA(
        is_get_meshsolution=True,
        Tsta=100,
        type_skin_effect=1,
        type_loss_model_core="Steinmetz",
        is_stacking_factor=True,
        is_calc_windage_loss=True,
        is_dynamic=True,
    )

    out_time.loss = OutLoss()
    out_time.simu.loss.run()

    # Check Power Dict
    power_dict_t = out_time.loss.get_power_dict()

    power_dict_ref = {
        "mechanical power": 62.30,
        "rotor core loss": 0.057,
        "stator core loss": 3.41,
        "prox loss": 0.06,
        "joule loss": 4.37,
        "magnet loss": 1.38,
        "total loss": 9.27,
    }

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [
        np.array([o.get_loss_scalar(speed / 60 * p) for speed in speed_array])
        for o in out.loss.loss_dict.values()
    ]
    power_val_ref = [62.30, 3.41, 0.06, 4.37, 0.06, 1.38, 9.27]

    print(np.isclose(list(power_dict.values()), power_val_ref, rtol=0.1, atol=0))
    # assert_allclose(list(power_dict.values()), power_val_ref, rtol = 0.1)

    if is_show_fig:
        group_names = ["stator core", "rotor core", "rotor magnets"]
        for loss in out.loss.loss_dict.values():
            if "joule" in loss.name or "proximity" in loss.name:
                loss.get_group(group_names + ["stator winding"]).plot_mesh()
            else:
                loss.get_group(group_names).plot_mesh()
        out.loss.plot_losses()

        # plot_2D(
        #     [speed_array],
        #     [ovl_list, joule_list, sc_list, rc_list, prox_list, mag_list],
        #     xlabel="Speed [rpm]",
        #     ylabel="Losses [W]",
        #     legend_list=[
        #         "Overall",
        #         "Winding Joule",
        #         "Stator core",
        #         "Rotor core",
        #         "Winding proximity",
        #         "Magnets",
        #     ],
        # )

    return out


# To run it without pytest
if __name__ == "__main__":
    # test_FEMM_Loss_SPMSM()
    test_LossFEA_SPMSM()
