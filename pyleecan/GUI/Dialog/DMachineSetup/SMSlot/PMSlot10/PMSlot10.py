# -*- coding: utf-8 -*-

import PySide2.QtCore
from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap
from ......Classes.SlotM10 import SlotM10
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.Gen_PMSlot10 import Gen_PMSlot10
from ......Methods.Slot.Slot import SlotCheckError

translate = PySide2.QtCore.QCoreApplication.translate


class PMSlot10(Gen_PMSlot10, QWidget):
    """Page to set the Slot Magnet Type 10"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Rectangular Magnet"
    notch_name = "Rectangular"
    slot_type = SlotM10

    def __init__(self, lamination=None, is_notch=False):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PMSlot10
            A PMSlot10 widget
        lamination : Lamination
            current lamination to edit
        is_notch : bool
            True to adapt the slot GUI for the notch setup
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.lamination = lamination
        self.slot = lamination.slot
        self.is_notch = is_notch

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_Wmag.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_Hmag.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_Wmag,
            self.unit_H0,
            self.unit_Hmag,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Notch setup
        if is_notch:
            # Hide magnet related widget
            wid_list = [self.in_Wmag, self.lf_Wmag, self.unit_Wmag]
            wid_list += [self.in_Hmag, self.lf_Hmag, self.unit_Hmag]
            wid_list += [self.txt_constraint]  # Constraint Wmag < W0
            for wid in wid_list:
                wid.hide()
            # Set values for check
            self.slot.Hmag = 0
            self.slot.Wmag = 0
            # Selecting the right image
            if not self.lamination.is_internal:
                # Use schematics on the external without magnet
                self.img_slot.setPixmap(
                    QPixmap(
                        u":/images/images/MachineSetup/WMSlot/SlotM10_empty_ext_sta.png"
                    )
                )
            else:
                # Use schematics on the inner without magnet
                self.img_slot.setPixmap(
                    QPixmap(
                        u":/images/images/MachineSetup/WMSlot/SlotM10_empty_int_rot.png"
                    )
                )

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_Wmag.setValue(self.slot.Wmag)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_Hmag.setValue(self.slot.Hmag)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_Wmag.editingFinished.connect(self.set_Wmag)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_Hmag.editingFinished.connect(self.set_Hmag)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PMSlot10
            A PMSlot10 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wmag(self):
        """Signal to update the value of Wmag according to the line edit

        Parameters
        ----------
        self : PMSlot10
            A PMSlot10 object
        """
        self.slot.Wmag = self.lf_Wmag.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PMSlot10
            A PMSlot10 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Hmag(self):
        """Signal to update the value of Hmag according to the line edit

        Parameters
        ----------
        self : PMSlot10
            A PMSlot10 object
        """
        self.slot.Hmag = self.lf_Hmag.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
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
        if lam.slot.W0 is None:
            return "You must set W0 !"
        elif lam.slot.Wmag is None:
            return "You must set Wmag !"
        elif lam.slot.H0 is None:
            return "You must set H0 !"
        elif lam.slot.Hmag is None:
            return "You must set Hmag !"

        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return "Unable to compute yoke height:" + str(error)

        if yoke_height <= 0:
            return "The slot height is greater than the lamination !"
