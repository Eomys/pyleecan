# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.WSlotCirc.WSlotCirc import WSlotCirc


import pytest


class TestSlotCirc(object):
    """Test that the widget SlotCirc behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotCirc(H0=10e-3, W0=45e-3, is_H0_bore=False)
        self.widget = WSlotCirc(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSlotCirc")
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

        assert self.widget.lf_H0.value() == 0.01
        assert self.widget.lf_W0.value() == 0.045
        assert self.widget.c_H0_bore.currentIndex() == 1
        assert self.widget.c_H0_bore.currentText() == "Opening Segment"

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

    def test_set_H0_bore(self):
        """Check that the Widget allow to update is_H0_bore"""
        assert not self.test_obj.slot.is_H0_bore
        self.widget.c_H0_bore.setCurrentIndex(0)
        assert self.widget.c_H0_bore.currentText() == "Opening Arc"

        assert self.test_obj.slot.is_H0_bore
        self.widget.c_H0_bore.setCurrentIndex(1)
        assert self.widget.c_H0_bore.currentText() == "Opening Segment"
        assert not self.test_obj.slot.is_H0_bore

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotCirc(H0=10e-3, W0=45e-3, is_H0_bore=False)
        self.widget = WSlotCirc(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.01127 [m]"

        self.test_obj.slot = SlotCirc(H0=10e-3, W0=45e-3, is_H0_bore=True)
        self.widget = WSlotCirc(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.01 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        # H0
        self.test_obj.slot = SlotCirc(H0=None, W0=0.10)
        self.widget = WSlotCirc(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        # W0
        self.test_obj.slot = SlotCirc(H0=0.10, W0=None)
        assert self.widget.check(self.test_obj) == "You must set W0 !"


if __name__ == "__main__":
    a = TestSlotCirc()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.test_output_txt()
    a.teardown_class()
    print("Done")
