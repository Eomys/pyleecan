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
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelJordan import LossModelJordan
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelWinding import LossModelWinding
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.LossModelWindage import LossModelWindage
from pyleecan.Classes.OutLossModel import OutLossModel
from pyleecan.Functions.Electrical.comp_loss_joule import comp_loss_joule


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D 


is_show_fig = True


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
    
    # Get parameters for proximity effect loss computation for phase windings
    AWG = 25
    TemperatureRise = 100
    WindingFill1 = machine.stator.Kf1
    WindingFill2 = machine.stator.comp_fill_factor()
    WindingFill=0.3882
    d = machine.stator.winding.conductor.Wwire
    dwire=0.324861*0.0254*np.exp(-0.115942*AWG) # wire diameter in meters as a function of AWG
    owire = (58*10**6)/(1+TemperatureRise*0.004) # conductivity of the wire in S/m at prescribed deltaT
    cePhase = (np.pi**2/8)*dwire**2*WindingFill*owire
    txt=f"""Meeker
---------------
d={dwire}
cond={owire}
kp={cePhase}
windingfill={0.3882}
"""

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
        Nt_tot=16*20,
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
        is_get_meshsolution=True,
        Tsta=120,
        model_dict={"stator core": LossModelSteinmetz(group = "stator core",
                                                      k_hy=k_hy,
                                                      k_ed=k_ed,
                                                      alpha_f=alpha_f,
                                                      alpha_B=alpha_B),
                    "rotor core": LossModelSteinmetz(group = "rotor core",
                                                     k_hy=k_hy,
                                                     k_ed=k_ed,
                                                     alpha_f=alpha_f,
                                                     alpha_B=alpha_B),
                    "joule": LossModelWinding(group = "stator winding"),
                    "proximity": LossModelProximity(group = "stator winding"),
                    "magnets": LossModelMagnet(group = "rotor magnets")}
    )


    out = simu.run()

    # assert_almost_equal(Cprox, simu.loss.model_dict["proximity"].k_p, decimal=0)

    power_dict = {
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    txt+=f"""
Pyleecan
---------------
d={d}
cond={machine.stator.winding.conductor.cond_mat.elec.get_conductivity(T_op=120)}
kp={simu.loss.model_dict['proximity'].k_p}
windingfill={WindingFill2}
"""
    print(power_dict)
    print(txt)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list if o.name != 'overall']
    array_list.append(sum(array_list))

    power_val_ref = {"mechanical power": 62.30,
                     "rotor core loss": 0.057,
                     "stator core loss": 3.41,
                     "prox loss": 0.06,
                     "joule loss": 4.37,
                     "magnet loss": 1.38,
                     "total loss": 9.27
    }

    # assert_almost_equal(list(power_dict.values()), list(power_val_ref.values()), decimal=0)
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
                    label=f"{loss.name} Loss",
                    group_names = group_names
                )
                group_names.pop()
            else:
                
                loss.get_mesh_solution().plot_contour(
                    "freqs=sum",
                    label=f"{loss.name} Loss",
                    group_names = group_names
                )

        plot_2D(
            [speed_array],
            array_list,
            xlabel="Speed [rpm]",
            ylabel="Losses [W]",
            legend_list=[o.name for o in out.loss.loss_list] + ["overall loss"],
        )

    return out

def test_LossFEMM_SPMSM():
    """Test to calculate losses in SPMSM using LossFEMM model from https://www.femm.info/wiki/SPMLoss """

    machine = load(join(DATA_DIR, "Machine", "SPMSM_18s16p_loss.json"))

    Ch = 0.00844 / 0.453592
    Ce = 31.2e-6 / 0.453592
    Cprox = 4.1018  # sigma_w * cond.Hwire * cond.Wwire

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

    simu.loss = LossFEMM(Ce = Ce, Ch = Ch, Cp=Cprox, is_get_meshsolution=True, Tsta=120, type_skin_effect = 0)

    out = simu.run()

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()
    outloss_list = list()
    OP = out.elec.OP.copy()
    # for speed in speed_array:
    #     OP.felec = speed / 60 * p
    #     out_dict = {"coeff_dict": out.loss.coeff_dict}
    #     outloss = OutLoss()
    #     outloss.store(out_dict, lam=machine.stator, OP=OP, type_skin_effect=0, Tsta=120)
    #     outloss_list.append(outloss)

    # joule_list = [o.Pjoule for o in outloss_list]
    # sc_list = [o.Pstator for o in outloss_list]
    # rc_list = [o.Protor for o in outloss_list]
    # prox_list = [o.Pprox for o in outloss_list]
    # mag_list = [o.Pmagnet for o in outloss_list]
    # ovl_list = [o.get_loss_overall() for o in outloss_list]

    power_dict = {
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    print(power_dict)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list]
    power_val_ref = [62.30, 3.41, 0.06, 4.37, 0.06, 1.38]

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
                    label=f"{loss.name} Loss",
                    group_names = group_names
                )
                group_names.pop()
            else:
                
                loss.get_mesh_solution().plot_contour(
                    "freqs=sum",
                    label=f"{loss.name} Loss",
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


# To run it without pytest
if __name__ == "__main__":

    test_FEMM_Loss_SPMSM()
    # test_LossFEMM_SPMSM()
