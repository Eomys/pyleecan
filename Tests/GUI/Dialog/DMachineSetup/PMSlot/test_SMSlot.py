# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.SlotM13 import SlotM13
from pyleecan.Classes.SlotM14 import SlotM14
from pyleecan.Classes.SlotM15 import SlotM15
from pyleecan.Classes.SlotM16 import SlotM16
from pyleecan.Classes.SlotM17 import SlotM17
from pyleecan.Classes.SlotM18 import SlotM18
from pyleecan.Classes.SlotM19 import SlotM19
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.SMSlot import SMSlot
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot12.PMSlot12 import PMSlot12
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot13.PMSlot13 import PMSlot13
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot14.PMSlot14 import PMSlot14
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot15.PMSlot15 import PMSlot15
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot16.PMSlot16 import PMSlot16
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.PMSlot17 import PMSlot17
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot18.PMSlot18 import PMSlot18
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot19.PMSlot19 import PMSlot19
import pytest
from Tests.GUI import gui_option  # Set unit as [m]


class TestSMSlot(object):
    """Test that the widget SMSlot behave like it should (for SIPMSM)"""

    def setup_method(self):
        test_obj = MachineSIPMSM()
        # For comp_output compatibility
        test_obj.stator = LamSlotWind(Rint=0.95, Rext=0.99)
        test_obj.rotor = LamSlotMag(Rint=0.1, Rext=0.9)
        test_obj.rotor.slot = SlotM11(
            Zs=8, W0=pi / 24, H0=5e-3, Wmag=pi / 24, Hmag=3e-3
        )
        test_obj.rotor.magnet.mat_type.name = "test3"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        self.widget = SMSlot(
            machine=test_obj, material_dict=material_dict, is_stator=False
        )
        self.widget.is_test = True
        self.test_obj = test_obj

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSMSlot")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the GUI initialize correctly"""
        # To remember to update after adding a new type
        assert self.widget.c_slot_type.count() == 10

        assert self.widget.c_slot_type.currentIndex() == 1
        assert self.widget.c_slot_type.currentText() == "Polar Magnet"
        assert isinstance(self.widget.w_slot, PMSlot11)
        assert self.widget.w_mat.in_mat_type.text() == "mat_mag:"
        assert self.widget.w_mat.c_mat_type.count() == 3
        assert self.widget.w_mat.c_mat_type.currentIndex() == 2
        assert (
            self.widget.w_slot.w_out.out_wind_surface.text()
            == "Active surface: 0.0003521 [m²]"
        )

    def test_set_material(self):
        """Check that you can change the material"""
        self.widget.w_mat.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.rotor.magnet.mat_type.name == "test1"
        assert self.test_obj.rotor.magnet.mat_type.elec.rho == 0.31

    def test_set_type_magnetization(self):
        """Check that you can change tha magnetization"""
        # type_magnetization set test
        self.widget.c_type_magnetization.setCurrentIndex(2)
        assert self.test_obj.rotor.magnet.type_magnetization == 2
        self.widget.c_type_magnetization.setCurrentIndex(0)
        assert self.test_obj.rotor.magnet.type_magnetization == 0

    def test_set_type_10(self):
        """Check that the Widget is able to set Magnet type 10"""
        self.widget.c_slot_type.setCurrentIndex(0)
        assert type(self.widget.w_slot) == PMSlot10
        assert self.widget.c_slot_type.currentText() == "Rectangular Magnet"
        assert type(self.test_obj.rotor.slot) == SlotM10

    def test_set_type_11(self):
        """Check that the Widget is able to set Magnet type 11"""
        self.widget.c_slot_type.setCurrentIndex(1)
        assert type(self.widget.w_slot) == PMSlot11
        assert self.widget.c_slot_type.currentText() == "Polar Magnet"
        assert type(self.test_obj.rotor.slot) == SlotM11

    def test_set_type_12(self):
        """Check that the Widget is able to set Magnet type 12"""
        self.widget.c_slot_type.setCurrentIndex(2)
        assert type(self.widget.w_slot) == PMSlot12
        assert (
            self.widget.c_slot_type.currentText() == "Rectangular Magnet with polar top"
        )
        assert type(self.test_obj.rotor.slot) == SlotM12

    def test_set_type_13(self):
        """Check that the Widget is able to set Magnet type 13"""
        self.widget.c_slot_type.setCurrentIndex(3)
        assert type(self.widget.w_slot) == PMSlot13
        assert (
            self.widget.c_slot_type.currentText()
            == "Rectangular Magnet with curved top"
        )
        assert type(self.test_obj.rotor.slot) == SlotM13

    def test_set_type_14(self):
        """Check that the Widget is able to set Magnet type 14"""
        self.widget.c_slot_type.setCurrentIndex(4)
        assert type(self.widget.w_slot) == PMSlot14
        assert self.widget.c_slot_type.currentText() == "Polar Magnet with curved top"
        assert type(self.test_obj.rotor.slot) == SlotM14

    def test_set_type_15(self):
        """Check that the Widget is able to set Magnet type 15"""
        self.widget.c_slot_type.setCurrentIndex(5)
        assert type(self.widget.w_slot) == PMSlot15
        assert (
            self.widget.c_slot_type.currentText()
            == "Polar Magnet with curved top and parallel sides"
        )
        assert type(self.test_obj.rotor.slot) == SlotM15

    def test_set_type_16(self):
        """Check that the Widget is able to set Magnet type 16"""
        self.widget.c_slot_type.setCurrentIndex(6)
        assert type(self.widget.w_slot) == PMSlot16
        assert self.widget.c_slot_type.currentText() == "Spoke Rectangular Magnet"
        assert type(self.test_obj.rotor.slot) == SlotM16

    def test_set_type_17(self):
        """Check that the Widget is able to set Magnet type 17"""
        self.widget.c_slot_type.setCurrentIndex(7)
        assert type(self.widget.w_slot) == PMSlot17
        assert (
            self.widget.c_slot_type.currentText()
            == "Cylindrical magnet (no lamination)"
        )
        assert type(self.test_obj.rotor.slot) == SlotM17

    def test_set_type_18(self):
        """Check that the Widget is able to set Magnet type 18"""
        self.widget.c_slot_type.setCurrentIndex(8)
        assert type(self.widget.w_slot) == PMSlot18
        assert self.widget.c_slot_type.currentText() == "Ring Magnet"
        assert type(self.test_obj.rotor.slot) == SlotM18

    def test_set_type_19(self):
        """Check that the Widget is able to set Magnet type 19"""
        self.widget.c_slot_type.setCurrentIndex(9)
        assert type(self.widget.w_slot) == PMSlot19
        assert (
            self.widget.c_slot_type.currentText() == "Trapezoidal Magnet with polar top"
        )
        assert type(self.test_obj.rotor.slot) == SlotM19


if __name__ == "__main__":
    a = TestSMSlot()
    a.setup_class()
    a.setup_method()
    a.test_plot_schematics()
    a.teardown_class()
    print("Done")
