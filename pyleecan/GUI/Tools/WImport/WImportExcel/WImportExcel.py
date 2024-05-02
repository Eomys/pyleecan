from os.path import isfile

import numpy
import re
from pandas import ExcelFile, read_excel
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QMessageBox, QDialog

from .....Classes.ImportMatrixVal import ImportMatrixVal
from .....Classes.ImportMatrixXls import ImportMatrixXls
from .....GUI.Tools.WImport.WImportExcel.Ui_WImportExcel import Ui_WImportExcel

pattern_validation_input = re.compile(r"[a-zA-Z]{1,}\d+:[a-zA-Z]{1,}\d+")


class WImportExcel(Ui_WImportExcel, QDialog):
    """Widget to define an ImportMatrixXls"""

    import_name = "Import from Excel"
    import_type = ImportMatrixXls
    saveNeeded = Signal()
    dataTypeChanged = Signal()

    def __init__(
        self,
        parent=None,
        data=None,
        plot_title=None,
        expected_shape=None,
        load_path=None,
        nb_cols=None,
        headers=None,
    ):
        """Initialization of the widget

        Parameters
        ----------
        data : ImportMatrixXls
            Data import to define
        plot_title : str
            Name of the imported data
        expected_shape : list
            List to enforce a shape, [None, 2] enforce 2D matrix with 2 columns
        load_path : str
            Path of the excel file
        nb_cols : int
            Number of max columns in the table
        headers : str
            If specified, the user will be able to choose the order of the units for the plot
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setMaximumHeight(300)
        self.setMaximumWidth(300)
        if data is None or not isinstance(data, ImportMatrixXls):
            self.data = ImportMatrixXls()
        else:
            self.data = data
        self.plot_title = plot_title
        self.expected_shape = expected_shape
        self.tab_window = None  # For table popup
        self.load_path = load_path
        self.int_row_list = None
        self.cols = None
        self.headers = headers
        self.datas = None
        self.b_ok.setEnabled(False)

        if nb_cols == 2:
            self.c_order.setHidden(False)
            self.c_order.setItemText(0, headers[0])
            self.c_order.setItemText(1, headers[1])
            self.in_order.setHidden(False)
        else:
            self.c_order.setHidden(True)
            self.in_order.setHidden(True)

        # Display current state of ImportMatrixXls
        self.update()

        # Connect the slot/signal
        self.c_sheet.currentIndexChanged.connect(self.set_sheet)
        self.le_range.textChanged.connect(self.set_range)
        self.b_ok.clicked.connect(self.save)
        self.b_cancel.clicked.connect(self.cancel)

    def update(self):
        """Fill the widget with the current value of the data"""
        self.set_sheet_list()
        self.le_range.setText(self.data.usecols)

    def set_sheet_list(self):
        """Complete the combobox with the sheet name from the Excel file"""
        if is_excel_file(self.load_path):
            # Get Sheet names
            xls_file = ExcelFile(self.load_path)
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
        if pattern_validation_input.match(self.le_range.text()) is not None:
            self.b_ok.setEnabled(True)
            pattern_row = r"\d+"
            pattern_cols = r"[a-zA-Z]{1,}"
            str_row_list = re.findall(pattern_row, self.le_range.text())
            self.int_row_list = list(map(int, str_row_list))
            str_col_list = re.findall(pattern_cols, self.le_range.text())
            self.cols = str_col_list[0].upper() + ":" + str_col_list[1].upper()
        else:
            self.b_ok.setEnabled(False)

    def s_convert(self):
        """Convert data to ImportMatrixVal"""
        try:
            data = self.data.get_data()
        except Exception as e:
            QMessageBox.critical(self, self.tr("Error"), str(e))
            return
        self.data = ImportMatrixVal(value=data)
        self.dataTypeChanged.emit()

    def save(self):
        """Update the data before closing"""
        skipped_rows = self.int_row_list[0] - 1
        data_excel = read_excel(
            self.load_path,
            sheet_name=self.c_sheet.currentText(),
            skiprows=skipped_rows,
            nrows=self.int_row_list[1] - skipped_rows,
            usecols=self.cols,
            header=None,
        )
        self.datas = data_excel.values
        if self.c_order.currentIndex() == 1:
            self.data_reversed = list()
            for single_point in data_excel.values:
                self.data_reversed.append(single_point[::-1])  # Reverse column
            self.datas = numpy.array(self.data_reversed)
        self.accept()

    def cancel(self):
        """Close"""
        self.close()


def is_excel_file(file_path):
    """Check if the path is correct for an excel file"""

    return (
        file_path is not None
        and isfile(file_path)
        and (file_path[-4:] == ".xls" or file_path[-5:] == ".xlsx")
    )
