# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from numpy import pi
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.PWSlot22 import PWSlot22


import pytest


@pytest.mark.GUI
class test_PWSlot22(TestCase):
    """Test that the widget PWSlot22 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW22(H0=0.10, H2=0.12, W0=0.13, W2=0.15)
        self.widget = PWSlot22(self.test_obj)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot22")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H0.value(), 0.10)
        self.assertEqual(self.widget.lf_H2.value(), 0.12)
        self.assertEqual(self.widget.lf_W0.value(), 0.13)
        self.assertEqual(self.widget.lf_W2.value(), 0.15)

        self.test_obj.slot = SlotW22(H0=0.20, H2=0.22, W0=0.23, W2=0.25)
        self.widget = PWSlot22(self.test_obj)
        self.assertEqual(self.widget.lf_H0.value(), 0.20)
        self.assertEqual(self.widget.lf_H2.value(), 0.22)
        self.assertEqual(self.widget.lf_W0.value(), 0.23)
        self.assertEqual(self.widget.lf_W2.value(), 0.25)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W0, 0.31)
        self.assertEqual(self.test_obj.slot.W0, 0.31)

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W2, 0.33)
        self.assertEqual(self.test_obj.slot.W2, 0.33)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H0, 0.34)
        self.assertEqual(self.test_obj.slot.H0, 0.34)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H2, 0.36)
        self.assertEqual(self.test_obj.slot.H2, 0.36)

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.8,
            Nrvd=4,
            Wrvd=0.05,
        )
        self.test_obj.slot = SlotW22(Zs=6, W0=pi / 20, W2=pi / 10, H0=20e-3, H2=150e-3)
        self.widget = PWSlot22(self.test_obj)
        self.assertEqual(
            self.widget.w_out.out_slot_height.text(), "Slot height: 0.17 m"
        )
