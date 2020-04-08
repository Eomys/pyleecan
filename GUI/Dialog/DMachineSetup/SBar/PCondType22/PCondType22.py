# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from pyleecan.Classes.CondType22 import CondType22
from pyleecan.GUI import gui_option
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType22.Gen_PCondType22 import (
    Gen_PCondType22,
)


class PCondType22(Gen_PCondType22, QWidget):
    """Page to setup Conductor Type 22
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for SBar combobox
    cond_name = "Die cast bar"
    cond_type = CondType22

    def __init__(self, machine=None, matlib=[]):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : PCondType22
            A PCondType22 widget
        machine : Machine
            current machine to edit
        matlib : list
            List of available Material
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set material combobox according to matlib names
        self.matlib = matlib
        self.w_mat.def_mat = "Copper1"

        # Set unit name (m ou mm)
        self.u = gui_option.unit

        # Fill the fields with the machine values (if they're filled)
        self.machine = machine

        # Make sure that the rotor's conductor is a 2_2
        conductor = machine.rotor.winding.conductor
        if conductor is None or not isinstance(conductor, CondType22):
            self.machine.rotor.winding.conductor = CondType22()
            self.machine.rotor.winding.conductor._set_None()

        self.w_mat.update(conductor, "cond_mat", matlib)

        # Update active surface for output display
        self.machine.rotor.winding.conductor.Sbar = (
            self.machine.rotor.slot.comp_surface()
        )
        # Display the main output
        self.w_out.comp_output()
        self.w_mat.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Emit the saveNeeded signal
        """
        self.saveNeeded.emit()
