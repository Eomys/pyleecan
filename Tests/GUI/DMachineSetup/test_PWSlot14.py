# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.PWSlot14 import PWSlot14


import pytest


@pytest.mark.GUI
class TestPWSlot14(object):
    """Test that the widget PWSlot14 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW14(H0=0.10, H1=0.11, H3=0.12, W0=0.13, W3=0.14)
        self.widget = PWSlot14(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot14")
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
        assert self.widget.lf_H3.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W3.value() == 0.14

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

    def test_set_H3(self):
        """Check that the Widget allow to update H3"""
        self.widget.lf_H3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H3, str(value))
        self.widget.lf_H3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H3 == value

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W0, str(value))
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == value

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W3, str(value))
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == value

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotW14(H0=0.005, H1=0.01, H3=0.025, W0=0.005, W3=0.02)
        self.widget = PWSlot14(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.03987 m"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=None, W3=0.16)
        self.widget = PWSlot14(self.test_obj)
        assert self.widget.check(self.test_obj) == "PWSlot14 check"
        self.test_obj.slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=0.31, W3=None)
        assert self.widget.check(self.test_obj) == "PWSlot14 check"
        self.test_obj.slot = SlotW14(H0=0.10, H3=0.11, H1=None, W0=0.31, W3=0.16)
        assert self.widget.check(self.test_obj) == "PWSlot14 check"
        self.test_obj.slot = SlotW14(H0=0.10, H3=None, H1=0.12, W0=0.31, W3=0.16)
        assert self.widget.check(self.test_obj) == "PWSlot14 check"
        self.test_obj.slot = SlotW14(H0=None, H3=0.11, H1=0.12, W0=0.31, W3=0.16)
        assert self.widget.check(self.test_obj) == "PWSlot14 check"
