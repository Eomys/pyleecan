# -*- coding: utf-8 -*-

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from ....Classes.CondType21 import CondType21
from ....Classes.CondType22 import CondType22
from ....Classes.LamSquirrelCage import LamSquirrelCage
from ....Classes.MachineSCIM import MachineSCIM
from ....Classes.Material import Material
from ....Classes.SlotW22 import SlotW22
from ....GUI.Dialog.DMachineSetup.SBar.PCondType21.PCondType21 import PCondType21
from ....GUI.Dialog.DMachineSetup.SBar.PCondType22.PCondType22 import PCondType22
from ....GUI.Dialog.DMachineSetup.SBar.SBar import SBar


class test_SBar(TestCase):
    """Test that the widget SBar behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = MachineSCIM()
        self.test_obj.rotor = LamSquirrelCage(Hscr=0.11, Lscr=0.12)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding.Lewout = 0.13
        self.test_obj.rotor.ring_mat.name = "test3"
        self.test_obj.rotor.winding.conductor = CondType21(Hbar=0.014, Wbar=0.015)
        self.test_obj.rotor.winding.conductor.cond_mat.name = "test1"

        self.matlib = list()
        self.matlib.append(Material(name="test1"))
        self.matlib[-1].elec.rho = 0.31
        self.matlib.append(Material(name="test2"))
        self.matlib[-1].elec.rho = 0.32
        self.matlib.append(Material(name="test3"))
        self.matlib[-1].elec.rho = 0.33

        self.widget = SBar(machine=self.test_obj, matlib=self.matlib, is_stator=False)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test SBar")
        # gui_option.unit.unit_m =0 #m
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value
        """

        self.assertEqual(self.widget.lf_Hscr.value(), 0.11)
        self.assertEqual(self.widget.lf_Lscr.value(), 0.12)
        self.assertEqual(self.widget.lf_Lewout.value(), 0.13)
        self.assertEqual(self.widget.w_mat.c_mat_type.currentIndex(), 2)
        self.assertEqual(self.widget.w_mat.c_mat_type.currentText(), "test3")
        self.assertIs(type(self.widget.w_bar), PCondType21)
        self.assertEqual(self.widget.c_bar_type.count(), 2)
        self.assertEqual(self.widget.c_bar_type.currentIndex(), 0)
        self.assertEqual(self.widget.c_bar_type.currentText(), "Rectangular bar")
        self.assertEqual(self.widget.w_bar.lf_Hbar.value(), 0.014)
        self.assertEqual(self.widget.w_bar.lf_Wbar.value(), 0.015)
        self.assertEqual(self.widget.w_bar.w_mat.c_mat_type.currentIndex(), 0)
        self.assertEqual(self.widget.w_bar.w_mat.c_mat_type.currentText(), "test1")
        # Check output txt
        self.assertEqual(self.widget.w_bar.w_out.out_Sbar.text(), "Sbar: 0.00021 m²")
        self.assertEqual(self.widget.w_bar.w_out.out_Sslot.text(), "Sslot: 0.002088 m²")
        self.assertEqual(
            self.widget.w_bar.w_out.out_ratio.text(), "Sbar / Sslot: 10.06 %"
        )

    def test_init_Cond22(self):
        self.test_obj.rotor = LamSquirrelCage(Hscr=0.21, Lscr=0.22)
        self.test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.rotor.winding.Lewout = 0.23
        self.test_obj.rotor.ring_mat.name = "test2"
        self.test_obj.rotor.winding.conductor = CondType22()
        self.test_obj.rotor.winding.conductor.cond_mat.name = "test3"
        self.widget = SBar(machine=self.test_obj, matlib=self.matlib, is_stator=False)

        self.assertEqual(self.widget.lf_Hscr.value(), 0.21)
        self.assertEqual(self.widget.lf_Lscr.value(), 0.22)
        self.assertEqual(self.widget.lf_Lewout.value(), 0.23)
        self.assertEqual(self.widget.w_mat.c_mat_type.currentIndex(), 1)
        self.assertEqual(self.widget.w_mat.c_mat_type.currentText(), "test2")
        self.assertIs(type(self.widget.w_bar), PCondType22)
        self.assertEqual(self.widget.c_bar_type.currentIndex(), 1)
        self.assertEqual(self.widget.c_bar_type.currentText(), "Die cast bar")
        self.assertEqual(self.widget.w_bar.w_mat.c_mat_type.currentIndex(), 2)
        self.assertEqual(self.widget.w_bar.w_mat.c_mat_type.currentText(), "test3")
        # Check output txt
        self.assertEqual(self.widget.w_bar.w_out.out_Sbar.text(), "Sbar: 0.002088 m²")
        self.assertEqual(self.widget.w_bar.w_out.out_Sslot.text(), "Sslot: 0.002088 m²")
        self.assertEqual(
            self.widget.w_bar.w_out.out_ratio.text(), "Sbar / Sslot: 100 %"
        )

    def test_set_Hscr(self):
        """Check that the Widget allow to update Hscr"""
        # Clear the field before writing the new value
        self.widget.lf_Hscr.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Hscr, str(value))
        self.widget.lf_Hscr.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.Hscr, value)

    def test_set_Lscr(self):
        """Check that the Widget allow to update Lscr"""
        # Clear the field before writing the new value
        self.widget.lf_Lscr.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Lscr, str(value))
        self.widget.lf_Lscr.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.rotor.Lscr, value)

    def test_set_Hbar(self):
        """Check that the Widget allow to update Hbar"""
        # Clear the field before writing the new value
        self.widget.w_bar.lf_Hbar.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_bar.lf_Hbar, str(value))
        self.widget.w_bar.lf_Hbar.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.winding.conductor.Hbar, value)

    def test_set_Wbar(self):
        """Check that the Widget allow to update Wbar"""
        # Clear the field before writing the new value
        self.widget.w_bar.lf_Wbar.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_bar.lf_Wbar, str(value))
        self.widget.w_bar.lf_Wbar.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.winding.conductor.Wbar, value)

    def test_set_Lewout(self):
        """Check that the Widget allow to update Lewout"""
        # Clear the field before writing the new value
        self.widget.lf_Lewout.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Lewout, str(value))
        self.widget.lf_Lewout.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.test_obj.rotor.winding.Lewout, value)

    def test_set_material(self):
        """Check that the combobox update the material"""
        self.widget.w_mat.c_mat_type.setCurrentIndex(0)
        self.assertEqual(self.test_obj.rotor.ring_mat.name, "test1")
        self.assertEqual(self.test_obj.rotor.ring_mat.elec.rho, 0.31)

        self.widget.w_mat.c_mat_type.setCurrentIndex(1)
        self.assertEqual(self.test_obj.rotor.ring_mat.name, "test2")
        self.assertEqual(self.test_obj.rotor.ring_mat.elec.rho, 0.32)

        self.widget.w_mat.c_mat_type.setCurrentIndex(2)
        self.assertEqual(self.test_obj.rotor.ring_mat.name, "test3")
        self.assertEqual(self.test_obj.rotor.ring_mat.elec.rho, 0.33)

    def test_set_cond_type(self):
        """Check that you can change the conductor type
        """
        # To remember to update the test
        self.assertEqual(self.widget.c_bar_type.count(), 2)
        # Check init position
        self.assertIs(type(self.widget.w_bar), PCondType21)
        self.assertIs(type(self.test_obj.rotor.winding.conductor), CondType21)

        self.widget.c_bar_type.setCurrentIndex(1)
        self.assertIs(type(self.widget.w_bar), PCondType22)
        self.assertIs(type(self.test_obj.rotor.winding.conductor), CondType22)

        self.widget.c_bar_type.setCurrentIndex(0)
        self.assertIs(type(self.widget.w_bar), PCondType21)
        self.assertIs(type(self.test_obj.rotor.winding.conductor), CondType21)
