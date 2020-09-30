# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot60.PWSlot60 import PWSlot60


import pytest


@pytest.mark.GUI
class TestPWSlot60(object):
    """Test that the widget PWSlot60 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW60(
            R1=0.10, H1=0.11, H2=0.12, W1=0.13, W2=0.14, W3=0.15, H3=0.16, H4=0.17
        )
        self.widget = PWSlot60(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot60")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_R1.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W1.value() == 0.13
        assert self.widget.lf_W2.value() == 0.14
        assert self.widget.lf_W3.value() == 0.15
        assert self.widget.lf_H3.value() == 0.16
        assert self.widget.lf_H4.value() == 0.17

    def test_output(self):
        """Check that the output are computed"""
        self.test_obj = LamSlotWind(
            Rint=0, Rext=0.1325, is_internal=True, is_stator=False, L1=0.9
        )
        self.test_obj.slot = SlotW60(
            Zs=12,
            W1=25e-3,
            W2=12.5e-3,
            H1=20e-3,
            H2=20e-3,
            R1=0.1325,
            H3=2e-3,
            H4=1e-3,
            W3=2e-3,
        )
        self.widget = PWSlot60(self.test_obj)
        assert self.widget.out_slot_height.text() == "Slot height: 0.04038 m"
        assert self.widget.out_tooth_width.isHidden()

    def test_set_R1(self):
        """Check that the Widget allow to update R1"""
        self.widget.lf_R1.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_R1, "0.34")
        self.widget.lf_R1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.R1 == 0.34
        assert self.test_obj.slot.R1 == 0.34

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W1, "0.31")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == 0.31
        assert self.test_obj.slot.W1 == 0.31

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W2, str(0.32))
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W2 == 0.32
        assert self.test_obj.slot.W2 == 0.32

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W3, "0.33")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == 0.33
        assert self.test_obj.slot.W3 == 0.33

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

    def test_set_H3(self):
        """Check that the Widget allow to update H3"""
        self.widget.lf_H3.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H3, "0.37")
        self.widget.lf_H3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H3 == 0.37
        assert self.test_obj.slot.H3 == 0.37

    def test_set_H4(self):
        """Check that the Widget allow to update H4"""
        self.widget.lf_H4.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H4, "0.38")
        self.widget.lf_H4.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H4 == 0.38
        assert self.test_obj.slot.H4 == 0.38
