# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM53.PHoleM53 import PHoleM53
from pyleecan.Classes.Material import Material


import pytest


@pytest.mark.GUI
class test_PHoleM53(TestCase):
    """Test that the widget PHoleM53 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
            HoleM53(
                H0=0.10, H1=0.11, H2=0.12, H3=0.13, W1=0.14, W2=0.15, W3=0.16, W4=0.17
            )
        )
        self.test_obj.hole[0].magnet_0.mat_type.name = "Magnet3"
        self.test_obj.hole[0].magnet_1.mat_type.name = "Magnet2"

        self.matlib = list()
        self.matlib.append(Material(name="Magnet1"))
        self.matlib.append(Material(name="Magnet2"))
        self.matlib.append(Material(name="Magnet3"))
        self.widget = PHoleM53(self.test_obj.hole[0], self.matlib)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PHoleM53")
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
        self.assertEqual(self.widget.lf_H3.value(), 0.13)
        self.assertEqual(self.widget.lf_W1.value(), 0.14)
        self.assertEqual(self.widget.lf_W2.value(), 0.15)
        self.assertEqual(self.widget.lf_W3.value(), 0.16)
        self.assertEqual(self.widget.lf_W4.value(), 0.17)
        # Check material
        self.assertFalse(self.widget.w_mat_0.isHidden())
        self.assertEqual(self.widget.w_mat_0.c_mat_type.currentText(), "Magnet3")
        self.assertEqual(self.widget.w_mat_0.c_mat_type.currentIndex(), 2)
        self.assertFalse(self.widget.w_mat_1.isHidden())
        self.assertEqual(self.widget.w_mat_1.c_mat_type.currentText(), "Magnet2")
        self.assertEqual(self.widget.w_mat_1.c_mat_type.currentIndex(), 1)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        # Clear the field before writing the new value
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.311")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H0, 0.311)
        self.assertEqual(self.test_obj.hole[0].H0, 0.311)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.352")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H1, 0.352)
        self.assertEqual(self.test_obj.hole[0].H1, 0.352)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.363")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H2, 0.363)
        self.assertEqual(self.test_obj.hole[0].H2, 0.363)

    def test_set_H3(self):
        """Check that the Widget allow to update H3"""
        # Clear the field before writing the new value
        self.widget.lf_H3.clear()
        QTest.keyClicks(self.widget.lf_H3, "0.314")
        self.widget.lf_H3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H3, 0.314)
        self.assertEqual(self.test_obj.hole[0].H3, 0.314)

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.355")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W1, 0.355)
        self.assertEqual(self.test_obj.hole[0].W1, 0.355)

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.366")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W2, 0.366)
        self.assertEqual(self.test_obj.hole[0].W2, 0.366)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.357")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W3, 0.357)
        self.assertEqual(self.test_obj.hole[0].W3, 0.357)

    def test_set_W4(self):
        """Check that the Widget allow to update W4"""
        self.widget.lf_W4.clear()
        QTest.keyClicks(self.widget.lf_W4, "0.368")
        self.widget.lf_W4.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W4, 0.368)
        self.assertEqual(self.test_obj.hole[0].W4, 0.368)

    def test_set_material_0(self):
        """Check that you can change the material of magnet_0"""
        self.widget.w_mat_0.c_mat_type.setCurrentIndex(0)

        self.assertEqual(self.widget.w_mat_0.c_mat_type.currentText(), "Magnet1")
        self.assertEqual(self.test_obj.hole[0].magnet_0.mat_type.name, "Magnet1")

    def test_set_material_1(self):
        """Check that you can change the material of magnet_1"""
        self.widget.w_mat_1.c_mat_type.setCurrentIndex(0)

        self.assertEqual(self.widget.w_mat_1.c_mat_type.currentText(), "Magnet1")
        self.assertEqual(self.test_obj.hole[0].magnet_1.mat_type.name, "Magnet1")
