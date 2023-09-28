# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM16 import SlotM16
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot16.PMSlot16 import PMSlot16


import pytest


class TestPMSlot16(object):
    """Test that the widget PMSlot16 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM16(H0=0.10, W0=0.13, W1=0.14, H1=0.15)
        self.widget = PMSlot16(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot16")
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
        assert self.widget.lf_H1.value() == 0.15
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Check Unit
        assert self.widget.unit_W0.text() == "[m]"
        # Change value in GUI
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == 0.31
        assert self.test_obj.slot.W0 == 0.31

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        # Check Unit
        assert self.widget.unit_W1.text() == "[m]"
        # Change value in GUI
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.33")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == 0.33
        assert self.test_obj.slot.W1 == 0.33

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        # Check Unit
        assert self.widget.unit_H0.text() == "[m]"
        # Change value in GUI
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == 0.34
        assert self.test_obj.slot.H0 == 0.34

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        # Check Unit
        assert self.widget.unit_H1.text() == "[m]"
        # Change value in GUI
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.36")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == pytest.approx(0.36)
        assert self.test_obj.slot.H1 == pytest.approx(0.36)

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotM16(H0=0.005, H1=0.05, W0=0.01, W1=0.05)
        self.widget = PMSlot16(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.05506 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        # H0
        self.test_obj.slot = SlotM16(H0=None, H1=0.10, W0=0.10, W1=0.10)
        self.widget = PMSlot16(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        # H1
        self.test_obj.slot = SlotM16(H0=0.10, H1=None, W0=0.10, W1=0.10)
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        # W0
        self.test_obj.slot = SlotM16(H0=0.10, H1=0.10, W0=None, W1=0.10)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        # W1
        self.test_obj.slot = SlotM16(H0=0.10, H1=0.10, W0=0.10, W1=None)
        assert self.widget.check(self.test_obj) == "You must set W1 !"


if __name__ == "__main__":
    a = TestPMSlot16()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.test_set_H1()
    a.teardown_class()
    print("Done")
