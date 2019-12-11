# -*- coding: utf-8 -*-
"""
@date Created on Wed May 17 15:51:11 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
"""

import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM51.PHoleM51 import PHoleM51


class test_PHoleM51(TestCase):
    """Test that the widget PHoleM51 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
            HoleM51(
                H0=0.10,
                H1=0.11,
                H2=0.12,
                W0=0.13,
                W1=0.14,
                W2=0.15,
                W3=0.16,
                W4=0.17,
                W5=0.18,
                W6=0.19,
                W7=0.2,
            )
        )
        self.widget = PHoleM51(self.test_obj.hole[0])

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PHoleM51")
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
        self.assertEqual(self.widget.lf_W3.value(), 0.16)
        self.assertEqual(self.widget.lf_W4.value(), 0.17)
        self.assertEqual(self.widget.lf_W5.value(), 0.18)
        self.assertEqual(self.widget.lf_W6.value(), 0.19)
        self.assertEqual(self.widget.lf_W7.value(), 0.2)

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
        # Clear the field before writing the new value
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W1, 0.32)
        self.assertEqual(self.test_obj.hole[0].W1, 0.32)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.33")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W3, 0.33)
        self.assertEqual(self.test_obj.hole[0].W3, 0.33)

    def test_set_W4(self):
        """Check that the Widget allow to update W4"""
        # Clear the field before writing the new value
        self.widget.lf_W4.clear()
        QTest.keyClicks(self.widget.lf_W4, "0.34")
        self.widget.lf_W4.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W4, 0.34)
        self.assertEqual(self.test_obj.hole[0].W4, 0.34)

    def test_set_W5(self):
        """Check that the Widget allow to update W5"""
        # Clear the field before writing the new value
        self.widget.lf_W5.clear()
        QTest.keyClicks(self.widget.lf_W5, "0.35")
        self.widget.lf_W5.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W5, 0.35)
        self.assertEqual(self.test_obj.hole[0].W5, 0.35)

    def test_set_W6(self):
        """Check that the Widget allow to update W6"""
        # Clear the field before writing the new value
        self.widget.lf_W6.clear()
        QTest.keyClicks(self.widget.lf_W6, "0.36")
        self.widget.lf_W6.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W6, 0.36)
        self.assertEqual(self.test_obj.hole[0].W6, 0.36)

    def test_set_W7(self):
        """Check that the Widget allow to update W7"""
        # Clear the field before writing the new value
        self.widget.lf_W7.clear()
        QTest.keyClicks(self.widget.lf_W7, "0.37")
        self.widget.lf_W7.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W7, 0.37)
        self.assertEqual(self.test_obj.hole[0].W7, 0.37)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.38")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H0, 0.38)
        self.assertEqual(self.test_obj.hole[0].H0, 0.38)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.39")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H1, 0.39)
        self.assertEqual(self.test_obj.hole[0].H1, 0.39)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.40")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.H2, 0.40)
        self.assertEqual(self.test_obj.hole[0].H2, 0.40)
