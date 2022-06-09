from os.path import join

import pytest

import numpy as np
from numpy.testing import assert_almost_equal

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

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_FEMM_Loss_Prius", machine=machine)

    # Current for MTPA
    Ic = 230 * np.exp(1j * 140 * np.pi / 180)
    SPEED = 1200

    simu.input = InputCurrent(
        Nt_tot=4 * 40 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=SPEED, Id_ref=Ic.real, Iq_ref=Ic.imag),
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

    simu.loss = Loss(
        is_get_meshsolution=True,
        Tsta=100,
        model_dict={"stator core": LossModelSteinmetz(group = "stator core"),
                    "rotor core": LossModelSteinmetz(group = "rotor core"),
                    "joule": LossModelWinding(group = "stator winding"),
                    "proximity": LossModelProximity(group = "stator winding"),
                    "magnets": LossModelMagnet(group = "rotor magnets")}
    )

    out = simu.run()
    
    out.loss.loss_list.append(sum(out.loss.loss_list))
    out.loss.loss_list[-1].name = "overall"

    power_dict = {
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    print(power_dict)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list]
    
    # def calc_loss(coeff, B):
    #     f=80
    #     if len(coeff)==4:
    #         return coeff[0] * 80 ** coeff[2] *B**coeff[3]+coeff[1]*(f*B)**2
    #     else:
    #         return coeff[0]*80*B**coeff[1]+coeff[2]*(80*B)**coeff[3]+coeff[4]*(80*B)**coeff[5]
    
    # B_list=np.linspace(0,3.5,100)
    # loss=simu.loss.model_dict["stator core Steinmetz"]
    # coeffs = loss.k_hy, loss.k_ed, loss.alpha_f, loss.alpha_B
    # plot_loss_S=np.array([calc_loss(coeffs, B) for B in B_list])
    # loss=simu.loss.model_dict["stator core Bertotti"]
    # coeffs = loss.k_hy, loss.alpha_hy, loss.k_ed, loss.alpha_ed, loss.k_ex, loss.alpha_ex
    # plot_loss_B=np.array([calc_loss(coeffs, B) for B in B_list])
    # import matplotlib.pyplot as plt 
    
    # plt.plot(B_list, plot_loss_S, color='red')
    # plt.plot(B_list, plot_loss_B, color='blue')
    # plt.show()

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
    # txt = f"total_power: {out.mag.Pem_av}\n"
    # txt += F"speed = {SPEED} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(out.elec.OP.felec)}" for o in out.loss.loss_list])
    # txt += F"speed = {SPEED/3} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(SPEED /3/60 * p)}" for o in out.loss.loss_list])

    # with open(F"{SPEED} rpm.txt", "w") as f:
    #     f.write(txt)


    return out

@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_Loss_diff():
    """Test to calculate losses in Toyota_Prius using LossFEMM model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius_loss.json"))

    simu = Simu1(name="test_FEMM_Loss_Prius", machine=machine)

    # Current for MTPA
    Ic = 230 * np.exp(1j * 140 * np.pi / 180)
    SPEED = 1200

    simu.input = InputCurrent(
        Nt_tot=4 * 40 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=SPEED, Id_ref=Ic.real, Iq_ref=Ic.imag),
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

    simu.loss = Loss(
        is_get_meshsolution=True,
        Tsta=100,
        model_dict={"rotor core Bertotti": LossModelBertotti(group = "rotor core"),
                    "rotor core Steinmetz": LossModelSteinmetz(group = "rotor core")}
    )

    out = simu.run()

    out.loss.loss_list.append((out.loss.loss_list[0]-out.loss.loss_list[1]))

    power_dict = {
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    print(power_dict)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list]

    if is_show_fig:
        group_names = [
            "stator core",
            "rotor core",
            "rotor magnets"
        ]
        for loss in out.loss.loss_list:
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
    # txt = f"total_power: {out.mag.Pem_av}\n"
    # txt += F"speed = {SPEED} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(out.elec.OP.felec)}" for o in out.loss.loss_list])
    # txt += F"speed = {SPEED/3} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(SPEED /3/60 * p)}" for o in out.loss.loss_list])

    # with open(F"{SPEED} rpm.txt", "w") as f:
    #     f.write(txt)


    return out


# To run it without pytest
if __name__ == "__main__":

    # test_FEMM_Loss_SPMSM()

    # test_FEMM_Loss_Prius()
    test_FEMM_Loss_diff()
