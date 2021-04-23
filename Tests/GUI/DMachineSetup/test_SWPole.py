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


class TestSWPole(object):
    """Test that the widget SWPole behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineWRSM()
        test_obj.rotor = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.rotor.slot = SlotW60(
            Zs=0, R1=0.10, H1=0.11, H2=0.12, W1=0.14, W2=0.15, H3=0.16, H4=0.17, W3=0.18
        )
        test_obj.rotor.winding.p = 4

        widget = SWPole(test_obj, matlib=[], is_stator=False)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget initialize to the correct slot"""
        assert setup["widget"].in_Zs.text() == "Zs = 2*p = 8"
        assert setup["widget"].c_slot_type.currentIndex() == 0
        assert type(setup["widget"].w_slot) == PWSlot60

    def test_init_61(self, setup):
        """Check that the Widget initialize to the correct slot"""
        setup["test_obj"].rotor.slot = SlotW61(
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
        setup["test_obj"].rotor.winding.p = 8

        setup["widget"] = SWPole(setup["test_obj"], matlib=[], is_stator=False)

        assert setup["widget"].in_Zs.text() == "Zs = 2*p = 16"
        assert setup["widget"].c_slot_type.currentIndex() == 1
        assert type(setup["widget"].w_slot) == PWSlot61

    def test_c_slot_type(self, setup):
        """Check that the combobox allow to update the slot type"""

        setup["widget"].c_slot_type.setCurrentIndex(1)
        assert type(setup["test_obj"].rotor.slot) == SlotW61
        assert setup["test_obj"].rotor.slot.Zs == 8
        assert type(setup["widget"].w_slot) == PWSlot61

        setup["widget"].c_slot_type.setCurrentIndex(0)
        assert type(setup["test_obj"].rotor.slot) == SlotW60
        assert setup["test_obj"].rotor.slot.Zs == 8
        assert type(setup["widget"].w_slot) == PWSlot60
