# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget

from .....Classes.LamSlotWind import LamSlotWind
from .....Classes.Slot import Slot
from .....Classes.SlotW60 import SlotW60
from .....Classes.SlotW61 import SlotW61
from .....Classes.SlotW62 import SlotW62
from .....Classes.SlotW63 import SlotW63
from .....Classes.SlotW29 import SlotW29
from .....Classes.Slot import Slot
from .....GUI.Dialog.DMachineSetup.SWPole.PWSlot60.PWSlot60 import PWSlot60
from .....GUI.Dialog.DMachineSetup.SWPole.PWSlot61.PWSlot61 import PWSlot61
from .....GUI.Dialog.DMachineSetup.SWPole.PWSlot62.PWSlot62 import PWSlot62
from .....GUI.Dialog.DMachineSetup.SWPole.PWSlot63.PWSlot63 import PWSlot63
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot29.PWSlot29 import PWSlot29
from .....GUI.Dialog.DMachineSetup.SWPole.Ui_SWPole import Ui_SWPole
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon

# List to convert index of combobox to slot type
INIT_INDEX = [SlotW60, SlotW61, SlotW62, SlotW63, SlotW29]
NAME_INDEX = [slot.__name__ for slot in INIT_INDEX]
WIDGET_LIST = [PWSlot60, PWSlot61, PWSlot62, PWSlot63, PWSlot29]


class SWPole(Ui_SWPole, QWidget):
    """Step to set the lamination pole (for WRSM)"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup
    step_name = "Pole"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWPole
            A SWPole widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.material_dict = material_dict
        self.is_stator = is_stator
        self.test_err_msg = None  # To check the error messages in test

        self.b_help.hide()

        # Avoid erase all the parameters when navigating though the slots
        self.previous_slot = {
            SlotW60: None,
            SlotW61: None,
            SlotW62: None,
            SlotW63: None,
            SlotW29: None,
        }

        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor

        # If the Slot is not set, initialize it with a SlotW60
        if self.obj.slot is None or type(self.obj.slot) not in INIT_INDEX:
            self.obj.slot = SlotW60()
            self.obj.slot._set_None()

        # Avoid error when loading WRSM with wrong rotor slot
        if type(self.obj.slot) not in INIT_INDEX:
            self.obj.slot = SlotW60()
            self.obj.slot._set_None()

        self.obj.slot.Zs = self.obj.winding.p * 2
        self.update_slot_text(self.obj.slot.Zs)

        # Set the correct index for the type checkbox
        index = NAME_INDEX.index(type(self.obj.slot).__name__)
        self.c_slot_type.setCurrentIndex(index)

        # Update the slot widget
        self.s_update_slot()

        # Connect the slot/signal
        self.c_slot_type.currentIndexChanged.connect(self.s_change_slot)
        self.b_plot.clicked.connect(self.s_plot)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_slot_type(self, index):
        """Initialize self.obj with the slot corresponding to index

        Parameters
        ----------
        self : SWPole
            A SWPole object
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

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_slot_text(self, Zs):
        """Update in_Zs and out_slot_pitch with the correct value

        Parameters
        ----------
        self : SWPole
            A SWPole object
        Zs : int
            The current value of Zs
        """
        sp_txt = self.tr("Slot pitch: 360 / Zs = ")
        self.in_Zs.setText("Zs: 2*p = " + str(Zs))

        if Zs in [None, 0]:
            self.out_Slot_pitch.setText(sp_txt + "?")
        else:
            Slot_pitch = 360.0 / Zs
            Slot_pitch_rad = Slot_pitch * pi / 180

            self.out_Slot_pitch.setText(
                sp_txt
                + "%.4g" % (Slot_pitch)
                + " [°] ("
                + "%.4g" % (Slot_pitch_rad)
                + " [rad])"
            )

    def s_update_slot(self):
        """Update the slot widget

        Parameters
        ----------
        self : SWPole
            a SWPole object
        """

        # Regenerate the pages with the new values
        self.w_slot.setParent(None)
        self.w_slot = WIDGET_LIST[self.c_slot_type.currentIndex()](self.obj)
        self.w_slot.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_slot)
        self.main_layout.insertWidget(1, self.w_slot)

    def s_change_slot(self, index):
        """Signal to update the interface and show a specific page

        Parameters
        ----------
        self : SWPole
            a SWPole object
        index : int
            Index of w_page_stack to show
        """
        # Current slot is removed and replaced by the new one
        self.set_slot_type(index)
        self.s_update_slot()

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : SWPole
            A SWPole object
        """
        # We have to make sure the slot is right before trying to plot it
        error = self.check(self.obj)

        if error:  # Error => Display it
            self.test_err_msg = error
            QMessageBox().critical(self, self.tr("Error"), self.test_err_msg)
        else:  # No error => Plot the lamination
            self.obj.plot()
            set_plot_gui_icon()

    @staticmethod
    def check(lam):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lam : Lamination
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)

        """

        # Call the check method of the slot (every slot type have a
        # different check method)
        try:
            index = INIT_INDEX.index(type(lam.slot))
            return WIDGET_LIST[index].check(lam)
        except Exception as e:
            return str(e)
