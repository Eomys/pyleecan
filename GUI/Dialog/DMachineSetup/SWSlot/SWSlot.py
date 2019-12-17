# -*- coding: utf-8 -*-
"""@package pyleecan.GUI.Dialog.DMachineSetup.SWSlot.SWSlot
Winding Slot Setup Page
@date Created on Wed Jul 15 14:14:29 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import pi
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotWind import SlotWind
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.Gen_SWSlot import Gen_SWSlot
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot10.PWSlot10 import PWSlot10
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot11.PWSlot11 import PWSlot11
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot12.PWSlot12 import PWSlot12
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot13.PWSlot13 import PWSlot13
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.PWSlot14 import PWSlot14
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot15.PWSlot15 import PWSlot15
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot16.PWSlot16 import PWSlot16
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot21.PWSlot21 import PWSlot21
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.PWSlot22 import PWSlot22
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot23.PWSlot23 import PWSlot23
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot24.PWSlot24 import PWSlot24
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.PWSlot25 import PWSlot25
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot26.PWSlot26 import PWSlot26
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot27.PWSlot27 import PWSlot27
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.PWSlot28 import PWSlot28
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot29.PWSlot29 import PWSlot29

# List to convert index of combobox to slot type
WIDGET_LIST = [
    PWSlot10,
    PWSlot11,
    PWSlot12,
    PWSlot13,
    PWSlot14,
    PWSlot15,
    PWSlot16,
    PWSlot21,
    PWSlot22,
    PWSlot23,
    PWSlot24,
    PWSlot25,
    PWSlot26,
    PWSlot27,
    PWSlot28,
    PWSlot29,
]
INIT_INDEX = [wid.slot_type for wid in WIDGET_LIST]
SLOT_NAME = [wid.slot_name for wid in WIDGET_LIST]


class SWSlot(Gen_SWSlot, QWidget):
    """Step to set the slot with winding
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for DMachineSetup nav
    step_name = "Slot"

    def __init__(self, machine, matlib=[], is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWSlot
            A SWSlot widget
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
        self.matlib = matlib
        self.is_stator = is_stator

        self.b_help.url = "https://eomys.com/produits/manatee/howtos/article/"
        self.b_help.url += "how-to-set-up-the-slots"

        # Fill the combobox with the available slot
        self.c_slot_type.clear()
        for slot in SLOT_NAME:
            self.c_slot_type.addItem(slot)
        # Avoid erase all the parameters when navigating though the slots
        self.previous_slot = dict()
        for slot_type in INIT_INDEX:
            self.previous_slot[slot_type] = None

        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor

        # If the Slot is not set, initialize it with a 1_0
        if self.obj.slot is None or type(self.obj.slot) in [SlotWind, Slot]:
            self.obj.slot = SlotW10()
            self.obj.slot._set_None()

        if self.obj.slot.Zs is None:
            self.si_Zs.clear()
        else:
            self.si_Zs.setValue(self.obj.slot.Zs)

        self.set_slot_pitch(self.obj.slot.Zs)

        # Set the correct index for the type checkbox and display the object
        index = INIT_INDEX.index(type(self.obj.slot))
        self.c_slot_type.setCurrentIndex(index)

        # Update the slot widget
        self.s_update_slot()

        # Connect the slot
        self.c_slot_type.currentIndexChanged.connect(self.s_change_slot)
        self.si_Zs.editingFinished.connect(self.set_Zs)
        self.b_plot.clicked.connect(self.s_plot)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup
        """
        self.saveNeeded.emit()

    def set_slot_type(self, index):
        """Initialize self.obj with the slot corresponding to index

        Parameters
        ----------
        self : SWSlot 
            A SWSlot object
        index : int
            Index of the selected slot type in the list
        """

        # Save the slot
        self.previous_slot[type(self.obj.slot)] = self.obj.slot

        # Call the corresponding constructor
        Zs = self.obj.slot.Zs
        if self.previous_slot[INIT_INDEX[index]] is None:
            # No previous slot of this type
            self.obj.slot = INIT_INDEX[index]()
            self.obj.slot._set_None()  # No default value
            self.obj.slot.Zs = Zs
        else:  # Load the previous slot of this type
            self.obj.slot = self.previous_slot[INIT_INDEX[index]]
            if self.obj.slot.Zs is not None:
                # Update Zs without trying to compute output
                self.si_Zs.blockSignals(True)
                self.si_Zs.setValue(self.obj.slot.Zs)
                self.si_Zs.blockSignals(False)

                self.set_slot_pitch(self.obj.slot.Zs)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Zs(self):
        """Signal to update the value of Zs according to the spinbox

        Parameters
        ----------
        self : SWSlot 
            A SWSlot object
        """
        value = self.si_Zs.value()
        self.obj.slot.Zs = value
        self.set_slot_pitch(value)
        self.w_slot.w_out.comp_output()

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_slot_pitch(self, Zs):
        """Update out_slot_pitch with the correct value

        Parameters
        ----------
        self : SWSlot 
            A SWSlot object
        Zs : int
            The current value of Zs
        """
        sp_txt = self.tr("Slot pitch = 360 / Zs = ")

        if Zs in [None, 0]:
            self.out_Slot_pitch.setText(sp_txt + "?")
        else:
            Slot_pitch = 360.0 / Zs
            Slot_pitch_rad = Slot_pitch * pi / 180

            self.out_Slot_pitch.setText(
                sp_txt
                + "%.4g" % (Slot_pitch)
                + u" ° ("
                + "%.4g" % (Slot_pitch_rad)
                + " rad)"
            )

    def s_update_slot(self):
        """Update the slot widget

        Parameters
        ----------
        self : SWSlot
            A SWSlot object
        """

        # Regenerate the pages with the new values
        self.w_slot.setParent(None)
        self.w_slot = WIDGET_LIST[self.c_slot_type.currentIndex()](self.obj)
        self.w_slot.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_slot)
        self.main_layout.insertWidget(1, self.w_slot)

    def s_change_slot(self, index):
        """Signal to update the slot object and widget

        Parameters
        ----------
        self : SWSlot
            A SWSlot object
        index : int
            Current index of the combobox
        """
        # Current slot is removed and replaced by the new one
        self.set_slot_type(index)
        self.s_update_slot()

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : SWSlot
            A SWSlot object
        """
        # We have to make sure the slot is right before truing to plot it
        error = self.check(self.obj)

        if error:  # Error => Display it
            QMessageBox().critical(self, self.tr("Error"), error)
        else:  # No error => Plot the slot (No winding for LamSquirrelCage)
            if self.machine.type_machine == 10:
                # For SRM, this is the last step => Plot the complete machine
                self.machine.plot()
            else:
                self.obj.plot(is_lam_only=not (type(self.obj) is LamSlotWind))

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.Zs is None:
            return "You must set Zs !"

        # Call the check method of the slot (every slot type have a
        # different check method)
        index = INIT_INDEX.index(type(lam.slot))
        return WIDGET_LIST[index].check(lam)
