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
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52.PHoleM52 import PHoleM52


class test_PHoleM52(TestCase):
    """Test that the widget PHoleM52 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(HoleM52(H0=0.10, H1=0.11, H2=0.12, W0=0.13, W3=0.17))
        self.widget = PHoleM52(self.test_obj.hole[0])

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PHoleM52")
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
        self.assertEqual(self.widget.lf_W3.value(), 0.17)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W0, 0.31)
        self.assertEqual(self.test_obj.hole[0].W0, 0.31)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.323")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W3, 0.323)
        self.assertEqual(self.test_obj.hole[0].W3, 0.323)

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
