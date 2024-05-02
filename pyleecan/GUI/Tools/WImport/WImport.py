from qtpy.QtCore import Qt, Signal
from qtpy.QtWidgets import QWidget

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

        self.obj = None  # Object to edit
        self.verbose_name = ""  # Name to display / adapt the GUI
        self.plot_title = None  # Name to use for the plot
        # List to enforce a shape, [None, 2] enforce 2D matrix with 2 columns
        self.expected_shape = None
        self.param_name = ""  # Name of the quantity to set
        self.widget_list = []  # Available widget to import

        self.c_type_import.currentIndexChanged.connect(self.set_type_import)

    def update(self):
        """Update the display of the Widget"""
        self.in_param.setText(self.verbose_name)
        # Fill the combobox with the meaningful widgets
        self.c_type_import.blockSignals(True)
        if self.param_name == "BH_curve":
            self.widget_list = [WImportExcel, WImportMatrixTable]
        else:
            self.widget_list = []
        # Generate the Combobox content
        self.c_type_import.clear()
        for widget in self.widget_list:
            self.c_type_import.addItem(widget.import_name)
        # Set the index according to data type
        type_list = [wid.import_type for wid in self.widget_list]
        data = getattr(self.obj, self.param_name)
        if type(data) not in type_list:
            # Initialization with first time
            data = type_list[0]()
            data._set_None()
            setattr(self.obj, self.param_name, data)
            self.emit_save()
        self.c_type_import.setCurrentIndex(type_list.index(type(data)))
        self.set_import_widget()
        self.c_type_import.blockSignals(False)

    def set_type_import(self):
        """Change the type of the import object according to the combobox"""
        data = self.widget_list[self.c_type_import.currentIndex()].import_type()
        data._set_None()
        setattr(self.obj, self.param_name, data)
        self.emit_save()
        self.set_import_widget()

    def set_import_widget(self):
        """Update the import widget
        Parameters
        ----------
        self : WImport
            A WImport object
        """
        data = getattr(self.obj, self.param_name)
        # Regenerate the pages with the new values
        self.w_import.setParent(None)
        self.w_import = self.widget_list[self.c_type_import.currentIndex()](
            data=data,
            plot_title=self.plot_title if self.plot_title else self.verbose_name,
            expected_shape=self.expected_shape,
        )
        self.w_import.data_type = self.verbose_name
        self.w_import.saveNeeded.connect(self.emit_save)
        self.w_import.dataTypeChanged.connect(self.update_type)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_import)
        self.main_layout.insertWidget(1, self.w_import)

    def update_type(self):
        """The Import widget has changed the type of the import"""
        setattr(self.obj, self.param_name, self.w_import.data)
        self.update()

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_plot_title(self, plot_title):
        self.plot_title = plot_title
        self.w_import.plot_title = plot_title
