# -*- coding: utf-8 -*-

import sys

from qtpy import QtWidgets
from qtpy.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Notch import Notch
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY


import pytest


class TestPMSlot10(object):
    """Test that the widget PMSlot10 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM10(H0=0.10, W0=0.13, W1=0.14, H1=0.15)
        self.test_obj.magnet = Magnet(type_magnetization=2)

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        self.material_dict = material_dict

        self.widget = PMSlot10(
            self.test_obj, notch_obj=None, material_dict=self.material_dict
        )

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot10")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""
        assert self.widget.w_mag.c_type_magnetization.currentIndex() == 2
        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.15
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Check Unit
        assert self.widget.unit_W0.text() == "[m]"
        # Change value in GUI
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == 0.31
        assert self.test_obj.slot.W0 == 0.31

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        # Check Unit
        assert self.widget.unit_W1.text() == "[m]"
        # Change value in GUI
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.33")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == 0.33
        assert self.test_obj.slot.W1 == 0.33

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        # Check Unit
        assert self.widget.unit_H0.text() == "[m]"
        # Change value in GUI
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == 0.34
        assert self.test_obj.slot.H0 == 0.34

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        # Check Unit
        assert self.widget.unit_H1.text() == "[m]"
        # Change value in GUI
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.36")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == pytest.approx(0.36)
        assert self.test_obj.slot.H1 == pytest.approx(0.36)

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotM10(H0=0.005, H1=0.005, W0=0.01, W1=0.01)
        self.widget = PMSlot10(
            self.test_obj, notch_obj=None, material_dict=self.material_dict
        )
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.005063 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        # H0
        self.test_obj.slot = SlotM10(H0=None, H1=0.10, W0=0.10, W1=0.10)
        self.widget = PMSlot10(
            self.test_obj, notch_obj=None, material_dict=self.material_dict
        )
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        # H1
        self.test_obj.slot = SlotM10(H0=0.10, H1=None, W0=0.10, W1=0.10)
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        # W0
        self.test_obj.slot = SlotM10(H0=0.10, H1=0.10, W0=None, W1=0.10)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        # W1
        self.test_obj.slot = SlotM10(H0=0.10, H1=0.10, W0=0.10, W1=None)
        assert self.widget.check(self.test_obj) == "You must set W1 !"

    def test_set_material(self):
        """Check that you can change the material"""
        self.widget.w_mag.w_mat.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.magnet.mat_type.name == "test1"
        assert self.test_obj.magnet.mat_type.elec.rho == 0.31
        self.widget.w_mag.w_mat.c_mat_type.setCurrentIndex(2)
        assert self.test_obj.magnet.mat_type.name == "test3"
        assert self.test_obj.magnet.mat_type.elec.rho == 0.33

    def test_set_type_magnetization(self):
        """Check that you can change tha magnetization"""
        # type_magnetization set test
        self.widget.w_mag.c_type_magnetization.setCurrentIndex(2)
        assert self.test_obj.magnet.type_magnetization == 2
        self.widget.w_mag.c_type_magnetization.setCurrentIndex(0)
        assert self.test_obj.magnet.type_magnetization == 0

    def test_set_Wkey(self):
        """Check that the Widget allow to update Wkey"""

        # test if widget is disabled if notch_obj=None
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM10(H0=0.10, W0=0.13, W1=0.14, H1=0.15)
        self.mat1 = Material(name="Steel1")
        self.mat2 = Material(name="Steel2")
        self.material_dict = {LIB_KEY: [self.mat2, self.mat1], MACH_KEY: list()}

        # Empty notch
        notch = Notch()
        self.widget = PMSlot10(
            self.test_obj, material_dict=self.material_dict, notch_obj=notch
        )
        assert not self.widget.g_key.isChecked()
        assert self.widget.unit_W1.isEnabled() == False
        assert self.widget.in_W1.isEnabled() == False
        assert self.widget.lf_W1.isEnabled() == False

        # Notch with key
        notch = Notch(key_mat=self.mat1)
        self.widget = PMSlot10(
            self.test_obj, material_dict=self.material_dict, notch_obj=notch
        )

        assert self.widget.g_key.isChecked()
        assert self.widget.unit_W1.isEnabled() == True
        assert self.widget.in_W1.isEnabled() == True
        assert self.widget.lf_W1.isEnabled() == True
        self.widget.g_key.setChecked(False)
        assert self.widget.notch_obj.key_mat is None
        assert self.widget.unit_W1.isEnabled() == False
        assert self.widget.in_W1.isEnabled() == False
        assert self.widget.lf_W1.isEnabled() == False
        self.widget.g_key.setChecked(True)
        assert self.widget.notch_obj.key_mat.name == "Steel1"
        assert self.widget.w_key_mat.c_mat_type.currentIndex() == 1
        assert self.widget.w_key_mat.c_mat_type.currentText() == "Steel1"  # default
        # Check Unit
        assert self.widget.unit_W1.text() == "[m]"
        # Change value in GUI
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.61")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == 0.61

    def test_set_Hkey(self):
        """Check that the Widget allow to update Hkey"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM10(H0=0.10, W0=0.13, W1=0.14, H1=0.15)
        self.mat1 = Material(name="Steel1")
        self.mat2 = Material(name="Steel2")
        self.material_dict = {LIB_KEY: [self.mat2, self.mat1], MACH_KEY: list()}
        # Empty notch
        notch = Notch()
        self.widget = PMSlot10(
            self.test_obj, material_dict=self.material_dict, notch_obj=notch
        )
        assert not self.widget.g_key.isChecked()
        assert self.widget.unit_H1.isEnabled() == False
        assert self.widget.in_H1.isEnabled() == False
        assert self.widget.lf_H1.isEnabled() == False

        # Notch with key
        notch = Notch(key_mat=self.mat1)
        self.widget = PMSlot10(
            self.test_obj, material_dict=self.material_dict, notch_obj=notch
        )
        assert self.widget.g_key.isChecked()
        assert self.widget.unit_H1.isEnabled() == True
        assert self.widget.in_H1.isEnabled() == True
        assert self.widget.lf_H1.isEnabled() == True

        self.widget.g_key.setChecked(False)
        assert self.widget.notch_obj.key_mat is None
        assert self.widget.unit_H1.isEnabled() == False
        assert self.widget.in_H1.isEnabled() == False
        assert self.widget.lf_H1.isEnabled() == False
        self.widget.g_key.setChecked(True)
        assert self.widget.notch_obj.key_mat.name == "Steel1"
        assert self.widget.w_key_mat.c_mat_type.currentIndex() == 1
        assert self.widget.w_key_mat.c_mat_type.currentText() == "Steel1"  # default

        # Check Unit
        assert self.widget.unit_H1.text() == "[m]"
        # Change value in GUI
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.61")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == 0.61


if __name__ == "__main__":
    a = TestPMSlot10()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.test_output_txt()
    a.teardown_class()
    a.test_set_material()
    a.test_set_Wkey()
    print("Done")
