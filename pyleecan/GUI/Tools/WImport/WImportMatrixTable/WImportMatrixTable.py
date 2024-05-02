from os.path import join

import matplotlib.pyplot as plt
from pandas import DataFrame
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QFileDialog, QMessageBox, QWidget

from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from .....Classes.ImportMatrixVal import ImportMatrixVal
from .....Classes.ImportMatrixXls import ImportMatrixXls
from .....definitions import USER_DIR
from .....GUI.Tools.WImport.WImportMatrixTable.Ui_WImportMatrixTable import (
    Ui_WImportMatrixTable,
)
from .....GUI.Tools.WTableData.DTableData import DTableData


class WImportMatrixTable(Ui_WImportMatrixTable, QWidget):
    """Widget to define an ImportMatrixVal"""

    import_name = "User-defined Table"
    import_type = ImportMatrixVal
    saveNeeded = Signal()
    dataTypeChanged = Signal()

    def __init__(self, parent=None, data=None, plot_title="", expected_shape=None):
        """Initialization of the widget

        Parameters
        ----------
        data : ImportMatrixVal
            Data import to define
        plot_title : str
            Name of to use for the plot and table display
        expected_shape : list
            List to enforce a shape, [None, 2] enforce 2D matrix with 2 columns
        """
        # Initialzation of the widget
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)

        # Check data type
        if data is None or not isinstance(data, ImportMatrixVal):
            self.data = ImportMatrixVal()
        else:
            self.data = data
        self.plot_title = plot_title
        self.expected_shape = expected_shape
        self.tab_window = None  # For the table popup

        self.update()

        # Connect the slot/signal
        self.b_plot.clicked.connect(self.s_plot)
        self.b_tab.clicked.connect(self.s_table)
        self.b_convert.clicked.connect(self.s_convert)

    def update(self):
        """Fill the widget with the current value of the data"""
        data = self.data.get_data()
        shape_str = str(data.shape) if data is not None else "(-,-)"
        self.in_matrix.setText("Matrix size: " + shape_str)

    def s_table(self):
        """display the data in a table"""
        try:
            data = self.data.get_data()
        except Exception as e:
            QMessageBox.critical(self, self.tr("Error"), str(e))
            return
        # Enfoce shape
        shape_min = [1, 1]
        shape_max = [None, None]
        if self.expected_shape is not None and self.expected_shape[0] is not None:
            shape_min[0] = self.expected_shape[0]
            shape_max[0] = self.expected_shape[0]
        if self.expected_shape is not None and self.expected_shape[1] is not None:
            shape_min[1] = self.expected_shape[1]
            shape_max[1] = self.expected_shape[1]
        self.tab_window = DTableData(
            data=data, title=self.plot_title, shape_min=shape_min, shape_max=shape_max
        )
        self.tab_window.accepted.connect(self.update_data)
        self.tab_window.show()

    def update_data(self):
        self.data.value = self.tab_window.data
        self.update()

    def s_plot(self):
        """Plot the matrix (if 2D)"""
        try:
            data = self.data.get_data()
        except Exception as e:
            QMessageBox.critical(self, self.tr("Error"), str(e))
            return

        if len(data.shape) == 2 and data.shape[0] == 2:
            # Data in line
            fig, axes = plt.subplots()
            axes.plot(data[0, :], data[1, :])
            fig.show()
        elif len(data.shape) == 2 and data.shape[1] == 2:
            fig, axes = plt.subplots()
            axes.plot(data[:, 0], data[:, 1])
            fig.show()
        else:
            QMessageBox.critical(
                self,
                self.tr("Error"),
                "Unable to plot matrix of shape " + str(data.shape),
            )
            return
        if self.plot_title is not None:
            fig.canvas.manager.set_window_title(self.plot_title)
        set_plot_gui_icon()

    def s_convert(self):
        """Convert the ImportMatrixVal to a ImportMatrixXls by saving the matrix in Excel"""
        def_path = join(USER_DIR, self.plot_title + ".xls")
        save_file_path = QFileDialog.getSaveFileName(
            self, self.tr("Export to excel"), def_path, "Excel file (*.xls .*xlsx)"
        )[0]
        if save_file_path is not None:
            # Save the Excel file
            try:
                df = DataFrame(data=self.data.get_data())
                df.to_excel(save_file_path, index=False, header=False)
            except Exception as e:
                QMessageBox.critical(self, self.tr("Error"), str(e))
                return
            # Change the Data type
            self.data = ImportMatrixXls(file_path=save_file_path)
            self.dataTypeChanged.emit()
