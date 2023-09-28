from os.path import join

import pytest
from multiprocessing import cpu_count
import numpy as np
from numpy.testing import assert_almost_equal
from numpy.testing import assert_allclose
import matplotlib.pyplot as plt
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Skew import Skew
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEA import LossFEA
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelJoule import LossModelJoule
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.LossModelWindagePyrhonen import LossModelWindagePyrhonen


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
    """Test to calculate losses in Toyota_Prius using LossFEA model based on motoranalysis validation"""

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
            "mechanical": LossModelWindagePyrhonen(group="rotor core"),
        },
    )

    out = simu.run()

    out.loss.loss_dict["overall"] = sum(out.loss.loss_dict.values())

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
        for loss in out.loss.loss_dict.values():
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
def test_FEMM_Loss_diff():
    """Test to calculate losses in Toyota_Prius using LossFEA model based on motoranalysis validation"""

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

    out.loss.loss_dict["Difference"] = (
        out.loss.loss_dict.values()[0] - out.loss.loss_dict.values()[1]
    )

    print(out.loss.get_power_dict())

    if is_show_fig:
        group_names = ["stator core", "rotor core", "rotor magnets"]
        for loss in out.loss.loss_dict.values():
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
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(out.elec.OP.felec)}" for o in out.loss.loss_dict.values()])
    # txt += F"speed = {SPEED/3} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(SPEED /3/60 * p)}" for o in out.loss.loss_dict.values()])

    # with open(F"{SPEED} rpm.txt", "w") as f:
    #     f.write(txt)

    return out


@pytest.mark.Loss
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.long_5s
@pytest.mark.long_1m
def test_LossFEMM_Prius():
    """Test to calculate losses in Toyota_Prius using LossFEA model"""

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
        nb_worker=cpu_count(),
        is_get_meshsolution=True,
        is_fast_draw=True,
        is_calc_torque_energy=False,
    )

    simu.loss = LossFEA(is_get_meshsolution=True, Tsta=100, type_skin_effect=1)

    # Same with linear skew
    simu_skew = simu.copy()
    simu_skew.name = simu_skew.name + "_Skew"
    simu_skew.machine.rotor.skew = Skew(rate=1, type_skew="linear", Nstep=3)
    # simu_skew.machine.rotor.skew.plot()
    # plt.show()

    out = simu.run()

    # Check Power Dict
    power_dict = out.loss.get_power_dict()
    exp_power_dict = {
        "stator core": 292.64240263817754,
        "rotor core": 14.808165782336602,
        "joule": 7579.031160511537,
        "proximity": 16.826278397540907,
        "magnets": 12.178782086036916,
        "overall": 7915.486789415628,
        "total_power": 54596.16442311069,
    }
    assert len(power_dict.keys()) == len(exp_power_dict.keys())
    for key in power_dict:
        assert power_dict[key] == pytest.approx(exp_power_dict[key], rel=1e-2)

    out_skew = simu_skew.run()
    # Check Power Dict
    power_dict_skew = out_skew.loss.get_power_dict()
    exp_power_dict_skew = {
        "stator core": 262.1429040501597,
        "rotor core": 2.0164214385787242,
        "joule": 7579.031160511537,
        "proximity": 10.177251941106874,
        "magnets": 6.810952030240605,
        "overall": 7860.178689971623,
        "total_power": 51908.33963148792,
    }
    assert len(power_dict_skew.keys()) == len(exp_power_dict.keys())
    for key in power_dict_skew:
        assert power_dict_skew[key] == pytest.approx(exp_power_dict_skew[key], rel=1e-2)

    # Check Plot
    if is_show_fig:
        out.loss.plot_losses()
        out_skew.loss.plot_losses()
        group_names = ["stator core", "rotor core", "rotor magnets"]
        for loss in out.loss.loss_dict.values():
            if "joule" in loss.name or "proximity" in loss.name:
                loss.plot_mesh(group_names=group_names + ["stator winding"])
            else:
                loss.plot_mesh(group_names=group_names)
        for loss in out_skew.loss.loss_dict.values():
            if "joule" in loss.name or "proximity" in loss.name:
                loss.plot_mesh(group_names=group_names + ["stator winding"])
            else:
                loss.plot_mesh(group_names=group_names)

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
    """Test to calculate losses in Toyota_Prius using LossFEA model based on motoranalysis validation"""

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
            "mechanical": LossModelWindagePyrhonen(group="rotor core"),
        },
    )

    out = simu.run()

    out.loss.loss_dict["overall"] = sum(out.loss.loss_dict.values())

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

    # plot_2D(
    #     [speed_array],
    #     array_list,
    #     xlabel="Speed [rpm]",
    #     ylabel="Losses [W]",
    #     legend_list=[o.name for o in out.loss.loss_dict.values()],
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
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(out.elec.OP.felec)}" for o in out.loss.loss_dict.values()])
    # txt += F"speed = {SPEED/3} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(SPEED /3/60 * p)}" for o in out.loss.loss_dict.values()])

    # with open(F"{SPEED} rpm.txt", "w") as f:
    #     f.write(txt)

    return out


# To run it without pytest
if __name__ == "__main__":
    # test_FEMM_Loss_diff()
    # test_FEMM_Loss_Prius()
    test_LossFEMM_Prius()
    # test_FEMM_Id_Iq()
    print("Done")
