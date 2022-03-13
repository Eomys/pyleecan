from os.path import join

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEMM import LossFEMM

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


def test_FEMM_Loss_Prius():
    """Test to calculate losses in Toyota_Prius using LossFEMM model"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    Ch = 143  # hysteresis loss coefficient [W/(m^3*T^2*Hz)]
    Ce = 0.530  # eddy current loss coefficients [W/(m^3*T^2*Hz^2)]
    Cprox = 1  # sigma_w * cond.Hwire * cond.Wwire

    simu = Simu1(name="test_FEMM_Loss_Prius", machine=machine)

    simu.input = InputCurrent(
        Nt_tot=20 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=1000, Id_ref=-100, Iq_ref=200),
        is_periodicity_t=True,
        is_periodicity_a=True,
    )

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=4,
        is_get_meshsolution=True,
    )

    simu.loss = LossFEMM(Ce=Ce, Cp=Cprox, Ch=Ch, is_get_meshsolution=True, Tsta=100)

    out = simu.run()

    ovl_loss = out.loss.get_loss_overall()

    out.loss.meshsolution.plot_contour(
        "freqs=sum",
        label="Loss",
        group_names=["stator core", "stator winding", "rotor core", "rotor magnets"],
        # clim=[2e4, 2e7],
    )

    out.loss.meshsolution.plot_contour(
        "freqs=sum",
        label="Loss",
        group_names=["stator core", "stator winding"],
        # clim=[2e4, 2e7],
    )

    out.loss.meshsolution.plot_contour(
        "freqs=sum",
        label="Loss",
        group_names=["rotor core", "rotor magnets"],
        # clim=[2e4, 2e7],
    )


# To run it without pytest
if __name__ == "__main__":
    out = test_FEMM_Loss_Prius()
