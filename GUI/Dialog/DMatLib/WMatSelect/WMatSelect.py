from pyleecan.GUI.Dialog.DMatLib.WMatSelect.Ui_WMatSelect import Ui_WMatSelect
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog
from pyleecan.Classes.Material import Material
from PyQt5.QtCore import pyqtSignal


class WMatSelect(Ui_WMatSelect, QWidget):
    """Setup of a WMatSelect Main parameters"""

    # Signal to W_MachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()

    def __init__(self, parent=None):
        """Initialize the widget
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # Create the property of the widget
        self.mat_win = None  # DMatLib widget
        self.mat = Material()  # Current material
        self.matlib = list()  # Matlib
        self.matlib_path = ""  # Path to save the matlib
        self.def_mat = "M400-50A"  # Default material

        # Connect the
        self.c_mat_type.currentIndexChanged.connect(self.set_mat_type)
        self.b_matlib.clicked.connect(self.s_open_matlib)

    def update(self, mat, matlib=list(), matlib_path=""):
        self.c_mat_type.blockSignals(True)

        # Set material combobox according to matlib names
        self.mat = mat
        self.matlib = matlib
        self.matlib_path = matlib_path

        # Update the list of materials
        self.c_mat_type.clear()
        self.c_mat_type.addItems([mat.name for mat in matlib])

        if mat is None or mat.name is None:
            # Default lamination material: M400-50A
            index = self.c_mat_type.findText(self.def_mat)
            if index != -1:
                self.mat = Material(init_dict=self.matlib[index].as_dict())
        else:
            index = self.c_mat_type.findText(mat.name)
        self.c_mat_type.setCurrentIndex(index)
        self.c_mat_type.blockSignals(False)

    def setText(self, txt):
        self.in_mat_type.setText(txt)

    def set_mat_type(self, index):
        """Signal to update the value of mat_name according to the combobox

        Parameters
        ----------
        self :
            A P_LamParam object
        index :
            Current index of the combobox

        Returns
        -------

        """
        self.mat.__init__(init_dict=self.matlib[index].as_dict())
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_open_matlib(self):
        """Open the GUI to Edit the Material library

        Parameters
        ----------
        self :
            A P_LamParam object

        Returns
        -------

        """
        self.mat_win = DMatLib(self.matlib, self.c_mat_type.currentIndex())
        self.mat_win.accepted.connect(self.set_matlib)
        self.mat_win.show()

    def set_matlib(self):
        """Update the matlib with the new value

        Parameters
        ----------
        self :
            A P_Lam_Param object

        Returns
        -------

        """
        # Empty and fill the list to keep the same object
        # (to change it everywhere)
        del self.matlib[:]
        self.matlib.extend(self.mat_win.matlib)
        # Update the material
        index = int(self.mat_win.nav_mat.currentItem().text()[:3]) - 1
        mat_dict = (self.mat_win.matlib[index]).as_dict()
        self.mat.__init__(init_dict=mat_dict)
        # Clear the window
        self.mat_win = None
        # Update the widget
        # Avoid trigger signal currentIndexChanged
        self.c_mat_type.blockSignals(True)

        self.c_mat_type.clear()
        self.c_mat_type.addItems([mat.name for mat in self.matlib])

        index = self.c_mat_type.findText(self.mat.name)
        self.c_mat_type.setCurrentIndex(index)

        self.c_mat_type.blockSignals(False)
