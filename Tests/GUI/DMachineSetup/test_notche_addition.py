from PySide2 import QtWidgets
from os.path import join, isfile

import sys
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.Functions.load import load_matlib
from Tests import TEST_DATA_DIR

matlib_path = join(TEST_DATA_DIR, "Material")


class TestNotcheAddition(object):
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

    def test_adding_notch(self):
        """Checking that the UI allow the definition and the addition to a machine"""

        # Loading Prius machine

        # Checking notch and recovering dialog

        # Adding first notch (rectangular)

        # Checking plot/preview function

        # Adding second notch (circular)

        # Checking plot/preview function

        # Clicking on OK then selecting rotor lamination tab

        # Enabling notch on rotor

        # Adding first notch polar

        # checking preview/plot function
