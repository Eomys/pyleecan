# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.CondType22 import CondType22
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Material import Material
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType21.PCondType21 import PCondType21
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType22.PCondType22 import PCondType22
from pyleecan.GUI.Dialog.DMachineSetup.SBar.SBar import SBar


import pytest


@pytest.mark.GUI
class TestSBar(object):
    """Test that the widget SBar behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM()
        test_obj.rotor = LamSquirrelCage(Hscr=0.11, Lscr=0.12)
        test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.rotor.winding.Lewout = 0.13
        test_obj.rotor.ring_mat.name = "test3"
        test_obj.rotor.winding.conductor = CondType21(Hbar=0.014, Wbar=0.015)
        test_obj.rotor.winding.conductor.cond_mat.name = "test1"

        matlib = MatLib()
        matlib.dict_mat["RefMatLib"] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        matlib.dict_mat["RefMatLib"][0].elec.rho = 0.31
        matlib.dict_mat["RefMatLib"][1].elec.rho = 0.32
        matlib.dict_mat["RefMatLib"][2].elec.rho = 0.33

        widget = SBar(machine=test_obj, matlib=matlib, is_stator=False)

        yield {"widget": widget, "test_obj": test_obj, "matlib": matlib}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_Hscr.value() == 0.11
        assert setup["widget"].lf_Lscr.value() == 0.12
        assert setup["widget"].lf_Lewout.value() == 0.13
        assert setup["widget"].w_mat.c_mat_type.currentIndex() == 2
        assert setup["widget"].w_mat.c_mat_type.currentText() == "test3"
        assert type(setup["widget"].w_bar) is PCondType21
        assert setup["widget"].c_bar_type.count() == 2
        assert setup["widget"].c_bar_type.currentIndex() == 0
        assert setup["widget"].c_bar_type.currentText() == "Rectangular bar"
        assert setup["widget"].w_bar.lf_Hbar.value() == 0.014
        assert setup["widget"].w_bar.lf_Wbar.value() == 0.015
        assert setup["widget"].w_bar.w_mat.c_mat_type.currentIndex() == 0
        assert setup["widget"].w_bar.w_mat.c_mat_type.currentText() == "test1"
        # Check output txt
        assert setup["widget"].w_bar.w_out.out_Sbar.text() == "Sbar: 0.00021 m²"
        assert setup["widget"].w_bar.w_out.out_Sslot.text() == "Sslot: 0.002088 m²"
        assert setup["widget"].w_bar.w_out.out_ratio.text() == "Sbar / Sslot: 10.06 %"

        setup["test_obj"].rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        setup["test_obj"].rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding.Lewout = 0.23
        setup["test_obj"].rotor.ring_mat.name = "test2"
        setup["test_obj"].rotor.winding.conductor = None
        setup["widget"] = SBar(machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False)

        assert setup["widget"].c_bar_type.currentIndex() == 0

    def test_init_Cond22(self, setup):
        setup["test_obj"].rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        setup["test_obj"].rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding.Lewout = 0.23
        setup["test_obj"].rotor.ring_mat.name = "test2"
        setup["test_obj"].rotor.winding.conductor = CondType22()
        setup["test_obj"].rotor.winding.conductor.cond_mat.name = "test3"
        setup["widget"] = SBar(machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False)

        assert setup["widget"].lf_Hscr.value() == 0.21
        assert setup["widget"].lf_Lscr.value() == 0.22
        assert setup["widget"].lf_Lewout.value() == 0.23
        assert setup["widget"].w_mat.c_mat_type.currentIndex() == 1
        assert setup["widget"].w_mat.c_mat_type.currentText() == "test2"
        assert type(setup["widget"].w_bar) is PCondType22
        assert setup["widget"].c_bar_type.currentIndex() == 1
        assert setup["widget"].c_bar_type.currentText() == "Die cast bar"
        assert setup["widget"].w_bar.w_mat.c_mat_type.currentIndex() == 2
        assert setup["widget"].w_bar.w_mat.c_mat_type.currentText() == "test3"
        # Check output txt
        assert setup["widget"].w_bar.w_out.out_Sbar.text() == "Sbar: 0.002088 m²"
        assert setup["widget"].w_bar.w_out.out_Sslot.text() == "Sslot: 0.002088 m²"
        assert setup["widget"].w_bar.w_out.out_ratio.text() == "Sbar / Sslot: 100 %"

    def test_set_Hscr(self, setup):
        """Check that the Widget allow to update Hscr"""
        # Clear the field before writing the new value
        setup["widget"].lf_Hscr.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Hscr, str(value))
        setup["widget"].lf_Hscr.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.Hscr == value

    def test_set_Lscr(self, setup):
        """Check that the Widget allow to update Lscr"""
        # Clear the field before writing the new value
        setup["widget"].lf_Lscr.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Lscr, str(value))
        setup["widget"].lf_Lscr.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.Lscr == value

    def test_set_Hbar(self, setup):
        """Check that the Widget allow to update Hbar"""
        # Clear the field before writing the new value
        setup["widget"].w_bar.lf_Hbar.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].w_bar.lf_Hbar, str(value))
        setup["widget"].w_bar.lf_Hbar.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.conductor.Hbar == value

    def test_set_Wbar(self, setup):
        """Check that the Widget allow to update Wbar"""
        # Clear the field before writing the new value
        setup["widget"].w_bar.lf_Wbar.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].w_bar.lf_Wbar, str(value))
        setup["widget"].w_bar.lf_Wbar.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.conductor.Wbar == value

    def test_set_Lewout(self, setup):
        """Check that the Widget allow to update Lewout"""
        # Clear the field before writing the new value
        setup["widget"].lf_Lewout.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Lewout, str(value))
        setup["widget"].lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.Lewout == value

    def test_set_material(self, setup):
        """Check that the combobox update the material"""
        setup["widget"].w_mat.c_mat_type.setCurrentIndex(0)
        assert setup["test_obj"].rotor.ring_mat.name == "test1"
        assert setup["test_obj"].rotor.ring_mat.elec.rho == 0.31

        setup["widget"].w_mat.c_mat_type.setCurrentIndex(1)
        assert setup["test_obj"].rotor.ring_mat.name == "test2"
        assert setup["test_obj"].rotor.ring_mat.elec.rho == 0.32

        setup["widget"].w_mat.c_mat_type.setCurrentIndex(2)
        assert setup["test_obj"].rotor.ring_mat.name == "test3"
        assert setup["test_obj"].rotor.ring_mat.elec.rho == 0.33

    def test_set_cond_type(self, setup):
        """Check that you can change the conductor type"""
        # To remember to update the test
        assert setup["widget"].c_bar_type.count() == 2
        # Check init position
        assert type(setup["widget"].w_bar) is PCondType21
        assert type(setup["test_obj"].rotor.winding.conductor) is CondType21
        setup["widget"].c_bar_type.setCurrentIndex(1)
        assert type(setup["widget"].w_bar) is PCondType22
        assert type(setup["test_obj"].rotor.winding.conductor) is CondType22
        setup["widget"].c_bar_type.setCurrentIndex(0)
        assert type(setup["widget"].w_bar) is PCondType21
        assert type(setup["test_obj"].rotor.winding.conductor) is CondType21

    def test_init_PCondType21(self, setup):
        """Check that the init is setting a conductor if None"""
        setup["test_obj"].rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        setup["test_obj"].rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding.Lewout = 0.23
        setup["test_obj"].rotor.ring_mat.name = "test2"
        setup["test_obj"].rotor.winding.conductor = None
        setup["widget"] = PCondType21(machine=setup["test_obj"], matlib=setup["matlib"])
        assert type(setup["widget"].machine.rotor.winding.conductor) is CondType21

    def test_init_PCondType22(self, setup):
        """Check that the init is setting a conductor if None"""
        setup["test_obj"].rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        setup["test_obj"].rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding.Lewout = 0.23
        setup["test_obj"].rotor.ring_mat.name = "test2"
        setup["test_obj"].rotor.winding.conductor = None
        setup["widget"] = PCondType22(machine=setup["test_obj"], matlib=setup["matlib"])
        assert type(setup["widget"].machine.rotor.winding.conductor) is CondType22

    def test_check(self, setup):
        """Check that the check method return errors"""
        lam = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding.Lewout = None
        lam.ring_mat.name = "test2"
        lam.winding.conductor = None
        assert setup["widget"].check(lam) == "You must set Lewout !"

        lam = LamSquirrelCage(Hscr=None, Lscr=0.22)
        assert setup["widget"].check(lam) == "You must set Hscr !"

        lam = LamSquirrelCage(Hscr=0.21, Lscr=None)
        assert setup["widget"].check(lam) == "You must set Lscr !"

        lam = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding.Lewout = 0.23
        lam.ring_mat.name = "test2"
        lam.winding.conductor = CondType21(Hbar=None, Wbar=0.015)
        assert setup["widget"].check(lam) == "You must set Hbar !"

        lam.winding.conductor = CondType21(Hbar=0.014, Wbar=None)
        assert setup["widget"].check(lam) == "You must set Wbar !"
