# -*- coding: utf-8 -*-

import PySide2.QtCore
from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from ......Classes.SlotM18 import SlotM18
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot18.Gen_PMSlot18 import Gen_PMSlot18
from ......Methods.Slot.Slot import SlotCheckError

translate = PySide2.QtCore.QCoreApplication.translate


class PMSlot18(Gen_PMSlot18, QWidget):
    """Page to set the Slot Magnet Type 18"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Ring Magnet"
    slot_type = SlotM18

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PMSlot18
            A PMSlot18 widget
        lamination : Lamination
            current lamination to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.lamination = lamination
        self.slot = lamination.slot
        self.material_dict = material_dict

        # Set FloatEdit unit
        self.lf_H0.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_H0,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        self.lf_H0.setValue(self.slot.H0)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Setup the widgets according to current values
        self.w_mag.update(lamination, self.material_dict)

        # Connect the signal
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.w_mag.saveNeeded.connect(self.emit_save)

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PMSlot18
            A PMSlot18 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lam: LamSlotMag
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.H0 is None:
            return "You must set H0 !"

        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return translate("Unable to compute yoke height:", "PMSlot18") + str(error)
