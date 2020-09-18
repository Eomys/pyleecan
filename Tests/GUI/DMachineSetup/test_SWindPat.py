# -*- coding: utf-8 -*-

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

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


class test_SWindPat(TestCase):
    """Test that the widget SWindPat behave like it should"""

    def setUp(self):
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
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test SWindPat")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.si_qs.value(), 6)
        self.assertEqual(self.widget.si_coil_pitch.value(), 8)
        self.assertEqual(self.widget.si_Nslot.value(), 10)
        self.assertEqual(self.widget.c_wind_type.currentIndex(), 2)
        self.assertEqual(self.widget.is_reverse.checkState(), Qt.Checked)
        self.assertEqual(
            self.widget.out_shape.text(), "Winding Matrix shape: [2, 1, 36, 6]"
        )

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
        self.assertEqual(type(self.test_obj.stator.winding), WindingDW2L)
        self.assertEqual(self.test_obj.stator.winding.p, 8)
        self.assertEqual(self.test_obj.stator.winding.qs, 4)
        self.assertEqual(self.widget.si_qs.isEnabled(), True)
        self.assertEqual(self.widget.si_coil_pitch.isHidden(), False)
        self.assertEqual(self.widget.si_Nslot.value(), 0)
        self.assertEqual(self.widget.c_wind_type.currentIndex(), 2)
        self.assertEqual(
            self.widget.c_wind_type.currentText(), "Double Layer Distributed"
        )
        self.assertEqual(self.widget.is_reverse.checkState(), Qt.Unchecked)
        self.assertEqual(
            self.widget.out_shape.text(), "Winding Matrix shape: [2, 1, 36, 4]"
        )
        # Check result rotor
        self.assertEqual(type(self.test_obj.rotor.winding), WindingCW2LT)
        self.assertEqual(self.test_obj.rotor.winding.p, 8)
        self.assertEqual(self.test_obj.rotor.winding.qs, 1)
        self.assertEqual(self.widget2.si_qs.value(), 1)
        self.assertEqual(self.widget2.si_qs.isEnabled(), False)
        self.assertEqual(self.widget2.si_coil_pitch.isHidden(), True)
        self.assertEqual(self.widget2.si_Nslot.value(), 0)
        self.assertEqual(self.widget2.c_wind_type.currentIndex(), 0)
        self.assertEqual(
            self.widget2.c_wind_type.currentText(), "DC wound winding for salient pole"
        )
        self.assertEqual(self.widget2.is_reverse.checkState(), Qt.Unchecked)
        self.assertEqual(
            self.widget2.out_shape.text(), "Winding Matrix shape: [1, 2, 36, 1]"
        )

    def test_set_wind_type(self):
        """Check that the Widget allow to update type_winding"""
        self.widget.c_wind_type.setCurrentIndex(0)
        self.assertEqual(type(self.test_obj.stator.winding), WindingCW2LT)
        self.assertEqual(
            self.widget.out_shape.text(), "Winding Matrix shape: [1, 2, 36, 6]"
        )

        self.widget.c_wind_type.setCurrentIndex(1)
        self.assertEqual(type(self.test_obj.stator.winding), WindingCW1L)
        self.assertEqual(
            self.widget.out_shape.text(), "Winding Matrix shape: [1, 1, 36, 6]"
        )

        self.widget.c_wind_type.setCurrentIndex(2)
        self.assertEqual(type(self.test_obj.stator.winding), WindingDW2L)
        self.assertEqual(
            self.widget.out_shape.text(), "Winding Matrix shape: [2, 1, 36, 6]"
        )

        self.widget.c_wind_type.setCurrentIndex(3)
        self.assertEqual(type(self.test_obj.stator.winding), WindingDW1L)
        self.assertEqual(
            self.widget.out_shape.text(), "Winding Matrix shape: [1, 1, 36, 6]"
        )

        self.widget.c_wind_type.setCurrentIndex(4)
        self.assertEqual(type(self.test_obj.stator.winding), WindingCW2LR)
        self.assertEqual(
            self.widget.out_shape.text(), "Winding Matrix shape: [2, 1, 36, 6]"
        )

    def test_set_qs(self):
        """Check that the Widget allow to update qs"""
        self.widget.si_qs.clear()  # Clear the field before writing
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_qs, str(value))
        self.widget.si_qs.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.qs, value)
        self.assertEqual(
            self.widget.out_shape.text(),
            "Winding Matrix shape: [2, 1, 36, " + str(value) + "]",
        )

    def test_set_is_reverse(self):
        """Check that the Widget allow to update is_reverse_wind"""
        self.widget.is_reverse.setCheckState(Qt.Unchecked)
        self.assertFalse(self.test_obj.stator.winding.is_reverse_wind)
        self.widget.is_reverse.setCheckState(Qt.Checked)
        self.assertTrue(self.test_obj.stator.winding.is_reverse_wind)

    def test_set_coil_pitch(self):
        """Check that the Widget allow to update coil_pitch"""
        self.widget.si_coil_pitch.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(self.widget.si_coil_pitch, str(value))
        self.widget.si_coil_pitch.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.coil_pitch, value)

    def test_set_Nslot(self):
        """Check that the Widget allow to update Nslot"""
        self.widget.si_Nslot.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(self.widget.si_Nslot, str(value))
        self.widget.si_Nslot.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.Nslot_shift_wind, value)
