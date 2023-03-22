# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11


import pytest


class TestPMSlot11(object):
    """Test that the widget PMSlot11 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM11(Zs=8, H0=0.10, W0=0.13, Wmag=0.14, Hmag=0.15)
        self.widget = PMSlot11(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot11")
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
        assert self.widget.c_W0_unit.currentText() == "rad"
        assert self.widget.c_Wmag_unit.currentText() == "rad"

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Check Unit
        assert self.widget.c_W0_unit.currentText() == "rad"
        # Change value in GUI
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == 0.31
        assert self.test_obj.slot.W0 == 0.31

    def test_set_W0_deg(self):
        """Check that the Widget allow to update W0"""
        # Check Unit
        self.widget.c_W0_unit.setCurrentIndex(1)
        assert self.widget.c_W0_unit.currentText() == "deg"
        # Change value in GUI
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "45")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == pi / 4
        assert self.test_obj.slot.W0 == pi / 4

    def test_change_unit_W0(self):
        """Check that the value of W0 is updated if the unit is changed"""
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.c_W0_unit.currentText() == "rad"

        self.widget.c_W0_unit.setCurrentIndex(1)

        assert self.widget.c_W0_unit.currentText() == "deg"
        # Only objet is updated, widget value is the same
        assert self.widget.lf_W0.value() == 0.13
        assert self.test_obj.slot.W0 == pytest.approx(0.13 * pi / 180, rel=0.1)

    def test_set_Wmag(self):
        """Check that the Widget allow to update Wmag"""
        # Check Unit
        assert self.widget.c_W0_unit.currentText() == "rad"
        # Change value in GUI
        self.widget.lf_Wmag.clear()
        QTest.keyClicks(self.widget.lf_Wmag, "0.33")
        self.widget.lf_Wmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.Wmag == 0.33
        assert self.test_obj.slot.Wmag == 0.33

    def test_set_Wmag_deg(self):
        """Check that the Widget allow to update Wmag"""
        # Check Unit
        self.widget.c_Wmag_unit.setCurrentIndex(1)
        assert self.widget.c_Wmag_unit.currentText() == "deg"
        # Change value in GUI
        self.widget.lf_Wmag.clear()
        QTest.keyClicks(self.widget.lf_Wmag, "45")
        self.widget.lf_Wmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.Wmag == pi / 4
        assert self.test_obj.slot.Wmag == pi / 4

    def test_change_unit_Wmag(self):
        """Check that the value of Wmag is updated if the unit is changed"""
        assert self.widget.lf_Wmag.value() == 0.14
        assert self.widget.c_Wmag_unit.currentText() == "rad"

        self.widget.c_Wmag_unit.setCurrentIndex(1)

        assert self.widget.c_Wmag_unit.currentText() == "deg"
        # Only objet is updated, widget value is the same
        assert self.widget.lf_Wmag.value() == 0.14
        assert self.test_obj.slot.Wmag == pytest.approx(0.14 * pi / 180, rel=0.1)

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
        self.test_obj.slot = SlotM11(H0=0.005, Hmag=0.005, W0=0.01, Wmag=0.01)
        self.widget = PMSlot11(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.005 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.9)
        # H0
        self.test_obj.slot = SlotM11(H0=None, Hmag=0.10, W0=0.10, Wmag=0.10)
        self.widget = PMSlot11(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        # Hmag
        self.test_obj.slot = SlotM11(H0=0.10, Hmag=None, W0=0.10, Wmag=0.10)
        assert self.widget.check(self.test_obj) == "You must set Hmag !"
        # W0
        self.test_obj.slot = SlotM11(H0=0.10, Hmag=0.10, W0=None, Wmag=0.10)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        # Wmag
        self.test_obj.slot = SlotM11(H0=0.10, Hmag=0.10, W0=0.10, Wmag=None)
        assert self.widget.check(self.test_obj) == "You must set Wmag !"
        # Wmag < W0
        self.test_obj.slot = SlotM11(H0=0.10, Hmag=0.10, W0=0.10, Wmag=0.12)
        assert self.widget.check(self.test_obj) == "You must have Wmag <= W0"
        # Wmag < pi/p
        self.test_obj.slot = SlotM11(Zs=8, H0=0.10, Hmag=0.10, W0=pi / 4, Wmag=pi / 4)
        assert (
            self.widget.check(self.test_obj)
            == "You must have Wmag < pi/p (use ring magnet instead)"
        )
        self.test_obj.slot = SlotM11(Zs=12, H0=0.10, Hmag=0.10, W0=0.623, Wmag=0.623)
        assert (
            self.widget.check(self.test_obj)
            == "You must have Wmag < pi/p (use ring magnet instead)"
        )
        self.test_obj.slot = SlotM11(
            Zs=8, H0=0.10, Hmag=0.10, W0=(pi / 4) * 0.99, Wmag=(pi / 4) * 0.99
        )
        assert (
            self.widget.check(self.test_obj)
            == "You must have Wmag < pi/p (use ring magnet instead)"
        )
        self.test_obj.slot = SlotM11(
            Zs=8, H0=0.10, Hmag=0.10, W0=(pi / 4) * 0.98, Wmag=(pi / 4) * 0.98
        )
        assert self.widget.check(self.test_obj) is None


if __name__ == "__main__":
    a = TestPMSlot11()
    a.setup_class()
    a.setup_method()
    a.test_check()
    a.test_change_unit_W0()
    a.test_change_unit_Wmag()
    a.teardown_class()
    print("Done")
