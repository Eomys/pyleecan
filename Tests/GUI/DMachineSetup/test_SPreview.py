import sys
from random import uniform
from os import makedirs
from os.path import join, isfile, isdir
import mock

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest


from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.SPreview.SPreview import SPreview
from Tests import TEST_DATA_DIR as data_test, save_gui_path
from pyleecan.definitions import MAIN_DIR
from pyleecan.Functions.load import load_matlib

matlib_path = join(data_test, "Material")
machine_path = join(MAIN_DIR, "Data", "Machine")

SCIM_dict = {
    "file_path": join(machine_path, "SCIM_001.json").replace("\\", "/"),
    "table": [
        ("Machine Type", "SCIM"),
        ("Stator slot number", "36"),
        ("Rotor slot number", "28"),
        ("Pole pair number", "3"),
        ("Topology", "Inner Rotor"),
        ("Stator phase number", "3"),
        ("Stator winding resistance", "0.02392 Ohm"),
        ("Machine total mass", "328.1 kg"),
    ],
    "Nrow": 8,
}
IPMSM_dict = {
    "file_path": join(machine_path, "Toyota_Prius.json").replace("\\", "/"),
    "table": [
        ("Machine Type", "IPMSM"),
        ("Stator slot number", "48"),
        ("Pole pair number", "4"),
        ("Topology", "Inner Rotor"),
        ("Stator phase number", "3"),
        ("Stator winding resistance", "0.03595 Ohm"),
        ("Machine total mass", "33.38 kg"),
    ],
    "Nrow": 7,
}
load_preview_test = [SCIM_dict, IPMSM_dict]


class TestSPreview(object):

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSPreview")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        # MatLib widget
        material_dict = load_matlib(matlib_path=matlib_path)
        self.widget = DMachineSetup(material_dict=material_dict, machine_path=machine_path)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    @pytest.mark.parametrize("test_dict", load_preview_test)
    def test_load(self, test_dict):
        """Check that you can load a machine"""
        assert isfile(test_dict["file_path"])

        return_value = (test_dict["file_path"], "Json (*.json)")
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.b_load.clicked.emit()

        # Check load MachineType
        assert type(self.widget.w_step) is SPreview
        # Check the table
        assert (
            self.widget.w_step.tab_machine.tab_param.rowCount() == test_dict["Nrow"]
        )
        for ii, content in enumerate(test_dict["table"]):
            assert (
                self.widget.w_step.tab_machine.tab_param.item(ii, 0).text()
                == content[0]
            )
            assert (
                self.widget.w_step.tab_machine.tab_param.item(ii, 1).text()
                == content[1]
            )
        # Check Draw FEMM
        FEMM_dir = join(save_gui_path, "Draw_FEMM")
        if not isdir(FEMM_dir):
            makedirs(FEMM_dir)
        femm_path = join(FEMM_dir, self.widget.machine.name+".fem")
        assert not isfile(femm_path)

        return_value = (
            femm_path,
            "FEMM (*.fem)",
        )
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
        ):
            self.widget.w_step.tab_machine.b_FEMM.clicked.emit()
        assert isfile(femm_path)

if __name__ == "__main__":
    a = TestSPreview()
    a.setup_class()
    a.setup_method()
    for ii, test_dict in enumerate(load_preview_test):
        print(ii)
        a.test_load(test_dict)
    # a.test_load(load_preview_test[0])
    print("Done")