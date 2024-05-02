# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
import matplotlib.pyplot as plt
from qtpy import QtWidgets
from qtpy.QtTest import QTest
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.SlotUD import SlotUD
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
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlotUD.PWSlotUD import PWSlotUD
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


class TestSWSlot(object):
    """Test that the widget SWSlot behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlot29")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = MachineSCIM()
        self.test_obj.stator = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.stator.slot = SlotW10(
            Zs=123,
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H1_is_rad=False,
        )
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)
        self.widget.is_test = True

    def test_init(self):
        """Check that the Widget initialize to the correct slot"""

        assert self.widget.si_Zs.value() == 123
        assert self.widget.c_slot_type.currentText() == "Slot Type 10"
        assert self.widget.c_slot_type.currentIndex() == 1
        assert type(self.widget.w_slot) == PWSlot10

        self.test_obj = MachineSCIM()
        self.test_obj.rotor = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.rotor.slot = SlotW10(
            Zs=123,
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H1_is_rad=False,
        )
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=False)

    def test_set_slot_11(self):
        """Check that you can edit a Slot 11"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW11(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 11"
        assert self.widget.c_slot_type.currentIndex() == 2
        assert type(self.widget.w_slot) == PWSlot11

    def test_set_slot_12(self):
        """Check that you can edit a Slot 12"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW12(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 12"
        assert self.widget.c_slot_type.currentIndex() == 3
        assert type(self.widget.w_slot) == PWSlot12

    def test_set_slot_13(self):
        """Check that you can edit a Slot 13"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW13(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 13"
        assert self.widget.c_slot_type.currentIndex() == 4
        assert type(self.widget.w_slot) == PWSlot13

    def test_set_slot_14(self):
        """Check that you can edit a Slot 14"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW14(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 14"
        assert self.widget.c_slot_type.currentIndex() == 5
        assert type(self.widget.w_slot) == PWSlot14

    def test_set_slot_15(self):
        """Check that you can edit a Slot 15"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW15(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 15"
        assert self.widget.c_slot_type.currentIndex() == 6
        assert type(self.widget.w_slot) == PWSlot15

    def test_set_slot_16(self):
        """Check that you can edit a Slot 16"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW16(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 16"
        assert self.widget.c_slot_type.currentIndex() == 7
        assert type(self.widget.w_slot) == PWSlot16

    def test_set_slot_21(self):
        """Check that you can edit a Slot 21"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW21(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 21"
        assert self.widget.c_slot_type.currentIndex() == 8
        assert type(self.widget.w_slot) == PWSlot21

    def test_set_slot_22(self):
        """Check that you can edit a Slot 22"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW22(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 22"
        assert self.widget.c_slot_type.currentIndex() == 9
        assert type(self.widget.w_slot) == PWSlot22

    def test_set_slot_23(self):
        """Check that you can edit a Slot 23"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW23(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 23"
        assert self.widget.c_slot_type.currentIndex() == 10
        assert type(self.widget.w_slot) == PWSlot23

    def test_set_slot_24(self):
        """Check that you can edit a Slot 24"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW24(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 24"
        assert self.widget.c_slot_type.currentIndex() == 11
        assert type(self.widget.w_slot) == PWSlot24

    def test_set_slot_25(self):
        """Check that you can edit a Slot 25"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW25(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 25"
        assert self.widget.c_slot_type.currentIndex() == 12
        assert type(self.widget.w_slot) == PWSlot25

    def test_set_slot_26(self):
        """Check that you can edit a Slot 26"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW26(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 26"
        assert self.widget.c_slot_type.currentIndex() == 13
        assert type(self.widget.w_slot) == PWSlot26

    def test_set_slot_27(self):
        """Check that you can edit a Slot 27"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW27(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 27"
        assert self.widget.c_slot_type.currentIndex() == 14
        assert type(self.widget.w_slot) == PWSlot27

    def test_set_slot_28(self):
        """Check that you can edit a Slot 28"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW28(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 28"
        assert self.widget.c_slot_type.currentIndex() == 15
        assert type(self.widget.w_slot) == PWSlot28

    def test_set_slot_29(self):
        """Check that you can edit a Slot 29"""
        Zs = int(uniform(1, 100))
        self.test_obj.stator.slot = SlotW29(Zs=Zs)
        self.widget = SWSlot(self.test_obj, material_dict=dict(), is_stator=True)

        assert self.widget.si_Zs.value() == Zs
        assert self.widget.c_slot_type.currentText() == "Slot Type 29"
        assert self.widget.c_slot_type.currentIndex() == 16
        assert type(self.widget.w_slot) == PWSlot29

    def test_set_Zs(self):
        """Check that the Widget allow to update Zs"""
        # Clear the field before writing the new value
        self.widget.si_Zs.clear()
        value = int(uniform(1, 100))
        self.widget.si_Zs.setValue(value)

        assert self.test_obj.stator.slot.Zs == value

    def test_set_slot_type(self):
        """Check that the slot_type can change"""
        self.widget.set_slot_type(1)
        assert self.widget.si_Zs.value() == 123

    def test_c_slot_type(self):
        """Check that the combobox allow to update the slot type"""
        slot_list = [
            SlotUD,
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
            PWSlotUD,
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
            self.widget.c_slot_type.setCurrentIndex(ii)
            assert type(self.test_obj.stator.slot) == slot_list[ii]
            assert type(self.widget.w_slot) == WIDGET_LIST[ii]
            assert self.widget.w_slot.w_out.out_Wlam.text() == "Stator width: 0.1 [m]"


if __name__ == "__main__":
    a = TestSWSlot()
    a.setup_class()
    a.setup_method()
    a.test_c_slot_type()
    a.teardown_class()
    print("Done")
