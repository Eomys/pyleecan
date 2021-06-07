import pytest
from os.path import join
import matplotlib.pyplot as plt
from numpy import linspace, pi

from pyleecan.Functions.load import load
from pyleecan.Classes.LamSlotMulti import LamSlotMulti
from pyleecan.Classes.SlotW22 import SlotW22

from pyleecan.definitions import DATA_DIR


@pytest.mark.SIPMSM
def test_LamSlotMulti():
    # Load machine
    SPMSM_001 = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))

    # New lamination main dimensions definition
    stator = LamSlotMulti(
        # Kf1=0.96,
        # L1=0.05,
        # Nrvd=0,
        # Wrvd=0,
        Rint=0.02785,
        Rext=0.05,
        is_internal=False,
        is_stator=True,
    )

    # New slots definition
    Slot1 = SPMSM_001.stator.slot.copy()  # reuse existing slot
    Slot2 = SPMSM_001.stator.slot.copy()
    Slot2.H0 = 0.002
    Slot2.H2 -= 0.002
    Slot2.W0 -= 0.15

    # Slots are duplicated to get 6 of each in alternance
    slot_list = list()
    for ii in range(6):
        slot_list.append(SlotW22(init_dict=Slot1.as_dict()))
        slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

    # Assign slots to stator and set positions
    stator.slot_list = slot_list
    stator.alpha = linspace(0, 360, 12, endpoint=False) * pi / 180

    # Assign stator to machine
    SPMSM_001.stator = stator
    SPMSM_001.plot()
    plt.show()


if __name__ == "__main__":
    test_LamSlotMulti()
