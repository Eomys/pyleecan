# -*- coding: utf-8 -*-

import sys
from random import uniform
from numpy import pi

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot13.PWSlot13 import PWSlot13


import pytest


@pytest.mark.GUI
class TestPWSlot13(object):
    """Test that the widget PWSlot13 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW13(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            W3=0.16,
            H1_is_rad=False,
        )
        self.widget = PWSlot13(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot13")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

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
        assert self.widget.lf_W3.value() == 0.16
        # Index 0 is m
        assert self.widget.c_H1_unit.currentIndex() == 0

        self.test_obj.slot = SlotW13(
            H0=0.20,
            H1=0.21,
            H2=0.22,
            W0=0.23,
            W1=0.24,
            W2=0.25,
            W3=0.26,
            H1_is_rad=True,
        )
        self.widget = PWSlot13(self.test_obj)
        assert self.widget.lf_H0.value() == 0.20
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W0.value() == 0.23
        assert self.widget.lf_W1.value() == 0.24
        assert self.widget.lf_W2.value() == 0.25
        assert self.widget.lf_W3.value() == 0.26
        # Index 1 is rad
        assert self.widget.c_H1_unit.currentIndex() == 1

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H0, str(value))
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == value

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == value

        self.widget.c_H1_unit.setCurrentIndex(3)
        self.widget.lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == value / 180 * pi

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H2, str(value))
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H2 == value

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W0, str(value))
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == value

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W1, str(value))
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == value

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W2, str(value))
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W2 == value

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W3, str(value))
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == value

    def test_set_H1_is_rad(self):
        """Check that the Widget allow to update H1_is_rad"""
        assert not self.test_obj.slot.H1_is_rad

        self.widget.c_H1_unit.setCurrentIndex(1)  # Index 1 is rad

        assert self.test_obj.slot.H1_is_rad

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotW13(
            H0=0.005,
            H1=0.01,
            H2=0.02,
            W0=0.005,
            W1=0.02,
            W2=0.01,
            W3=0.025,
            H1_is_rad=False,
        )
        self.widget = PWSlot13(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.03502 m"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW13(
            H0=None, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.6
        )
        self.widget = PWSlot13(self.test_obj)
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
        self.test_obj.slot = SlotW13(
            H0=0.10, H1=None, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.6
        )
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
        self.test_obj.slot = SlotW13(
            H0=0.10, H1=0.11, H2=None, W0=0.13, W1=0.14, W2=0.15, W3=0.6
        )
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
        self.test_obj.slot = SlotW13(
            H0=0.10, H1=0.11, H2=0.12, W0=None, W1=0.14, W2=0.15, W3=0.6
        )
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
        self.test_obj.slot = SlotW13(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=None, W2=0.15, W3=0.6
        )
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
        self.test_obj.slot = SlotW13(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=None, W3=0.6
        )
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
        self.test_obj.slot = SlotW13(
            H0=0.10, H1=5.3, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=None
        )
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
        self.test_obj.slot = SlotW13(
            H0=0.10, H1=5.3, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.6
        )
        assert self.widget.check(self.test_obj) == "PWSlot13 check"
