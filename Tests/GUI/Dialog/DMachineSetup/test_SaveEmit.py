# -*- coding: utf-8 -*-

from os.path import join
import sys
import logging
import mock

from PySide2.QtGui import *
from PySide2 import QtWidgets

from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.definitions import DATA_DIR

matlib_path = join(DATA_DIR, "Material")

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)

# python -m pytest .\Tests\GUI\Dialog\DMachineSetup\test_SaveEmit.py


class TestSaveEmit(object):
    """Test that the save_needed behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSaveEmit")
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
        material_dict = load_matlib(matlib_path=matlib_path)
        self.widget = DMachineSetup(
            material_dict=material_dict,
            machine_path=join(DATA_DIR, "Machine"),
        )

    def test_save_emit(self):
        """Check that the Widget allow send the save_needed signal"""
        self.widget.save_needed()
        assert self.widget.is_save_needed == True

        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.question",
            return_value=QtWidgets.QMessageBox.No,
        ):
            self.widget.close()
        assert self.widget.qmessagebox_question is not None


if __name__ == "__main__":
    a = TestSaveEmit()
    a.setup_class()
    a.setup_method()
    a.test_save_emit()
    a.teardown_class()
    print("Done")
