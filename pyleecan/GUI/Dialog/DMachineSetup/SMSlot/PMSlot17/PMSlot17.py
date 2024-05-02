# -*- coding: utf-8 -*-

import qtpy.QtCore
from numpy import pi
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget

from ......Classes.SlotM17 import SlotM17
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.Gen_PMSlot17 import Gen_PMSlot17
from ......Methods.Slot.Slot import SlotCheckError

translate = qtpy.QtCore.QCoreApplication.translate


class PMSlot17(Gen_PMSlot17, QWidget):
    """Page to set the Slot Magnet Type 17"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Cylindrical magnet (no lamination)"
    slot_type = SlotM17

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PMSlot17
            A PMSlot17 widget
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
        self.lf_Lmag.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_Lmag,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        if self.lamination.magnet.Lmag is None:
            self.lamination.magnet.Lmag = self.lamination.L1
        self.lf_Lmag.setValue(self.lamination.magnet.Lmag)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Setup the widgets according to current values
        self.w_mag.update(lamination, self.material_dict)

        # Connect the signal
        self.lf_Lmag.editingFinished.connect(self.set_Lmag)
        self.w_mag.saveNeeded.connect(self.emit_save)

    def set_Lmag(self):
        """Signal to update the value of Lmag according to the line edit

        Parameters
        ----------
        self : PMSlot17
            A PMSlot17 object
        """
        self.lamination.magnet.Lmag = self.lf_Lmag.value()
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
        if lam.magnet.Lmag is None:
            return "You must set Lmag !"

        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return translate("Unable to compute yoke height:", "PMSlot17") + str(error)
