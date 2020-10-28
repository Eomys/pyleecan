# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWindParam.SWindParam import SWindParam


import pytest


@pytest.mark.GUI
class TestSWindParam(object):
    """Test that the widget SWindParam behave like it should"""

    def setup_method(self, method):
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
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test SWindParam")
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

        assert self.widget_1.si_Npcpp.value() == 10
        assert self.widget_1.si_Ntcoil.value() == 11
        assert self.widget_1.in_Npcpp.text() == "Npcpp :"
        assert self.widget_1.in_Ntcoil.text() == "Ntcoil :"
        assert self.widget_1.in_Zs.text() == "Zs: 36"
        assert self.widget_1.in_qs.text() == "qs: 3"
        assert self.widget_1.out_Ncspc.text() == "Ncspc: ?"
        assert self.widget_1.out_Ntspc.text() == "Ntspc: ?"

        assert self.widget_2.si_Npcpp.value() == 20
        assert self.widget_2.si_Ntcoil.value() == 21
        assert self.widget_2.in_Npcpp.text() == "Npcpp :"
        assert self.widget_2.in_Ntcoil.text() == "Ntcoil :"
        assert self.widget_2.in_Zs.text() == "Zs: 36"
        assert self.widget_2.in_qs.text() == "qs: 3"
        assert self.widget_2.out_Ncspc.text() == "Ncspc: ?"
        assert self.widget_2.out_Ntspc.text() == "Ntspc: ?"
        self.test_obj = MachineSCIM()
        self.test_obj.rotor = LamSlotWind(is_stator=False)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding = Winding(Npcpp=20, Ntcoil=None)

        self.test_obj.type_machine = 9

        self.widget_2 = SWindParam(machine=self.test_obj, matlib=[], is_stator=False)

        assert self.widget_2.in_Zs.isHidden()
        assert self.widget_2.in_Nlay.isHidden()

    def test_set_Npcp1(self):
        """Check that the Widget allow to update Npcp1"""
        # Clear the field before writing the new value
        self.widget_1.si_Npcpp.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_1.si_Npcpp, str(value))
        self.widget_1.si_Npcpp.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.Npcpp == value

    def test_set_Npcp2(self):
        """Check that the Widget allow to update Npcp2"""
        # Clear the field before writing the new value
        self.widget_2.si_Npcpp.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_2.si_Npcpp, str(value))
        self.widget_2.si_Npcpp.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.Npcpp == value

    def test_set_Ntcoil1(self):
        """Check that the Widget allow to update Ntcoil1"""
        # Clear the field before writing the new value
        self.widget_1.si_Ntcoil.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_1.si_Ntcoil, str(value))
        self.widget_1.si_Ntcoil.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.Ntcoil == value

    def test_set_Ntcoil2(self):
        """Check that the Widget allow to update Ntcoil2"""
        # Clear the field before writing the new value
        self.widget_2.si_Ntcoil.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_2.si_Ntcoil, str(value))
        self.widget_2.si_Ntcoil.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.Ntcoil == value

    def test_check(self):
        """Check that the check method return errors"""
        rotor = LamSlotWind(is_stator=False)
        rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(Npcpp=20, Ntcoil=None)

        assert self.widget_1.check(rotor) == "You must set Ntcoil !"
