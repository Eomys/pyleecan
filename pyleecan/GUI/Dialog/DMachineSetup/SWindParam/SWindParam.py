# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget

from .....GUI.Dialog.DMachineSetup.SWindParam.Gen_SWindParam import Gen_SWindParam


class SWindParam(Gen_SWindParam, QWidget):
    """Step to define the winding parameters"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for DMachineSetup nav
    step_name = "Winding Parameter"

    def __init__(self, machine, matlib, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWindParam
            A SWindParam widget
        machine : Machine
            current machine to edit
        matlib : MatLib
            Material Library
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.matlib = matlib
        self.is_stator = is_stator

        # Fill the fields with the machine values (if they're filled)
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor

        if self.obj.winding.Ntcoil is None:
            self.si_Ntcoil.clear()
        else:
            self.si_Ntcoil.setValue(self.obj.winding.Ntcoil)

        # Adapt GUI for rotor WRSM
        if not is_stator and machine.type_machine == 9:
            self.in_Zs.hide()
            self.in_Nlay.hide()
            self.obj.winding.Npcpp = 1  # Enforce the value
            self.si_Npcpp.setEnabled(False)

        if self.obj.winding.Npcpp is None:
            self.obj.winding.Npcpp = 1  # Default value

        self.comp_output()
        self.si_Npcpp.setValue(self.obj.winding.Npcpp)

        # Connect the widget
        self.si_Ntcoil.editingFinished.connect(self.set_Ntcoil)
        self.si_Npcpp.editingFinished.connect(self.set_Npcp)

    def set_Ntcoil(self):
        """Signal to update the value of Ntcoil according to the line edit

        Parameters
        ----------
        self : SWindParam
            A SWindParam object
        """
        self.obj.winding.Ntcoil = self.si_Ntcoil.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Npcp(self):
        """Signal to update the value of Npcp according to the line edit

        Parameters
        ----------
        self : SWindParam
            A SWindParam object
        """
        self.obj.winding.Npcpp = self.si_Npcpp.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the winding output

        Parameters
        ----------
        self : SWindParam
            A SWindParam object
        """

        Zs = self.obj.slot.Zs
        qs = self.obj.winding.qs

        try:
            Ntspc = str(self.obj.winding.comp_Ntspc(Zs))
        except:
            Ntspc = "?"
        try:
            Ncspc = str(self.obj.winding.comp_Ncspc(Zs))
        except:
            Ncspc = "?"
        try:
            (Nrad, Ntan) = self.obj.winding.get_dim_wind()
            Nlay = str(Nrad * Ntan)
        except:
            Nlay = "?"

        self.in_Zs.setText(self.tr("Zs: ") + str(Zs))
        self.in_qs.setText(self.tr("qs: ") + str(qs))
        self.out_Ncspc.setText(self.tr("Ncspc: ") + Ncspc)
        self.out_Ntspc.setText(self.tr("Ntspc: ") + Ntspc)
        self.in_Nlay.setText(self.tr("Nlay: ") + str(Nlay))

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

        try:
            obj = lamination.winding  # For readibility

            # Check that everything is set
            if obj.Ntcoil is None:
                return "You must set Ntcoil !"
            if obj.Npcpp is None:
                return "You must set Npcpp !"
        except Exception as e:
            return str(e)
