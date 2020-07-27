from os.path import isfile

import matplotlib.pyplot as plt
from pandas import DataFrame, ExcelFile, read_excel
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QWidget

from .....Classes.ImportMatrixVal import ImportMatrixVal
from .....Classes.ImportMatrixXls import ImportMatrixXls
from .....definitions import USER_DIR
from .....GUI.Tools.WImport.WImportMatrixTable.Ui_WImportMatrixTable import (
    Ui_WImportMatrixTable,
)
from .....GUI.Tools.WTableData.WTableData import DTableData


class WImportMatrixTable(Ui_WImportMatrixTable, QWidget):
    """Widget to define an ImportMatrixVal
    """

    import_name = "Defined as a Matrix"
    import_type = ImportMatrixVal
    saveNeeded = pyqtSignal()
    dataTypeChanged = pyqtSignal()

    def __init__(self, data=None):
        """Initialization of the widget

        Parameters
        ----------
        data : ImportMatrixVal 
            Data import to define
        """
        # Initialzation of the widget
        QWidget.__init__(self)
        self.setupUi(self)

        # Check data type
        if data is None or not isinstance(data, ImportMatrixVal):
            self.data = ImportMatrixVal()
        else:
            self.data = data
        self.data_type = ""  # Option to adapt the preview / check

        self.update()

        # Connect the slot/signal
        self.b_plot.clicked.connect(self.s_plot)
        self.b_tab.clicked.connect(self.s_table)
        self.b_convert.clicked.connect(self.s_convert)

    def update(self):
        """Fill the widget with the current value of the data
        """
        self.in_matrix.setText("Matrix size: " + str(self.data.get_data().shape))

    def s_table(self):
        """display the data in a table
        """
        try:
            data = self.data.get_data()
        except Exception as e:
            QMessageBox.critical(self, self.tr("Error"), str(e))
            return
        tab = DTableData(data=data)
        return_code = tab.exec_()

    def s_plot(self):
        """Plot the matrix (if 2D)
        """
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

    def s_convert(self):
        """Convert the ImportMatrixVal to a ImportMatrixXls by saving the matrix in Excel
        """
        save_file_path = QFileDialog.getSaveFileName(
            self, self.tr("Export to excel"), USER_DIR, "Excel file (*.xls .*xlsx)"
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
