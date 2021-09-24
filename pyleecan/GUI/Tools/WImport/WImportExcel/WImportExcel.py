from os.path import isfile

import matplotlib.pyplot as plt
from pandas import ExcelFile, read_excel
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget

from .....Classes.ImportMatrixVal import ImportMatrixVal
from .....Classes.ImportMatrixXls import ImportMatrixXls
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from .....GUI.Tools.WImport.WImportExcel.Gen_WImportExcel import Gen_WImportExcel
from .....GUI.Tools.WTableData.DTableData import DTableData


class WImportExcel(Gen_WImportExcel, QWidget):
    """Widget to define an ImportMatrixXls"""

    import_name = "Import from Excel"
    import_type = ImportMatrixXls
    saveNeeded = Signal()
    dataTypeChanged = Signal()

    def __init__(self, parent=None, data=None, plot_title=None, expected_shape=None):
        """Initialization of the widget

        Parameters
        ----------
        data : ImportMatrixXls
            Data import to define
        plot_title : str
            Name of the imported data
        expected_shape : list
            List to enforce a shape, [None, 2] enforce 2D matrix with 2 columns
        """
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)

        if data is None or not isinstance(data, ImportMatrixXls):
            self.data = ImportMatrixXls()
        else:
            self.data = data
        self.plot_title = plot_title
        self.expected_shape = expected_shape
        self.tab_window = None  # For table popup

        # Not used yet
        self.g_axe1.hide()
        self.g_axe2.hide()

        # Setup Path selector
        self.w_file_path.is_file = True
        self.w_file_path.obj = self.data
        self.w_file_path.verbose_name = "Excel file path"
        self.w_file_path.param_name = "file_path"
        self.w_file_path.extension = "Excel File (*.xls *.xlsx)"
        # Display current state of ImportMatrixXls
        self.update()

        # Connect the slot/signal
        self.w_file_path.pathChanged.connect(self.update)
        self.c_sheet.currentIndexChanged.connect(self.set_sheet)
        self.le_range.editingFinished.connect(self.set_range)
        self.b_plot.clicked.connect(self.s_plot)
        self.b_tab.clicked.connect(self.s_table)
        self.b_convert.clicked.connect(self.s_convert)

    def update(self):
        """Fill the widget with the current value of the data"""
        self.w_file_path.update()
        self.set_sheet_list()
        self.le_range.setText(self.data.usecols)
        if is_excel_file(self.data.file_path):
            self.b_plot.setEnabled(True)
            self.b_tab.setEnabled(True)
            self.b_convert.setEnabled(True)
        else:
            self.b_plot.setEnabled(False)
            self.b_tab.setEnabled(False)
            self.b_convert.setEnabled(False)

    def set_sheet_list(self):
        """Complete the combobox with the sheet name from the Excel file"""
        if is_excel_file(self.data.file_path):
            # Get Sheet names
            xls_file = ExcelFile(self.data.file_path)
            # Disable combobox if only one sheet
            if len(xls_file.sheet_names) > 1:
                self.c_sheet.setEnabled(True)
            else:
                self.c_sheet.setEnabled(False)
            self.c_sheet.blockSignals(True)
            # Fill combobox
            self.c_sheet.clear()
            for name in xls_file.sheet_names:
                self.c_sheet.addItem(name)
            # Select current index
            if (
                self.data.sheet not in ["", None]
                and self.data.sheet in xls_file.sheet_names
            ):
                self.c_sheet.setCurrentText(self.data.sheet)
            else:
                self.data.sheet = xls_file.sheet_names[0]
                self.c_sheet.setCurrentIndex(0)
            self.c_sheet.blockSignals(False)
        else:
            self.c_sheet.setEnabled(False)

    def set_sheet(self):
        """Change the current sheet selected"""
        self.data.sheet = self.c_sheet.currentText()

    def set_range(self):
        """Change the range of data selected"""
        self.data.usecols = self.le_range.text()
        if self.data.usecols == "":
            self.data.usecols = None

    def s_table(self):
        """display the data in a table"""
        try:
            data = self.data.get_data()
        except Exception as e:
            QMessageBox.critical(self, self.tr("Error"), str(e))
            return
        self.tab_window = DTableData(data=data, title=self.plot_title)
        self.tab_window.show()

    def s_plot(self):
        """display the data in a plot"""
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
            # Data in column
            fig, axes = plt.subplots()
            axes.plot(data[:, 0], data[:, 1])
            fig.show()
        if self.plot_title is not None:
            fig.canvas.manager.set_window_title(self.plot_title)
        set_plot_gui_icon()

    def s_convert(self):
        """Convert data to ImportMatrixVal"""
        try:
            data = self.data.get_data()
        except Exception as e:
            QMessageBox.critical(self, self.tr("Error"), str(e))
            return
        self.data = ImportMatrixVal(value=data)
        self.dataTypeChanged.emit()


def is_excel_file(file_path):
    """Check if the path is correct for an excel file"""

    return (
        file_path is not None
        and isfile(file_path)
        and (file_path[-4:] == ".xls" or file_path[-5:] == ".xlsx")
    )
