from os.path import join

import pytest

import numpy as np
from numpy.testing import assert_almost_equal
from pyleecan.Classes.EEC_SCIM import EEC_SCIM

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.LUTslip import LUTslip
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPslip import OPslip
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelJoule import LossModelJoule
from pyleecan.Classes.LossModelProximity import LossModelProximity


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D
from pyleecan.Functions.Plot import dict_2D


is_show_fig = True


@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_loss_SCIM():
    """Test to calculate losses in Toyota_Prius using Loss model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "SCIM_5kw_Zaheer.json"))

    simu = Simu1(name="test_FEMM_Loss_SCIM_5kw_Zaheer", machine=machine)

    simu.input = InputCurrent(
        Nt_tot=4 * 40,
        Na_tot=200 * 8,
        OP=OPslip(felec=50, slip_ref=0, I0_ref=6.6, IPhi0_ref=140 * np.pi / 180),
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
        model_dict={
            "stator core Steinmetz": LossModelSteinmetz(
                group="stator core", is_show_fig=True
            ),
            "rotor core Steinmetz": LossModelSteinmetz(group="rotor core"),
            "joule": LossModelJoule(group="stator winding", type_skin_effect=1),
            "proximity": LossModelProximity(group="stator winding"),
        },
    )

    out = simu.run()

    print(out.loss.get_power_dict())

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
        # group_names = [
        #     "stator core",
        #     "rotor core",
        # ]
        # for loss in out.loss.loss_dict.values():
        #     if "joule" in loss.name or "proximity" in loss.name :
        #         group_names.append("stator winding")
        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )
        #         group_names.pop()
        #     else:

        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )

        out.loss.plot_losses()

        # Plot the flux
        out.mag.B.plot_2D_Data("angle", **dict_2D)
        # Plot the torque
        out.mag.Tem.plot_2D_Data("time", **dict_2D)
        # Plot the current
        out.elec.get_Is().plot_2D_Data("time", "phase[]", **dict_2D)

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
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(out.elec.OP.felec)}" for o in out.loss.loss_dict.values()])
    # txt += F"speed = {SPEED/3} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(SPEED /3/60 * p)}" for o in out.loss.loss_dict.values()])

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
def test_FEMM_loss_SCIM_with_param():
    """Test to calculate losses in Toyota_Prius using Loss model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "SCIM_5kw_Zaheer.json"))
    machine.rotor.skew = None

    simu = Simu1(name="test_FEMM_Loss_SCIM_5kW", machine=machine)

    param_list = [
        {
            "U0_ref": 202.5,
            "N0": 728.7,
            "slip_ref": 0.284,
            "Tem_av": 24.6,
            "I1_abs": 9,
            "Pjoule_s": 50,
            "Pjoule_r": 40,
        },
        {
            "U0_ref": 200,
            "N0": 9664,
            "slip_ref": 0.018,
            "Tem_av": 107,
            "I1_abs": 181,
            "Pjoule_s": 1869,
            "Pjoule_r": 1979,
        },
    ]
    param_dict = param_list[0]

    param_dict["Lm"] = np.array(
        [
            0.00364256,
            0.00364256,
            0.00295137,
            0.00213818,
            0.00160483,
            0.00128478,
            0.00107101,
            0.00091922,
            0.00080651,
            0.00071975,
            0.00065101,
        ]
    )

    param_dict["Im"] = np.array(
        [
            0,
            1.00000000e-01,
            3.34222222e01,
            6.67444444e01,
            1.00066667e02,
            1.33388889e02,
            1.66711111e02,
            2.00033333e02,
            2.33355556e02,
            2.66677778e02,
            3.00000000e02,
        ]
    )

    Lm_table = param_dict["Lm"] * 10
    Im_table = param_dict["Im"] * 1e-1

    # simu.input = InputCurrent(
    #     Nt_tot=4 * 40 ,
    #     Na_tot=200 * 8,
    #     OP=OPslip(N0 = 4832, slip_ref = 0.03, I0_ref=333),
    #     is_periodicity_t=True,
    #     is_periodicity_a=True,
    # )

    simu.input = InputVoltage(
        OP=OPslip(
            U0_ref=param_dict["U0_ref"],
            N0=param_dict["N0"],
            slip_ref=param_dict["slip_ref"],
        ),
        Na_tot=100 * 2,
        Nt_tot=100 * 2,
        is_periodicity_a=True,
        is_periodicity_t=False,
        # Nrev=1,
        angle_rotor_initial=0 * 0.02,
    )

    ELUT_Audi_eTron = LUTslip()
    ELUT_Audi_eTron.simu = Simu1(machine=machine)
    R1_135 = 1 / (3 * 6.6 ** 2 / 50)  # from Joule losses
    ELUT_Audi_eTron.simu.elec = Electrical(
        eec=EEC_SCIM(
            R1=0.582,
            L1=6e-3,
            Tsta=60,
            R2=1.4e-6,
            L2=44e-9,
            Trot=60,
            Lm_table=Lm_table,
            Im_table=Im_table,
            type_skin_effect=0,
            Lm=0.627,
            Im=1 * np.exp(1j * 80 * np.pi / 180),
        )
        # eec=EEC_SCIM(
        #     R1=R1_135,
        #     L1=0.975 * 1.0899e-04,
        #     Tsta=135,
        #     R2=0.0108,
        #     L2=8.4080e-04,
        #     Trot=20,
        #     Lm_table=Lm_table,
        #     Im_table=Im_table,
        #     type_skin_effect=0,
        # )
    )

    # Configure simulation
    simu.elec = Electrical(
        Tsta=80,
        Trot=80,
        LUT_enforced=ELUT_Audi_eTron,
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
        model_dict={
            "stator core Steinmetz": LossModelSteinmetz(group="stator core"),
            "rotor core Steinmetz": LossModelSteinmetz(group="rotor core"),
            "joule stator": LossModelJoule(group="stator winding", type_skin_effect=1),
            "joule rotor": LossModelJoule(group="rotor winding", type_skin_effect=1),
            "proximity": LossModelProximity(group="stator winding"),
        },
    )

    out = simu.run()

    print(out.loss.get_power_dict())

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
        # group_names = [
        #     "stator core",
        #     "rotor core",
        # ]
        # for loss in out.loss.loss_dict.values():
        #     if "joule" in loss.name or "proximity" in loss.name :
        #         group_names.append("stator winding")
        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )
        #         group_names.pop()
        #     else:

        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )

        out.loss.plot_losses()

        # Plot the flux
        out.mag.B.plot_2D_Data("angle", **dict_2D)
        # Plot the torque
        out.mag.Tem.plot_2D_Data("time", **dict_2D)
        # Plot the current
        out.elec.get_Is().plot_2D_Data("time", "phase[]", **dict_2D)

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
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(out.elec.OP.felec)}" for o in out.loss.loss_dict.values()])
    # txt += F"speed = {SPEED/3} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(SPEED /3/60 * p)}" for o in out.loss.loss_dict.values()])

    # with open(F"{SPEED} rpm.txt", "w") as f:
    #     f.write(txt)

    return out


# To run it without pytest
if __name__ == "__main__":

    # out = test_FEMM_loss_SCIM()
    out = test_FEMM_loss_SCIM_with_param()
