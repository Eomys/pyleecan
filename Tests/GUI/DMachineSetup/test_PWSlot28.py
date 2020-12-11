# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.PWSlot28 import PWSlot28


import pytest


@pytest.mark.GUI
class TestPWSlot28(object):
    """Test that the widget PWSlot28 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW28(H0=0.10, R1=0.11, H3=0.12, W0=0.13, W3=0.14)
        widget = PWSlot28(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_R1.value() == 0.11
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

    def test_set_R1(self, setup):
        """Check that the Widget allow to update R1"""
        setup["widget"].lf_R1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_R1, str(value))
        setup["widget"].lf_R1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.R1 == value

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
        setup["test_obj"] = LamSlotWind(
            Rint=35e-3,
            Rext=84e-3,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        setup["test_obj"].slot = SlotW28(
            Zs=42, W0=3.5e-3, H0=0.45e-3, R1=3.5e-3, H3=14e-3, W3=5e-3
        )
        setup["widget"] = PWSlot28(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.02019 m"

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.1, Rext=0.2)
        setup["test_obj"].slot = SlotW28(H0=0.10, H3=0.11, R1=0.12, W0=None, W3=0.16)
        setup["widget"] = PWSlot28(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot28 check"
        setup["test_obj"].slot = SlotW28(H0=0.10, H3=0.11, R1=0.12, W0=0.31, W3=None)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot28 check"
        setup["test_obj"].slot = SlotW28(H0=0.10, H3=0.11, R1=None, W0=0.31, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot28 check"
        setup["test_obj"].slot = SlotW28(H0=0.10, H3=None, R1=0.12, W0=0.31, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot28 check"
        setup["test_obj"].slot = SlotW28(H0=None, H3=0.11, R1=0.12, W0=0.31, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot28 check"
