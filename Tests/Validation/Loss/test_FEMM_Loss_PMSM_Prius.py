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
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelJoule import LossModelJoule
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.LossModelWindage import LossModelWindage


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D


is_show_fig = True


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
        Nt_tot=4 * 10 * 15,
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
        model_dict={
            "stator core": LossModelSteinmetz(group="stator core", is_show_fig=True),
            "rotor core": LossModelSteinmetz(group="rotor core"),
            "joule": LossModelJoule(group="stator winding"),
            "proximity": LossModelProximity(group="stator winding"),
            "magnets": LossModelMagnet(group="rotor magnets"),
            "mechanical": LossModelWindage(group="rotor core"),
        },
    )

    out = simu.run()

    out.loss.loss_list.append(sum(out.loss.loss_list))
    out.loss.loss_list[-1].name = "overall"

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

    out.plot_B_mesh()

    if is_show_fig:
        group_names = ["stator core", "rotor core", "rotor magnets"]
        for loss in out.loss.loss_list:
            if "joule" in loss.name or "proximity" in loss.name:
                loss.plot_mesh(group_names=group_names + ["stator winding"])
            else:
                loss.plot_mesh(group_names=group_names)
        out.loss.plot_losses()

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
        model_dict={
            "Stator core Bertotti": LossModelBertotti(
                group="stator core", is_show_fig=True
            ),
            "Stator core Steinmetz": LossModelSteinmetz(
                group="stator core", is_show_fig=True
            ),
        },
    )

    out = simu.run()

    out.loss.loss_list.append((out.loss.loss_list[0] - out.loss.loss_list[1]))
    out.loss.loss_list[-1].name = "Difference"

    print(out.loss.get_power_dict())

    if is_show_fig:
        group_names = ["stator core", "rotor core", "rotor magnets"]
        for loss in out.loss.loss_list:
            if "joule" in loss.name or "proximity" in loss.name:
                loss.plot_mesh(group_names=group_names + ["stator winding"])
            else:
                loss.plot_mesh(group_names=group_names)
        out.loss.plot_losses()

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


def test_LossFEMM_Prius():
    """Test to calculate losses in Toyota_Prius using LossFEMM model"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    Ch = 143  # hysteresis loss coefficient [W/(m^3*T^2*Hz)]
    Ce = 0.530  # eddy current loss coefficients [W/(m^3*T^2*Hz^2)]
    Cprox = 1  # sigma_w * cond.Hwire * cond.Wwire

    simu = Simu1(name="test_FEMM_Loss_Prius", machine=machine)

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

    simu.loss = LossFEMM(is_get_meshsolution=True, Tsta=100, type_skin_effect=1)

    out = simu.run()

    print(out.loss.get_power_dict())

    if is_show_fig:
        group_names = ["stator core", "rotor core", "rotor magnets"]
        for loss in out.loss.loss_list:
            if "joule" in loss.name or "proximity" in loss.name:
                loss.plot_mesh(group_names=group_names + ["stator winding"])
            else:
                loss.plot_mesh(group_names=group_names)
        out.loss.plot_losses()

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


@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_Id_Iq():
    """Test to calculate losses in Toyota_Prius using LossFEMM model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_FEMM_Loss_Prius", machine=machine)

    # Current for MTPA
    SPEED = 1200

    simu.input = InputCurrent(
        Nt_tot=4 * 40 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=SPEED, Id_ref=-50, Iq_ref=200),
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
            "stator core": LossModelSteinmetz(group="stator core"),
            "rotor core": LossModelSteinmetz(group="rotor core"),
            "joule": LossModelJoule(group="stator winding"),
            "proximity": LossModelProximity(group="stator winding"),
            "magnets": LossModelMagnet(group="rotor magnets"),
            "mechanical": LossModelWindage(group="rotor core"),
        },
    )

    out = simu.run()

    out.loss.loss_list.append(sum(out.loss.loss_list))
    out.loss.loss_list[-1].name = "overall"

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
        out.plot_B_mesh()
    # group_names = [
    #     "stator core",
    #     "rotor core",
    #     "rotor magnets"
    # ]
    # for loss in out.loss.loss_list:
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

    # plot_2D(
    #     [speed_array],
    #     array_list,
    #     xlabel="Speed [rpm]",
    #     ylabel="Losses [W]",
    #     legend_list=[o.name for o in out.loss.loss_list],
    # )

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

    # test_FEMM_Loss_diff()
    # test_FEMM_Loss_Prius()
    test_LossFEMM_Prius()
    # test_FEMM_Id_Iq()