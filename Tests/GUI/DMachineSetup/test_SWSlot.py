# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW15 import SlotW15
from pyleecan.Classes.SlotW16 import SlotW16
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.Classes.SlotW29 import SlotW29
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot10.PWSlot10 import PWSlot10
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot11.PWSlot11 import PWSlot11
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot12.PWSlot12 import PWSlot12
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot13.PWSlot13 import PWSlot13
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.PWSlot14 import PWSlot14
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot15.PWSlot15 import PWSlot15
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot16.PWSlot16 import PWSlot16
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot21.PWSlot21 import PWSlot21
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.PWSlot22 import PWSlot22
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot23.PWSlot23 import PWSlot23
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot24.PWSlot24 import PWSlot24
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.PWSlot25 import PWSlot25
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot26.PWSlot26 import PWSlot26
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot27.PWSlot27 import PWSlot27
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.PWSlot28 import PWSlot28
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot29.PWSlot29 import PWSlot29
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.SWSlot import SWSlot


import pytest


class TestSWSlot(object):
    """Test that the widget SWSlot behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.stator.slot = SlotW10(
            Zs=123,
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H1_is_rad=False,
        )
        widget = SWSlot(test_obj, matlib=[], is_stator=True)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget initialize to the correct slot"""

        assert setup["widget"].si_Zs.value() == 123
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 10"
        assert setup["widget"].c_slot_type.currentIndex() == 0
        assert type(setup["widget"].w_slot) == PWSlot10

        setup["test_obj"] = MachineSCIM()
        setup["test_obj"].rotor = LamSlotWind(Rint=0.1, Rext=0.2)
        setup["test_obj"].rotor.slot = SlotW10(
            Zs=123,
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H1_is_rad=False,
        )
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=False)

    def test_set_slot_11(self, setup):
        """Check that you can edit a Slot 11"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW11(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 11"
        assert setup["widget"].c_slot_type.currentIndex() == 1
        assert type(setup["widget"].w_slot) == PWSlot11

    def test_set_slot_12(self, setup):
        """Check that you can edit a Slot 12"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW12(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 12"
        assert setup["widget"].c_slot_type.currentIndex() == 2
        assert type(setup["widget"].w_slot) == PWSlot12

    def test_set_slot_13(self, setup):
        """Check that you can edit a Slot 13"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW13(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 13"
        assert setup["widget"].c_slot_type.currentIndex() == 3
        assert type(setup["widget"].w_slot) == PWSlot13

    def test_set_slot_14(self, setup):
        """Check that you can edit a Slot 14"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW14(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 14"
        assert setup["widget"].c_slot_type.currentIndex() == 4
        assert type(setup["widget"].w_slot) == PWSlot14

    def test_set_slot_15(self, setup):
        """Check that you can edit a Slot 15"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW15(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 15"
        assert setup["widget"].c_slot_type.currentIndex() == 5
        assert type(setup["widget"].w_slot) == PWSlot15

    def test_set_slot_16(self, setup):
        """Check that you can edit a Slot 16"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW16(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 16"
        assert setup["widget"].c_slot_type.currentIndex() == 6
        assert type(setup["widget"].w_slot) == PWSlot16

    def test_set_slot_21(self, setup):
        """Check that you can edit a Slot 21"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW21(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 21"
        assert setup["widget"].c_slot_type.currentIndex() == 7
        assert type(setup["widget"].w_slot) == PWSlot21

    def test_set_slot_22(self, setup):
        """Check that you can edit a Slot 22"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW22(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 22"
        assert setup["widget"].c_slot_type.currentIndex() == 8
        assert type(setup["widget"].w_slot) == PWSlot22

    def test_set_slot_23(self, setup):
        """Check that you can edit a Slot 23"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW23(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 23"
        assert setup["widget"].c_slot_type.currentIndex() == 9
        assert type(setup["widget"].w_slot) == PWSlot23

    def test_set_slot_24(self, setup):
        """Check that you can edit a Slot 24"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW24(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 24"
        assert setup["widget"].c_slot_type.currentIndex() == 10
        assert type(setup["widget"].w_slot) == PWSlot24

    def test_set_slot_25(self, setup):
        """Check that you can edit a Slot 25"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW25(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 25"
        assert setup["widget"].c_slot_type.currentIndex() == 11
        assert type(setup["widget"].w_slot) == PWSlot25

    def test_set_slot_26(self, setup):
        """Check that you can edit a Slot 26"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW26(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 26"
        assert setup["widget"].c_slot_type.currentIndex() == 12
        assert type(setup["widget"].w_slot) == PWSlot26

    def test_set_slot_27(self, setup):
        """Check that you can edit a Slot 27"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW27(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 27"
        assert setup["widget"].c_slot_type.currentIndex() == 13
        assert type(setup["widget"].w_slot) == PWSlot27

    def test_set_slot_28(self, setup):
        """Check that you can edit a Slot 28"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW28(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 28"
        assert setup["widget"].c_slot_type.currentIndex() == 14
        assert type(setup["widget"].w_slot) == PWSlot28

    def test_set_slot_29(self, setup):
        """Check that you can edit a Slot 29"""
        Zs = int(uniform(1, 100))
        setup["test_obj"].stator.slot = SlotW29(Zs=Zs)
        setup["widget"] = SWSlot(setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_Zs.value() == Zs
        assert setup["widget"].c_slot_type.currentText() == "Slot Type 29"
        assert setup["widget"].c_slot_type.currentIndex() == 15
        assert type(setup["widget"].w_slot) == PWSlot29

    def test_set_Zs(self, setup):
        """Check that the Widget allow to update Zs"""
        # Clear the field before writing the new value
        setup["widget"].si_Zs.clear()
        value = int(uniform(1, 100))
        QTest.keyClicks(setup["widget"].si_Zs, str(value))
        setup["widget"].si_Zs.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.slot.Zs == value

    def test_set_slot_type(self, setup):
        """Check that the slot_type can change"""
        setup["widget"].set_slot_type(1)
        setup["widget"].set_slot_type(1)
        assert setup["widget"].si_Zs.value() == 123

    def test_c_slot_type(self, setup):
        """Check that the combobox allow to update the slot type"""
        slot_list = [
            SlotW10,
            SlotW11,
            SlotW12,
            SlotW13,
            SlotW14,
            SlotW15,
            SlotW16,
            SlotW21,
            SlotW22,
            SlotW23,
            SlotW24,
            SlotW25,
            SlotW26,
            SlotW27,
            SlotW28,
            SlotW29,
        ]
        WIDGET_LIST = [
            PWSlot10,
            PWSlot11,
            PWSlot12,
            PWSlot13,
            PWSlot14,
            PWSlot15,
            PWSlot16,
            PWSlot21,
            PWSlot22,
            PWSlot23,
            PWSlot24,
            PWSlot25,
            PWSlot26,
            PWSlot27,
            PWSlot28,
            PWSlot29,
        ]
        for ii in range(len(WIDGET_LIST)):
            setup["widget"].c_slot_type.setCurrentIndex(ii)
            assert type(setup["test_obj"].stator.slot) == slot_list[ii]
            assert type(setup["widget"].w_slot) == WIDGET_LIST[ii]
            assert (
                setup["widget"].w_slot.w_out.out_Wlam.text() == "Stator width: 0.1 [m]"
            )
