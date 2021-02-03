# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot12.PWSlot12 import PWSlot12


import pytest


@pytest.mark.GUI
class TestPWSlot12(object):
    """Test that the widget PWSlot12 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW12(H0=0.10, H1=0.11, R1=0.12, R2=0.13)
        widget = PWSlot12(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_R1.value() == 0.12
        assert setup["widget"].lf_R2.value() == 0.13

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

    def test_set_R1(self, setup):
        """Check that the Widget allow to update R1"""
        setup["widget"].lf_R1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_R1, str(value))
        setup["widget"].lf_R1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.R1 == value

    def test_set_R2(self, setup):
        """Check that the Widget allow to update R2"""
        setup["widget"].lf_R2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_R2, str(value))
        setup["widget"].lf_R2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.R2 == value

    def test_output_txt(self, setup):
        """Check that the Output text is computed and correct"""
        setup["test_obj"].slot = SlotW12(H0=0.01, H1=0.02, R1=0.005, R2=0.005)
        setup["widget"] = PWSlot12(setup["test_obj"])
        assert (
            setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.04506 [m]"
        )

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.1, Rext=0.2)
        setup["test_obj"].slot = SlotW12(H0=0.10, H1=0.11, R1=0.12, R2=None)
        setup["widget"] = PWSlot12(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "You must set R2 !"
        setup["test_obj"].slot = SlotW12(H0=None, H1=0.11, R1=0.12, R2=0.005)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H0 !"
        setup["test_obj"].slot = SlotW12(H0=0.10, H1=None, R1=0.12, R2=0.005)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H1 !"
