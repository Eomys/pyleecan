# -*- coding: utf-8 -*-

import sys
from os import remove, mkdir
from os.path import abspath, join, isdir
from shutil import copyfile, rmtree

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QDialogButtonBox

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Material import Material
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup

from Tests import save_load_path as save_path, TEST_DATA_DIR, is_clean_result


import pytest


class Test_Workflow_DMatLib(object):
    """Test that the widget DMatLib behave like it should when called from a Widget"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        work_path = join(save_path, "Material Workflow")
        # Delete old test if needed
        if isdir(work_path):
            rmtree(work_path)
        mkdir(work_path)
        copyfile(
            join(TEST_DATA_DIR, "Material", "Magnet1.json"),
            join(work_path, "Magnet1.json"),
        )
        copyfile(
            join(TEST_DATA_DIR, "Material", "Copper1.json"),
            join(work_path, "Copper1.json"),
        )
        copyfile(
            join(TEST_DATA_DIR, "Material", "Insulator1.json"),
            join(work_path, "Insulator1.json"),
        )
        copyfile(
            join(TEST_DATA_DIR, "Material", "M400-50A.json"),
            join(work_path, "M400-50A.json"),
        )
        matlib = MatLib(work_path)

        yield {"work_path": work_path, "matlib": matlib}

        self.app.quit()

        topLevelWidgets = QtWidgets.QApplication.topLevelWidgets()
        for widget in topLevelWidgets:
            widget.close()

        if is_clean_result:
            rmtree(work_path)

    def test_init_empty(self, setup):
        """Check that the widget can open with an unknown material"""
        self.machine = MachineIPMSM()
        self.machine.stator = LamSlotWind()
        self.machine.rotor = LamHole()
        self.machine._set_None()
        self.machine.stator.winding.p = 4
        self.machine.type_machine = 8
        self.machine.rotor.hole = [HoleM50()]
        self.machine.rotor.hole[0].magnet_0.mat_type.name = "Magnet_doesnot_exist"
        self.widget = SMHoleMag(
            machine=self.machine, matlib=setup["matlib"], is_stator=False
        )
        # Check default material
        assert self.widget.tab_hole.widget(0).w_hole.w_mat_1.c_mat_type.count() == 4
        assert (
            self.widget.tab_hole.widget(0).w_hole.w_mat_1.c_mat_type.currentText() == ""
        )
        assert (
            self.widget.tab_hole.widget(0).w_hole.w_mat_1.c_mat_type.currentIndex()
            == -1
        )
        # Click to open matlib
        assert self.widget.tab_hole.widget(0).w_hole.w_mat_1.current_dialog is None
        self.widget.tab_hole.widget(0).w_hole.w_mat_1.b_matlib.clicked.emit()
        assert (
            type(self.widget.tab_hole.widget(0).w_hole.w_mat_1.current_dialog)
            == DMatLib
        )
        # Check Matlib init
        assert (
            self.widget.tab_hole.widget(0).w_hole.w_mat_1.current_dialog.nav_mat.count()
            == 4
        )
        assert (
            self.widget.tab_hole.widget(0)
            .w_hole.w_mat_1.current_dialog.nav_mat.currentItem()
            .text()
            == "001 - Copper1"
        )

    @pytest.mark.skip
    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""
        self.machine = MachineIPMSM()
        self.machine.stator = LamSlotWind()
        self.machine.rotor = LamHole()
        self.machine._set_None()
        self.machine.rotor.hole = list()  # No hole
        self.machine.stator.winding.p = 4
        self.machine.type_machine = 8
        self.widget = SMHoleMag(
            machine=self.machine, matlib=setup["matlib"], is_stator=False
        )

        wid = self.widget.tab_hole.widget(0).w_hole.w_mat_1
        # Check default (hole is set to type 50)
        assert wid.c_mat_type.count() == 4
        assert wid.c_mat_type.currentText() == "Magnet1"
        assert wid.c_mat_type.currentIndex() == 3

        # Click to open matlib
        assert wid.current_dialog is None
        wid.b_matlib.clicked.emit()
        assert type(wid.current_dialog) == DMatLib

        # Check Matlib ini
        assert wid.current_dialog.nav_mat.count() == 4
        assert wid.current_dialog.nav_mat.currentItem().text() == "004 - Magnet1"
        assert wid.current_dialog.current_dialog is None

        # Duplicate Magnet1 to Magnet_test
        assert wid.current_dialog.current_dialog is None
        wid.current_dialog.b_duplicate.clicked.emit()
        assert type(wid.current_dialog.current_dialog) == DMatSetup
        wid.current_dialog.current_dialog.le_name.setText("Magnet_test_python")
        wid.current_dialog.current_dialog.le_name.editingFinished.emit()
        assert wid.current_dialog.current_dialog.mat.name == "Magnet_test_python"
        wid.current_dialog.current_dialog.lf_rho_elec.setText("1234.56789")
        wid.current_dialog.current_dialog.lf_rho_elec.editingFinished.emit()
        assert wid.current_dialog.current_dialog.mat.elec.rho == 1234.56789

        # Check creation
        wid.current_dialog.current_dialog.done(1)
        assert wid.current_dialog.nav_mat.count() == 5
        # self.widget.current_dialog.current_dialog.accepted()
        # button = self.widget.current_dialog.current_dialog.b_close.button(QDialogButtonBox.Ok)
        # QTest.mouseClick(button, Qt.LeftButton)
        # self.assertEqual(self.widget.current_dialog.nav_mat.count(), 93)
        # self.assertEqual(
        #     self.widget.current_dialog.nav_mat.currentItem().text(), "094 - Magnet_test_python"
        # )
