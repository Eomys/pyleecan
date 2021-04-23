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
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType12.PCondType12 import (
    PCondType12,
)
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib


class TestSWindCond(object):
    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind(is_stator=True)
        test_obj.stator.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.stator.winding = Winding(Npcpp=10, Ntcoil=11, Lewout=40e-3)
        test_obj.stator.winding.conductor = CondType11(
            Nwppc_rad=2, Nwppc_tan=3, Hwire=10e-3, Wwire=20e-3, Wins_wire=30e-3
        )

        test_obj.rotor = LamSlotWind(is_stator=False)
        test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.rotor.winding = Winding(Npcpp=20, Ntcoil=21)
        test_obj.rotor.winding.conductor = CondType12(
            Nwppc=4, Wwire=11e-3, Wins_wire=21e-3, Wins_cond=31e-3
        )

        matlib = MatLib()
        matlib.dict_mat["RefMatLib"] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        matlib.dict_mat["RefMatLib"][0].elec.rho = 0.31
        matlib.dict_mat["RefMatLib"][1].elec.rho = 0.32
        matlib.dict_mat["RefMatLib"][2].elec.rho = 0.33

        widget_1 = SWindCond(machine=test_obj, matlib=matlib, is_stator=True)
        widget_2 = SWindCond(machine=test_obj, matlib=matlib, is_stator=False)

        yield {
            "widget": widget_1,
            "widget2": widget_2,
            "test_obj": test_obj,
            "matlib": matlib,
        }

        self.app.quit()

    def test_init(self, setup):
        assert setup["widget"].c_cond_type.currentIndex() == 0
        assert setup["widget"].w_cond.si_Nwpc1_rad.value() == 2
        assert setup["widget"].w_cond.si_Nwpc1_tan.value() == 3
        assert setup["widget"].w_cond.lf_Hwire.value() == 10e-3
        assert setup["widget"].w_cond.lf_Wwire.value() == 20e-3
        assert setup["widget"].w_cond.lf_Wins_wire.value() == 30e-3
        assert setup["widget"].w_cond.lf_Lewout.value() == 40e-3

        assert setup["widget2"].c_cond_type.currentIndex() == 1
        assert setup["widget2"].w_cond.si_Nwpc1.value() == 4
        assert setup["widget2"].w_cond.lf_Wwire.value() == 11e-3
        assert setup["widget2"].w_cond.lf_Wins_wire.value() == 21e-3
        assert setup["widget2"].w_cond.lf_Wins_cond.value() == 31e-3

        setup["test_obj"].stator.winding.conductor = None
        setup["widget"] = SWindCond(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=True
        )

        assert setup["widget"].w_mat_0.in_mat_type.text() == "mat_wind1: "
        assert type(setup["test_obj"].stator.winding.conductor) is CondType11

    def test_set_si_Nwpc1_rad(self, setup):
        """Check that the Widget allow to update si_Nwpc1_rad"""
        # Clear the field before writing the new value
        setup["widget"].w_cond.si_Nwpc1_rad.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(setup["widget"].w_cond.si_Nwpc1_rad, str(value))
        setup[
            "widget"
        ].w_cond.si_Nwpc1_rad.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.conductor.Nwppc_rad == value

    def test_set_si_Nwpc1_tan(self, setup):
        """Check that the Widget allow to update si_Nwpc1_tan"""
        # Clear the field before writing the new value
        setup["widget"].w_cond.si_Nwpc1_tan.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(setup["widget"].w_cond.si_Nwpc1_tan, str(value))
        setup[
            "widget"
        ].w_cond.si_Nwpc1_tan.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.conductor.Nwppc_tan == value

    def test_set_si_Nwpc1(self, setup):
        """Check that the Widget allow to update si_Nwpc1"""
        # Clear the field before writing the new value
        setup["widget2"].w_cond.si_Nwpc1.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(setup["widget2"].w_cond.si_Nwpc1, str(value))
        setup["widget2"].w_cond.si_Nwpc1.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.conductor.Nwppc == value

    def test_set_Wins_wire(self, setup):
        """Check that the Widget allow to update Wins_wire"""
        # Clear the field before writing the new value
        setup["widget"].w_cond.lf_Wins_wire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(setup["widget"].w_cond.lf_Wins_wire, str(value))
        setup[
            "widget"
        ].w_cond.lf_Wins_wire.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.conductor.Wins_wire == value

        # Clear the field before writing the new value
        setup["widget2"].w_cond.lf_Wins_wire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(setup["widget2"].w_cond.lf_Wins_wire, str(value))
        setup[
            "widget2"
        ].w_cond.lf_Wins_wire.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.conductor.Wins_wire == value

    def test_set_Wwire(self, setup):
        """Check that the Widget allow to update Wins_wire"""
        # Clear the field before writing the new value
        setup["widget"].w_cond.lf_Wwire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(setup["widget"].w_cond.lf_Wwire, str(value))
        setup["widget"].w_cond.lf_Wwire.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.conductor.Wwire == value

        # Clear the field before writing the new value
        setup["widget2"].w_cond.lf_Wwire.clear()
        value = uniform(5, 100)
        QTest.keyClicks(setup["widget2"].w_cond.lf_Wwire, str(value))
        setup["widget2"].w_cond.lf_Wwire.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.conductor.Wwire == value

    def test_set_Lewout(self, setup):
        """Check that the Widget allow to update Lewout"""
        # Clear the field before writing the new value
        setup["widget"].w_cond.lf_Lewout.clear()
        value = uniform(5, 100)
        QTest.keyClicks(setup["widget"].w_cond.lf_Lewout, str(value))
        setup["widget"].w_cond.lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.Lewout == value

        # Clear the field before writing the new value
        setup["widget2"].w_cond.lf_Lewout.clear()
        value = uniform(5, 100)
        QTest.keyClicks(setup["widget2"].w_cond.lf_Lewout, str(value))
        setup["widget2"].w_cond.lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.Lewout == value

    def test_set_Wins_cond(self, setup):
        """Check that the Widget allow to update Wins_cond"""
        # Clear the field before writing the new value
        setup["widget2"].w_cond.lf_Wins_cond.clear()
        value = uniform(5, 100)
        QTest.keyClicks(setup["widget2"].w_cond.lf_Wins_cond, str(value))
        setup[
            "widget2"
        ].w_cond.lf_Wins_cond.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.conductor.Wins_cond == value

    def test_set_cond_type(self, setup):
        """Check that the Widget allow to update conductor type"""
        assert type(setup["test_obj"].stator.winding.conductor) is CondType11

        setup["widget"].c_cond_type.setCurrentIndex(1)
        assert type(setup["test_obj"].stator.winding.conductor) is CondType12

        setup["widget"].c_cond_type.setCurrentIndex(0)
        assert type(setup["test_obj"].stator.winding.conductor) is CondType11

    def test_check(self, setup):
        """Check that the check method return errors"""
        rotor = LamSlotWind(is_stator=False)
        rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(Npcpp=20, Ntcoil=None)
        rotor.winding.conductor = CondType12(
            Nwppc=4, Wwire=None, Wins_wire=21e-3, Wins_cond=31e-3
        )

        assert setup["widget2"].check(rotor) == "You must set Wwire !"

    def test_init_PCondType12(self, setup):
        """Check that the init is setting a conductor if None"""
        lam = LamSlotWind(is_stator=False)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding = Winding(Npcpp=20, Ntcoil=21, Lewout=None)
        lam.winding.conductor = None
        widget = PCondType12(lamination=lam)
        assert type(widget.cond) is CondType12
        assert widget.cond.Nwppc == 1
        assert widget.cond.Wins_wire == 0
        assert widget.cond.Wins_cond == 0
        assert widget.lam.winding.Lewout == 0

    def test_check_PCondType12(self, setup):
        """Check that the check methods is correctly working"""
        lam = LamSlotWind(is_stator=False)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding = Winding(Npcpp=20, Ntcoil=21, Lewout=0.15)
        lam.winding.conductor = None
        widget = PCondType12(lamination=lam)
        widget.cond.Wwire = 0.5

        widget.lam.winding.Lewout = None
        assert widget.check() == "You must set Lewout !"
        widget.cond.Wins_cond = None
        assert widget.check() == "You must set Wins_cond !"
        widget.cond._Wins_wire = None
        assert widget.check() == "You must set Wins_wire !"
        widget.cond.Wwire = None
        assert widget.check() == "You must set Wwire !"
        widget.cond.Nwppc = None
        assert widget.check() == "You must set Nwppc !"
