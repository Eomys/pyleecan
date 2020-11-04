# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.PWSlot25 import PWSlot25


import pytest


@pytest.mark.GUI
class TestPWSlot25(object):
    """Test that the widget PWSlot25 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW25(H1=0.11, H2=0.12, W3=0.14, W4=0.15)
        self.widget = PWSlot25(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot25")
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

        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W3.value() == 0.14
        assert self.widget.lf_W4.value() == 0.15

        self.test_obj.slot = SlotW25(H1=0.21, H2=0.22, W3=0.24, W4=0.25)
        self.widget = PWSlot25(self.test_obj)
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W3.value() == 0.24
        assert self.widget.lf_W4.value() == 0.25

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.32")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == 0.32
        assert self.test_obj.slot.W3 == 0.32

    def test_set_W4(self):
        """Check that the Widget allow to update W4"""
        self.widget.lf_W4.clear()
        QTest.keyClicks(self.widget.lf_W4, "0.33")
        self.widget.lf_W4.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W4 == 0.33
        assert self.test_obj.slot.W4 == 0.33

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == 0.35
        assert self.test_obj.slot.H1 == 0.35

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
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=1,
            Wrvd=0.1,
        )
        self.test_obj.slot = SlotW25(Zs=12, W4=150e-3, W3=75e-3, H1=30e-3, H2=150e-3)
        self.widget = PWSlot25(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.1789 m"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW25(H2=0.10, H1=0.11, W4=None, W3=0.16)
        self.widget = PWSlot25(self.test_obj)
        assert self.widget.check(self.test_obj) == "PWSlot25 check"
        self.test_obj.slot = SlotW25(H2=0.10, H1=0.11, W4=0.1, W3=None)
        assert self.widget.check(self.test_obj) == "PWSlot25 check"
        self.test_obj.slot = SlotW25(H2=0.10, H1=None, W4=0.1, W3=0.16)
        assert self.widget.check(self.test_obj) == "PWSlot25 check"
        self.test_obj.slot = SlotW25(H2=None, H1=0.11, W4=0.1, W3=0.16)
        assert self.widget.check(self.test_obj) == "PWSlot25 check"
