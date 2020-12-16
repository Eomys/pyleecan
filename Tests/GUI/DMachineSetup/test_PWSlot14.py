# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.PWSlot14 import PWSlot14


import pytest


@pytest.mark.GUI
class TestPWSlot14(object):
    """Test that the widget PWSlot14 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW14(H0=0.10, H1=0.11, H3=0.12, W0=0.13, W3=0.14)
        widget = PWSlot14(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H3.value() == 0.12
        assert setup["widget"].lf_W0.value() == 0.13
        assert setup["widget"].lf_W3.value() == 0.14

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        setup["widget"].lf_H0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_H0, str(value))
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H0 == value

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        setup["widget"].lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_H1, str(value))
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H1 == value

    def test_set_H3(self, setup):
        """Check that the Widget allow to update H3"""
        setup["widget"].lf_H3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_H3, str(value))
        setup["widget"].lf_H3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H3 == value

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        setup["widget"].lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_W0, str(value))
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W0 == value

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        setup["widget"].lf_W3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_W3, str(value))
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W3 == value

    def test_output_txt(self, setup):
        """Check that the Output text is computed and correct"""
        setup["test_obj"].slot = SlotW14(H0=0.005, H1=0.01, H3=0.025, W0=0.005, W3=0.02)
        setup["widget"] = PWSlot14(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.03987 m"

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.7, Rext=0.5)
        setup["test_obj"].slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=None, W3=0.16)
        setup["widget"] = PWSlot14(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "You must set W0 !"
        setup["test_obj"].slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=0.31, W3=None)
        assert setup["widget"].check(setup["test_obj"]) == "You must set W3 !"
        setup["test_obj"].slot = SlotW14(H0=0.10, H3=0.11, H1=None, W0=0.31, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H1 !"
        setup["test_obj"].slot = SlotW14(H0=0.10, H3=None, H1=0.12, W0=0.31, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H3 !"
        setup["test_obj"].slot = SlotW14(H0=None, H3=0.11, H1=0.12, W0=0.31, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H0 !"
        setup["test_obj"].slot = SlotW14(H0=0.10, H3=0.11, H1=0.12, W0=0.31, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "The slot height is greater than the lamination !"