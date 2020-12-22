# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget

from .....Classes.LamSlotWind import LamSlotWind
from .....Classes.Slot import Slot
from .....Classes.SlotM10 import SlotM10
from .....Classes.SlotWind import SlotWind
from .....GUI.Dialog.DMachineSetup.SMSlot.Ui_SMSlot import Ui_SMSlot
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot12.PMSlot12 import PMSlot12
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot13.PMSlot13 import PMSlot13
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot14.PMSlot14 import PMSlot14

# List to convert index of combobox to slot type
WIDGET_LIST = [
    PMSlot10,
    PMSlot11,
    PMSlot12,
    PMSlot13,
    PMSlot14,
]
INIT_INDEX = [wid.slot_type for wid in WIDGET_LIST]
SLOT_NAME = [wid.slot_name for wid in WIDGET_LIST]


class SMSlot(Ui_SMSlot, QWidget):
    """Step to set the slot with winding"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Magnet"

    def __init__(self, machine, matlib, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SMSlot
            A SMSlot widget
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
            self.obj.slot = SlotM10()
            self.obj.slot._set_None()

        self.set_slot_pitch(self.obj.slot.Zs)

        # Set magnetization
        if self.obj.magnet.type_magnetization not in [0, 1, 2]:
            self.obj.magnet.type_magnetization = 0  # Set default value
        self.c_type_magnetization.setCurrentIndex(self.obj.magnet.type_magnetization)

        # Set material
        self.w_mat.setText(self.tr("mat_mag:"))
        self.w_mat.def_mat = "Magnet1"
        self.w_mat.update(self.machine.rotor.magnet, "mat_type", self.matlib)

        # Set the correct index for the type checkbox and display the object
        index = INIT_INDEX.index(type(self.obj.slot))
        self.c_slot_type.setCurrentIndex(index)

        # Update the slot widget
        self.s_update_slot()

        # Connect the slot
        self.c_slot_type.currentIndexChanged.connect(self.s_change_slot)
        self.c_type_magnetization.currentIndexChanged.connect(
            self.s_set_type_magnetization
        )
        self.b_plot.clicked.connect(self.s_plot)
        self.w_mat.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_slot_type(self, index):
        """Initialize self.obj with the slot corresponding to index

        Parameters
        ----------
        self : SMSlot
            A SMSlot object
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
                self.set_slot_pitch(self.obj.slot.Zs)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_slot_pitch(self, Zs):
        """Update out_slot_pitch with the correct value

        Parameters
        ----------
        self : SMSlot
            A SMSlot object
        Zs : int
            The current value of Zs
        """
        sp_txt = self.tr("p = " + str(int(Zs / 2)) + " / Slot pitch = ")

        Slot_pitch = 360.0 / Zs
        Slot_pitch_rad = Slot_pitch * pi / 180

        self.out_Slot_pitch.setText(
            sp_txt
            + "%.4g" % (Slot_pitch)
            + u" ° ("
            + "%.4g" % (Slot_pitch_rad)
            + " rad)"
        )

    def s_set_type_magnetization(self, index):
        """Signal to update the value of type_magnetization according to the combobox

        Parameters
        ----------
        self : SMagnet
            A SMagnet object
        index : int
            Current index of the combobox
        """
        self.machine.rotor.magnet.type_magnetization = index
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_update_slot(self):
        """Update the slot widget

        Parameters
        ----------
        self : SMSlot
            A SMSlot object
        """

        # Regenerate the pages with the new values
        self.w_slot.setParent(None)
        self.w_slot = WIDGET_LIST[self.c_slot_type.currentIndex()](self.obj)
        self.w_slot.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_slot)
        self.main_layout.insertWidget(2, self.w_slot)

    def s_change_slot(self, index):
        """Signal to update the slot object and widget

        Parameters
        ----------
        self : SMSlot
            A SMSlot object
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
        self : SMSlot
            A SMSlot object
        """
        # We have to make sure the slot is right before trying to plot it
        error = self.check(self.obj)

        if error:  # Error => Display it
            QMessageBox().critical(self, self.tr("Error"), error)
        else:  # No error => Plot the slot (No winding for LamSquirrelCage)
            self.obj.plot()

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamSlotMag
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        try:
            # Call the check method of the slot (every slot type have a
            # different check method)
            index = INIT_INDEX.index(type(lam.slot))
            return WIDGET_LIST[index].check(lam)
        except Exception as e:
            return str(e)
