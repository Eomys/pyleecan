import sys
from random import uniform

import pytest
from qtpy import QtWidgets
from qtpy.QtTest import QTest

from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Material import Material
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.Winding import Winding
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType12.PCondType12 import (
    PCondType12,
)
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY


class TestSWindCond(object):
    def setup_method(self):
        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind(is_stator=True)
        test_obj.stator.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.stator.winding = Winding(Npcp=10, Ntcoil=11, Lewout=40e-3)
        test_obj.stator.winding.conductor = CondType11(
            Nwppc_rad=2, Nwppc_tan=3, Hwire=10e-3, Wwire=20e-3, Wins_wire=30e-3
        )

        test_obj.rotor = LamSlotWind(is_stator=False)
        test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.rotor.winding = Winding(Npcp=20, Ntcoil=21)
        test_obj.rotor.winding.conductor = CondType12(
            Nwppc=4, Wwire=11e-3, Wins_wire=21e-3, Wins_cond=31e-3
        )

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        widget_1 = SWindCond(
            machine=test_obj, material_dict=material_dict, is_stator=True
        )
        widget_2 = SWindCond(
            machine=test_obj, material_dict=material_dict, is_stator=False
        )

        self.widget = widget_1
        self.widget2 = widget_2
        self.test_obj = test_obj
        self.material_dict = material_dict

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSWindCond")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    @pytest.mark.SCIM
    def test_init(self):
        assert self.widget.c_cond_type.currentIndex() == 0
        assert self.widget.w_cond.si_Nwpc1_rad.value() == 2
        assert self.widget.w_cond.si_Nwpc1_tan.value() == 3
        assert self.widget.w_cond.lf_Hwire.value() == 10e-3
        assert self.widget.w_cond.lf_Wwire.value() == 20e-3
        assert self.widget.w_cond.lf_Wins_wire.value() == 30e-3
        assert self.widget.w_cond.lf_Lewout.value() == 40e-3
        assert self.widget.w_cond.w_mat_0.title() == "Strand material"

        assert self.widget2.c_cond_type.currentIndex() == 1
        assert self.widget2.w_cond.si_Nwpc1.value() == 4
        assert self.widget2.w_cond.lf_Wwire.value() == 11e-3
        assert self.widget2.w_cond.lf_Wins_wire.value() == 21e-3
        assert self.widget2.w_cond.lf_Wins_cond.value() == 31e-3
        assert self.widget2.w_cond.w_mat_0.title() == "Strand material"

        self.test_obj.stator.winding.conductor = None
        self.widget = SWindCond(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=True,
        )

        assert type(self.test_obj.stator.winding.conductor) is CondType11

    @pytest.mark.SCIM
    def test_set_si_Nwpc1_rad(self):
        """Check that the Widget allow to update si_Nwpc1_rad"""
        # Clear the field before writing the new value
        self.widget.w_cond.si_Nwpc1_rad.clear()
        value = int(uniform(5, 100))
        self.widget.w_cond.si_Nwpc1_rad.setValue(value)
        self.widget.w_cond.si_Nwpc1_rad.editingFinished.emit()

        assert self.test_obj.stator.winding.conductor.Nwppc_rad == value
        assert self.widget.w_cond.in_Wwire.text() == "Strand width"
        assert self.widget.w_cond.w_mat_0.title() == "Strand material"

    @pytest.mark.SCIM
    def test_set_si_Nwpc1_tan(self):
        """Check that the Widget allow to update si_Nwpc1_tan"""
        # Clear the field before writing the new value
        self.widget.w_cond.si_Nwpc1_tan.clear()
        value = int(uniform(5, 100))
        self.widget.w_cond.si_Nwpc1_tan.setValue(value)
        self.widget.w_cond.si_Nwpc1_tan.editingFinished.emit()

        assert self.test_obj.stator.winding.conductor.Nwppc_tan == value
        assert self.widget.w_cond.in_Wwire.text() == "Strand width"
        assert self.widget.w_cond.w_mat_0.title() == "Strand material"

    @pytest.mark.SCIM
    def test_set_si_Nwpc1(self):
        """Check that the Widget allow to update si_Nwpc1"""
        # Clear the field before writing the new value
        self.widget2.w_cond.si_Nwpc1.clear()
        value = int(uniform(5, 100))
        self.widget2.w_cond.si_Nwpc1.setValue(value)
        self.widget2.w_cond.si_Nwpc1.editingFinished.emit()

        assert self.test_obj.rotor.winding.conductor.Nwppc == value
        assert self.widget2.w_cond.in_Wwire.text() == "Strand diameter"
        assert self.widget2.w_cond.w_mat_0.title() == "Strand material"
        assert not self.widget2.w_cond.lf_Wins_cond.isHidden()

    @pytest.mark.SCIM
    def test_set_Wins_wire(self):
        """Check that the Widget allow to update Wins_wire"""
        # Clear the field before writing the new value
        self.widget.w_cond.lf_Wins_wire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget.w_cond.lf_Wins_wire, str(value))
        self.widget.w_cond.lf_Wins_wire.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.conductor.Wins_wire == value

        # Clear the field before writing the new value
        self.widget2.w_cond.lf_Wins_wire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget2.w_cond.lf_Wins_wire, str(value))
        self.widget2.w_cond.lf_Wins_wire.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.conductor.Wins_wire == value

    @pytest.mark.SCIM
    def test_set_Wwire(self):
        """Check that the Widget allow to update Wins_wire"""
        # Clear the field before writing the new value
        self.widget.w_cond.lf_Wwire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget.w_cond.lf_Wwire, str(value))
        self.widget.w_cond.lf_Wwire.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.conductor.Wwire == value

        # Clear the field before writing the new value
        self.widget2.w_cond.lf_Wwire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget2.w_cond.lf_Wwire, str(value))
        self.widget2.w_cond.lf_Wwire.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.conductor.Wwire == value

    @pytest.mark.SCIM
    def test_set_Lewout(self):
        """Check that the Widget allow to update Lewout"""
        # Clear the field before writing the new value
        self.widget.w_cond.lf_Lewout.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget.w_cond.lf_Lewout, str(value))
        self.widget.w_cond.lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.winding.Lewout == value

        # Clear the field before writing the new value
        self.widget2.w_cond.lf_Lewout.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget2.w_cond.lf_Lewout, str(value))
        self.widget2.w_cond.lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.Lewout == value

    @pytest.mark.SCIM
    def test_set_Wins_cond(self):
        """Check that the Widget allow to update Wins_cond"""
        # Clear the field before writing the new value
        self.widget2.w_cond.lf_Wins_cond.clear()
        value = uniform(5, 100)
        QTest.keyClicks(self.widget2.w_cond.lf_Wins_cond, str(value))
        # To trigger the slot
        self.widget2.w_cond.lf_Wins_cond.editingFinished.emit()

        assert self.test_obj.rotor.winding.conductor.Wins_cond == value

    @pytest.mark.SCIM
    def test_set_cond_type(self):
        """Check that the Widget allow to update conductor type"""
        assert type(self.test_obj.stator.winding.conductor) is CondType11

        self.widget.c_cond_type.setCurrentIndex(1)
        assert type(self.test_obj.stator.winding.conductor) is CondType12

        self.widget.c_cond_type.setCurrentIndex(0)
        assert type(self.test_obj.stator.winding.conductor) is CondType11

    @pytest.mark.SCIM
    def test_check(self):
        """Check that the check method return errors"""
        rotor = LamSlotWind(is_stator=False)
        rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(Npcp=20, Ntcoil=None)
        rotor.winding.conductor = CondType12(
            Nwppc=4, Wwire=None, Wins_wire=21e-3, Wins_cond=31e-3
        )

        assert self.widget2.check(rotor) == "Strand diameter must be set"

    @pytest.mark.SCIM
    def test_init_PCondType12(self):
        """Check that the init is setting a conductor if None"""
        lam = LamSlotWind(is_stator=False)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding = Winding(Npcp=20, Ntcoil=21, Lewout=None)
        lam.winding.conductor = None
        widget = PCondType12(lamination=lam, material_dict=self.material_dict)
        assert type(widget.cond) is CondType12
        assert widget.cond.Nwppc == 1
        assert widget.cond.Wins_wire is None
        assert widget.cond.Wins_cond is None
        assert widget.lam.winding.Lewout == 0

    @pytest.mark.SCIM
    def test_check_PCondType12(self):
        """Check that the check methods is correctly working"""
        lam = LamSlotWind(is_stator=False)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding = Winding(Npcp=20, Ntcoil=21, Lewout=0.15)
        lam.winding.conductor = None
        widget = PCondType12(lamination=lam, material_dict=self.material_dict)
        widget.cond.Wwire = 0.5
        widget.cond.Wins_wire = 0.01
        widget.cond.Wins_cond = 0.1
        assert (
            widget.check(lam) == "Overall diameter must be larger than strand diameter"
        )

        widget.cond.Wins_cond = 0.6
        widget.lam.winding.Lewout = None
        assert widget.check(lam) == "End winding length must be set"
        widget.cond.Nwppc = 2
        widget.cond.Wins_cond = None
        assert widget.check(lam) == "Overall diameter must be set"
        widget.cond.Wins_wire = (
            None  # Not mandatory parameter + change how check is handled
        )
        assert widget.check(lam) == "End winding length must be set"
        widget.cond.Wwire = None
        assert widget.check(lam) == "Strand diameter must be set"
        widget.cond.Nwppc = None
        assert widget.check(lam) == "Strands per hand must be set"

    def test_insulation_group(self):
        # CondType11
        # Deactivate insulation
        self.widget.w_cond.g_ins.setChecked(False)
        assert not self.widget.w_cond.in_Wins_wire.isEnabled()
        assert not self.widget.w_cond.lf_Wins_wire.isEnabled()
        assert not self.widget.w_cond.unit_Wins_wire.isEnabled()
        assert not self.widget.w_cond.w_mat_1.isEnabled()
        assert self.test_obj.stator.winding.conductor.Wins_wire is None
        # Activate insulation
        self.widget.w_cond.g_ins.setChecked(True)
        assert self.widget.w_cond.in_Wins_wire.isEnabled()
        assert self.widget.w_cond.lf_Wins_wire.isEnabled()
        assert self.widget.w_cond.unit_Wins_wire.isEnabled()
        assert self.widget.w_cond.w_mat_1.isEnabled()
        assert self.widget.w_cond.lf_Wins_wire.value() == 0.03
        assert self.test_obj.stator.winding.conductor.Wins_wire == 0.03

        # CondType12
        # Hide insulation
        self.widget2.w_cond.g_ins.setChecked(False)
        assert not self.widget2.w_cond.in_Wins_wire.isEnabled()
        assert not self.widget2.w_cond.lf_Wins_wire.isEnabled()
        assert not self.widget2.w_cond.unit_Wins_wire.isEnabled()
        assert not self.widget2.w_cond.in_Wins_cond.isEnabled()
        assert not self.widget2.w_cond.lf_Wins_cond.isEnabled()
        assert not self.widget2.w_cond.unit_Wins_cond.isEnabled()
        assert not self.widget2.w_cond.w_mat_1.isEnabled()
        assert self.test_obj.rotor.winding.conductor.Wins_wire is None
        assert self.test_obj.rotor.winding.conductor.Wins_cond is None
        # Show insulation
        self.widget2.w_cond.g_ins.setChecked(True)
        assert self.widget2.w_cond.in_Wins_wire.isEnabled()
        assert self.widget2.w_cond.lf_Wins_wire.isEnabled()
        assert self.widget2.w_cond.unit_Wins_wire.isEnabled()
        assert self.widget2.w_cond.in_Wins_cond.isEnabled()
        assert self.widget2.w_cond.lf_Wins_cond.isEnabled()
        assert self.widget2.w_cond.unit_Wins_cond.isEnabled()
        assert self.widget2.w_cond.w_mat_1.isEnabled()
        assert self.widget2.w_cond.lf_Wins_wire.value() == 0.021
        assert self.widget2.w_cond.lf_Wins_cond.value() == 0.031
        assert self.test_obj.rotor.winding.conductor.Wins_wire == 0.021
        assert self.test_obj.rotor.winding.conductor.Wins_cond == 0.031


if __name__ == "__main__":
    a = TestSWindCond()
    a.setup_class()
    a.setup_method()
    # a.test_init()
    # a.test_set_Wins_wire()
    # a.test_set_Wwire()
    # a.test_set_Lewout()
    # a.test_set_Wins_cond()
    # a.test_check()
    # a.test_init_PCondType12()
    # a.test_check_PCondType12()
    # a.test_set_si_Nwpc1_rad()
    # a.test_set_si_Nwpc1_tan()
    # a.test_set_si_Nwpc1()
    a.test_insulation_group()
    a.teardown_class()
    print("Done")
