# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotUD import SlotUD
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlotUD.PWSlotUD import PWSlotUD


import pytest


class TestPWSlotUD(object):
    """Test that the widget PWSlotUD behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlotUD")
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
        self.test_obj.slot = SlotUD(Zs=42)
        self.widget = PWSlotUD(self.test_obj, self.material_dict)

    @pytest.mark.SlotUD
    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert not self.widget.g_wedge.isChecked()
        self.test_obj.slot = SlotUD(
            wedge_mat=self.mat4,
        )
        self.widget = PWSlotUD(self.test_obj, self.material_dict)
        assert self.widget.g_wedge.isChecked()
        assert self.widget.w_wedge_mat.c_mat_type.count() == 4
        assert self.widget.w_wedge_mat.c_mat_type.currentText() == "Mat4"

    @pytest.mark.SlotUD
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

    @pytest.mark.SlotUD
    def test_open_dxf_gui(self):
        """Check that the DXF gui can be open"""
        assert self.widget.dxf_gui is None
        self.widget.b_dxf.clicked.emit()
        assert self.widget.dxf_gui is not None
        assert self.widget.dxf_gui.si_Zs.value() == 42
        self.widget.dxf_gui.close()


if __name__ == "__main__":
    a = TestPWSlotUD()
    a.setup_class()
    a.setup_method()
    # a.test_init()
    # a.test_set_wedge()
    a.test_open_dxf_gui()
    a.teardown_class()
    print("Done")
