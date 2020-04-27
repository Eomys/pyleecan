# -*- coding: utf-8 -*-

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot12.PWSlot12 import PWSlot12


class test_PWSlot12(TestCase):
    """Test that the widget PWSlot12 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW12(H0=0.10, H1=0.11, R1=0.12, R2=0.13)
        self.widget = PWSlot12(self.test_obj)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot12")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H0.value(), 0.10)
        self.assertEqual(self.widget.lf_H1.value(), 0.11)
        self.assertEqual(self.widget.lf_R1.value(), 0.12)
        self.assertEqual(self.widget.lf_R2.value(), 0.13)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H0, str(value))
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H0, value)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H1, value)

    def test_set_R1(self):
        """Check that the Widget allow to update R1"""
        self.widget.lf_R1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_R1, str(value))
        self.widget.lf_R1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.R1, value)

    def test_set_R2(self):
        """Check that the Widget allow to update R2"""
        self.widget.lf_R2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_R2, str(value))
        self.widget.lf_R2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.R2, value)

    def test_output_txt(self):
        """Check that the Output text is computed and correct
        """
        self.test_obj.slot = SlotW12(H0=0.01, H1=0.02, R1=0.005, R2=0.005)
        self.widget = PWSlot12(self.test_obj)
        self.assertEqual(
            self.widget.w_out.out_slot_height.text(), "Slot height: 0.04506 m"
        )
