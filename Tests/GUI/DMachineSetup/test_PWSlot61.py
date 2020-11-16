# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot61.PWSlot61 import PWSlot61


import pytest


@pytest.mark.GUI
class TestPWSlot61(object):
    """Test that the widget PWSlot61 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        widget = PWSlot61(test_obj)

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
        assert setup["widget"].lf_H3.value() == 0.16
        assert setup["widget"].lf_H4.value() == 0.17
        assert setup["widget"].lf_W3.value() == 0.18

    def test_out(self, setup):
        """Checking output"""
        setup["test_obj"] = LamSlotWind(
            Rint=0, Rext=0.1325, is_internal=True, is_stator=False, L1=0.9
        )
        setup["test_obj"].slot = SlotW61(
            Zs=12,
            W0=15e-3,
            W1=35e-3,
            W2=12.5e-3,
            H0=15e-3,
            H1=20e-3,
            H2=25e-3,
            H3=1e-3,
            H4=2e-3,
            W3=3e-3,
        )
        setup["widget"] = PWSlot61(setup["test_obj"])
        assert setup["widget"].out_slot_height.text() == "Slot height: 0.05994 m"
        assert setup["widget"].out_tooth_width.isHidden()

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        setup["widget"].lf_W0.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_W0, "0.31")
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W0 == 0.31
        assert setup["test_obj"].slot.W0 == 0.31

    def test_set_W1(self, setup):
        """Check that the Widget allow to update W1"""
        setup["widget"].lf_W1.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_W1, str(0.32))
        setup["widget"].lf_W1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W1 == 0.32
        assert setup["test_obj"].slot.W1 == 0.32

    def test_set_W2(self, setup):
        """Check that the Widget allow to update W2"""
        setup["widget"].lf_W2.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_W2, "0.33")
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W2 == 0.33
        assert setup["test_obj"].slot.W2 == 0.33

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        setup["widget"].lf_H0.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_H0, "0.34")
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H0 == 0.34
        assert setup["test_obj"].slot.H0 == 0.34

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        setup["widget"].lf_H1.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_H1, "0.35")
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H1 == 0.35
        assert setup["test_obj"].slot.H1 == 0.35

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_H2, "0.36")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H2 == 0.36
        assert setup["test_obj"].slot.H2 == 0.36

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        setup["widget"].lf_W3.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_W3, "0.37")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W3 == 0.37
        assert setup["test_obj"].slot.W3 == 0.37

    def test_set_H3(self, setup):
        """Check that the Widget allow to update H3"""
        setup["widget"].lf_H3.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_H3, "0.38")
        setup["widget"].lf_H3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H3 == 0.38
        assert setup["test_obj"].slot.H3 == 0.38

    def test_set_H4(self, setup):
        """Check that the Widget allow to update H4"""
        setup["widget"].lf_H4.clear()  # Clear the field before writing
        QTest.keyClicks(setup["widget"].lf_H4, "0.39")
        setup["widget"].lf_H4.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H4 == 0.39
        assert setup["test_obj"].slot.H4 == 0.39

    def test_check(self, setup):
        """Check that the check is working correctly"""

        setup["test_obj"] = LamSlotWind(Rint=0.7, Rext=0.5)
        setup["test_obj"].slot = SlotW61(
            H0=None,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        setup["widget"] = PWSlot61(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=None,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=None,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=None,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=None,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=None,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=None,
            H4=0.17,
            W3=0.18,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=None,
            W3=0.18,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=None,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"

        setup["test_obj"].slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.912,
            W0=0.13,
            W1=0.14,
            W2=0.12,
            H3=0.16,
            H4=0.17,
            W3=0.00000158,
        )
        assert setup["widget"].check(setup["test_obj"]) == "SWSlot_61 check"
