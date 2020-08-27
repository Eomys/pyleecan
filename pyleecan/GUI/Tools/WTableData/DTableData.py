from numpy import hstack, vstack, zeros
from PyQt5.QtWidgets import QDialog

from ....GUI.Tools.FloatEdit import FloatEdit
from ....GUI.Tools.WTableData.Ui_DTableData import Ui_DTableData


class DTableData(Ui_DTableData, QDialog):
    def __init__(
        self,
        data=zeros((1, 1)),
        Vmin=-999999999,
        Vmax=999999999,
        title=None,
        shape_min=(1, 1),
        shape_max=(None, None),
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
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.data = data
        self.Vmin = Vmin
        self.Vmax = Vmax
        self.title = title  # To change the dialog title
        self.shape_min = shape_min
        self.shape_max = shape_max

        self.update()
        self.si_row.valueChanged.connect(self.set_Nrow)
        self.si_col.valueChanged.connect(self.set_Ncol)

    def update(self):
        """Update the Widget according to the current data
        """
        self.si_row.setValue(self.data.shape[0])
        self.si_col.setValue(self.data.shape[1])

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

    def update_tab(self):
        """Update the Table to display the current data + setup edit
        """
        self.w_tab.clear()
        self.w_tab.setRowCount(self.data.shape[0])
        self.w_tab.setColumnCount(self.data.shape[1])
        for ii in range(self.data.shape[0]):
            for jj in range(self.data.shape[1]):
                self.w_tab.setCellWidget(ii, jj, FloatEdit())
                # Add the min/max to the widget
                self.w_tab.cellWidget(ii, jj).validator().setBottom(self.Vmin)
                self.w_tab.cellWidget(ii, jj).validator().setTop(self.Vmax)
                # Set the values
                self.w_tab.cellWidget(ii, jj).setValue(self.data[ii, jj])
                # Connect the slot
                # self.w_tab.cellWidget(ii, jj).editingFinished.connect(self.set_data)

    def set_Nrow(self):
        """Change the number of row
        """
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
        """Change the number of column
        """
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

    def accept(self):
        """Update the data before closing
        """
        self.data = zeros((self.si_row.value(), self.si_col.value()))
        for ii in range(self.si_row.value()):
            for jj in range(self.si_col.value()):
                self.data[ii, jj] = self.w_tab.cellWidget(ii, jj).value()
        super().accept()
