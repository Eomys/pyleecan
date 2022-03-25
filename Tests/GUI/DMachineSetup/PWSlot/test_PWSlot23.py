# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt, QPoint

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot23.PWSlot23 import PWSlot23


import pytest


class TestPWSlot23(object):
    """Test that the widget PWSlot23 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = SlotW23(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        test_obj.slot.W3 = None
        widget = PWSlot23(test_obj)

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

        setup["test_obj"].slot = SlotW23(
            H0=0.20, H1=0.21, H2=0.22, W0=0.23, W1=0.24, W2=0.25, H1_is_rad=True
        )
        setup["test_obj"].slot.W3 = None
        setup["widget"] = PWSlot23(setup["test_obj"])
        assert setup["widget"].lf_H0.value() == 0.20
        assert setup["widget"].lf_H1.value() == 0.21
        assert setup["widget"].lf_H2.value() == 0.22
        assert setup["widget"].lf_W0.value() == 0.23
        assert setup["widget"].lf_W1.value() == 0.24
        assert setup["widget"].lf_W2.value() == 0.25
        # Index 1 is rad
        # self.assertEqual(setup["widget"].c_H1_unit.currentIndex(),1)

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        setup["widget"].lf_W0.clear()  # Clear the field before writing
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

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W2"""
        setup["widget"].lf_W3.setEnabled(True)

        setup["widget"].lf_W3.clear()
        QTest.keyClicks(setup["widget"].lf_W3, "0.99")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.W3 == 0.99
        assert setup["test_obj"].slot.W3 == 0.99

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

        #    @pytest.mark.GUI
        #    def test_set_H1_is_rad(setUp):
        #        """Check that the Widget allow to update H1_is_rad
        #        """
        #        self.assertTrue(not setup["test_obj"].slot.H1_is_rad)
        #
        #        setup["widget"].c_H1_unit.setCurrentIndex(1)#Index 1 is rad
        #
        #        self.assertTrue(setup["test_obj"].slot.H1_is_rad)

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()
        QTest.keyClicks(setup["widget"].lf_H2, "0.36")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].slot.H2 == 0.36
        assert setup["test_obj"].slot.H2 == 0.36

    def test_is_cst_tooth(self, setup):
        """Check that the Widget allow be checked"""
        assert setup["widget"].slot.W1 is not None
        assert setup["widget"].slot.W2 is not None
        QTest.mouseClick(setup["widget"].is_cst_tooth, Qt.LeftButton)
        assert setup["widget"].is_cst_tooth.isChecked() == True
        assert setup["widget"].slot.W1 is None
        assert setup["widget"].slot.W2 is None
        assert setup["widget"].lf_W1.isEnabled() == False
        assert setup["widget"].lf_W2.isEnabled() == False
        assert setup["widget"].lf_W3.isEnabled() == True

        QTest.mouseClick(setup["widget"].is_cst_tooth, Qt.LeftButton)
        assert setup["widget"].is_cst_tooth.isChecked() == False
        assert setup["widget"].lf_W1.isEnabled() == True
        assert setup["widget"].lf_W2.isEnabled() == True
        assert setup["widget"].lf_W3.isEnabled() == False

    def test_output_txt(self, setup):
        """Check that the Output text is computed and correct"""
        setup["test_obj"] = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=5,
            Wrvd=0.02,
        )
        setup["test_obj"].slot = SlotW23(
            Zs=6, W0=50e-3, W1=90e-3, W2=100e-3, H0=20e-3, H1=35e-3, H2=130e-3
        )
        setup["widget"] = PWSlot23(setup["test_obj"])
        assert setup["widget"].w_out.out_slot_height.text() == "Slot height: 0.1345 [m]"

    def test_check(self, setup):
        """Check that the check function is correctly returning error messages"""
        setup["test_obj"] = LamSlotWind(Rint=0.7, Rext=0.5)
        setup["test_obj"].slot = SlotW23(
            H0=0.10, H1=0.11, H2=0.12, W0=None, W1=0.14, W2=0.15, H1_is_rad=False
        )
        setup["widget"] = PWSlot23(setup["test_obj"])
        assert setup["widget"].check(setup["test_obj"]) == "You must set W0 !"
        setup["test_obj"].slot = SlotW23(
            H0=None, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set H0 !"
        setup["test_obj"].slot = SlotW23(
            H0=0.10, H1=None, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set H1 !"
        setup["test_obj"].slot = SlotW23(
            H0=0.10, H1=0.11, H2=None, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert setup["widget"].check(setup["test_obj"]) == "You must set H2 !"
        setup["test_obj"].slot = SlotW23(
            H0=0.10, H1=0.11, H2=0.12, W0=0.0011, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert (
            setup["widget"].check(setup["test_obj"])
            == "The slot height is greater than the lamination !"
        )
