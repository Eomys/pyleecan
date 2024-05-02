# -*- coding: utf-8 -*-

import sys

import pytest
from qtpy import QtWidgets
from qtpy.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW63 import SlotW63
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot63.PWSlot63 import PWSlot63


class TestPWSlot63(object):
    """Test that the widget PWSlot63 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlot63")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW63(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
        )
        self.widget = PWSlot63(self.test_obj)

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15

    def test_out(self):
        """Checking output"""
        self.test_obj = LamSlotWind(
            Rint=0, Rext=0.135, is_internal=True, is_stator=False, L1=0.9
        )
        self.test_obj.slot = SlotW63(
            Zs=12,
            H0=30e-3,
            W0=30e-3,
            H1=0.78539,
            W1=80e-3,
            H2=40e-3,
            W2=15e-3,
        )

        self.widget = PWSlot63(self.test_obj)
        assert self.widget.out_slot_height.text() == "Slot height: 0.09126 m"
        assert self.widget.out_tooth_width.isHidden()

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
        QTest.keyClicks(self.widget.lf_W1, str(0.32))
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

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H2 == 0.36
        assert self.test_obj.slot.H2 == 0.36

    def test_check(self):
        """Check that the check is working correctly"""

        self.test_obj = LamSlotWind(Rint=0.7, Rext=0.5)
        self.test_obj.slot = SlotW63(
            H0=None,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
        )
        self.widget = PWSlot63(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        self.test_obj.slot = SlotW63(
            H0=0.10,
            H1=None,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
        )
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        self.test_obj.slot = SlotW63(
            H0=0.10,
            H1=0.11,
            H2=None,
            W0=0.13,
            W1=0.14,
            W2=0.15,
        )
        assert self.widget.check(self.test_obj) == "You must set H2 !"
        self.test_obj.slot = SlotW63(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=None,
            W1=0.14,
            W2=0.15,
        )
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        self.test_obj.slot = SlotW63(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=None,
            W2=0.15,
        )
        assert self.widget.check(self.test_obj) == "You must set W1 !"
        self.test_obj.slot = SlotW63(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=None,
        )
        assert self.widget.check(self.test_obj) == "You must set W2 !"

        self.test_obj.slot = SlotW63(
            H0=0.50,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.12,
        )
        assert (
            self.widget.check(self.test_obj)
            == "The slot height is greater than the lamination !"
        )

        self.test_obj.slot = SlotW63(
            H0=70e-3,
            W0=50e-3,
            H1=30e-3,
            W1=20e-3,
            W2=15e-3,
            H2=60e-3,
        )
        assert self.widget.check(self.test_obj) == "You must have W1 > W0"


if __name__ == "__main__":
    a = TestPWSlot63()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    print("Done")
