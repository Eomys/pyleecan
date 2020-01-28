from pyleecan.GUI.Dialog.DMatLib.WMatSelect.Ui_WMatSelect import Ui_WMatSelect
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog
from pyleecan.Classes.Material import Material
from PyQt5.QtCore import pyqtSignal


class WMatSelect(Ui_WMatSelect, QWidget):
    """
    Material related widget including a Label, a Combobox to select a material 
    and a Button to edit a material libary.  
    WMatSelect is instantiated to empty material data, so it has to be referenced
    to actual material data with the update method prior to its first usage.
    """

    # Signal to W_MachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()

    def __init__(self, parent=None):
        """
        Set a reference to a material libray and material data path, 
        updates the Combobox by the material names of the libary 
        and set a referenced material by name.

        Parameters
        ----------
        self :
            A WMatSelect object
        parent :
            A reference to the widgets parent
        
        Returns
        -------

        """

        # Build the interface according to the .ui file
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # Create the property of the widget
        self.mat_win = None  # DMatLib widget
        self.obj = None  # object that has a material attribute
        self.mat_attr_name = ""  # material attribute name
        self.matlib = list()  # Matlib
        self.matlib_path = ""  # Path to save the matlib
        self.def_mat = "M400-50A"  # Default material

        # Connect the
        self.c_mat_type.currentIndexChanged.connect(self.set_mat_type)
        self.b_matlib.clicked.connect(self.s_open_matlib)

    def update(self, obj, mat_attr_name, matlib=list(), matlib_path=""):
        """
        Set a reference to a material libray and material data path, 
        updates the Combobox by the material names of the libary 
        and set a referenced material by name.

        Parameters
        ----------
        self :
            A WMatSelect object
        obj :
            A pyleecan object that has a material attribute
        mat_attr_name :
            A string of the material attribute name
        matlib :
            A material libary, i.e. a list of Material objects
        matlib_path :
            A string containing the path of material data

        Returns
        -------

        """
        self.c_mat_type.blockSignals(True)

        # Set material combobox according to matlib names
        self.obj = obj
        self.mat_attr_name = mat_attr_name
        self.matlib = matlib
        self.matlib_path = matlib_path

        # Update the list of materials
        self.c_mat_type.clear()
        self.c_mat_type.addItems([mat.name for mat in matlib])

        mat = getattr(self.obj, mat_attr_name, None)
        if mat is None or mat.name is None:
            # Default lamination material: M400-50A
            index = self.c_mat_type.findText(self.def_mat)
            if index != -1:
                # self.mat.__init__(init_dict=self.matlib[index].as_dict())
                setattr(self.obj, self.mat_attr_name, self.matlib[index])
        else:
            index = self.c_mat_type.findText(mat.name)
        self.c_mat_type.setCurrentIndex(index)
        self.c_mat_type.blockSignals(False)

    def setText(self, txt):
        """
        Set the Label's text

        Parameters
        ----------
        self :
            A WMatSelect object
        txt :
            A text string 
        
        Returns
        -------

        """
        self.in_mat_type.setText(txt)

    def set_mat_type(self, index):
        """
        Signal to set the referenced material from the material libary
        by the selected Combobox index 

        Parameters
        ----------
        self :
            A WMatSelect object
        index :
            Current index of the combobox

        Returns
        -------

        """
        setattr(self.obj, self.mat_attr_name, self.matlib[index])
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_open_matlib(self):
        """
        Open the GUI (DMatLib widget) to Edit the Material library

        Parameters
        ----------
        self :
            A WMatSelect object

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
            A WMatSelect object

        Returns
        -------

        """
        # Empty and fill the list to keep the same object (to change it everywhere)
        # del self.matlib[:]
        # self.matlib.extend(self.mat_win.matlib)
        # Update the material
        index = int(self.mat_win.nav_mat.currentItem().text()[:3]) - 1

        # not needed if machine materials are "connected" properly
        # mat_dict = (self.mat_win.matlib[index]).as_dict()
        # self.mat.__init__(init_dict=mat_dict)

        # Do not clear for now to keep editor (DMatLib) open
        # # Clear the window
        # self.mat_win.deleteLater()
        # self.mat_win = None

        # Update the widget
        # Avoid trigger signal currentIndexChanged
        self.c_mat_type.blockSignals(True)

        self.c_mat_type.clear()
        self.c_mat_type.addItems([mat.name for mat in self.matlib])
        index = self.c_mat_type.findText(getattr(self.obj, self.mat_attr_name).name)
        self.c_mat_type.setCurrentIndex(index)

        self.c_mat_type.blockSignals(False)
