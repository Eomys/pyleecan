# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.PWSlot28 import PWSlot28


import pytest


@pytest.mark.GUI
class TestPWSlot28(object):
    """Test that the widget PWSlot28 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW28(H0=0.10, R1=0.11, H3=0.12, W0=0.13, W3=0.14)
        self.widget = PWSlot28(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot28")
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
        assert self.widget.lf_R1.value() == 0.11
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

    def test_set_R1(self):
        """Check that the Widget allow to update R1"""
        self.widget.lf_R1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_R1, str(value))
        self.widget.lf_R1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.R1 == value

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
        self.test_obj = LamSlotWind(
            Rint=35e-3,
            Rext=84e-3,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        self.test_obj.slot = SlotW28(
            Zs=42, W0=3.5e-3, H0=0.45e-3, R1=3.5e-3, H3=14e-3, W3=5e-3
        )
        self.widget = PWSlot28(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.02019 m"
