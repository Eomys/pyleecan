# -*- coding: utf-8 -*-

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWindParam.SWindParam import SWindParam


import pytest


@pytest.mark.GUI
class test_SWindParam(TestCase):
    """Test that the widget SWindParam behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = MachineSCIM()
        self.test_obj.stator = LamSlotWind(is_stator=True)
        self.test_obj.stator.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.stator.winding = Winding(Npcpp=10, Ntcoil=11)

        self.test_obj.rotor = LamSlotWind(is_stator=False)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding = Winding(Npcpp=20, Ntcoil=21)

        self.widget_1 = SWindParam(machine=self.test_obj, matlib=[], is_stator=True)
        self.widget_2 = SWindParam(machine=self.test_obj, matlib=[], is_stator=False)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test SWindParam")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget_1.si_Npcpp.value(), 10)
        self.assertEqual(self.widget_1.si_Ntcoil.value(), 11)
        self.assertEqual(self.widget_1.in_Npcpp.text(), "Npcpp :")
        self.assertEqual(self.widget_1.in_Ntcoil.text(), "Ntcoil :")
        self.assertEqual(self.widget_1.in_Zs.text(), "Zs: 36")
        self.assertEqual(self.widget_1.in_qs.text(), "qs: 3")
        self.assertEqual(self.widget_1.out_Ncspc.text(), "Ncspc: ?")
        self.assertEqual(self.widget_1.out_Ntspc.text(), "Ntspc: ?")

        self.assertEqual(self.widget_2.si_Npcpp.value(), 20)
        self.assertEqual(self.widget_2.si_Ntcoil.value(), 21)
        self.assertEqual(self.widget_2.in_Npcpp.text(), "Npcpp :")
        self.assertEqual(self.widget_2.in_Ntcoil.text(), "Ntcoil :")
        self.assertEqual(self.widget_2.in_Zs.text(), "Zs: 36")
        self.assertEqual(self.widget_2.in_qs.text(), "qs: 3")
        self.assertEqual(self.widget_2.out_Ncspc.text(), "Ncspc: ?")
        self.assertEqual(self.widget_2.out_Ntspc.text(), "Ntspc: ?")

    def test_set_Npcp1(self):
        """Check that the Widget allow to update Npcp1"""
        # Clear the field before writing the new value
        self.widget_1.si_Npcpp.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_1.si_Npcpp, str(value))
        self.widget_1.si_Npcpp.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.Npcpp, value)

    def test_set_Npcp2(self):
        """Check that the Widget allow to update Npcp2"""
        self.widget_2.si_Npcpp.clear()  # Clear the field before writing
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_2.si_Npcpp, str(value))
        self.widget_2.si_Npcpp.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.rotor.winding.Npcpp, value)

    def test_set_Ntcoil1(self):
        """Check that the Widget allow to update Ntcoil1"""
        self.widget_1.si_Ntcoil.clear()  # Clear the field before writing
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_1.si_Ntcoil, str(value))
        self.widget_1.si_Ntcoil.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.stator.winding.Ntcoil, value)

    def test_set_Ntcoil2(self):
        """Check that the Widget allow to update Ntcoil2"""
        self.widget_2.si_Ntcoil.clear()  # Clear the field before writing
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_2.si_Ntcoil, str(value))
        self.widget_2.si_Ntcoil.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.rotor.winding.Ntcoil, value)
