# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot21.PWSlot21 import PWSlot21


import pytest

"""Test that the widget PWSlot21 behave like it should"""


@pytest.mark.GUI
class TestPWSlot21(object):
    """Test that the widget PWSlot21 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW21(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        self.widget = PWSlot21(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot21")
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
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        # Index 0 is m
        assert self.widget.c_H1_unit.currentIndex() == 0

        self.test_obj.slot = SlotW21(
            H0=0.20, H1=0.21, H2=0.22, W0=0.23, W1=0.24, W2=0.25, H1_is_rad=True
        )
        self.widget = PWSlot21(self.test_obj)
        assert self.widget.lf_H0.value() == 0.20
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W0.value() == 0.23
        assert self.widget.lf_W1.value() == 0.24
        assert self.widget.lf_W2.value() == 0.25
        # Index 1 is rad
        assert self.widget.c_H1_unit.currentIndex() == 1

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == 0.31
        assert self.test_obj.slot.W0 == 0.31

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == 0.32
        assert self.test_obj.slot.W1 == 0.32

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W2 == 0.33
        assert self.test_obj.slot.W2 == 0.33

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == 0.34
        assert self.test_obj.slot.H0 == 0.34

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == 0.35
        assert self.test_obj.slot.H1 == 0.35

    def test_set_H1_is_rad(self):
        """Check that the Widget allow to update H1_is_rad"""
        assert not self.test_obj.slot.H1_is_rad

        self.widget.c_H1_unit.setCurrentIndex(1)  # Index 1 is rad

        assert self.test_obj.slot.H1_is_rad

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H2 == 0.36
        assert self.test_obj.slot.H2 == 0.36

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.85,
            Nrvd=3,
            Wrvd=0.05,
        )
        self.test_obj.slot = SlotW21(
            Zs=6,
            W0=40e-3,
            W1=60e-3,
            W2=40e-3,
            H0=20e-3,
            H1=0,
            H2=130e-3,
            H1_is_rad=False,
        )
        self.widget = PWSlot21(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.1504 m"
