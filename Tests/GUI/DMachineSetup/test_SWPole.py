# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot60.PWSlot60 import PWSlot60
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot61.PWSlot61 import PWSlot61
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.SWPole import SWPole


import pytest


@pytest.mark.GUI
class TestSWPole(object):
    """Test that the widget SWPole behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = MachineWRSM()
        self.test_obj.rotor = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.rotor.slot = SlotW60(
            Zs=0, R1=0.10, H1=0.11, H2=0.12, W1=0.14, W2=0.15, H3=0.16, H4=0.17, W3=0.18
        )
        self.test_obj.rotor.winding.p = 4

        self.widget = SWPole(self.test_obj, matlib=[], is_stator=False)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test SWPole")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget initialize to the correct slot"""
        assert self.widget.in_Zs.text() == "Zs = 2*p = 8"
        assert self.widget.c_slot_type.currentIndex() == 0
        assert type(self.widget.w_slot) == PWSlot60

    def test_init_61(self):
        """Check that the Widget initialize to the correct slot"""
        self.test_obj.rotor.slot = SlotW61(
            Zs=0,
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.125,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        self.test_obj.rotor.winding.p = 8

        self.widget = SWPole(self.test_obj, matlib=[], is_stator=False)

        assert self.widget.in_Zs.text() == "Zs = 2*p = 16"
        assert self.widget.c_slot_type.currentIndex() == 1
        assert type(self.widget.w_slot) == PWSlot61

    def test_c_slot_type(self):
        """Check that the combobox allow to update the slot type"""

        self.widget.c_slot_type.setCurrentIndex(1)
        assert type(self.test_obj.rotor.slot) == SlotW61
        assert self.test_obj.rotor.slot.Zs == 8
        assert type(self.widget.w_slot) == PWSlot61

        self.widget.c_slot_type.setCurrentIndex(0)
        assert type(self.test_obj.rotor.slot) == SlotW60
        assert self.test_obj.rotor.slot.Zs == 8
        assert type(self.widget.w_slot) == PWSlot60
