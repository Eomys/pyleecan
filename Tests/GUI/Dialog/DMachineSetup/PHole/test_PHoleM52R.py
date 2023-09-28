# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM52R import HoleM52R
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52R.PHoleM52R import PHoleM52R
from pyleecan.Classes.Material import Material
from Tests.GUI import gui_option  # Set unit as [m]

import pytest


class TestPHoleM52R(object):
    """Test that the widget PHoleM52R behave like it should"""

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestBoreShape")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        test_obj = LamHole(Rint=0.1, Rext=0.2)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM52R(H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.17, R0=0.18)
        )
        test_obj.hole[0].magnet_0.mat_type.name = "Magnet2"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        self.widget = PHoleM52R(test_obj.hole[0], material_dict)

        self.test_obj = test_obj
        self.material_dict = material_dict

        self.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.17
        assert self.widget.lf_R0.value() == 0.18
        # Check material
        assert not self.widget.w_mat_1.isHidden()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet2"
        assert self.widget.w_mat_1.c_mat_type.currentIndex() == 1

        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
            HoleM52R(H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.17, R0=0.18)
        )
        self.test_obj.hole[0].magnet_0 == None

        self.widget = PHoleM52R(self.test_obj.hole[0], self.material_dict)
        assert not self.widget.w_mat_1.isHidden()

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W0 == 0.31
        assert self.test_obj.hole[0].W0 == 0.31

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        # Clear the field before writing the new value
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.323")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W1 == 0.323
        assert self.test_obj.hole[0].W1 == 0.323

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        # Clear the field before writing the new value
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H0 == 0.34
        assert self.test_obj.hole[0].H0 == 0.34

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        # Clear the field before writing the new value
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H1 == 0.35
        assert self.test_obj.hole[0].H1 == 0.35

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        # Clear the field before writing the new value
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H2 == 0.36
        assert self.test_obj.hole[0].H2 == 0.36

    def test_set_R0(self):
        """Check that the Widget allow to update R0"""
        # Clear the field before writing the new value
        self.widget.lf_R0.clear()
        QTest.keyClicks(self.widget.lf_R0, "0.36")
        self.widget.lf_R0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.R0 == 0.36
        assert self.test_obj.hole[0].R0 == 0.36

    def test_set_material_0(self):
        """Check that you can change the material of mat_void"""
        self.widget.w_mat_0.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_0.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].mat_void.name == "Magnet1"

    def test_set_material_1(self):
        """Check that you can change the material of magnet_0"""
        self.widget.w_mat_1.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].magnet_0.mat_type.name == "Magnet1"

    def test_comp_output(self):
        """Check that you can compute the output only if the hole is correctly set"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
            HoleM52R(H0=0.0010, H1=0.11, H2=0.00012, W0=0.0013, W1=0.0017)
        )
        self.widget.hole = self.test_obj.hole[0]
        self.widget.comp_output()

        # Nan are there because the value are not correct for the sin, cos and tan methods. But with true values, it works.

        assert self.widget.out_slot_surface.text() == "Slot suface: 0.0005166 m²"
        assert self.widget.out_magnet_surface.text() == "Magnet surface: 0.000143 m²"
        assert self.widget.out_alpha.text() == "alpha: 0.02362 rad (1.353°)"


if __name__ == "__main__":
    a = TestPHoleM52R()
    a.setup_class()
    a.setup_method()
    a.test_comp_output()
    a.teardown_class()
    print("Done")
