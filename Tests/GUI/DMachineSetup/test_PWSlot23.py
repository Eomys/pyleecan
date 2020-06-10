# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot23.PWSlot23 import PWSlot23


import pytest


@pytest.mark.GUI
class test_PWSlot23(TestCase):
    """Test that the widget PWSlot23 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW23(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        self.test_obj.slot.W3 = None
        self.widget = PWSlot23(self.test_obj)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot23")
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
        # self.assertEqual(self.widget.c_H1_unit.currentIndex(),0)#Index 0 is m

        self.test_obj.slot = SlotW23(
            H0=0.20, H1=0.21, H2=0.22, W0=0.23, W1=0.24, W2=0.25, H1_is_rad=True
        )
        self.test_obj.slot.W3 = None
        self.widget = PWSlot23(self.test_obj)
        self.assertEqual(self.widget.lf_H0.value(), 0.20)
        self.assertEqual(self.widget.lf_H1.value(), 0.21)
        self.assertEqual(self.widget.lf_H2.value(), 0.22)
        self.assertEqual(self.widget.lf_W0.value(), 0.23)
        self.assertEqual(self.widget.lf_W1.value(), 0.24)
        self.assertEqual(self.widget.lf_W2.value(), 0.25)
        # Index 1 is rad
        # self.assertEqual(self.widget.c_H1_unit.currentIndex(),1)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W0, 0.31)
        self.assertEqual(self.test_obj.slot.W0, 0.31)

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W1, 0.32)
        self.assertEqual(self.test_obj.slot.W1, 0.32)

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

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H1, 0.35)
        self.assertEqual(self.test_obj.slot.H1, 0.35)

    #    def test_set_H1_is_rad(self):
    #        """Check that the Widget allow to update H1_is_rad
    #        """
    #        self.assertTrue(not self.test_obj.slot.H1_is_rad)
    #
    #        self.widget.c_H1_unit.setCurrentIndex(1)#Index 1 is rad
    #
    #        self.assertTrue(self.test_obj.slot.H1_is_rad)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H2, 0.36)
        self.assertEqual(self.test_obj.slot.H2, 0.36)

    def test_output_txt(self):
        """Check that the Output text is computed and correct
        """
        self.test_obj = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=5,
            Wrvd=0.02,
        )
        self.test_obj.slot = SlotW23(
            Zs=6, W0=50e-3, W1=90e-3, W2=100e-3, H0=20e-3, H1=35e-3, H2=130e-3
        )
        self.widget = PWSlot23(self.test_obj)
        self.assertEqual(
            self.widget.w_out.out_slot_height.text(), "Slot height: 0.1345 m"
        )
