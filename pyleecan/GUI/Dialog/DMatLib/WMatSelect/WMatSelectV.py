from .....Functions.GUI.log_error import log_error
from .....GUI.Dialog.DMatLib.WMatSelect.Ui_WMatSelect import Ui_WMatSelect
from .....GUI.Dialog.DMatLib.DMatLib import DMatLib, LIB_KEY, MACH_KEY
from PySide2.QtWidgets import (
    QGroupBox,
    QMessageBox,
    QApplication,
    QComboBox,
    QVBoxLayout,
    QPushButton,
    QListView,
)
from .....Classes.Machine import Machine
from PySide2.QtCore import Signal
from PySide2.QtGui import QPalette


class WMatSelectV(QGroupBox):
    """
    Material related widget including a Label, a Combobox to select a material
    and a Button to edit a material libary.
    WMatSelect is instantiated to empty material data, so it has to be referenced
    to actual material data with the update method prior to its first usage.
    """

    # Signal to W_MachineSetup to know that the save popup is needed
    saveNeeded = Signal()

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
        QGroupBox.__init__(self, parent)

        self.verticalLayout = QVBoxLayout(self)

        self.c_mat_type = QComboBox(self)
        listView = QListView(self.c_mat_type)
        self.c_mat_type.setView(listView)
        self.c_mat_type.setObjectName("c_mat_type")
        self.verticalLayout.addWidget(self.c_mat_type)

        self.b_matlib = QPushButton(self)
        self.b_matlib.setObjectName("b_matlib")
        self.b_matlib.setText("Edit Materials")
        self.verticalLayout.addWidget(self.b_matlib)

        # To have grey title when disabled
        palette = QPalette()
        palette.setColor(
            QPalette.Disabled,
            QPalette.WindowText,
            QApplication.palette().color(QPalette.Disabled, QPalette.WindowText),
        )
        self.setPalette(palette)

        # Create the property of the widget
        self.current_dialog = None  # DMatLib widget
        self.obj = None  # object that has a material attribute
        self.mat_attr_name = ""  # material attribute name
        self.material_dict = dict()  #  Material library + machine
        self.def_mat = "M400-50A"  # Default material
        self.is_hide_button = False  # To hide the "Edit material" button
        self.test_err_msg = (
            None  # Used to stored the last error message displayed (used in test)
        )

        # Connect the signals
        self.c_mat_type.currentIndexChanged.connect(self.set_mat_type)
        self.b_matlib.clicked.connect(self.s_open_matlib)

    def update(self, obj, mat_attr_name, material_dict):
        """
        Set a reference to a material libray and material data path,
        updates the Combobox by the material names of the libary
        and set a referenced material by name.

        Parameters
        ----------
        self : WMatSelect
            A WMatSelect object
        obj : FrozenObject
            A pyleecan object that has a material attribute
        mat_attr_name : str
            A string of the material attribute name
        material_dict: dict
            Materials dictionary (library + machine)

        Returns
        -------

        """
        self.c_mat_type.blockSignals(True)
        # Set material combobox according to matlib names
        self.obj = obj
        self.mat_attr_name = mat_attr_name
        self.material_dict = material_dict

        # Get machine object to update the materials
        parent = obj.parent
        while parent is not None and not isinstance(parent, Machine):
            parent = parent.parent
        self.machine = parent

        if self.is_hide_button:
            self.b_matlib.hide()
        else:
            self.b_matlib.show()

        # Update the list of materials
        self.c_mat_type.clear()
        items_to_add = []
        # Add Library materials
        items_to_add.extend([mat.name for mat in material_dict[LIB_KEY]])
        # Add machine-specific materials
        items_to_add.extend([mat.name for mat in material_dict[MACH_KEY]])
        self.c_mat_type.addItems(items_to_add)

        mat = getattr(self.obj, mat_attr_name, None)
        if mat is None or mat.name is None:
            # Select default material
            index = self.c_mat_type.findText(self.def_mat)
            if index != -1:
                # Detecting if the material that we want to set for the wedge is stored in the Material Library or is machine_specific
                if index < len(self.material_dict[LIB_KEY]):
                    material_to_set = self.material_dict[LIB_KEY][index]
                else:
                    index_mat = index - len(self.material_dict[LIB_KEY])
                    material_to_set = self.material_dict[MACH_KEY][index_mat]

                setattr(self.obj, self.mat_attr_name, material_to_set)
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
        self.setTitle(txt)

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
        if index >= len(self.material_dict[LIB_KEY]):
            index -= len(self.material_dict[LIB_KEY])
            dict_key = MACH_KEY
        else:
            dict_key = LIB_KEY

        setattr(self.obj, self.mat_attr_name, self.material_dict[dict_key][index])
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
        # Making sure that we do not try to edit a material when is index is -1 => not a actual material
        if self.c_mat_type.currentIndex() == -1:
            self.test_err_msg = "Attempting to edit a material that is not set. Please select a material in the list to edit it."
            QMessageBox().warning(None, "Warning", self.test_err_msg)
            return None

        if self.c_mat_type.currentIndex() >= len(self.material_dict[LIB_KEY]):
            index = self.c_mat_type.currentIndex() - len(self.material_dict[LIB_KEY])
            is_lib_mat = False
        else:
            index = self.c_mat_type.currentIndex()
            is_lib_mat = True
        try:
            self.current_dialog = DMatLib(
                material_dict=self.material_dict,
                machine=self.machine,
                is_lib_mat=is_lib_mat,
                selected_id=index,
            )
            self.current_dialog.materialListChanged.connect(self.update_mat_list)
            self.current_dialog.saveNeeded.connect(self.emit_save)
            self.current_dialog.show()
        except Exception as e:
            log_error(self, "Error while opening the Material Library : \n" + str(e))

    def emit_save(self):
        """
        Emit saveNeeded if a material has been edited
        """
        self.saveNeeded.emit()

    def update_mat_list(self):
        """Update the combobox with the new materials

        Parameters
        ----------
        self :
            A WMatSelect object

        Returns
        -------

        """
        # Empty and fill the list to keep the same object (to change it everywhere)
        # del self.matlib[:]
        # self.matlib.extend(self.current_dialog.matlib)
        # Update the material
        # index = int(self.current_dialog.nav_mat.currentItem().text()[:3]) - 1

        # not needed if machine materials are "connected" properly
        # mat_dict = (self.current_dialog.matlib[index]).as_dict()
        # self.mat.__init__(init_dict=mat_dict)

        # Do not clear for now to keep editor (DMatLib) open
        # # Clear the window
        # self.current_dialog.deleteLater()
        # self.current_dialog = None

        # Update the widget
        # Avoid trigger signal currentIndexChanged
        self.c_mat_type.blockSignals(True)

        self.c_mat_type.clear()

        items_to_add = []
        # Add RefMatLib materials
        items_to_add.extend([mat.name for mat in self.material_dict[LIB_KEY]])
        # Add machine-specific materials
        items_to_add.extend([mat.name for mat in self.material_dict[MACH_KEY]])
        self.c_mat_type.addItems(items_to_add)

        index = self.c_mat_type.findText(getattr(self.obj, self.mat_attr_name).name)
        self.c_mat_type.setCurrentIndex(index)

        self.c_mat_type.blockSignals(False)
