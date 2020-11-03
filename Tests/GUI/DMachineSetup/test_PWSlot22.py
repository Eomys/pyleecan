# -*- coding: utf-8 -*-

import sys

from numpy import pi
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.PWSlot22 import PWSlot22


import pytest

"""Test that the widget PWSlot22 behave like it should"""


@pytest.mark.GUI
class TestPWSlot22(object):
    """Test that the widget PWSlot22 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW22(H0=0.10, H2=0.12, W0=0.13, W2=0.15)
        widget = PWSlot22(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W0.value() == 0.13
        assert setup["widget"].lf_W2.value() == 0.15

        setup["test_obj"].slot = SlotW22(H0=0.20, H2=0.22, W0=0.23, W2=0.25)
        setup["widget"] = PWSlot22(setup["test_obj"])
        assert setup["widget"].lf_H0.value() == 0.20
        assert setup["widget"].lf_H2.value() == 0.22
        assert setup["widget"].lf_W0.value() == 0.23
        assert setup["widget"].lf_W2.value() == 0.25

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        setup["widget"].lf_W0.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_W0, "0.31")
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W0 == 0.31
        assert setup["test_obj"].slot.W0 == 0.31

        setup["widget"].c_W0_unit.setCurrentIndex(3)
        setup["widget"].lf_W0.clear()  # Clear the field before writing
        value = 1.4
        QTest.keyClicks(setup["widget"].lf_W0, str(value))
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W0 == value / 180 * pi

    def test_set_W2(self, setup):
        """Check that the Widget allow to update W2"""
        setup["widget"].lf_W2.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_W2, "0.33")
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W2 == 0.33
        assert setup["test_obj"].slot.W2 == 0.33

        setup["widget"].c_W2_unit.setCurrentIndex(3)
        setup["widget"].lf_W2.clear()  # Clear the field before writing
        value = 1.4
        QTest.keyClicks(setup["widget"].lf_W2, str(value))
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W2 == value / 180 * pi

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        setup["widget"].lf_H0.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_H0, "0.34")
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H0 == 0.34
        assert setup["test_obj"].slot.H0 == 0.34

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_H2, "0.36")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H2 == 0.36
        assert setup["test_obj"].slot.H2 == 0.36

    def test_output_txt(self, setup):
        """Check that the Output text is computed and correct"""
        setup["test_obj"] = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.8,
            Nrvd=4,
            Wrvd=0.05,
        )
        setup["test_obj"].slot = SlotW22(Zs=6, W0=pi / 20, W2=pi / 10, H0=20e-3, H2=150e-3)
        setup["widget"] = PWSlot22(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.17 m"

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.1, Rext=0.2)
        setup["test_obj"].slot = SlotW22(H0=None, H2=0.12, W0=0.13, W2=0.15)
        setup["widget"] = PWSlot22(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot22 check"
        setup["test_obj"].slot = SlotW22(H0=0.10, H2=None, W0=0.13, W2=0.15)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot22 check"
        setup["test_obj"].slot = SlotW22(H0=0.10, H2=0.12, W0=None, W2=0.15)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot22 check"
        setup["test_obj"].slot = SlotW22(H0=0.10, H2=0.12, W0=0.13, W2=None)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot22 check"
        setup["test_obj"].slot = SlotW22(H0=0.10, H2=0.12, W0=0.13, W2=0.15, Zs=None)
        assert setup["widget"].check(setup["test_obj"]) == "PWSlot22 check"
