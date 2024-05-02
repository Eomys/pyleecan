from ....GUI.Tools.WPathSelector.Ui_WPathSelector import Ui_WPathSelector
from qtpy.QtWidgets import QWidget, QMessageBox, QDialog, QFileDialog
from os.path import isfile, isdir
from qtpy.QtCore import Signal
from ....definitions import config_dict


class WPathSelector(Ui_WPathSelector, QWidget):
    """Widget to select the path to a file or a folder"""

    pathChanged = Signal()  # Changed and correct

    def __init__(self, parent=None):
        """Create the widget

        Parameters
        ----------
        self : WPathSelector
            A WPathSelector object
        parent : QWidget
            A reference to the widgets parent
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # Create the property of the widget
        self.obj = None  # object that has a path property to set
        self.verbose_name = (
            ""  # Name to display in the GUI (leave empty to use param_name)
        )
        self.param_name = ""  # path property name
        self.is_file = True  # True path to a file, False path to a folder
        self.extension = ""  # Filter file type

        # Connect the slot/signals
        self.le_path.editingFinished.connect(self.set_obj_path)
        self.b_path.clicked.connect(self.select_path)

    def update(self):
        """Update the widget to match the value of the properties

        Parameters
        ----------
        self : WPathSelector
            A WPathSelector object

        Returns
        -------

        """
        # Set the correct text for the label
        if self.verbose_name in ["", None]:
            self.verbose_name = self.param_name
        self.in_path.setText(self.verbose_name + ": ")
        # Set the correct text for the button
        if self.is_file:
            self.b_path.setText("Select File")
        else:
            self.b_path.setText("Select Folder")
        # Get the current path to display
        if self.obj is not None:
            self.le_path.setText(getattr(self.obj, self.param_name))

    def get_path(self):
        """Return the current path"""
        return self.le_path.text().replace("\\", "/")

    def set_path_txt(self, path):
        """Set the line edit text"""
        if path is not None:
            path = path.replace("\\", "/")
        self.le_path.setText(path)

    def set_obj_path(self):
        """Update the object with the current path (if correct)"""
        path = self.get_path().replace("\\", "/")
        if (self.is_file and isfile(path)) or (not self.is_file and isdir(path)):
            if self.obj is not None:
                if getattr(self.obj, self.param_name) != path:
                    setattr(self.obj, self.param_name, path)
                    self.pathChanged.emit()
            else:
                self.pathChanged.emit()

    def select_path(self):
        """Open a popup to select the correct path"""
        # Initial folder for the Dialog
        default_path = self.get_path()
        if self.is_file:  # Select a file
            if not isfile(default_path):
                default_path = ""
            path = QFileDialog.getOpenFileName(
                self,
                "Select " + self.verbose_name + " file",
                default_path,
                filter=self.extension,
            )[0]
        else:  # Select a Folder
            if not isdir(default_path):
                default_path = ""
            path = QFileDialog.getExistingDirectory(
                self, "Select " + self.verbose_name + " directory", default_path
            )
        # Update the path
        if path:  # check for empty string as well as None
            path = path.replace("\\", "/")
            self.le_path.setText(path)
            self.set_obj_path()
