from os.path import join

import pytest

import numpy as np
from numpy.testing import assert_almost_equal
from numpy.testing import assert_allclose

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEMM import LossFEMM


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D 


is_show_fig = False


def test_LossFEMM_SPMSM():
    """Test to calculate losses in SPMSM using LossFEMM model from https://www.femm.info/wiki/SPMLoss """

    machine = load(join(DATA_DIR, "Machine", "SPMSM_18s16p_loss.json"))

    Ch = 0.00844 / 0.453592
    Ce = 31.2e-6 / 0.453592
    Cprox = 4.1018  # sigma_w * cond.Hwire * cond.Wwire

    simu = Simu1(name="test_FEMM_Loss_SPMSM", machine=machine)

    simu.input = InputCurrent(
        Nt_tot=16 * 20 * 10,
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

    simu.loss = LossFEMM(k_hy=Ch, k_ed=Ce, k_h=Cprox, is_get_meshsolution=True, Tsta=120, type_skin_effect = 0)

    out = simu.run()

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    power_dict = {
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    print(power_dict)
    
    power_dict_ref = {"mechanical power": 62.30,
                     "rotor core loss": 0.057,
                     "stator core loss": 3.41,
                     "prox loss": 0.06,
                     "joule loss": 4.37,
                     "magnet loss": 1.38,
                     "total loss": 9.27
    }

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list]
    power_val_ref = [62.30, 3.41, 0.06, 4.37, 0.06, 1.38, 9.27]

    print(np.isclose(list(power_dict.values()), power_val_ref, rtol = 0.1, atol=0))
    # assert_allclose(list(power_dict.values()), power_val_ref, rtol = 0.1)

    if is_show_fig:
        group_names = [
            "stator core",
            "rotor core",
            "rotor magnets"
        ]
        for loss in out.loss.loss_list:
            if "joule" in loss.name or "proximity" in loss.name :
                group_names.append("stator winding")
                loss.get_mesh_solution().plot_contour(
                    "freqs=sum",
                    label=f"{loss.name} loss density (W/m^3)",
                    group_names = group_names
                )
                group_names.pop()
            else:
                
                loss.get_mesh_solution().plot_contour(
                    "freqs=sum",
                    label=f"{loss.name} loss density (W/m^3)",
                    group_names = group_names
                )

        plot_2D(
            [speed_array],
            array_list,
            xlabel="Speed [rpm]",
            ylabel="Losses [W]",
            legend_list=[o.name for o in out.loss.loss_list],
        )

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
    test_LossFEMM_SPMSM()
