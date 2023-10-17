# -*- coding: utf-8 -*-

import PySide2.QtCore
from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap

from ......Classes.SlotM19 import SlotM19
from ..... import gui_option
from ..PMSlot19.Gen_PMSlot19 import Gen_PMSlot19
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Resources import pixmap_dict

translate = PySide2.QtCore.QCoreApplication.translate


class PMSlot19(Gen_PMSlot19, QWidget):
    """Page to set the Slot Magnet Type 19"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Trapezoidal Magnet with polar top"
    notch_name = "Trapezoidal"
    slot_type = SlotM19

    def __init__(self, lamination=None, notch_obj=None, material_dict=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PMSlot19
            A PMSlot19 widget
        lamination : Lamination
            current lamination to edit
        notch_obj : notch
            current notch to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.lamination = lamination
        self.slot = lamination.slot
        self.is_notch = notch_obj is not None
        self.notch_obj = notch_obj
        self.material_dict = material_dict

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_W1.unit = "m"
        self.lf_H0.unit = "m"

        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_W1,
            self.unit_H0,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Notch setup
        if self.is_notch:
            # Selecting the right image
            if self.lamination.is_internal:
                self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotM19_empty_int_rotor"]))
            else:
                # Use schematics on the external without magnet.
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotM19_empty_ext_stator"])
                )
            # Hide magnet widgets
            self.w_mag.hide()
        else:
            # Setup the widgets according to current values
            self.w_mag.update(lamination, self.material_dict)
            # Use schematics on the inner without magnet
            self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotM19_mag_int_rotor"]))

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_W1.setValue(self.slot.W1)
        self.lf_H0.setValue(self.slot.H0)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.w_mag.saveNeeded.connect(self.emit_save)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PMSlot19
            A PMSlot19 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PMSlot19
            A PMSlot19 object
        """
        self.slot.W1 = self.lf_W1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PMSlot19
            A PMSlot19 object
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
        if lam.slot.W0 is None:
            return "You must set W0 !"
        elif lam.slot.W1 is None:
            return "You must set W1 !"
        elif lam.slot.H0 is None:
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
            return "Unable to compute yoke height:" + str(error)

        if yoke_height <= 0:
            return "The slot height is greater than the lamination !"
