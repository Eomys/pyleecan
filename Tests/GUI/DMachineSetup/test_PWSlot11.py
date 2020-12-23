# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot11.PWSlot11 import PWSlot11


import pytest


@pytest.mark.GUI
class TestPWSlot11(object):
    """Test that the widget PWSlot11 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW11(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            R1=0.16,
            H1_is_rad=False,
        )
        widget = PWSlot11(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W0.value() == 0.13
        assert setup["widget"].lf_W1.value() == 0.14
        assert setup["widget"].lf_W2.value() == 0.15
        assert setup["widget"].lf_R1.value() == 0.16
        # Index 0 is m
        assert setup["widget"].c_H1_unit.currentIndex() == 0

        setup["test_obj"].slot = SlotW11(
            H0=0.20,
            H1=0.21,
            H2=0.22,
            W0=0.23,
            W1=0.24,
            W2=0.25,
            R1=0.26,
            H1_is_rad=True,
        )
        setup["widget"] = PWSlot11(setup["test_obj"])
        assert setup["widget"].lf_H0.value() == 0.20
        assert setup["widget"].lf_H1.value() == 0.21
        assert setup["widget"].lf_H2.value() == 0.22
        assert setup["widget"].lf_W0.value() == 0.23
        assert setup["widget"].lf_W1.value() == 0.24
        assert setup["widget"].lf_W2.value() == 0.25
        assert setup["widget"].lf_R1.value() == 0.26
        # Index 1 is rad
        assert setup["widget"].c_H1_unit.currentIndex() == 1

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        setup["widget"].lf_W0.clear()
        QTest.keyClicks(setup["widget"].lf_W0, "0.31")
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W0 == 0.31
        assert setup["test_obj"].slot.W0 == 0.31

    def test_set_W1(self, setup):
        """Check that the Widget allow to update W1"""
        setup["widget"].lf_W1.clear()
        QTest.keyClicks(setup["widget"].lf_W1, "0.32")
        setup["widget"].lf_W1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W1 == 0.32
        assert setup["test_obj"].slot.W1 == 0.32

    def test_set_W2(self, setup):
        """Check that the Widget allow to update W2"""
        setup["widget"].lf_W2.clear()
        QTest.keyClicks(setup["widget"].lf_W2, "0.33")
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W2 == 0.33
        assert setup["test_obj"].slot.W2 == 0.33

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        setup["widget"].lf_H0.clear()
        QTest.keyClicks(setup["widget"].lf_H0, "0.34")
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H0 == 0.34
        assert setup["test_obj"].slot.H0 == 0.34

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        setup["widget"].lf_H1.clear()
        QTest.keyClicks(setup["widget"].lf_H1, "0.35")
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H1 == 0.35
        assert setup["test_obj"].slot.H1 == 0.35

        setup["widget"].c_H1_unit.setCurrentIndex(3)
        setup["widget"].lf_H1.clear()  # Clear the field before writing
        value = 1.4
        QTest.keyClicks(setup["widget"].lf_H1, str(value))
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H1 == value / 180 * pi

    def test_set_H1_is_rad(self, setup):
        """Check that the Widget allow to update H1_is_rad"""
        assert not setup["test_obj"].slot.H1_is_rad

        setup["widget"].c_H1_unit.setCurrentIndex(1)  # Index 1 is rad

        assert setup["test_obj"].slot.H1_is_rad

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()
        QTest.keyClicks(setup["widget"].lf_H2, "0.36")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H2 == 0.36
        assert setup["test_obj"].slot.H2 == 0.36

    def test_set_R1(self, setup):
        """Check that the Widget allow to update R1"""
        setup["widget"].lf_R1.clear()
        QTest.keyClicks(setup["widget"].lf_R1, "0.37")
        setup["widget"].lf_R1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.R1 == 0.37
        assert setup["test_obj"].slot.R1 == 0.37

    def test_output_txt(self, setup):
        """Check that the Output text is computed and correct"""
        setup["test_obj"].slot = SlotW11(
            H0=0.005,
            H1=0.005,
            H2=0.02,
            W0=0.01,
            W1=0.02,
            W2=0.01,
            R1=0.005,
            H1_is_rad=False,
        )
        setup["widget"] = PWSlot11(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.03006 m"

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.7, Rext=0.5)
        setup["test_obj"].slot = SlotW11(
            H0=None, H1=0.11, H2=0.12, W0=0.11, W1=0.14, W2=0.15, R1=0.6
        )
        setup["widget"] = PWSlot11(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "You must set H0 !"
        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=None, H2=0.12, W0=0.11, W1=0.14, W2=0.15, R1=0.6
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set H1 !"
        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=0.11, H2=None, W0=0.11, W1=0.14, W2=0.15, R1=0.6
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set H2 !"
        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=0.11, H2=0.12, W0=None, W1=0.14, W2=0.15, R1=0.6
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set W0 !"
        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=0.11, H2=0.12, W0=0.11, W1=None, W2=0.15, R1=0.6
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set W1 !"
        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=0.11, H2=0.12, W0=0.11, W1=0.14, W2=None, R1=0.6
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set W2 !"
        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=5.3, H2=0.12, W0=0.11, W1=0.14, W2=0.15, R1=None
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set R1 !"
        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=5.3, H2=0.12, W0=0.11, W1=0.14, W2=0.15, R1=0.6
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must have H1 < 90°"

        setup["test_obj"].slot = SlotW11(
            H0=0.10, H1=0.5, H2=0.12, W0=0.11, W1=0.14, W2=0.15, R1=0.03
        )
        assert (
            setup["widget"].check(setup["test_obj"])
            == "The slot height is greater than the lamination !"
        )
