# -*- coding: utf-8 -*-

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM58 import HoleM58
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM58.PHoleM58 import PHoleM58
from Tests.GUI import gui_option  # Set unit to m
from pyleecan.Classes.Material import Material


import pytest


@pytest.mark.GUI
class test_PHoleM58(TestCase):
    """Test that the widget PHoleM58 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
            HoleM58(
                H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.17, R0=0.19
            )
        )
        self.test_obj.hole[0].magnet_0.mat_type.name = "Magnet3"

        self.matlib = list()
        self.matlib.append(Material(name="Magnet1"))
        self.matlib.append(Material(name="Magnet2"))
        self.matlib.append(Material(name="Magnet3"))

        self.widget = PHoleM58(self.test_obj.hole[0], self.matlib)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PHoleM58")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H0.value(), 0.10)
        self.assertEqual(self.widget.lf_H1.value(), 0.11)
        self.assertEqual(self.widget.lf_H2.value(), 0.12)
        self.assertEqual(self.widget.lf_W0.value(), 0.13)
        self.assertEqual(self.widget.lf_W1.value(), 0.14)
        self.assertEqual(self.widget.lf_W2.value(), 0.15)
        self.assertEqual(self.widget.lf_W3.value(), 0.17)
        self.assertEqual(self.widget.lf_R0.value(), 0.19)
        # Check material
        self.assertFalse(self.widget.w_mat_0.isHidden())
        self.assertEqual(self.widget.w_mat_0.c_mat_type.currentText(), "Magnet3")
        self.assertEqual(self.widget.w_mat_0.c_mat_type.currentIndex(), 2)

        self.test_obj.hole[0] = HoleM58(
            H0=0.20, H1=0.21, H2=0.22, W0=0.23, W1=0.24, W2=0.25, W3=0.27, R0=0.29
        )
        self.widget = PHoleM58(self.test_obj.hole[0])
        self.assertEqual(self.widget.lf_H0.value(), 0.20)
        self.assertEqual(self.widget.lf_H1.value(), 0.21)
        self.assertEqual(self.widget.lf_H2.value(), 0.22)
        self.assertEqual(self.widget.lf_W0.value(), 0.23)
        self.assertEqual(self.widget.lf_W1.value(), 0.24)
        self.assertEqual(self.widget.lf_W2.value(), 0.25)
        self.assertEqual(self.widget.lf_W3.value(), 0.27)
        self.assertEqual(self.widget.lf_R0.value(), 0.29)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W0, 0.31)
        self.assertEqual(self.test_obj.hole[0].W0, 0.31)

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W1, 0.32)
        self.assertEqual(self.test_obj.hole[0].W1, 0.32)

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W2, 0.33)
        self.assertEqual(self.test_obj.hole[0].W2, 0.33)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.323")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W3, 0.323)
        self.assertEqual(self.test_obj.hole[0].W3, 0.323)

    def test_set_R0(self):
        """Check that the Widget allow to update R0"""
        self.widget.lf_R0.clear()
        QTest.keyClicks(self.widget.lf_R0, "0.334")
        self.widget.lf_R0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.R0, 0.334)
        self.assertEqual(self.test_obj.hole[0].R0, 0.334)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H0, 0.34)
        self.assertEqual(self.test_obj.hole[0].H0, 0.34)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H1, 0.35)
        self.assertEqual(self.test_obj.hole[0].H1, 0.35)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H2, 0.36)
        self.assertEqual(self.test_obj.hole[0].H2, 0.36)

    def test_set_material_0(self):
        """Check that you can change the material of magnet_0"""
        self.widget.w_mat_0.c_mat_type.setCurrentIndex(0)

        self.assertEqual(self.widget.w_mat_0.c_mat_type.currentText(), "Magnet1")
        self.assertEqual(self.test_obj.hole[0].magnet_0.mat_type.name, "Magnet1")
