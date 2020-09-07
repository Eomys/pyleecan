# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52.PHoleM52 import PHoleM52
from pyleecan.Classes.Material import Material


import pytest


@pytest.mark.GUI
class TestPHoleM52(object):
    """Test that the widget PHoleM52 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(HoleM52(H0=0.10, H1=0.11, H2=0.12, W0=0.13, W3=0.17))
        self.test_obj.hole[0].magnet_0.mat_type.name = "Magnet2"

        self.matlib = MatLib()
        self.matlib.dict_mat["RefMatLib"] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        self.widget = PHoleM52(self.test_obj.hole[0], self.matlib)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PHoleM52")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W3.value() == 0.17
        # Check material
        assert not self.widget.w_mat_1.isHidden()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet2"
        assert self.widget.w_mat_1.c_mat_type.currentIndex() == 1

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W0 == 0.31
        assert self.test_obj.hole[0].W0 == 0.31

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        # Clear the field before writing the new value
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.323")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W3 == 0.323
        assert self.test_obj.hole[0].W3 == 0.323

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
