# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW30 import SlotW30
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot30.PWSlot30 import PWSlot30


class TestPWSlot30(object):
    """Test that the widget PWSlot30 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlot30")
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
        self.test_obj.slot = SlotW30(
            H0=0.10, R1=0.11, H1=0.12, W0=0.13, W3=0.14, R2=0.15
        )
        self.widget = PWSlot30(self.test_obj, self.material_dict)

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_R1.value() == 0.11
        assert self.widget.lf_H1.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W3.value() == 0.14
        assert self.widget.lf_R2.value() == 0.15
        assert not self.widget.g_wedge.isChecked()

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H0, str(value))
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == value

    def test_set_R1(self):
        """Check that the Widget allow to update R1"""
        self.widget.lf_R1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_R1, str(value))
        self.widget.lf_R1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.R1 == value

    def test_set_R2(self):
        """Check that the Widget allow to update R2"""
        self.widget.lf_R2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_R2, str(value))
        self.widget.lf_R2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.R2 == value

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == value

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
        self.test_obj = LamSlotWind(
            Rint=35e-3,
            Rext=100e-3,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        self.test_obj.slot = SlotW30(
            Zs=12,
            W0=10e-3,
            W3=10e-3,
            H0=10e-3,
            H1=40e-3,
            R1=2e-3,
            R2=2e-3,
        )
        self.widget = PWSlot30(self.test_obj)
        msg = f"{self.widget.w_out.out_slot_height.text()}"
        assert (
            self.widget.w_out.out_slot_height.text() == "Slot height: 0.05013 [m]"
        ), msg

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW30(
            H0=0.10, H1=0.11, R1=0.12, W0=None, W3=0.16, R2=0.17
        )
        self.widget = PWSlot30(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        self.test_obj.slot = SlotW30(
            H0=0.10, H1=0.11, R1=0.12, W0=0.31, W3=None, R2=0.17
        )
        assert self.widget.check(self.test_obj) == "You must set W3 !"
        self.test_obj.slot = SlotW30(
            H0=0.10, H1=0.11, R1=None, W0=0.31, W3=0.16, R2=0.17
        )
        assert self.widget.check(self.test_obj) == "You must set R1 !"
        self.test_obj.slot = SlotW30(
            H0=0.10, H1=None, R1=0.12, W0=0.31, W3=0.16, R2=0.17
        )
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        self.test_obj.slot = SlotW30(
            H0=None, H1=0.11, R1=0.12, W0=0.31, W3=0.16, R2=0.17
        )
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        self.test_obj.slot = SlotW30(
            H0=0.10, H1=0.11, R1=0.1, W0=0.31, W3=0.16, R2=None
        )
        assert self.widget.check(self.test_obj) == "You must set R2 !"

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
    a = TestPWSlot30()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.test_output_txt()
    a.teardown_class()
    print("Done")
