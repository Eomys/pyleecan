from numpy import hstack, vstack, zeros, savetxt
from qtpy.QtWidgets import QDialog, QFileDialog
from pandas import read_csv
from ....GUI.Tools.FloatEdit import FloatEdit
from ....GUI.Tools.WTableData.Ui_DTableData import Ui_DTableData
from os.path import isfile
from qtpy.QtWidgets import QMessageBox
from ..WImport.WImportExcel.WImportExcel import WImportExcel
import matplotlib.pyplot as plt
from ....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from qtpy.QtCore import Signal


class DTableData(Ui_DTableData, QDialog):
    saveNeeded = Signal()

    def __init__(
        self,
        parent=None,
        data=None,
        Vmin=-999999999,
        Vmax=999999999,
        title=None,
        shape_min=(1, 1),
        shape_max=(None, None),
        col_header=None,
        unit_order=None,
        button_plot_title="",
    ):
        """Initialization of the widget

        Parameters
        ----------
        data : ndarray
            Data to display/edit
        Vmin : float
            Minimum value of the data
        Vmax : float
            Maximum value of the data
        title : str
            Title for the Dialog window
        shape_min : list
            [Min row number, Min column number], None for "no" constraint
        shape_max : list
            [Max row number, Max column number], None for "no" constraint
        col_header : list
            Provide Header to the columns (None to remove header)
        unit_order : list
            ["A(B)", "B(A)"], for excel import, to allow the user to specify the order of his units when two units
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.data = data if data is not None else zeros((1, 2))
        self.Vmin = Vmin
        self.Vmax = Vmax
        self.def_value = 0  # Value to set in empty cell (get_data)
        self.title = title  # To change the dialog title
        self.button_plot_title = button_plot_title
        self.shape_min = shape_min
        self.shape_max = shape_max
        self.col_header = col_header
        self.unit_order = unit_order
        self.N_row_txt = "N_row"
        self.N_col_txt = "N_column"
        self.isEnabled_widget = True  # To maintain when updating
        # Import/Export Hidden by default, need to be shown in widget definition
        self.b_import.hide()
        self.b_export.hide()

        self.wimport_excel = None

        self.update()
        self.si_row.valueChanged.connect(self.set_Nrow)
        self.si_col.valueChanged.connect(self.set_Ncol)
        self.b_export.clicked.connect(self.export_csv)
        self.b_import.clicked.connect(self.import_csv)
        self.b_plot.clicked.connect(self.s_plot)

    def update(self):
        """Update the Widget according to the current data"""
        self.si_row.setValue(self.data.shape[0])
        self.si_col.setValue(self.data.shape[1])
        self.in_col.setText(self.N_col_txt)
        self.in_row.setText(self.N_row_txt)

        self.b_plot.setText("Plot " + self.button_plot_title)
        # Set row shape limit
        Rmin = 1
        Rmax = 999999999
        if self.shape_min[0] is not None:
            Rmin = max(Rmin, self.shape_min[0])
        if self.shape_max[0] is not None and self.shape_max[0] >= Rmin:
            Rmax = min(Rmax, self.shape_max[0])
        self.si_row.setMinimum(Rmin)
        self.si_row.setMaximum(Rmax)

        if Rmin == Rmax:
            self.si_row.setValue(Rmin)
            self.set_Nrow()
            self.si_row.setEnabled(False)
        else:
            self.si_row.setEnabled(True)

        # Set column shape limit
        Cmin = 1
        Cmax = 999999999
        if self.shape_min[1] is not None:
            Cmin = max(Cmin, self.shape_min[1])
        if self.shape_max[1] is not None and self.shape_max[1] >= Cmin:
            Cmax = min(Cmax, self.shape_max[1])
        self.si_col.setMinimum(Cmin)
        self.si_col.setMaximum(Cmax)

        if Cmin == Cmax:
            self.si_col.setValue(Cmin)

            self.si_col.setEnabled(False)
        else:
            self.si_col.setEnabled(True)

        # Set title
        if self.title is not None:
            self.setWindowTitle(self.title)

        # Fill the table
        self.update_tab()

    def clear(self):
        self.w_tab.clear()
        self.si_row.setValue(0)

    def update_tab(self):
        """Update the Table to display the current data + setup edit"""
        self.w_tab.clear()
        nrow = self.data.shape[0]
        # Reshape vector to matrix with one column
        if len(self.data.shape) == 1:
            self.data = self.data.reshape((nrow, 1))
        ncol = self.data.shape[1]
        self.si_row.setValue(nrow)
        self.si_col.setValue(ncol)
        self.w_tab.setRowCount(nrow)
        self.w_tab.setColumnCount(ncol)

        # Set column header
        if self.col_header is not None:
            self.w_tab.setHorizontalHeaderLabels(self.col_header)

        for ii in range(nrow):
            for jj in range(ncol):
                self.w_tab.setCellWidget(ii, jj, FloatEdit())
                # Add the min/max to the widget
                self.w_tab.cellWidget(ii, jj).validator().setBottom(self.Vmin)
                self.w_tab.cellWidget(ii, jj).validator().setTop(self.Vmax)
                # Set the values
                self.w_tab.cellWidget(ii, jj).setValue(self.data[ii, jj])
                # Enable / Disable
                self.w_tab.cellWidget(ii, jj).setEnabled(self.isEnabled_widget)
                # Connect the slot
                self.w_tab.cellWidget(ii, jj).editingFinished.connect(self.emit_save)

        if ncol == 2:
            self.b_plot.setHidden(False)
        else:
            self.b_plot.setHidden(True)

    def set_Nrow(self):
        """Change the number of row"""
        Nrow_1 = self.data.shape[0]
        Nrow_2 = self.si_row.value()

        if Nrow_1 < Nrow_2:
            # Add some new lines
            data = zeros((Nrow_2, self.data.shape[1]))
            data[:Nrow_1, :] = self.data
            self.data = data
            self.update_tab()
        elif Nrow_1 > Nrow_2:
            # Remove the last lines
            self.data = self.data[:Nrow_2, :]
            self.update_tab()
        # Else do nothing

    def set_Ncol(self):
        """Change the number of column"""
        Ncol_1 = self.data.shape[1]
        Ncol_2 = self.si_col.value()

        if Ncol_1 < Ncol_2:
            # Add some new columns
            data = zeros((self.data.shape[0], Ncol_2))
            data[:, :Ncol_1] = self.data
            self.data = data
            self.update_tab()
        elif Ncol_1 > Ncol_2:
            # Remove the last columns
            self.data = self.data[:, :Ncol_2]
            self.update_tab()
        # Else do nothing

    def get_data(self):
        """Return the current data matrix"""
        data = zeros((self.si_row.value(), self.si_col.value()))
        for ii in range(self.si_row.value()):
            for jj in range(self.si_col.value()):
                cellwidget = self.w_tab.cellWidget(ii, jj)
                data[ii, jj] = (
                    cellwidget.value() if cellwidget is not None else self.def_value
                )
        return data

    def setEnabled_widgets(self, isEnabled):
        self.isEnabled_widget = isEnabled
        self.b_import.setEnabled(isEnabled)
        self.b_export.setEnabled(isEnabled)
        self.si_row.setEnabled(isEnabled)
        self.si_col.setEnabled(isEnabled)
        self.in_row.setEnabled(isEnabled)
        self.in_col.setEnabled(isEnabled)
        for ii in range(self.w_tab.rowCount()):
            for jj in range(self.w_tab.columnCount()):
                wid = self.w_tab.cellWidget(ii, jj)
                if wid is not None:
                    self.w_tab.cellWidget(ii, jj).setEnabled(isEnabled)

    def export_csv(self):
        """Write the current table data into a csv file"""
        data = self.get_data()
        save_file_path = QFileDialog.getSaveFileName(
            self, self.tr("Save file"), "", "CSV (*.csv)"
        )[0]
        if save_file_path not in [None, ""]:
            savetxt(save_file_path, data, delimiter=",")

    def import_csv(self):
        """Import the data from a csv file and update the tavle"""
        load_path = str(
            QFileDialog.getOpenFileName(
                self,
                self.tr("Load Data file"),
                "",
                "CSV, Excel (*.csv *.xls *.xlsx);;All files (*.*)",
            )[0]
        )
        if isfile(load_path):
            if load_path.endswith(".csv"):
                try:
                    df = read_csv(
                        load_path,
                        header=None,
                    )
                    if type(df.values[0, 0]) is str:
                        # Load remove first line
                        df = read_csv(
                            load_path,
                        )
                except Exception as e:
                    QMessageBox().critical(
                        self,
                        self.tr("Error"),
                        self.tr("Error while loading csv file:\n" + str(e)),
                    )
                    return
                val = df.values
                # Check Shape
                shape = val.shape
                if self.verif_shape_data(shape) is not None:
                    return
                # Try to fill the table
                try:
                    old_data = self.data
                    self.data = val
                    self.col_header = None
                    self.update()
                    self.emit_save()
                except Exception as e:
                    QMessageBox().critical(
                        self,
                        self.tr("Error"),
                        self.tr("Error while loading csv file:\n" + str(e)),
                    )
            elif load_path.endswith(".xlsx"):
                self.wimport_excel = WImportExcel(
                    load_path=load_path,
                    nb_cols=self.shape_max[1],
                    headers=self.unit_order,
                )
                self.wimport_excel.accepted.connect(self.validate_wimport_excel)
                self.wimport_excel.show()

    def validate_wimport_excel(self):
        """UPDATE THE DATA IN THE TAB"""
        val = self.wimport_excel.datas
        # Check Shape
        shape = val.shape

        if self.verif_shape_data(shape) is not None:
            return

        # Try to fill the table
        try:
            old_data = self.data
            self.data = val
            self.update()
            self.emit_save()
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error while loading csv file:\n" + str(e)),
            )

    def verif_shape_data(self, shape):
        """Verif if the data has the right shape"""
        error = ""
        if self.shape_min:
            if self.shape_min[0] and shape[0] < self.shape_min[0]:
                error = "Minimum number of line should be " + str(self.shape_min[0])
            if self.shape_min[1] and shape[1] < self.shape_min[1]:
                error = "Minimum number of column should be " + str(self.shape_min[1])
        if self.shape_max:
            if self.shape_max[0] and shape[0] > self.shape_max[0]:
                error = "Maximum number of line should be " + str(self.shape_max[0])
            if self.shape_max[1] and shape[1] > self.shape_max[1]:
                error = "Maximum number of column should be " + str(self.shape_max[1])
        if error:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error while loading excel file:\n" + error),
            )
            return error

    def s_plot(self):
        """display the data in a plot"""
        try:
            data = self.data
        except Exception as e:
            QMessageBox.critical(self, self.tr("Error"), str(e))
            return
        if len(data.shape) == 2 and data.shape[0] == 2:
            # Data in line
            fig, axes = plt.subplots()
            axes.plot(data[0, :], data[1, :])
            axes.set_xlabel(self.col_header[0])
            axes.set_ylabel(self.col_header[1])
            fig.show()
        elif len(data.shape) == 2 and data.shape[1] == 2:
            # Data in column
            fig, axes = plt.subplots()
            axes.plot(data[:, 0], data[:, 1])
            axes.set_xlabel(self.col_header[0])
            axes.set_ylabel(self.col_header[1])
            fig.show()

        if self.col_header is not None:
            fig.canvas.manager.set_window_title(self.col_header[0] + " plot")
        set_plot_gui_icon()

    def accept(self):
        """Update the data before closing"""
        self.data = self.get_data()
        super().accept()

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
