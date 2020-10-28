# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest

from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.WindingCW2LR import WindingCW2LR
from pyleecan.Classes.WindingSC import WindingSC

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWindPat.SWindPat import SWindPat

import pytest


@pytest.mark.GUI
class TestSWindPat(object):
    """Test that the widget SWindPat behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = MachineSCIM()
        self.test_obj.stator = LamSlotWind()
        self.test_obj.stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.stator.winding = WindingDW2L()
        self.test_obj.stator.winding.qs = 6
        self.test_obj.stator.winding.coil_pitch = 8
        self.test_obj.stator.winding.Nslot_shift_wind = 10
        self.test_obj.stator.winding.is_reverse_wind = True

        self.widget = SWindPat(machine=self.test_obj, matlib=[], is_stator=True)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test SWindPat")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.si_qs.value() == 6
        assert self.widget.si_coil_pitch.value() == 8
        assert self.widget.si_Nslot.value() == 10
        assert self.widget.c_wind_type.currentIndex() == 2
        assert self.widget.is_reverse.checkState() == Qt.Checked
        assert self.widget.out_shape.text() == "Winding Matrix shape: [2, 1, 36, 6]"

    def test_init_WRSM(self):
        """Check that the GUI is correctly initialize with a WRSM machine"""
        self.test_obj = MachineWRSM(type_machine=9)

        self.test_obj.stator = LamSlotWind()
        self.test_obj.stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.stator.winding = WindingDW2L(p=8, qs=4)

        self.test_obj.rotor = LamSlotWind()
        self.test_obj.rotor.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding = Winding(p=8, qs=4)

        self.widget = SWindPat(machine=self.test_obj, matlib=[], is_stator=True)
        self.widget2 = SWindPat(machine=self.test_obj, matlib=[], is_stator=False)

        # Check result stator
        assert type(self.test_obj.stator.winding) == WindingDW2L
        assert self.test_obj.stator.winding.p == 8
        assert self.test_obj.stator.winding.qs == 4
        assert self.widget.si_qs.isEnabled() == True
        assert self.widget.si_coil_pitch.isHidden() == False
        assert self.widget.si_Nslot.value() == 0
        assert self.widget.c_wind_type.currentIndex() == 2
        assert self.widget.c_wind_type.currentText() == "Double Layer Distributed"
        assert self.widget.is_reverse.checkState() == Qt.Unchecked
        assert self.widget.out_shape.text() == "Winding Matrix shape: [2, 1, 36, 4]"
        # check result rotor
        assert type(self.test_obj.rotor.winding) == WindingCW2LT
        assert self.test_obj.rotor.winding.p == 8
        assert self.test_obj.rotor.winding.qs == 1
        assert self.widget2.si_qs.value() == 1
        assert self.widget2.si_qs.isEnabled() == False
        assert self.widget2.si_coil_pitch.isHidden() == True
        assert self.widget2.si_Nslot.value() == 0
        assert self.widget2.c_wind_type.currentIndex() == 0
        assert (
            self.widget2.c_wind_type.currentText()
            == "DC wound winding for salient pole"
        )
        assert self.widget2.is_reverse.checkState() == Qt.Unchecked
        assert self.widget2.out_shape.text() == "Winding Matrix shape: [1, 2, 36, 1]"

    def test_set_wind_type(self):
        """Check that the Widget allow to update type_winding"""
        self.widget.c_wind_type.setCurrentIndex(0)
        assert type(self.test_obj.stator.winding) == WindingCW2LT
        assert self.widget.out_shape.text() == "Winding Matrix shape: [1, 2, 36, 6]"

        self.widget.c_wind_type.setCurrentIndex(1)
        assert type(self.test_obj.stator.winding) == WindingCW1L
        assert self.widget.out_shape.text() == "Winding Matrix shape: [1, 1, 36, 6]"

        self.widget.c_wind_type.setCurrentIndex(2)
        assert type(self.test_obj.stator.winding) == WindingDW2L
        assert self.widget.out_shape.text() == "Winding Matrix shape: [2, 1, 36, 6]"

        self.widget.c_wind_type.setCurrentIndex(3)
        assert type(self.test_obj.stator.winding) == WindingDW1L
        assert self.widget.out_shape.text() == "Winding Matrix shape: [1, 1, 36, 6]"

        self.widget.c_wind_type.setCurrentIndex(4)
        assert type(self.test_obj.stator.winding) == WindingCW2LR
        assert self.widget.out_shape.text() == "Winding Matrix shape: [2, 1, 36, 6]"

    def test_set_qs(self):
        """Check that the Widget allow to update qs"""
        self.widget.si_qs.clear()  # Clear the field before writing
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_qs, str(value))
        self.widget.si_qs.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.qs == value
        assert (
            self.widget.out_shape.text()
            == "Winding Matrix shape: [2, 1, 36, " + str(value) + "]"
        )

    def test_set_is_reverse(self):
        """Check that the Widget allow to update is_reverse_wind"""
        self.widget.is_reverse.setCheckState(Qt.Unchecked)
        assert not self.test_obj.stator.winding.is_reverse_wind
        self.widget.is_reverse.setCheckState(Qt.Checked)
        assert self.test_obj.stator.winding.is_reverse_wind

    def test_set_coil_pitch(self):
        """Check that the Widget allow to update coil_pitch"""
        self.widget.si_coil_pitch.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(self.widget.si_coil_pitch, str(value))
        self.widget.si_coil_pitch.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.coil_pitch == value

    def test_set_Nslot(self):
        """Check that the Widget allow to update Nslot"""
        self.widget.si_Nslot.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(self.widget.si_Nslot, str(value))
        self.widget.si_Nslot.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.Nslot_shift_wind == value
