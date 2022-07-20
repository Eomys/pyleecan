# -*- coding: utf-8 -*-

import sys

from numpy import pi, array
from pyleecan.Classes.LamSlotMulti import LamSlotMulti
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW22 import SlotW22

import pytest


class TestLamSlotMulti(object):
    """Test that the methods of LamSlotMulti behave like it should"""

    def test_build_geometry(self):
        """Check that the build_geometry works"""

        rotor = LamSlotMulti(Rint=0.2, Rext=0.7, is_internal=True, is_stator=False)

        # Reference slot definition
        Slot1 = SlotW10(
            Zs=12, W0=50e-3, H0=30e-3, W1=100e-3, H1=30e-3, H2=100e-3, W2=120e-3
        )
        Slot2 = SlotW22(Zs=12, W0=pi / 12, H0=50e-3, W2=pi / 6, H2=125e-3)

        # Reference slot are duplicated to get 5 of each in alternance
        slot_list = list()
        for ii in range(5):
            slot_list.append(SlotW10(init_dict=Slot1.as_dict()))
            slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

        # Two slots in the list are modified (bigger than the others)
        rotor.slot_list = slot_list

        rotor.slot_list[0].H2 = 300e-3
        rotor.slot_list[7].H2 = 300e-3
        # Set slots position
        rotor.alpha = array([0, 29, 60, 120, 150, 180, 210, 240, 300, 330]) * pi / 180

        result = rotor.build_geometry(sym=2)
        assert len(result) == 1

        rotor.is_internal = False
        rotor.is_stator = True

        result = rotor.build_geometry(sym=2)
        assert len(result) == 1

if __name__ == "__main__":
    a = TestLamSlotMulti()
    a.test_build_geometry()
    print("Done")
