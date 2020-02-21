# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Dec 08 11:59:31 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.Classes.HoleM50 import HoleM50


class test_SMachineType(TestCase):
    """Test that the widget SMachineType behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = MachineSCIM(name="test_machine", type_machine=1)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 6
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )

        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test SMachineType")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.le_name.text(), "test_machine")
        self.assertEqual(self.widget.si_p.value(), 6)
        self.assertEqual(self.widget.c_type.currentIndex(), 0)
        self.assertEqual(self.widget.c_type.currentText(), "SCIM")
        self.assertEqual(self.widget.is_inner_rotor.checkState(), Qt.Checked)

        # DFIM
        self.test_obj = MachineDFIM(name="test_machine_dfim", type_machine=4)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 7
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        self.assertEqual(self.widget.le_name.text(), "test_machine_dfim")
        self.assertEqual(self.widget.si_p.value(), 7)
        self.assertEqual(self.widget.c_type.currentIndex(), 1)
        self.assertEqual(self.widget.c_type.currentText(), "DFIM")
        self.assertEqual(self.widget.is_inner_rotor.checkState(), Qt.Unchecked)

        # SyRM
        self.test_obj = MachineSyRM(name="test_machine_syrm", type_machine=5)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 21
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        self.assertEqual(self.widget.le_name.text(), "test_machine_syrm")
        self.assertEqual(self.widget.si_p.value(), 21)
        self.assertEqual(self.widget.c_type.currentIndex(), 2)
        self.assertEqual(self.widget.c_type.currentText(), "SyRM")
        self.assertEqual(self.widget.is_inner_rotor.checkState(), Qt.Unchecked)

        # SPMSM
        self.test_obj = MachineSIPMSM(name="test_machine_spmsm", type_machine=6)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 8
        self.test_obj.rotor = LamSlotMag(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        self.assertEqual(self.widget.le_name.text(), "test_machine_spmsm")
        self.assertEqual(self.widget.si_p.value(), 8)
        self.assertEqual(self.widget.c_type.currentIndex(), 3)
        self.assertEqual(self.widget.c_type.currentText(), "SPMSM")
        self.assertEqual(self.widget.is_inner_rotor.checkState(), Qt.Unchecked)

        # SIPMSM
        self.test_obj = MachineSIPMSM(name="test_machine_sipmsm", type_machine=7)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 9
        self.test_obj.rotor = LamSlotMag(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        self.assertEqual(self.widget.le_name.text(), "test_machine_sipmsm")
        self.assertEqual(self.widget.si_p.value(), 9)
        self.assertEqual(self.widget.c_type.currentIndex(), 4)
        self.assertEqual(self.widget.c_type.currentText(), "SIPMSM")
        self.assertEqual(self.widget.is_inner_rotor.checkState(), Qt.Checked)

        # IPMSM
        self.test_obj = MachineIPMSM(name="test_machine_ipmsm", type_machine=8)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 10
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        self.assertEqual(self.widget.le_name.text(), "test_machine_ipmsm")
        self.assertEqual(self.widget.si_p.value(), 10)
        self.assertEqual(self.widget.c_type.currentIndex(), 5)
        self.assertEqual(self.widget.c_type.currentText(), "IPMSM")
        self.assertEqual(self.widget.is_inner_rotor.checkState(), Qt.Unchecked)

        # WRSM
        self.test_obj = MachineWRSM(name="test_machine_wrsm", type_machine=9)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 5
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        self.assertEqual(self.widget.le_name.text(), "test_machine_wrsm")
        self.assertEqual(self.widget.si_p.value(), 5)
        self.assertEqual(self.widget.c_type.currentIndex(), 6)
        self.assertEqual(self.widget.c_type.currentText(), "WRSM")
        self.assertEqual(self.widget.is_inner_rotor.checkState(), Qt.Unchecked)

    def test_set_name(self):
        """Check that the Widget allow to update name"""
        # Clear the field before writing the new value
        self.widget.le_name.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.le_name, "test_" + str(value))
        self.widget.le_name.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.name, "test_" + str(value))

    def test_set_is_inner_rotor(self):
        """Check that the Widget allow to update is_inner_rotor"""
        self.widget.is_inner_rotor.setCheckState(Qt.Checked)
        self.assertTrue(self.test_obj.rotor.is_internal)

        self.widget.is_inner_rotor.setCheckState(Qt.Unchecked)
        self.assertFalse(self.test_obj.rotor.is_internal)

    def test_set_p_scim(self):
        """Check that the Widget allow to update p"""
        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_p, str(value))
        self.widget.si_p.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.p, value)
        self.assertEqual(self.test_obj.rotor.winding.p, value)

    def test_set_p_dfim(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineDFIM(name="test_machine_dfim", type_machine=4)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_p, str(value))
        self.widget.si_p.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.p, value)
        self.assertEqual(self.test_obj.rotor.winding.p, value)

    def test_set_p_spmsm(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineSIPMSM(name="test_machine_spmsm", type_machine=6)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamSlotMag(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_p, str(value))
        self.widget.si_p.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.p, value)
        self.assertEqual(self.test_obj.rotor.slot.Zs, 2 * value)

    def test_set_p_sipmsm(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineSIPMSM(name="test_machine_ipmsm", type_machine=7)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamSlotMag(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_p, str(value))
        self.widget.si_p.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.p, value)
        self.assertEqual(self.test_obj.rotor.slot.Zs, 2 * value)

    def test_set_p_ipmsm(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineIPMSM(name="test_machine_ipmsm", type_machine=8)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=0))
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_p, str(value))
        self.widget.si_p.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.p, value)
        self.assertEqual(self.test_obj.rotor.hole[0].Zh, 2 * value)

    def test_set_p_syrm(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineSyRM(name="test_machine_ipmsm", type_machine=5)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=0))
        self.widget = SMachineType(machine=self.test_obj, matlib=[], is_stator=False)

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(self.widget.si_p, str(value))
        self.widget.si_p.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.p, value)
        self.assertEqual(self.test_obj.rotor.hole[0].Zh, 2 * value)
