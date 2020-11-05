# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot24.PWSlot24 import PWSlot24


import pytest


@pytest.mark.GUI
class TestPWSlot24(object):
    """Test that the widget PWSlot24 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW24(H2=0.12, W3=0.15)
        self.widget = PWSlot24(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot24")
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

        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W3.value() == 0.15

        self.test_obj.slot = SlotW24(H2=0.22, W3=0.25)
        self.widget = PWSlot24(self.test_obj)
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W3.value() == 0.25

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.33")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == 0.33
        assert self.test_obj.slot.W3 == 0.33

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
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
            L1=0.8,
            Nrvd=4,
            Wrvd=0.05,
        )
        self.test_obj.slot = SlotW24(Zs=12, W3=100e-3, H2=150e-3)
        self.widget = PWSlot24(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.15 m"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.7, Rext=0.5)
        self.test_obj.slot = SlotW24(H2=0.12, W3=None)
        self.widget = PWSlot24(self.test_obj)
        assert self.widget.check(self.test_obj) == "PWSlot24 check"
        self.test_obj.slot = SlotW24(H2=None, W3=0.13)
        assert self.widget.check(self.test_obj) == "PWSlot24 check"
        self.test_obj.slot = SlotW24(H2=0.12, W3=0.100e-3)
        assert self.widget.check(self.test_obj) == "PWSlot24 yoke"
