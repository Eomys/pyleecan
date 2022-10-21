# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QDialog
from logging import getLogger
from .....loggers import GUI_LOG_NAME
from .....Classes.BoreFlower import BoreFlower
from .....GUI.Dialog.DMachineSetup.DBore.Ui_DBore import Ui_DBore
from .....GUI.Dialog.DMachineSetup.DBore.PBoreFlower.PBoreFlower import PBoreFlower
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from .....Functions.GUI.log_error import log_error

# List to convert index of combobox to bore type
WIDGET_LIST = [
    PBoreFlower,
]
INIT_INDEX = [wid.bore_type for wid in WIDGET_LIST]
BORE_NAME = [wid.bore_name for wid in WIDGET_LIST]


class DBore(Ui_DBore, QDialog):
    """Step to set the bore with winding"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, lam):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : DBore
            A DBore widget
        lam : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.obj = lam  # Current object backup
        self.lam = lam.copy()  # Copy to edit

        self.b_help.hide()

        # Fill the combobox with the available bore
        self.c_bore_type.clear()
        for bore in BORE_NAME:
            self.c_bore_type.addItem(bore)
        # Avoid erase all the parameters when navigating though the bores
        self.previous_bore = dict()
        for bore_type in INIT_INDEX:
            self.previous_bore[bore_type] = None

        # If the bore is not set, initialize it with a 1_0
        if self.lam.bore is None:
            self.lam.bore = BoreFlower(
                Rarc=self.obj.get_Rbo() * 0.85,
                alpha=pi / (2 * self.obj.get_pole_pair_number()),
            )

        # Set the correct index for the type checkbox and display the object
        index = INIT_INDEX.index(type(self.lam.bore))
        self.c_bore_type.setCurrentIndex(index)

        # Update the bore widget
        self.s_update_bore()

        # Connect the bore
        self.c_bore_type.currentIndexChanged.connect(self.s_change_bore)
        self.b_plot.clicked.connect(self.s_plot)
        self.b_cancel.clicked.connect(self.reject)
        self.b_ok.clicked.connect(self.valid_bore)

    def valid_bore(self):
        """Validate the bore and update the lamination

        Parameters
        ----------
        self : DBore
            a DBore object
        """
        error = self.check()

        if error:  # Error => Display it
            QMessageBox().critical(self, self.tr("Error"), error)
        else:
            self.accept()

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_bore_type(self, index):
        """Initialize self.lam with the bore corresponding to index

        Parameters
        ----------
        self : DBore
            A DBore object
        index : int
            Index of the selected bore type in the list
        """

        # Save the bore
        self.previous_bore[type(self.lam.bore)] = self.lam.bore

        # Call the corresponding constructor
        if self.previous_bore[INIT_INDEX[index]] is None:
            # No previous bore of this type
            self.lam.bore = INIT_INDEX[index]()
            self.lam.bore._set_None()  # No default value
        else:  # Load the previous bore of this type
            self.lam.bore = self.previous_bore[INIT_INDEX[index]]

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_update_bore(self):
        """Update the bore widget

        Parameters
        ----------
        self : DBore
            A DBore object
        """

        # Regenerate the pages with the new values
        self.w_bore.setParent(None)
        self.w_bore = WIDGET_LIST[self.c_bore_type.currentIndex()](self.lam)
        self.w_bore.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_bore)
        self.main_layout.insertWidget(1, self.w_bore)

    def s_change_bore(self, index):
        """Signal to update the bore object and widget

        Parameters
        ----------
        self : DBore
            A DBore object
        index : int
            Current index of the combobox
        """
        # Current bore is removed and replaced by the new one
        self.set_bore_type(index)
        self.s_update_bore()

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : DBore
            A DBore object
        """
        # We have to make sure the bore is right before trying to plot it
        error = self.check()
        if self.lam.is_stator:
            name = "Stator"
        else:
            name = "Rotor"

        if error:  # Error => Display it
            err_msg = "Error in " + name + " bore definition:\n" + error
            getLogger(GUI_LOG_NAME).debug(err_msg)
            QMessageBox().critical(self, self.tr("Error"), err_msg)
        else:  # No error => Plot the lamination
            try:
                self.lam.plot()
                set_plot_gui_icon()
            except Exception as e:
                err_msg = (
                    "Error while plotting " + name + " in bore definition:\n" + str(e)
                )
                log_error(self, err_msg)

    def check(self):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        self: DBore
            A DBore object

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        try:
            # Call the check method of the bore (every bore type have a
            # different check method)
            index = INIT_INDEX.index(type(self.lam.bore))
            return WIDGET_LIST[index].check(self.lam)
        except Exception as e:
            return str(e)
