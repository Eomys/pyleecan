# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.CondType22 import CondType22
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Material import Material
from pyleecan.Classes.SlotW22 import SlotW22
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType21.PCondType21 import PCondType21
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType22.PCondType22 import PCondType22
from pyleecan.GUI.Dialog.DMachineSetup.SBar.SBar import SBar


class TestSBar(object):
    """Test that the widget SBar behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSBar")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""

        test_obj = MachineSCIM()
        test_obj.rotor = LamSquirrelCage(Hscr=0.11, Lscr=0.12)
        test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.rotor.winding.Lewout = 0.13
        test_obj.rotor.ring_mat.name = "test3"
        test_obj.rotor.winding.conductor = CondType21(Hbar=0.014, Wbar=0.015)
        test_obj.rotor.winding.conductor.cond_mat.name = "test1"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        self.widget = SBar(
            machine=test_obj, material_dict=material_dict, is_stator=False
        )
        self.test_obj = test_obj
        self.material_dict = material_dict

    @pytest.mark.SCIM
    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_Hscr.value() == 0.11
        assert self.widget.lf_Lscr.value() == 0.12
        assert self.widget.lf_Lewout.value() == 0.13
        assert self.widget.w_mat_scr.c_mat_type.currentIndex() == 2
        assert self.widget.w_mat_scr.c_mat_type.currentText() == "test3"
        assert type(self.widget.w_bar) is PCondType21
        assert self.widget.c_bar_type.count() == 2
        assert self.widget.c_bar_type.currentIndex() == 0
        assert self.widget.c_bar_type.currentText() == "Rectangular bar"
        assert self.widget.w_bar.lf_Hbar.value() == 0.014
        assert self.widget.w_bar.lf_Wbar.value() == 0.015
        assert self.widget.w_bar.w_mat.c_mat_type.currentIndex() == 0
        assert self.widget.w_bar.w_mat.c_mat_type.currentText() == "test1"
        # Check output txt
        assert self.widget.w_bar.w_out.out_Sbar.text() == "Sbar: 0.00021 [m²]"
        assert self.widget.w_bar.w_out.out_Sslot.text() == "Sslot: 0.002088 [m²]"
        assert self.widget.w_bar.w_out.out_ratio.text() == "Sbar / Sslot: 10.06 [%]"

        self.test_obj.rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding.Lewout = 0.23
        self.test_obj.rotor.ring_mat.name = "test2"
        self.test_obj.rotor.winding.conductor = None
        self.widget = SBar(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )

        assert self.widget.c_bar_type.currentIndex() == 0

    @pytest.mark.SCIM
    def test_init_Cond22(self):
        self.test_obj.rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding.Lewout = 0.23
        self.test_obj.rotor.ring_mat.name = "test2"
        self.test_obj.rotor.winding.conductor = CondType22()
        self.test_obj.rotor.winding.conductor.cond_mat.name = "test3"
        self.widget = SBar(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )

        assert self.widget.lf_Hscr.value() == 0.21
        assert self.widget.lf_Lscr.value() == 0.22
        assert self.widget.lf_Lewout.value() == 0.23
        assert self.widget.w_mat_scr.c_mat_type.currentIndex() == 1
        assert self.widget.w_mat_scr.c_mat_type.currentText() == "test2"
        assert type(self.widget.w_bar) is PCondType22
        assert self.widget.c_bar_type.currentIndex() == 1
        assert self.widget.c_bar_type.currentText() == "Die cast bar"
        assert self.widget.w_bar.w_mat.c_mat_type.currentIndex() == 2
        assert self.widget.w_bar.w_mat.c_mat_type.currentText() == "test3"
        # Check output txt
        assert self.widget.w_bar.w_out.out_Sbar.text() == "Sbar: 0.002088 [m²]"
        assert self.widget.w_bar.w_out.out_Sslot.text() == "Sslot: 0.002088 [m²]"
        assert self.widget.w_bar.w_out.out_ratio.text() == "Sbar / Sslot: 100 [%]"

    @pytest.mark.SCIM
    def test_set_Hscr(self):
        """Check that the Widget allow to update Hscr"""
        # Clear the field before writing the new value
        self.widget.lf_Hscr.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Hscr, str(value))
        self.widget.lf_Hscr.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.Hscr == value

    @pytest.mark.SCIM
    def test_set_Lscr(self):
        """Check that the Widget allow to update Lscr"""
        # Clear the field before writing the new value
        self.widget.lf_Lscr.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Lscr, str(value))
        self.widget.lf_Lscr.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.Lscr == value

    @pytest.mark.SCIM
    def test_set_Hbar(self):
        """Check that the Widget allow to update Hbar"""
        # Clear the field before writing the new value
        self.widget.w_bar.lf_Hbar.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_bar.lf_Hbar, str(value))
        self.widget.w_bar.lf_Hbar.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.conductor.Hbar == value

    @pytest.mark.SCIM
    def test_set_Wbar(self):
        """Check that the Widget allow to update Wbar"""
        # Clear the field before writing the new value
        self.widget.w_bar.lf_Wbar.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_bar.lf_Wbar, str(value))
        self.widget.w_bar.lf_Wbar.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.conductor.Wbar == value

    @pytest.mark.SCIM
    def test_set_Lewout(self):
        """Check that the Widget allow to update Lewout"""
        # Clear the field before writing the new value
        self.widget.lf_Lewout.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Lewout, str(value))
        self.widget.lf_Lewout.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.winding.Lewout == value

    @pytest.mark.SCIM
    def test_set_material(self):
        """Check that the combobox update the material"""
        self.widget.w_mat_scr.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.rotor.ring_mat.name == "test1"
        assert self.test_obj.rotor.ring_mat.elec.rho == 0.31

        self.widget.w_mat_scr.c_mat_type.setCurrentIndex(1)
        assert self.test_obj.rotor.ring_mat.name == "test2"
        assert self.test_obj.rotor.ring_mat.elec.rho == 0.32

        self.widget.w_mat_scr.c_mat_type.setCurrentIndex(2)
        assert self.test_obj.rotor.ring_mat.name == "test3"
        assert self.test_obj.rotor.ring_mat.elec.rho == 0.33

    @pytest.mark.SCIM
    def test_set_cond_type(self):
        """Check that you can change the conductor type"""
        # To remember to update the test
        assert self.widget.c_bar_type.count() == 2
        # Check init position
        assert type(self.widget.w_bar) is PCondType21
        assert type(self.test_obj.rotor.winding.conductor) is CondType21
        self.widget.c_bar_type.setCurrentIndex(1)
        assert type(self.widget.w_bar) is PCondType22
        assert type(self.test_obj.rotor.winding.conductor) is CondType22
        self.widget.c_bar_type.setCurrentIndex(0)
        assert type(self.widget.w_bar) is PCondType21
        assert type(self.test_obj.rotor.winding.conductor) is CondType21

    @pytest.mark.SCIM
    def test_init_PCondType21(self):
        """Check that the init is setting a conductor if None"""
        self.test_obj.rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding.Lewout = 0.23
        self.test_obj.rotor.ring_mat.name = "test2"
        self.test_obj.rotor.winding.conductor = None
        self.widget = PCondType21(
            machine=self.test_obj, material_dict=self.material_dict
        )
        assert type(self.widget.machine.rotor.winding.conductor) is CondType21

    @pytest.mark.SCIM
    def test_init_PCondType22(self):
        """Check that the init is setting a conductor if None"""
        self.test_obj.rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding.Lewout = 0.23
        self.test_obj.rotor.ring_mat.name = "test2"
        self.test_obj.rotor.winding.conductor = None
        self.widget = PCondType22(
            machine=self.test_obj, material_dict=self.material_dict
        )
        assert type(self.widget.machine.rotor.winding.conductor) is CondType22

    @pytest.mark.SCIM
    def test_check(self):
        """Check that the check method return errors"""
        lam = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding.Lewout = None
        lam.ring_mat.name = "test2"
        lam.winding.conductor = None
        assert self.widget.check(lam) == "You must set Lewout !"

        lam = LamSquirrelCage(Hscr=None, Lscr=0.22)
        assert self.widget.check(lam) == "You must set Hscr !"

        lam = LamSquirrelCage(Hscr=0.21, Lscr=None)
        assert self.widget.check(lam) == "You must set Lscr !"

        lam = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        lam.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        lam.winding.Lewout = 0.23
        lam.ring_mat.name = "test2"
        lam.winding.conductor = CondType21(Hbar=None, Wbar=0.015)
        assert self.widget.check(lam) == "You must set Hbar !"

        lam.winding.conductor = CondType21(Hbar=0.014, Wbar=None)
        assert self.widget.check(lam) == "You must set Wbar !"


if __name__ == "__main__":
    a = TestSBar()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    print("Done")
