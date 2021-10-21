# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10


import pytest


class TestPMSlot10(object):
    """Test that the widget PMSlot10 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM10(H0=0.10, W0=0.13, Wmag=0.14, Hmag=0.15)
        self.widget = PMSlot10(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot10")
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
        assert self.widget.lf_Hmag.value() == 0.15
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_Wmag.value() == 0.14

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

    def test_set_Wmag(self):
        """Check that the Widget allow to update Wmag"""
        # Check Unit
        assert self.widget.unit_Wmag.text() == "[m]"
        # Change value in GUI
        self.widget.lf_Wmag.clear()
        QTest.keyClicks(self.widget.lf_Wmag, "0.33")
        self.widget.lf_Wmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.Wmag == 0.33
        assert self.test_obj.slot.Wmag == 0.33

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

    def test_set_Hmag(self):
        """Check that the Widget allow to update Hmag"""
        # Check Unit
        assert self.widget.unit_Hmag.text() == "[m]"
        # Change value in GUI
        self.widget.lf_Hmag.clear()
        QTest.keyClicks(self.widget.lf_Hmag, "0.36")
        self.widget.lf_Hmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.Hmag == pytest.approx(0.36)
        assert self.test_obj.slot.Hmag == pytest.approx(0.36)

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotM10(H0=0.005, Hmag=0.005, W0=0.01, Wmag=0.01)
        self.widget = PMSlot10(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.005063 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        # H0
        self.test_obj.slot = SlotM10(H0=None, Hmag=0.10, W0=0.10, Wmag=0.10)
        self.widget = PMSlot10(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        # Hmag
        self.test_obj.slot = SlotM10(H0=0.10, Hmag=None, W0=0.10, Wmag=0.10)
        assert self.widget.check(self.test_obj) == "You must set Hmag !"
        # W0
        self.test_obj.slot = SlotM10(H0=0.10, Hmag=0.10, W0=None, Wmag=0.10)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        # Wmag
        self.test_obj.slot = SlotM10(H0=0.10, Hmag=0.10, W0=0.10, Wmag=None)
        assert self.widget.check(self.test_obj) == "You must set Wmag !"


if __name__ == "__main__":
    a = TestPMSlot10()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.test_output_txt()
    a.teardown_class()
    print("Done")
