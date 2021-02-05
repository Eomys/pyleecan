# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot24.PWSlot24 import PWSlot24


import pytest


@pytest.mark.GUI
class TestPWSlot24(object):
    """Test that the widget PWSlot24 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW24(H2=0.12, W3=0.15)
        widget = PWSlot24(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W3.value() == 0.15

        setup["test_obj"].slot = SlotW24(H2=0.22, W3=0.25)
        setup["widget"] = PWSlot24(setup["test_obj"])
        assert setup["widget"].lf_H2.value() == 0.22
        assert setup["widget"].lf_W3.value() == 0.25

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        setup["widget"].lf_W3.clear()
        QTest.keyClicks(setup["widget"].lf_W3, "0.33")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W3 == 0.33
        assert setup["test_obj"].slot.W3 == 0.33

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
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.8,
            Nrvd=4,
            Wrvd=0.05,
        )
        setup["test_obj"].slot = SlotW24(Zs=12, W3=100e-3, H2=150e-3)
        setup["widget"] = PWSlot24(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.1489 [m]"

    def test_check(self, setup):
        """Check that the check is working correctly"""
        setup["test_obj"] = LamSlotWind(Rint=0.7, Rext=0.5)
        setup["test_obj"].slot = SlotW24(H2=0.12, W3=None)
        setup["widget"] = PWSlot24(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "You must set W3 !"
        setup["test_obj"].slot = SlotW24(H2=None, W3=0.13)
        assert setup["widget"].check(setup["test_obj"]) == "You must set H2 !"
        setup["test_obj"].slot = SlotW24(H2=0.12, W3=0.100e-3)
        assert (
            setup["widget"].check(setup["test_obj"])
            == "The slot height is greater than the lamination !"
        )
