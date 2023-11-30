# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
import mock

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotMagNS import LamSlotMagNS
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.SMSlot import SMSlot
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.WSlotMag.WSlotMag import WSlotMag
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot12.PMSlot12 import PMSlot12
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot13.PMSlot13 import PMSlot13
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot14.PMSlot14 import PMSlot14
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot15.PMSlot15 import PMSlot15
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot16.PMSlot16 import PMSlot16
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.PMSlot17 import PMSlot17
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot18.PMSlot18 import PMSlot18
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot19.PMSlot19 import PMSlot19
import pytest
from Tests.GUI import gui_option  # Set unit as [m]


class TestSMSlot(object):
    """Test that the widget SMSlot behave like it should (for SIPMSM)"""

    def setup_method(self):
        test_obj = MachineSIPMSM()
        # For comp_output compatibility
        test_obj.stator = LamSlotWind(Rint=0.95, Rext=0.99)
        test_obj.rotor = LamSlotMagNS(Rint=0.1, Rext=0.9)
        test_obj.rotor.slot = SlotM11(Zs=8, W0=pi / 24, H0=5e-3, W1=pi / 24, H1=3e-3)
        test_obj.rotor.slot_south = SlotM12(
            W0=0.0122,
            H0=0.001,
            W1=0.0122,
            H1=0.001,
            Zs=36,
        )
        test_obj.rotor.magnet_north.mat_type.name = "test3"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        self.widget = SMSlot(
            machine=test_obj, material_dict=material_dict, is_stator=False
        )
        self.test_obj = test_obj

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSMSlot")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the GUI initialize correctly"""
        assert (
            self.widget.out_Slot_pitch.text()
            == "p = 4 / Slot pitch = 45 [°] (0.7854 [rad])"
        )
        assert self.widget.c_NS_type.currentIndex() == 1
        assert self.widget.tab_slot.count() == 2
        assert self.widget.tab_slot.currentIndex() == 0
        assert self.widget.tab_slot.widget(0).c_slot_type.currentIndex() == 1
        assert (
            self.widget.tab_slot.widget(0).c_slot_type.currentText() == "Polar Magnet"
        )
        assert self.widget.tab_slot.widget(1).c_slot_type.currentIndex() == 2
        assert (
            self.widget.tab_slot.widget(1).c_slot_type.currentText()
            == "Rectangular Magnet with polar top"
        )

    def test_change_pole_distribution(self):
        """Check that the widget is able to change pole distribution"""
        # Uneven => Even
        previous_slot = self.widget.obj.slot
        self.widget.c_NS_type.setCurrentIndex(0)
        # Check that the lamination is well updated
        assert isinstance(self.widget.obj, LamSlotMag) == True
        assert isinstance(self.widget.obj.slot, type(previous_slot)) == True
        # Check that tab widget is well updated
        assert self.widget.tab_slot.count() == 1

        # Even => Uneven
        previous_slot = self.widget.obj.slot
        self.widget.c_NS_type.setCurrentIndex(1)
        # Check that the lamination is well updated
        assert isinstance(self.widget.obj, LamSlotMagNS) == True
        assert isinstance(self.widget.obj.slot, type(previous_slot)) == True
        assert isinstance(self.widget.obj.slot_south, type(previous_slot)) == True
        # Check that tab widget is well updated
        assert self.widget.tab_slot.count() == 2

    def test_update_slot_type(self):
        """Check that the slot is well updated in the lamination when it changed in the tab (for uneven case)"""
        # For North Pole
        self.widget.tab_slot.setCurrentIndex(0)
        self.widget.tab_slot.widget(0).c_slot_type.setCurrentIndex(9)
        assert self.widget.obj.slot == self.widget.tab_slot.widget(0).lam.slot
        # For South Pole
        self.widget.tab_slot.setCurrentIndex(1)
        self.widget.tab_slot.widget(1).c_slot_type.setCurrentIndex(9)
        assert self.widget.obj.slot_south == self.widget.tab_slot.widget(1).lam.slot

    def test_check(self):
        """Check the error message when plotting"""
        # Introduce an error in slot of North Pole
        assert self.widget.test_err_msg is None
        W0 = self.widget.tab_slot.widget(0).w_slot.lf_W0.value()
        self.widget.tab_slot.widget(0).w_slot.lf_W0.setValue(None)
        self.widget.tab_slot.widget(0).w_slot.lf_W0.editingFinished.emit()
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.b_plot.clicked.emit()
        assert "North Pole: You must set W0 !" in self.widget.test_err_msg
        # Revert error for next test
        self.widget.tab_slot.widget(0).w_slot.lf_W0.setValue(W0 * 2)
        self.widget.tab_slot.widget(0).w_slot.lf_W0.editingFinished.emit()
        self.widget.test_err_msg = None

        # Introduce an error in slot of South Pole
        assert self.widget.test_err_msg is None
        self.widget.tab_slot.widget(1).w_slot.lf_W0.setValue(None)
        self.widget.tab_slot.widget(1).w_slot.lf_W0.editingFinished.emit()
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.b_plot.clicked.emit()
        assert "South Pole: You must set W0 !" in self.widget.test_err_msg


if __name__ == "__main__":
    a = TestSMSlot()
    a.setup_class()
    a.setup_method()
    a.test_init()
    # a.test_change_pole_distribution()
    # a.test_update_slot_type()
    a.test_check()
    a.teardown_class()
    print("Done")
