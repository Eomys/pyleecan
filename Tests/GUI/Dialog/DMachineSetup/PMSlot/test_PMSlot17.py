# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM17 import SlotM17
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.PMSlot17 import PMSlot17


import pytest


class TestPMSlot17(object):
    """Test that the widget PMSlot17 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM17(Zs=2)
        self.test_obj.magnet.Lmag = 0.12
        self.widget = PMSlot17(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot17")
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

        assert self.widget.lf_Lmag.value() == 0.12

    def test_set_Lmag(self):
        """Check that the Widget allow to update Lmag"""
        # Check Unit
        assert self.widget.unit_Lmag.text() == "[m]"
        # Change value in GUI
        self.widget.lf_Lmag.clear()
        QTest.keyClicks(self.widget.lf_Lmag, "0.34")
        self.widget.lf_Lmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.lamination.magnet.Lmag == 0.34
        assert self.test_obj.magnet.Lmag == 0.34

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.9)
        # p check
        self.test_obj.slot = SlotM17(Zs=4)
        self.widget = PMSlot17(self.test_obj)
        assert self.widget.check(self.test_obj) == "SlotM17 must have p=1"


if __name__ == "__main__":
    a = TestPMSlot17()
    a.setup_class()
    a.setup_method()
    a.test_check()
    a.teardown_class()
    print("Done")
