# -*- coding: utf-8 -*-

import sys

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.PWSlot25 import PWSlot25


class TestPWSlot25(object):
    """Test that the widget PWSlot25 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlot25")
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
        self.test_obj.slot = SlotW25(H1=0.11, H2=0.12, W3=0.14, W4=0.15)
        self.widget = PWSlot25(self.test_obj, self.material_dict)

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W3.value() == 0.14
        assert self.widget.lf_W4.value() == 0.15
        assert not self.widget.g_wedge.isChecked()

        self.test_obj.slot = SlotW25(
            H1=0.21, H2=0.22, W3=0.24, W4=0.25, wedge_mat=self.mat2
        )
        self.widget = PWSlot25(self.test_obj, self.material_dict)
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W3.value() == 0.24
        assert self.widget.lf_W4.value() == 0.25
        assert self.widget.g_wedge.isChecked()
        assert self.widget.w_wedge_mat.c_mat_type.count() == 4
        assert self.widget.w_wedge_mat.c_mat_type.currentText() == "Mat2"

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.32")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == 0.32
        assert self.test_obj.slot.W3 == 0.32

    def test_set_W4(self):
        """Check that the Widget allow to update W4"""
        self.widget.lf_W4.clear()
        QTest.keyClicks(self.widget.lf_W4, "0.33")
        self.widget.lf_W4.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W4 == 0.33
        assert self.test_obj.slot.W4 == 0.33

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == 0.35
        assert self.test_obj.slot.H1 == 0.35

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H2 == 0.36
        assert self.test_obj.slot.H2 == 0.36

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=1,
            Wrvd=0.1,
        )
        self.test_obj.slot = SlotW25(Zs=12, W4=150e-3, W3=75e-3, H1=30e-3, H2=150e-3)
        self.widget = PWSlot25(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.1789 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW25(H2=0.10, H1=0.11, W4=None, W3=0.16)
        self.widget = PWSlot25(self.test_obj)
        # Missing
        assert self.widget.check(self.test_obj) == "You must set W4 !"
        self.test_obj.slot = SlotW25(H2=0.10, H1=0.11, W4=0.1, W3=None)
        assert self.widget.check(self.test_obj) == "You must set W3 !"
        self.test_obj.slot = SlotW25(H2=0.10, H1=None, W4=0.1, W3=0.16)
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        self.test_obj.slot = SlotW25(H2=None, H1=0.11, W4=0.1, W3=0.16)
        assert self.widget.check(self.test_obj) == "You must set H2 !"
        # Wrong
        self.test_obj.slot = SlotW25(Zs=4, H2=0.11, H1=0, W4=0.1, W3=0.16)
        assert (
            self.widget.check(self.test_obj)
            == "You must have H1>0 (use Slot 24 for H1=0)"
        )
        self.test_obj.slot = SlotW25(Zs=4, H2=0, H1=0.11, W4=0.1, W3=0.16)
        assert (
            self.widget.check(self.test_obj)
            == "You must have H2>0 (use Slot 24 for H2=0)"
        )
        self.test_obj.slot = SlotW25(Zs=4, H2=0.12, H1=0.11, W4=0.1, W3=0.1)
        assert (
            self.widget.check(self.test_obj)
            == "You must have W4 != W3 (use Slot 24 for W4=W3)"
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


if __name__ == "__main__":
    a = TestPWSlot25()
    a.setup_class()
    a.setup_method()
    a.test_check()
    a.teardown_class()
    print("Done")
