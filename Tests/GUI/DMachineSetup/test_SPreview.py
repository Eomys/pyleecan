import sys
from random import uniform
from os.path import join, isfile
import mock

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest


from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SPreview.SPreview import SPreview
from Tests import TEST_DATA_DIR as data_test
from pyleecan.definitions import MAIN_DIR

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
        ("Stator winding type", "double layer distributed"),
        ("Stator winding resistance", "0.02392 Ohm"),
        ("Machine total mass", "328.1 kg"),
    ],
    "Nrow": 9,
}
IPMSM_dict = {
    "file_path": join(machine_path, "IPMSM_A.json").replace("\\", "/"),
    "table": [
        ("Machine Type", "IPMSM"),
        ("Stator slot number", "48"),
        ("Pole pair number", "4"),
        ("Topology", "Inner Rotor"),
        ("Stator phase number", "3"),
        ("Stator winding type", "single layer distributed"),
        ("Stator winding resistance", "0.03595 Ohm"),
        ("Machine total mass", "33.38 kg"),
    ],
    "Nrow": 8,
}
load_preview_test = [SCIM_dict, IPMSM_dict]


@pytest.mark.GUI
class TestSPreview(object):
    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        # MatLib widget
        matlib = MatLib(matlib_path)
        dmatlib = DMatLib(matlib=matlib)
        widget = DMachineSetup(dmatlib=dmatlib, machine_path=machine_path)

        yield {"widget": widget}

        self.app.quit()

    @pytest.mark.parametrize("test_dict", load_preview_test)
    def test_load(self, setup, test_dict):
        """Check that you can load a machine"""
        assert isfile(test_dict["file_path"])

        return_value = (test_dict["file_path"], "Json (*.json)")
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            setup["widget"].b_load.clicked.emit()

        # Check load MachineType
        assert type(setup["widget"].w_step) is SPreview
        # Check the table
        assert (
            setup["widget"].w_step.tab_machine.tab_param.rowCount() == test_dict["Nrow"]
        )
        for ii, content in enumerate(test_dict["table"]):
            assert (
                setup["widget"].w_step.tab_machine.tab_param.item(ii, 0).text()
                == content[0]
            )
            assert (
                setup["widget"].w_step.tab_machine.tab_param.item(ii, 1).text()
                == content[1]
            )
