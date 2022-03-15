from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QWidget

from ....Classes.ImportGenVectLin import ImportGenVectLin
from ....GUI.Tools.WImport.Ui_WImport import Ui_WImport
from ....GUI.Tools.WImport.WImportExcel.WImportExcel import WImportExcel
from ....GUI.Tools.WImport.WImportLinspace.WImportLinspace import WImportLinspace
from ....GUI.Tools.WImport.WImportMatrixTable.WImportMatrixTable import (
    WImportMatrixTable,
)


class WImport(Ui_WImport, QWidget):
    saveNeeded = Signal()

    def __init__(self, parent=None):
        """Widget to define an ImportLinspace"""
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)

    # NOT USED ANYMORE

    #     self.obj = None  # Object to edit
    #     self.verbose_name = ""  # Name to display / adapt the GUI
    #     self.plot_title = None  # Name to use for the plot
    #     # List to enforce a shape, [None, 2] enforce 2D matrix with 2 columns
    #     self.expected_shape = None
    #     self.param_name = ""  # Name of the quantity to set
    #     # Setup tab values
    #     self.tab_values.setWindowFlags(self.tab_values.windowFlags() & ~Qt.Dialog)
    #     self.tab_values.title = self.in_param.text()
    #     self.tab_values.N_row_txt = "Nb of Points"
    #     self.tab_values.shape_max = (None, 2)
    #     self.tab_values.col_header = ["B-curve(T)", "H-curve(A/m)"]
    #     self.tab_values.unit_order = ["B(H)", "H(B)"]
    #     self.tab_values.si_col.hide()
    #     self.tab_values.in_col.hide()
    #     self.tab_values.b_close.hide()
    #     self.tab_values.b_import.setHidden(False)
    #     self.tab_values.b_export.setHidden(False)
    #     self.tab_values.update()

    # def emit_save(self):
    #     """Send a saveNeeded signal to the DMachineSetup"""
    #     self.saveNeeded.emit()

    # def set_plot_title(self, plot_title):
    #     self.plot_title = plot_title
    #     self.tab_values.plot_title = plot_title
