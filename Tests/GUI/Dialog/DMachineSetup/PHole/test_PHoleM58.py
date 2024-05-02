# -*- coding: utf-8 -*-

import sys

import pytest
from qtpy import QtWidgets
from qtpy.QtTest import QTest
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.HoleM58 import HoleM58
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM58.PHoleM58 import PHoleM58
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY


class TestPHoleM58(object):
    """Test that the widget PHoleM58 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPHoleM58")
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
        test_obj = LamHole(Rint=0.1, Rext=0.2)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM58(
                H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.17, R0=0.19
            )
        )
        test_obj.hole[0].magnet_0.mat_type.name = "Magnet3"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        self.widget = PHoleM58(test_obj.hole[0], material_dict)
        self.test_obj = test_obj
        self.material_dict = material_dict

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        assert self.widget.lf_W3.value() == 0.17
        assert self.widget.lf_R0.value() == 0.19
        # Check material
        assert not self.widget.w_mat_1.isHidden()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet3"
        assert self.widget.w_mat_1.c_mat_type.currentIndex() == 2
        self.test_obj.hole[0] = HoleM58(
            H0=0.20, H1=0.21, H2=0.22, W0=0.23, W1=0.24, W2=0.25, W3=0.27, R0=0.29
        )
        self.widget = PHoleM58(self.test_obj.hole[0], self.material_dict)
        assert self.widget.lf_H0.value() == 0.20
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W0.value() == 0.23
        assert self.widget.lf_W1.value() == 0.24
        assert self.widget.lf_W2.value() == 0.25
        assert self.widget.lf_W3.value() == 0.27
        assert self.widget.lf_R0.value() == 0.29

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
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W1 == 0.32
        assert self.test_obj.hole[0].W1 == 0.32

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W2 == 0.33
        assert self.test_obj.hole[0].W2 == 0.33

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.323")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W3 == 0.323
        assert self.test_obj.hole[0].W3 == 0.323

    def test_set_R0(self):
        """Check that the Widget allow to update R0"""
        self.widget.lf_R0.clear()
        QTest.keyClicks(self.widget.lf_R0, "0.334")
        self.widget.lf_R0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.R0 == 0.334
        assert self.test_obj.hole[0].R0 == 0.334

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H0 == 0.34
        assert self.test_obj.hole[0].H0 == 0.34

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H1 == 0.35
        assert self.test_obj.hole[0].H1 == 0.35

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H2 == 0.36
        assert self.test_obj.hole[0].H2 == 0.36

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

    def test_PHoleM58_None_Magnet(self):
        """Check that you can create PHoleM58 with None for magnet_0"""
        self.test_obj.hole.append(
            HoleM58(
                H0=0.10,
                H1=0.11,
                H2=0.12,
                W0=0.13,
                W1=0.14,
                W2=0.15,
                W3=0.17,
                R0=0.19,
                magnet_0=None,
            )
        )

        self.widget = PHoleM58(self.test_obj.hole[1], self.material_dict)

        assert self.widget.W1 == 0
        assert self.widget.W2 == 0
        assert self.widget.w_mat_1.isHidden()


if __name__ == "__main__":
    a = TestPHoleM58()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    print("Done")
