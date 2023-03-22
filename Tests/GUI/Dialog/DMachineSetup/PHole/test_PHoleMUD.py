# -*- coding: utf-8 -*-

import sys
import mock
from os.path import join

from PySide2 import QtWidgets

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleUD import HoleUD
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleMUD.PHoleMUD import PHoleMUD
from Tests.GUI import gui_option  # Set unit to m
from Tests import TEST_DATA_DIR
from pyleecan.Classes.Material import Material
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.definitions import DATA_DIR


import pytest

matlib_path = join(DATA_DIR, "Material")


class TestPHoleMUD(object):
    """Test that the widget PHoleM58 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestDMachineSetup")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        # MatLib widget
        material_dict = load_matlib(matlib_path=matlib_path)
        self.widget = DMachineSetup(
            material_dict=material_dict, machine_path=join(TEST_DATA_DIR, "Machine")
        )

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_load_dxf_11_magnets(self):
        """Check that the group with material for the magnet is correctly sorted with 10+ magnets"""

        # Loading the machine (fake prius with 10+ magnets)
        file_path = join(
            TEST_DATA_DIR, "Load_GUI", "Toyota_Prius_10+_magnet_dxf.json"
        ).replace("\\", "/")
        return_value = (file_path, "Json (*.json)")
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the import of dxf json
            self.widget.b_load.clicked.emit()

        # Setting the definition tab to Hole definition
        self.widget.nav_step.setCurrentRow(6)
        wid_hole = self.widget.w_step.tab_hole.widget(0).w_hole
        assert isinstance(wid_hole, PHoleMUD)

        # Checking each magnet name to make sure that they are sorted by number
        assert wid_hole.g_mat_layout.count() == 13

        for idx_mag_wid in range(1, wid_hole.g_mat_layout.count()):
            idx_label = (
                wid_hole.g_mat_layout.itemAt(idx_mag_wid)
                .wid.in_mat_type.text()
                .split(" ")[-1]
            )
            assert int(idx_label) == idx_mag_wid - 1
