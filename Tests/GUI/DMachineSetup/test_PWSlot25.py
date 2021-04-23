# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.PWSlot25 import PWSlot25


import pytest


class TestPWSlot25(object):
    """Test that the widget PWSlot25 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW25(H1=0.11, H2=0.12, W3=0.14, W4=0.15)
        widget = PWSlot25(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W3.value() == 0.14
        assert setup["widget"].lf_W4.value() == 0.15

        setup["test_obj"].slot = SlotW25(H1=0.21, H2=0.22, W3=0.24, W4=0.25)
        setup["widget"] = PWSlot25(setup["test_obj"])
        assert setup["widget"].lf_H1.value() == 0.21
        assert setup["widget"].lf_H2.value() == 0.22
        assert setup["widget"].lf_W3.value() == 0.24
        assert setup["widget"].lf_W4.value() == 0.25

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        setup["widget"].lf_W3.clear()
        QTest.keyClicks(setup["widget"].lf_W3, "0.32")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W3 == 0.32
        assert setup["test_obj"].slot.W3 == 0.32

    def test_set_W4(self, setup):
        """Check that the Widget allow to update W4"""
        setup["widget"].lf_W4.clear()
        QTest.keyClicks(setup["widget"].lf_W4, "0.33")
        setup["widget"].lf_W4.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W4 == 0.33
        assert setup["test_obj"].slot.W4 == 0.33

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        setup["widget"].lf_H1.clear()
        QTest.keyClicks(setup["widget"].lf_H1, "0.35")
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H1 == 0.35
        assert setup["test_obj"].slot.H1 == 0.35

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()
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
            L1=0.9,
            Nrvd=1,
            Wrvd=0.1,
        )
        setup["test_obj"].slot = SlotW25(
            Zs=12, W4=150e-3, W3=75e-3, H1=30e-3, H2=150e-3
        )
        setup["widget"] = PWSlot25(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.1789 [m]"

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.1, Rext=0.2)
        setup["test_obj"].slot = SlotW25(H2=0.10, H1=0.11, W4=None, W3=0.16)
        setup["widget"] = PWSlot25(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "You must set W4 !"
        setup["test_obj"].slot = SlotW25(H2=0.10, H1=0.11, W4=0.1, W3=None)
        assert setup["widget"].check(setup["test_obj"]) == "You must set W3 !"
        setup["test_obj"].slot = SlotW25(H2=0.10, H1=None, W4=0.1, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H1 !"
        setup["test_obj"].slot = SlotW25(H2=None, H1=0.11, W4=0.1, W3=0.16)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H2 !"
