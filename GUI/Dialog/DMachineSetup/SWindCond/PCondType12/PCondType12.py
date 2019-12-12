# -*- coding: utf-8 -*-
"""@package pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType12
Cond Type 1_2 setup widget
@date Created on Thu May 21 17:38:19 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from pyleecan.Classes.CondType12 import CondType12
from pyleecan.GUI import gui_option
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType12.Gen_PCondType12 import (
    Gen_PCondType12,
)


class PCondType12(Gen_PCondType12, QWidget):
    """Page to set the Conductor Type 12
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for SWindCond combobox
    cond_type = CondType12
    cond_name = "Random Round Wire"

    def __init__(self, lamination=None):
        """Initialize the GUI according to conductor

        Parameters
        ----------
        self : PCondType12
            A PCondType12 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set FloatEdit unit
        self.lf_Wwire.unit = "m"
        self.lf_Wins_wire.unit = "m"
        self.lf_Wins_cond.unit = "m"
        self.u = gui_option.unit

        # Set unit name (m ou mm)
        wid_list = [self.unit_Wwire, self.unit_Wins_cond, self.unit_Wins_wire]
        for wid in wid_list:
            wid.setText(self.u.get_m_name())

        # Fill the fields with the machine values (if they're filled)
        self.lam = lamination
        self.cond = self.lam.winding.conductor

        # Make sure that isinstance(cond, CondType12)
        if self.cond is None or not isinstance(self.cond, CondType12):
            self.cond = CondType12()
            self.cond._set_None()

        if self.cond.Nwppc is None:
            self.cond.Nwppc = 1  # Default value
        self.si_Nwpc1.setValue(self.cond.Nwppc)

        self.lf_Wwire.setValue(self.cond.Wwire)
        if self.cond.Wins_wire is None:
            self.cond.Wins_wire = 0  # Default value
        self.lf_Wins_wire.setValue(self.cond.Wins_wire)
        if self.cond.Wins_cond is None:
            self.cond.Wins_cond = 0  # Default value
        self.lf_Wins_cond.setValue(self.cond.Wins_cond)

        # Display the conductor main output
        self.w_out.comp_output()

        # Connect the signal/slot
        self.si_Nwpc1.editingFinished.connect(self.set_Nwppc)
        self.lf_Wwire.editingFinished.connect(self.set_Wwire)
        self.lf_Wins_wire.editingFinished.connect(self.set_Wins_wire)
        self.lf_Wins_cond.editingFinished.connect(self.set_Wins_cond)

    def set_Nwppc(self):
        """Signal to update the value of Nwppc according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        self.cond.Nwppc = self.si_Nwpc1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wwire(self):
        """Signal to update the value of Wwire according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        self.cond.Wwire = self.lf_Wwire.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wins_wire(self):
        """Signal to update the value of Wins_wire according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        self.cond.Wins_wire = self.lf_Wins_wire.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wins_cond(self):
        """Signal to update the value of Wins_cond according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        self.cond.Wins_cond = self.lf_Wins_cond.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if self.cond.Nwppc is None:
            return self.tr("You must set Nwpc1 !")
        elif self.cond.Wwire is None:
            return self.tr("You must set Wwire !")
        elif self.cond.Wins_wire is None:
            return self.tr("You must set Wins_wire !")
        elif self.cond.Wins_cond is None:
            return self.tr("You must set Wins_cond !")
