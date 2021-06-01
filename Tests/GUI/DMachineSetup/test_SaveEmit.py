# -*- coding: utf-8 -*-

from os.path import join, isfile
import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt, QTimer

from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup

from Tests import TEST_DATA_DIR

import pytest

matlib_path = join(TEST_DATA_DIR, "Material")


class TestSaveEmit(object):
    """Test that the save_needed behave like it should"""

    @pytest.fixture
    def setup_method(self, qtbot):
        """Run at the begining of every test to setup the gui"""
        material_dict = load_matlib(matlib_path=matlib_path)
        self.widget = DMachineSetup(
            material_dict=material_dict, machine_path=join(TEST_DATA_DIR, "Machine")
        )

        qtbot.addWidget(self.widget)
        yield qtbot

        assert self.widget.qmessagebox_question is not None

    def test_save_emit(self, setup_method):
        """Check that the Widget allow send the save_needed signal"""
        self.widget.save_needed()
        assert self.widget.is_save_needed == True
