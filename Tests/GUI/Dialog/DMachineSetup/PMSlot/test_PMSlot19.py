# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM19 import SlotM19
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot19.PMSlot19 import PMSlot19


import pytest


class TestPMSlot19(object):
    """Test that the widget PMSlot19 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM19(W0=0.13, W1=0.14, Hmag=0.15)
        self.widget = PMSlot19(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot19")
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

        assert self.widget.lf_Hmag.value() == 0.15
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
        self.test_obj.slot = SlotM19(Hmag=0.005, W0=0.01, W1=0.01)
        self.widget = PMSlot19(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.005 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        # Hmag
        self.test_obj.slot = SlotM19(Hmag=None, W0=0.10, W1=0.10)
        assert self.widget.check(self.test_obj) == "You must set Hmag !"
        # W0
        self.test_obj.slot = SlotM19(Hmag=0.10, W0=None, W1=0.10)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        # W1
        self.test_obj.slot = SlotM19(Hmag=0.10, W0=0.10, W1=None)
        assert self.widget.check(self.test_obj) == "You must set W1 !"


if __name__ == "__main__":
    a = TestPMSlot19()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    a.test_output_txt()
    print("Done")
