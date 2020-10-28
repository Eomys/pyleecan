import sys
from random import uniform

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Material import Material
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.Winding import Winding
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib


@pytest.mark.GUI
class TestSWindCond(object):
    def setup_method(self, method):
        """setup any state specific to the execution of the given module."""
        self.test_obj = MachineSCIM()
        self.test_obj.stator = LamSlotWind(is_stator=True)
        self.test_obj.stator.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.stator.winding = Winding(Npcpp=10, Ntcoil=11, Lewout=40e-3)
        self.test_obj.stator.winding.conductor = CondType11(
            Nwppc_rad=2, Nwppc_tan=3, Hwire=10e-3, Wwire=20e-3, Wins_wire=30e-3
        )

        self.test_obj.rotor = LamSlotWind(is_stator=False)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding = Winding(Npcpp=20, Ntcoil=21)
        self.test_obj.rotor.winding.conductor = CondType12(
            Nwppc=4, Wwire=11e-3, Wins_wire=21e-3, Wins_cond=31e-3
        )

        self.matlib = MatLib()
        self.matlib.dict_mat["RefMatLib"] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        self.matlib.dict_mat["RefMatLib"][0].elec.rho = 0.31
        self.matlib.dict_mat["RefMatLib"][1].elec.rho = 0.32
        self.matlib.dict_mat["RefMatLib"][2].elec.rho = 0.33

        self.widget_1 = SWindCond(
            machine=self.test_obj, matlib=self.matlib, is_stator=True
        )
        self.widget_2 = SWindCond(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )

    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to
        setup_class.
        """
        cls.app.quit()

    def test_init(self):
        assert self.widget_1.c_cond_type.currentIndex() == 0
        assert self.widget_1.w_cond.si_Nwpc1_rad.value() == 2
        assert self.widget_1.w_cond.si_Nwpc1_tan.value() == 3
        assert self.widget_1.w_cond.lf_Hwire.value() == 10e-3
        assert self.widget_1.w_cond.lf_Wwire.value() == 20e-3
        assert self.widget_1.w_cond.lf_Wins_wire.value() == 30e-3
        assert self.widget_1.w_cond.lf_Lewout.value() == 40e-3

        assert self.widget_2.c_cond_type.currentIndex() == 1
        assert self.widget_2.w_cond.si_Nwpc1.value() == 4
        assert self.widget_2.w_cond.lf_Wwire.value() == 11e-3
        assert self.widget_2.w_cond.lf_Wins_wire.value() == 21e-3
        assert self.widget_2.w_cond.lf_Wins_cond.value() == 31e-3

        self.test_obj.stator.winding.conductor = None
        self.widget_1 = SWindCond(
            machine=self.test_obj, matlib=self.matlib, is_stator=True
        )

        assert self.widget_1.w_mat_0.in_mat_type.text() == "mat_wind1: "
        assert type(self.test_obj.stator.winding.conductor) is CondType11

    def test_set_si_Nwpc1_rad(self):
        """Check that the Widget allow to update si_Nwpc1_rad"""
        # Clear the field before writing the new value
        self.widget_1.w_cond.si_Nwpc1_rad.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_1.w_cond.si_Nwpc1_rad, str(value))
        self.widget_1.w_cond.si_Nwpc1_rad.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.conductor.Nwppc_rad == value

    def test_set_si_Nwpc1_tan(self):
        """Check that the Widget allow to update si_Nwpc1_tan"""
        # Clear the field before writing the new value
        self.widget_1.w_cond.si_Nwpc1_tan.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_1.w_cond.si_Nwpc1_tan, str(value))
        self.widget_1.w_cond.si_Nwpc1_tan.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.conductor.Nwppc_tan == value

    def test_set_si_Nwpc1(self):
        """Check that the Widget allow to update si_Nwpc1"""
        # Clear the field before writing the new value
        self.widget_2.w_cond.si_Nwpc1.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(self.widget_2.w_cond.si_Nwpc1, str(value))
        self.widget_2.w_cond.si_Nwpc1.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.conductor.Nwppc == value

    def test_set_Wins_wire(self):
        """Check that the Widget allow to update Wins_wire"""
        # Clear the field before writing the new value
        self.widget_1.w_cond.lf_Wins_wire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget_1.w_cond.lf_Wins_wire, str(value))
        self.widget_1.w_cond.lf_Wins_wire.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.conductor.Wins_wire == value

        # Clear the field before writing the new value
        self.widget_2.w_cond.lf_Wins_wire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget_2.w_cond.lf_Wins_wire, str(value))
        self.widget_2.w_cond.lf_Wins_wire.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.conductor.Wins_wire == value

    def test_set_Lewout(self):
        """Check that the Widget allow to update Lewout"""
        # Clear the field before writing the new value
        self.widget_1.w_cond.lf_Lewout.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget_1.w_cond.lf_Lewout, str(value))
        self.widget_1.w_cond.lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.Lewout == value

        # Clear the field before writing the new value
        self.widget_2.w_cond.lf_Lewout.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget_2.w_cond.lf_Lewout, str(value))
        self.widget_2.w_cond.lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.Lewout == value

    def test_set_Wins_cond(self):
        """Check that the Widget allow to update Wins_cond"""
        # Clear the field before writing the new value
        self.widget_2.w_cond.lf_Wins_cond.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget_2.w_cond.lf_Wins_cond, str(value))
        self.widget_2.w_cond.lf_Wins_cond.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.conductor.Wins_cond == value

    def test_set_cond_type(self):
        """Check that the Widget allow to update conductor type"""
        assert type(self.test_obj.stator.winding.conductor) is CondType11

        self.widget_1.c_cond_type.setCurrentIndex(1)
        assert type(self.test_obj.stator.winding.conductor) is CondType12

        self.widget_1.c_cond_type.setCurrentIndex(0)
        assert type(self.test_obj.stator.winding.conductor) is CondType11

    def test_check(self):
        """Check that the check method return errors"""
        rotor = LamSlotWind(is_stator=False)
        rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(Npcpp=20, Ntcoil=None)
        rotor.winding.conductor = CondType12(
            Nwppc=4, Wwire=None, Wins_wire=21e-3, Wins_cond=31e-3
        )

        assert self.widget_2.check(rotor) == "You must set Wwire !"
