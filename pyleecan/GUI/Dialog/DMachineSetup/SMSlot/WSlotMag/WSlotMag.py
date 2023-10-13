# -*- coding: utf-8 -*-


from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget, QListView


from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot12.PMSlot12 import PMSlot12
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot13.PMSlot13 import PMSlot13
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot14.PMSlot14 import PMSlot14
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot15.PMSlot15 import PMSlot15
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot16.PMSlot16 import PMSlot16
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.PMSlot17 import PMSlot17
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot18.PMSlot18 import PMSlot18
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot19.PMSlot19 import PMSlot19
from ......GUI.Dialog.DMachineSetup.SMSlot.WSlotMag.Ui_WSlotMag import Ui_WSlotMag

# List to convert index of combobox to slot type
WIDGET_LIST = [
    PMSlot10,
    PMSlot11,
    PMSlot12,
    PMSlot13,
    PMSlot14,
    PMSlot15,
    PMSlot16,
    PMSlot17,
    PMSlot18,
    PMSlot19,
]
INIT_INDEX = [wid.slot_type for wid in WIDGET_LIST]
SLOT_NAME = [wid.slot_name for wid in WIDGET_LIST]


class WSlotMag(Ui_WSlotMag, QWidget):
    """Widget to Setup a slot"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Signal to SMSLotMag to know that a slot has changed
    typeSlotShanged = Signal()

    def __init__(self, lam, material_dict):
        """Initialize the GUI according to lamination

        Parameters
        ----------
        self : WSlotMag
            A WSlotMag object
        lam : LamSlotMag
            the lamination to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.is_stator = False
        self.lam = lam
        self.material_dict = material_dict
        self.wid_list = WIDGET_LIST

        # Fill the combobox with the available slots
        listView = QListView(self.c_slot_type)
        self.c_slot_type.clear()
        self.c_slot_type.setView(listView)
        for slot in SLOT_NAME:
            self.c_slot_type.addItem(slot)
        # Avoid erase all the parameters when navigating though the slots
        self.previous_slot = dict()
        for slot_type in INIT_INDEX:
            self.previous_slot[slot_type] = None

        # Set the correct index for the type checkbox and display the object
        index = INIT_INDEX.index(type(self.lam.slot))
        self.c_slot_type.setCurrentIndex(index)

        # Regenerate the pages with the new values
        self.w_slot.setParent(None)
        self.w_slot = self.wid_list[self.c_slot_type.currentIndex()](
            lamination=self.lam, material_dict=self.material_dict
        )
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_slot)
        self.main_layout.insertWidget(1, self.w_slot)

        # Connect the slot
        self.c_slot_type.currentIndexChanged.connect(self.s_change_slot)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_slot_type(self, c_index):
        """Initialize self.lam with the slot corresponding to index

        Parameters
        ----------
        self : WSlotMag
            A WSlotMag object
        c_index : int
            Index of the selected slot in the combobox
        """

        # Save the slot
        self.previous_slot[type(self.lam.slot)] = self.lam.slot

        # Call the corresponding constructor
        Zs = self.lam.slot.Zs
        if self.previous_slot[INIT_INDEX[c_index]] is None:
            # No previous slot of this type
            self.lam.slot = INIT_INDEX[c_index]()
            self.lam.slot._set_None()  # No default value
            self.lam.slot.Zs = Zs
        else:  # Load the previous slot of this type
            self.lam.slot = self.previous_slot[INIT_INDEX[c_index]]

        # Notify SMSlot that the slot changed
        self.typeSlotShanged.emit()

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_update_slot(self):
        """Update the slot widget

        Parameters
        ----------
        self : WSlotMag
            A WSlotMag object
        """

        # Regenerate the pages with the new values
        self.w_slot.setParent(None)
        self.w_slot = WIDGET_LIST[self.c_slot_type.currentIndex()](
            self.lam, material_dict=self.material_dict
        )
        self.w_slot.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_slot)
        self.main_layout.insertWidget(2, self.w_slot)

    def s_change_slot(self, index):
        """Signal to update the slot object and widget

        Parameters
        ----------
        self : WSlotMag
            A WSlotMag object
        index : int
            Current index of the combobox
        """
        # Current slot is removed and replaced by the new one
        self.set_slot_type(index)
        self.s_update_slot()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : WSlotMag
            A WSlotMag widget

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        return self.w_slot.check()
