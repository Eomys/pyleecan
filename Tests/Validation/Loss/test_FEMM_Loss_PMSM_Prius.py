from multiprocessing import cpu_count
from os.path import join

import numpy as np
import pytest

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossFEA import LossFEA
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelJoule import LossModelJoule
from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelWindagePyrhonen import LossModelWindagePyrhonen
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.OutLoss import OutLoss
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Skew import Skew
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load

is_show_fig = False


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
            "Stator core Bertotti": LossModelBertotti(group="stator core"),
            "Stator core Steinmetz": LossModelSteinmetz(group="stator core"),
        },
    )

    out = simu.run()

    simu.loss.model["Stator core Bertotti"].plot_fitting(is_show_fig=True)

    simu.loss.model["Stator core Steinmetz"].plot_fitting(is_show_fig=True)

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

    material = machine.stator.mat_type

    lm_steinmetz = LossModelSteinmetz()
    lm_steinmetz.comp_coeff(material)
    lm_steinmetz.plot_fitting(material, is_show_fig=True)

    lm_bertotti = LossModelBertotti()
    lm_bertotti.comp_coeff(material)
    lm_bertotti.plot_fitting(material, is_show_fig=True)

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
        type_meshsolution=0,
    )

    simu.loss = LossFEA(
        is_get_meshsolution=True,
        Tsta=100,
        type_skin_effect=1,
        type_loss_model_core="Steinmetz",
        is_stacking_factor=True,
        is_calc_windage_loss=True,
    )

    out = simu.run()

    # Check Power Dict
    power_dict = out.loss.get_power_dict()
    exp_power_dict = {
        "stator core": np.float64(292.6424838992634),
        "stator joule": np.float64(7579.031160511535),
        "stator proximity": np.float64(16.826278591731466),
        "rotor core": np.float64(14.808168474489523),
        "rotor magnets": np.float64(12.178779821075157),
        "airgap windage": 0.1650942739887786,
        "stator core + stator joule + stator proximity + rotor core + rotor magnets + airgap windage": np.float64(
            7915.651965572084
        ),
        "total_power": np.float64(54596.16438835998),
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
    exp_power_dict_t = {
        "stator core": np.float64(2140.899349547698),
        "stator joule": np.float64(7579.031160511535),
        "stator proximity": np.float64(16.826278591731466),
        "rotor core": np.float64(21.211897758961086),
        "rotor magnets": np.float64(12.178779821075157),
        "airgap windage": 0.1650942739887786,
        "stator core + stator joule + stator proximity + rotor core + rotor magnets + airgap windage": np.float64(
            9770.31256050499
        ),
        "total_power": np.float64(54596.16438835998),
    }

    assert len(power_dict_t.keys()) == len(exp_power_dict_t.keys())
    for key in power_dict_t:
        assert power_dict_t[key] == pytest.approx(exp_power_dict_t[key], rel=1e-2)

    # Same with Bertotti skew
    out1 = out.copy()
    out1.simu.loss = LossFEA(
        is_get_meshsolution=True,
        Tsta=100,
        type_skin_effect=1,
        type_loss_model_core="Bertotti",
        is_stacking_factor=True,
        is_calc_windage_loss=True,
    )

    out1.loss = OutLoss()
    out1.simu.loss.run()

    # Check Power Dict
    power_dict1 = out1.loss.get_power_dict()
    exp_power_dict1 = {
        "stator core": np.float64(2140.899349547698),
        "stator joule": np.float64(7579.031160511535),
        "stator proximity": np.float64(16.826278591731466),
        "rotor core": np.float64(21.211897758961086),
        "rotor magnets": np.float64(12.178779821075157),
        "airgap windage": 0.1650942739887786,
        "stator core + stator joule + stator proximity + rotor core + rotor magnets + airgap windage": np.float64(
            9770.31256050499
        ),
        "total_power": np.float64(54596.16438835998),
    }

    assert len(power_dict1.keys()) == len(exp_power_dict1.keys())
    for key in power_dict1:
        assert power_dict1[key] == pytest.approx(exp_power_dict1[key], rel=1e-2)

    # Same with linear skew
    simu_skew = simu.copy()
    simu_skew.mag.Slice_enforced = None
    simu_skew.name = simu_skew.name + "_Skew"
    simu_skew.machine.rotor.skew = Skew(rate=1, type_skew="linear", Nstep=3)
    # simu_skew.machine.rotor.skew.plot()
    # plt.show()

    out_skew = simu_skew.run()
    # Check Power Dict
    power_dict_skew = out_skew.loss.get_power_dict()
    exp_power_dict_skew = {
        "stator core": np.float64(843.9902596031727),
        "stator joule": np.float64(7579.031160511535),
        "stator proximity": np.float64(10.177251957104662),
        "rotor core": np.float64(131.44773545261035),
        "rotor magnets": np.float64(6.810951828576413),
        "airgap windage": 0.1650942739887786,
        "stator core + stator joule + stator proximity + rotor core + rotor magnets + airgap windage": np.float64(
            8571.62245362699
        ),
        "total_power": np.float64(51908.33966357775),
    }
    assert len(power_dict_skew.keys()) == len(exp_power_dict_skew.keys())
    for key in power_dict_skew:
        assert power_dict_skew[key] == pytest.approx(exp_power_dict_skew[key], rel=1e-2)

    # Same with Bertotti skew
    out_skew1 = out_skew.copy()
    out_skew1.simu.loss = LossFEA(
        is_get_meshsolution=True,
        Tsta=100,
        type_skin_effect=1,
        type_loss_model_core="Bertotti",
        is_stacking_factor=True,
        is_calc_windage_loss=True,
    )

    out_skew1.loss = OutLoss()
    out_skew1.simu.loss.run()
    # Check Power Dict
    power_dict_skew1 = out_skew1.loss.get_power_dict()
    exp_power_dict_skew1 = {
        "stator core": np.float64(947.4377834715955),
        "stator joule": np.float64(7579.031160511535),
        "stator proximity": np.float64(10.177251957104662),
        "rotor core": np.float64(62.9250367839353),
        "rotor magnets": np.float64(6.810951828576413),
        "airgap windage": 0.1650942739887786,
        "stator core + stator joule + stator proximity + rotor core + rotor magnets + airgap windage": np.float64(
            8606.547278826736
        ),
        "total_power": np.float64(51908.33966357775),
    }
    assert len(power_dict_skew1.keys()) == len(exp_power_dict_skew1.keys())
    for key in power_dict_skew1:
        assert power_dict_skew1[key] == pytest.approx(
            exp_power_dict_skew1[key], rel=1e-2
        )

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
