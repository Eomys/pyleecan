# -*- coding: utf-8 -*-
"""
@date Created on Thu Apr 27 14:05:46 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
"""

import sys
from os import remove, mkdir
from os.path import abspath, join, isdir
from shutil import copyfile, rmtree
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QDialogButtonBox

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatLamination import MatLamination
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup

from pyleecan.Tests import save_load_path as save_path, DATA_DIR, is_clean_result


class test_Workflow_DMatLib(TestCase):
    """Test that the widget DMatLib behave like it should when called from a Widget
    """

    def setUp(self):
        """Run at the begining of every test to create the workspace
        """
        self.work_path = join(save_path, "Material Workflow")
        # Delete old test if needed
        if isdir(self.work_path):
            rmtree(self.work_path)
        mkdir(self.work_path)
        copyfile(
            join(DATA_DIR, "Material", "Magnet1.json"),
            join(self.work_path, "Magnet1.json"),
        )
        copyfile(
            join(DATA_DIR, "Material", "Copper1.json"),
            join(self.work_path, "Copper1.json"),
        )
        copyfile(
            join(DATA_DIR, "Material", "Insulator1.json"),
            join(self.work_path, "Insulator1.json"),
        )
        copyfile(
            join(DATA_DIR, "Material", "M400-50A.json"),
            join(self.work_path, "M400-50A.json"),
        )
        self.matlib = load_matlib(self.work_path)

    def teardown(self):
        """Delete the workspace at the end of the tests
        """
        if is_clean_result:
            rmtree(self.work_path)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test Workflow MatLib")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init_empty(self):
        """Check that the widget can open with an unknown material
        """
        self.machine = MachineIPMSM()
        self.machine.stator = LamSlotWind()
        self.machine.rotor = LamHole()
        self.machine._set_None()
        self.machine.stator.winding.p = 4
        self.machine.type_machine = 8
        self.machine.rotor.hole = [HoleM50()]
        self.machine.rotor.hole[0].magnet_0.mat_type.name = "Magnet_doesnot_exist"
        self.widget = SMHoleMag(
            machine=self.machine, matlib=self.matlib, is_stator=False
        )

        # Check default material
        self.assertEqual(self.widget.w_mat.c_mat_type.count(), 4)
        self.assertEqual(self.widget.w_mat.c_mat_type.currentText(), "")
        self.assertEqual(self.widget.w_mat.c_mat_type.currentIndex(), -1)
        # Click to open matlib
        self.assertFalse(hasattr(self.widget, "mat_win"))
        self.widget.w_mat.b_matlib.clicked.emit()
        self.assertEqual(type(self.widget.w_mat.mat_win), DMatLib)
        # Check Matlib init
        self.assertEqual(self.widget.w_mat.mat_win.nav_mat.count(), 4)
        self.assertEqual(
            self.widget.w_mat.mat_win.nav_mat.currentItem().text(), "001 - Copper1"
        )

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value
        """
        self.machine = MachineIPMSM()
        self.machine.stator = LamSlotWind()
        self.machine.rotor = LamHole()
        self.machine._set_None()
        self.machine.stator.winding.p = 4
        self.machine.type_machine = 8
        self.widget = SMHoleMag(
            machine=self.machine, matlib=self.matlib, is_stator=False
        )

        # Check default (hole is set to type 50)
        self.assertEqual(self.widget.w_mat.c_mat_type.count(), 4)
        self.assertEqual(self.widget.w_mat.c_mat_type.currentText(), "Magnet1")
        self.assertEqual(self.widget.w_mat.c_mat_type.currentIndex(), 3)
        # Click to open matlib
        self.assertFalse(hasattr(self.widget, "mat_win"))
        self.widget.w_mat.b_matlib.clicked.emit()
        self.assertEqual(type(self.widget.w_mat.mat_win), DMatLib)
        # Check Matlib init
        self.assertEqual(self.widget.w_mat.mat_win.nav_mat.count(), 4)
        self.assertEqual(
            self.widget.w_mat.mat_win.nav_mat.currentItem().text(), "004 - Magnet1"
        )
        # Duplicate Magnet1
        self.assertFalse(hasattr(self.widget.w_mat.mat_win, "mat_win"))
        self.widget.w_mat.mat_win.b_duplicate.clicked.emit()
        self.assertEqual(type(self.widget.w_mat.mat_win.mat_win), DMatSetup)
        # Edit Magnet1 to Magnet_test
        self.widget.w_mat.mat_win.mat_win.le_name.setText("Magnet_test_python")
        self.widget.w_mat.mat_win.mat_win.le_name.editingFinished.emit()
        self.assertEqual(
            self.widget.w_mat.mat_win.mat_win.mat.name, "Magnet_test_python"
        )

        self.widget.w_mat.mat_win.mat_win.lf_rho_elec.setText("1234.56789")
        self.widget.w_mat.mat_win.mat_win.lf_rho_elec.editingFinished.emit()
        self.assertEqual(self.widget.w_mat.mat_win.mat_win.mat.elec.rho, 1234.56789)
        # Close the Edit GUI and check Matlib modification

        # Doesn't Work
        # self.widget.mat_win.mat_win.accept()
        # self.widget.mat_win.mat_win.accepted()
        # button = self.widget.mat_win.mat_win.b_close.button(QDialogButtonBox.Ok)
        # QTest.mouseClick(button, Qt.LeftButton)
        # self.assertEqual(self.widget.mat_win.nav_mat.count(), 93)
        # self.assertEqual(
        #     self.widget.mat_win.nav_mat.currentItem().text(), "094 - Magnet_test_python"
        # )
