# -*- coding: utf-8 -*-

from os.path import join, isfile
from os import remove

import sys

import mock  # for unittest of raw_input
from PySide2 import QtWidgets

from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.MachineSRM import MachineSRM
from pyleecan.Classes.MachineLSPM import MachineLSPM
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.Functions.load import load_matlib
from Tests import save_gui_path as save_path
from Tests import TEST_DATA_DIR
from pyleecan.definitions import DATA_DIR

from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType

load_test = list()
load_test.append({"type": "SCIM", "index": 0, "name": "SCIM_001", "p": 1, "count": 12})
load_test.append({"type": "DFIM", "index": 1, "name": "DFIM_001", "p": 2, "count": 13})
load_test.append(
    {"type": "SynRM", "index": 2, "name": "SynRM_001", "p": 2, "count": 11}
)
load_test.append(
    {"type": "SPMSM", "index": 3, "name": "SIPMSM_008", "p": 4, "count": 11}
)
load_test.append(
    {"type": "IPMSM", "index": 4, "name": "machine_IPMSM_A", "p": 5, "count": 11}
)
load_test.append({"type": "WRSM", "index": 5, "name": "WRSM_001", "p": 6, "count": 13})
load_test.append(
    {"type": "SRM", "index": 6, "name": "SRM_test_load", "p": None, "count": 11}
)
load_test.append({"type": "LSPM", "index": 7, "name": "LSPM_001", "p": 2, "count": 13})
from PySide2.QtCore import Qt

ENABLE_ITEM = Qt.ItemIsSelectable | Qt.ItemIsEnabled


import pytest


matlib_path = join(DATA_DIR, "Material")


class TestDMachineSetup(object):
    """Test that the widget DMachineSetup behave like it should"""

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

    @pytest.mark.parametrize("test_dict", load_test)
    def test_load(self, test_dict):
        """Check that you can load a machine"""

        return_value = (
            join(join(TEST_DATA_DIR, "Load_GUI"), test_dict["name"] + ".json"),
            "Json (*.json)",
        )
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.b_load.clicked.emit()
        self.widget.nav_step.setCurrentRow(0)
        # To remember to update when adding a new machine type
        assert self.widget.w_step.c_type.count() == 8
        # Check load MachineType
        assert type(self.widget.w_step) == SMachineType
        assert self.widget.w_step.c_type.currentIndex() == test_dict["index"]
        assert self.widget.w_step.c_type.currentText() == test_dict["type"]
        if test_dict["p"] is not None:
            assert self.widget.w_step.si_p.value() == test_dict["p"]
        else:
            assert self.widget.w_step.si_p.isHidden()
        assert self.widget.w_step.le_name.text() == test_dict["name"]
        # Check that the nav_step is correct
        assert self.widget.nav_step.count() == test_dict["count"]

    def test_set_save_machine_type(self):
        """Check that the Widget allow to change the machine type and save"""
        # Check that all the machine type are available
        assert self.widget.w_step.c_type.count() == 8
        # DFIM
        self.widget.w_step.c_type.setCurrentIndex(1)
        assert self.widget.w_step.c_type.currentText() == "DFIM"
        assert type(self.widget.machine) == MachineDFIM
        save_function(self.widget, "test_dfim_save")
        # SynRM
        self.widget.w_step.c_type.setCurrentIndex(2)
        assert self.widget.w_step.c_type.currentText() == "SynRM"
        assert type(self.widget.machine) == MachineSyRM
        save_function(self.widget, "test_synrm_save")
        # SIPMSM
        self.widget.w_step.c_type.setCurrentIndex(3)
        assert self.widget.w_step.c_type.currentText() == "SPMSM"
        assert type(self.widget.machine) == MachineSIPMSM
        save_function(self.widget, "test_sipmsm_save")
        # IPMSM
        self.widget.w_step.c_type.setCurrentIndex(4)
        assert self.widget.w_step.c_type.currentText() == "IPMSM"
        assert type(self.widget.machine) == MachineIPMSM
        save_function(self.widget, "test_ipmsm_save")
        # WRSM
        self.widget.w_step.c_type.setCurrentIndex(5)
        assert self.widget.w_step.c_type.currentText() == "WRSM"
        assert type(self.widget.machine) == MachineWRSM
        save_function(self.widget, "test_wrsm_save")
        # SRM
        self.widget.w_step.c_type.setCurrentIndex(6)
        assert self.widget.w_step.c_type.currentText() == "SRM"
        assert type(self.widget.machine) == MachineSRM
        save_function(self.widget, "test_srm_save")
        # LSPM
        self.widget.w_step.c_type.setCurrentIndex(7)
        assert self.widget.w_step.c_type.currentText() == "LSPM"
        assert type(self.widget.machine) == MachineLSPM
        save_function(self.widget, "test_lspm_save")
        # SCIM
        self.widget.w_step.c_type.setCurrentIndex(0)
        assert self.widget.w_step.c_type.currentText() == "SCIM"
        assert type(self.widget.machine) == MachineSCIM


def save_function(widget, file_name):
    """Function to save a machine from the GUI"""
    file_path = join(save_path, file_name + ".json")

    # Check that the file didn't already exist
    if isfile(file_path):
        remove(file_path)
    assert not isfile(file_path)

    return_value = (file_path, "Json (*.json)")
    with mock.patch(
        "PySide2.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
    ):
        # To trigger the slot
        widget.b_save.clicked.emit()

    # Check that the file now exist => delete for next test
    assert isfile(file_path)
    remove(file_path)
    # Check that the GUI have been updated
    assert type(widget.w_step) == SMachineType
    assert widget.w_step.le_name.text() == file_name


if __name__ == "__main__":
    a = TestDMachineSetup()
    a.setup_class()
    a.setup_method()
    # for ii, test_dict in enumerate(load_test):
    #     print(ii)
    #     a.test_load(test_dict)
    a.test_load(load_test[0])
    print("Done")
