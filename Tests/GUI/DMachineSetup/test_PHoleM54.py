# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM54.PHoleM54 import PHoleM54
from pyleecan.Classes.Material import Material


class test_PHoleM54(TestCase):
    """Test that the widget PHoleM54 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(HoleM54(H0=0.10, H1=0.11, W0=0.12, R1=0.13))
        self.widget = PHoleM54(self.test_obj.hole[0], matlib=[])

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PHoleM54")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H0.value(), 0.10)
        self.assertEqual(self.widget.lf_H1.value(), 0.11)
        self.assertEqual(self.widget.lf_W0.value(), 0.12)
        self.assertEqual(self.widget.lf_R1.value(), 0.13)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.W0, 0.31)
        self.assertEqual(self.test_obj.hole[0].W0, 0.31)

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

    def test_set_R1(self):
        """Check that the Widget allow to update R1"""
        self.widget.lf_R1.clear()
        QTest.keyClicks(self.widget.lf_R1, "0.36")
        self.widget.lf_R1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.hole.R1, 0.36)
        self.assertEqual(self.test_obj.hole[0].R1, 0.36)
