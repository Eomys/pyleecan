# -*- coding: utf-8 -*-

import sys
from numpy import array
import mock
from qtpy import QtWidgets
from qtpy.QtTest import QTest
from os import remove
from os.path import isfile, join
from pyleecan.GUI.Tools.WTableData.DTableData import DTableData
from Tests import save_gui_path as save_path

import pytest


class TestDTableData(object):
    """Test that the widget DTableData behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        data = array([[1, 2, 3], [4, 5, 6]])
        widget = DTableData(data=data)
        yield {"widget": widget}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget is correctly initialized"""

        assert setup["widget"].in_row.text() == "N_row"
        assert setup["widget"].in_col.text() == "N_column"
        assert setup["widget"].si_row.value() == 2
        assert setup["widget"].si_col.value() == 3
        assert setup["widget"].w_tab.rowCount() == 2
        assert setup["widget"].w_tab.columnCount() == 3
        assert setup["widget"].w_tab.cellWidget(0, 0).value() == 1
        assert setup["widget"].w_tab.cellWidget(0, 1).value() == 2
        assert setup["widget"].w_tab.cellWidget(0, 2).value() == 3
        assert setup["widget"].w_tab.cellWidget(1, 0).value() == 4
        assert setup["widget"].w_tab.cellWidget(1, 1).value() == 5
        assert setup["widget"].w_tab.cellWidget(1, 2).value() == 6

    def test_export_import(self, setup):
        """Check that you can export / import data"""

        file_path = join(save_path, "test_DTableData_export.csv")
        if isfile(file_path):
            remove(file_path)

        # Check export
        assert not isfile(file_path)
        return_value = (file_path, "CSV (*.csv)")
        with mock.patch(
            "qtpy.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
        ):
            # To trigger the slot
            setup["widget"].b_export.clicked.emit()

        assert isfile(file_path)

        # Remove one line
        setup["widget"].si_row.setValue(1)
        assert setup["widget"].w_tab.rowCount() == 1

        # Check import
        with mock.patch(
            "qtpy.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            setup["widget"].b_import.clicked.emit()
        assert setup["widget"].si_row.value() == 2
        assert setup["widget"].si_col.value() == 3
        assert setup["widget"].w_tab.rowCount() == 2
        assert setup["widget"].w_tab.columnCount() == 3
        assert setup["widget"].w_tab.cellWidget(0, 0).value() == 1
        assert setup["widget"].w_tab.cellWidget(0, 1).value() == 2
        assert setup["widget"].w_tab.cellWidget(0, 2).value() == 3
        assert setup["widget"].w_tab.cellWidget(1, 0).value() == 4
        assert setup["widget"].w_tab.cellWidget(1, 1).value() == 5
        assert setup["widget"].w_tab.cellWidget(1, 2).value() == 6

        # Delete Test file
        remove(file_path)
