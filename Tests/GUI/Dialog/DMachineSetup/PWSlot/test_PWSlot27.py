# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
from qtpy import QtWidgets
from qtpy.QtTest import QTest
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot27.PWSlot27 import PWSlot27


class TestPWSlot27(object):
    """Test that the widget PWSlot27 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlot27")
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
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2, mat_type=None)
        self.test_obj.slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        self.widget = PWSlot27(self.test_obj, self.material_dict)

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        assert self.widget.lf_W3.value() == 0.16
        assert not self.widget.g_wedge.isChecked()

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

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H2, str(value))
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H2 == value

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W0, str(value))
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == value

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W1, str(value))
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == value

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W2, str(value))
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W2 == value

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W3, str(value))
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == value

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        self.test_obj.slot = SlotW27(
            Zs=6, H0=0.05, W0=30e-3, H1=0.125, W1=0.06, H2=0.05, W2=0.09, W3=0.04
        )
        self.widget = PWSlot27(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.2252 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=None, W2=0.15, W3=0.16
        )
        self.widget = PWSlot27(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set W1 !"
        self.test_obj.slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=None, W3=0.16
        )
        assert self.widget.check(self.test_obj) == "You must set W2 !"
        self.test_obj.slot = SlotW27(
            H0=None, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        self.test_obj.slot = SlotW27(
            H0=0.10, H1=None, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        self.test_obj.slot = SlotW27(
            H0=0.10, H1=0.11, H2=None, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        assert self.widget.check(self.test_obj) == "You must set H2 !"
        self.test_obj.slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=None
        )
        assert self.widget.check(self.test_obj) == "You must set W3 !"
        self.test_obj.slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=None, W1=0.14, W2=0.15, W3=0.16
        )
        assert self.widget.check(self.test_obj) == "You must set W0 !"

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


if __name__ == "__main__":
    a = TestPWSlot27()
    a.setup_class()
    a.setup_method()
    # a.test_init()
    a.test_set_wedge()
    a.teardown_class()
    print("Done")
