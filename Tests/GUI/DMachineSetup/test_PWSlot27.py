# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot27.PWSlot27 import PWSlot27


import pytest


@pytest.mark.GUI
class TestPWSlot27(object):
    """Test that the widget PWSlot27 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        widget = PWSlot27(test_obj)

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
        assert setup["widget"].lf_W3.value() == 0.16

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

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_H2, str(value))
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H2 == value

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        setup["widget"].lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_W0, str(value))
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W0 == value

    def test_set_W1(self, setup):
        """Check that the Widget allow to update W1"""
        setup["widget"].lf_W1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_W1, str(value))
        setup["widget"].lf_W1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W1 == value

    def test_set_W2(self, setup):
        """Check that the Widget allow to update W2"""
        setup["widget"].lf_W2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_W2, str(value))
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W2 == value

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
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        setup["test_obj"].slot = SlotW27(
            Zs=6, H0=0.05, W0=30e-3, H1=0.125, W1=0.06, H2=0.05, W2=0.09, W3=0.04
        )
        setup["widget"] = PWSlot27(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.2252 m"

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.1, Rext=0.2)
        setup["test_obj"].slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=None, W2=0.15, W3=0.16
        )
        setup["widget"] = PWSlot27(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot27 check"
        setup["test_obj"].slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=None, W3=0.16
        )
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot27 check"
        setup["test_obj"].slot = SlotW27(
            H0=None, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot27 check"
        setup["test_obj"].slot = SlotW27(
            H0=0.10, H1=None, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot27 check"
        setup["test_obj"].slot = SlotW27(
            H0=0.10, H1=0.11, H2=None, W0=0.13, W1=0.14, W2=0.15, W3=0.16
        )
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot27 check"
        setup["test_obj"].slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=None
        )
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot27 check"
        setup["test_obj"].slot = SlotW27(
            H0=0.10, H1=0.11, H2=0.12, W0=None, W1=0.14, W2=0.15, W3=0.16
        )
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot27 check"
