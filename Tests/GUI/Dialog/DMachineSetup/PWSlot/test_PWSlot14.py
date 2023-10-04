# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.PWSlot14 import PWSlot14
from pyleecan.GUI.Resources import pixmap_dict


class TestPWSlot14(object):
    """Test that the widget PWSlot14 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlot14")
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
        self.material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        self.mat1 = Material(name="Mat1")
        self.mat2 = Material(name="Mat2")
        self.mat3 = Material(name="M400-50A")
        self.mat4 = Material(name="Mat4")
        self.material_dict[LIB_KEY] = [
            self.mat1,
            self.mat2,
            self.mat3,
        ]
        self.material_dict[MACH_KEY] = [
            self.mat4,
        ]
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2, mat_type=self.mat3)
        self.test_obj.slot = SlotW14(
            H0=0.10,
            H1=0.11,
            H3=0.12,
            W0=0.13,
            W3=0.14,
            wedge_type=1,
        )
        self.widget = PWSlot14(self.test_obj, self.material_dict)

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H3.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W3.value() == 0.14
        assert not self.widget.g_wedge.isChecked()
        assert self.widget.c_wedge_type.currentIndex() == 1

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H0, str(value))
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == value

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == value

    def test_set_H3(self):
        """Check that the Widget allow to update H3"""
        self.widget.lf_H3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H3, str(value))
        self.widget.lf_H3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H3 == value

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W0, str(value))
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == value

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W3, str(value))
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == value

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotW14(H0=0.005, H1=0.01, H3=0.025, W0=0.005, W3=0.02)
        self.widget = PWSlot14(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.03987 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.7, Rext=0.5)
        self.test_obj.slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=None, W3=0.16)
        self.widget = PWSlot14(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        self.test_obj.slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=0.31, W3=None)
        assert self.widget.check(self.test_obj) == "You must set W3 !"
        self.test_obj.slot = SlotW14(H0=0.10, H3=0.11, H1=None, W0=0.31, W3=0.16)
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        self.test_obj.slot = SlotW14(H0=0.10, H3=None, H1=0.12, W0=0.31, W3=0.16)
        assert self.widget.check(self.test_obj) == "You must set H3 !"
        self.test_obj.slot = SlotW14(H0=None, H3=0.11, H1=0.12, W0=0.31, W3=0.16)
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        self.test_obj.slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=0.31, W3=0.16)
        assert (
            self.widget.check(self.test_obj)
            == "The slot height is greater than the lamination !"
        )

    def test_set_wedge(self):
        """Check that the GUI enables to edit the wedges"""
        assert self.test_obj.slot.wedge_mat is None
        assert not self.widget.g_wedge.isChecked()
        # Add new wedge
        assert self.widget.w_wedge_mat.c_mat_type.count() == 0
        self.widget.g_wedge.setChecked(True)
        assert self.widget.w_wedge_mat.c_mat_type.count() == 4
        assert self.test_obj.slot.wedge_mat is not None
        assert self.test_obj.slot.wedge_mat.name == "M400-50A"
        # Change material
        assert self.widget.w_wedge_mat.c_mat_type.currentIndex() == 2
        self.widget.w_wedge_mat.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.slot.wedge_mat is not None
        assert self.test_obj.slot.wedge_mat.name == "Mat1"
        # Remove wedge
        self.widget.g_wedge.setChecked(False)
        assert self.test_obj.slot.wedge_mat is None
        # Add wedge again
        self.widget.g_wedge.setChecked(True)
        assert self.widget.w_wedge_mat.c_mat_type.count() == 4
        assert self.test_obj.slot.wedge_mat is not None
        assert self.test_obj.slot.wedge_mat.name == "M400-50A"

        # Add new type wedge
        self.widget.c_wedge_type.setCurrentIndex(1)
        assert str(self.widget.c_wedge_type.currentText()) == "Standard"
        assert self.test_obj.slot.wedge_type == 1


if __name__ == "__main__":
    a = TestPWSlot14()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    a.test_set_wedge()
    print("Done")
