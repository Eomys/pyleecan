import pytest
from os.path import join
import matplotlib.pyplot as plt
from numpy import linspace, pi

from pyleecan.Functions.load import load
from pyleecan.Classes.LamSlotMultiWind import LamSlotMultiWind
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.Classes.NotchEvenDist import NotchEvenDist

from pyleecan.definitions import DATA_DIR
from Tests import save_plot_path as save_path


@pytest.mark.LamSlotMulti
def test_LamSlotMultiWind(is_show_fig=False):
    # Load machine
    SPMSM_001 = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))

    # New lamination main dimensions definition
    stator = LamSlotMultiWind(
        Kf1=0.96,
        L1=0.05,
        Nrvd=0,
        Wrvd=0,
        Rint=0.02785,
        Rext=0.05,
        is_internal=False,
        is_stator=True,
        winding=SPMSM_001.stator.winding.copy(),
        mat_type=SPMSM_001.stator.mat_type.copy(),
    )

    # New slots definition
    Slot1 = SPMSM_001.stator.slot.copy()
    Slot2 = SPMSM_001.stator.slot.copy()
    Slot2.H0 = 0.002
    Slot2.H2 -= 0.002
    Slot2.W0 -= 0.15
    Slot2.is_bore = False

    # Slots are duplicated to get 6 of each in alternance
    slot_list = list()
    for ii in range(6):
        slot_list.append(SlotW22(init_dict=Slot1.as_dict()))
        slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

    # Assign slots to stator and set positions
    stator.slot_list = slot_list
    stator.alpha = linspace(0, 360, 12, endpoint=False) * pi / 180 + pi / 12

    # Define rectangular notches
    Slot3 = SlotW11(
        Zs=6,
        W0=0.006,
        H0=0.001,
        H1=0.001,
        W1=0.006,
        H2=0.001,
        W2=0.006,
        R1=0.0004,
        is_bore=False,
    )
    notch_1 = NotchEvenDist(notch_shape=Slot3, alpha=pi / 6)
    Slot4 = SlotCirc(Zs=6, W0=0.0035 * 2, H0=0.0035, is_bore=False)
    notch_2 = NotchEvenDist(notch_shape=Slot4, alpha=2 * pi / 6)
    stator.notch = [notch_1, notch_2]

    # Assign stator to machine
    SPMSM_001.stator = stator

    # Plot the machine
    SPMSM_001.plot(
        is_show_fig=is_show_fig, save_path=join(save_path, "test_LamSlotMultiWind.png")
    )


if __name__ == "__main__":
    test_LamSlotMultiWind(is_show_fig=True)
    plt.show()
