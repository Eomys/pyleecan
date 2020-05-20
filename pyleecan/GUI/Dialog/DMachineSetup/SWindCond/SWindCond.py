# -*- coding: utf-8 -*-


from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget

from .....Classes.CondType11 import CondType11
from .....Classes.CondType12 import CondType12
from .....GUI.Dialog.DMachineSetup.SWindCond.PCondType11.PCondType11 import PCondType11
from .....GUI.Dialog.DMachineSetup.SWindCond.PCondType12.PCondType12 import PCondType12
from .....GUI.Dialog.DMachineSetup.SWindCond.Ui_SWindCond import Ui_SWindCond

# For the Conductor combobox
wid_list = [PCondType11, PCondType12]
type_list = [wid.cond_type for wid in wid_list]
name_list = [wid.cond_name for wid in wid_list]


class SWindCond(Ui_SWindCond, QWidget):
    """Step to define the winding conductor
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for DMachineSetup nav
    step_name = "Winding Conductor"

    def __init__(self, machine, w_matlib, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWindCond
            A SWindCond widget
        machine : Machine
            current machine to edit
        matlib : list
            List of available Material
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.w_matlib = w_matlib
        self.is_stator = is_stator

        # Add DMatLib to WMatSelect
        self.w_mat.mat_win = w_matlib

        # Fill the fields with the machine values (if they're filled)
        if self.is_stator:
            self.obj = machine.stator
            self.w_mat.in_mat_type.setText(self.tr("mat_wind1: "))
        else:
            self.obj = machine.rotor
            self.w_mat.in_mat_type.setText(self.tr("mat_wind2: "))
        self.w_mat.def_mat = "Copper1"

        # Fill the combobox with the available conductor
        self.c_cond_type.clear()
        for cond in name_list:
            self.c_cond_type.addItem(cond)

        # Set default conductor if conductor not set
        if (
            self.obj.winding.conductor is None
            or type(self.obj.winding.conductor) not in type_list
        ):
            # CondType11 is the default
            self.obj.winding.conductor = CondType11()
            self.obj.winding.conductor._set_None()

        # Set the conductor material
        self.w_mat.update(self.obj.winding.conductor, "cond_mat", self.w_matlib)

        # Initialize the needed conductor widget
        index = type_list.index(type(self.obj.winding.conductor))
        self.s_update(index)
        self.c_cond_type.setCurrentIndex(index)

        # Connect the widget
        self.c_cond_type.currentIndexChanged.connect(self.s_set_cond_type)
        self.w_mat.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup
        """
        self.saveNeeded.emit()

    def s_set_cond_type(self, index):
        """Setup the Gui for the selected conductor type

        Parameters
        ----------
        self : SWindCond
            A SWindCond object
        index : int
            Index of the selected conductor type
        """

        # Initialize the new one
        self.obj.winding.conductor = type_list[index]()
        self.obj.winding.conductor._set_None()
        # Update the GUI
        self.s_update(index)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_update(self, index):
        """Update the GUI to show the current conductor widget

        Parameters
        ----------
        self : SWindCond
            a SWindCond object
        index : int
            Index of the selected conductor type
        """
        # Regenerate the pages with the new values
        self.w_cond.setParent(None)
        self.w_cond = wid_list[index](self.obj)
        self.w_cond.saveNeeded.connect(self.emit_save)

        # Refresh the GUI
        self.main_layout.removeWidget(self.w_cond)
        self.main_layout.insertWidget(1, self.w_cond)

    @staticmethod
    def check(lamination):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        obj = lamination.winding  # For readibility

        # Check that the conductor properties are set
        if type(obj.conductor) is CondType11:
            for name in ["Hwire", "Wwire", "Wins_wire", "Nwppc_rad", "Nwppc_tan"]:
                if obj.conductor.__getattribute__(name) is None:
                    return "You must set " + name + " !"
        elif type(obj.conductor) is CondType12:
            for name in ["Wwire", "Wins_wire", "Wins_cond", "Nwppc"]:
                if obj.conductor.__getattribute__(name) is None:
                    return "You must set " + name + " !"
