# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QMessageBox, QWidget, QListView
from logging import getLogger
from .....loggers import GUI_LOG_NAME
from .....Classes.Slot import Slot
from .....Classes.SlotM10 import SlotM10
from .....Classes.LamSlotMagNS import LamSlotMagNS
from .....Classes.LamSlotMag import LamSlotMag
from .....Methods.Slot.Slot import SlotCheckError
from .....GUI.Dialog.DMachineSetup.SMSlot.WSlotMag.WSlotMag import WSlotMag
from .....GUI.Dialog.DMachineSetup.SMSlot.Ui_SMSlot import Ui_SMSlot
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot12.PMSlot12 import PMSlot12
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot13.PMSlot13 import PMSlot13
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot14.PMSlot14 import PMSlot14
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot15.PMSlot15 import PMSlot15
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot16.PMSlot16 import PMSlot16
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.PMSlot17 import PMSlot17
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot18.PMSlot18 import PMSlot18
from .....GUI.Dialog.DMachineSetup.SMSlot.PMSlot19.PMSlot19 import PMSlot19
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from .....Functions.GUI.log_error import log_error

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


class SMSlot(Ui_SMSlot, QWidget):
    """Step to set the slot with magnet"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Magnet"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SMSlot
            A SMSlot widget
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
        self.is_test = False  # To skip show fig for tests
        self.test_err_msg = None  # To test the error messages

        # Get the correct object to set
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor
        # Set default values
        if isinstance(self.obj, LamSlotMag):
            if self.obj.magnet.Nseg is None:
                self.obj.magnet.Nseg = 1
        elif isinstance(self.obj, LamSlotMagNS):
            if self.obj.magnet_north.Nseg is None:
                self.obj.magnet_north.Nseg = 1
            if self.obj.magnet_south.Nseg is None:
                self.obj.magnet_south.Nseg = 1

        if isinstance(self.obj, LamSlotMag):
            self.c_NS_type.setCurrentIndex(0)
            # If the Slot is not set, initialize it with a SlotM10
            if self.obj.slot is None or type(self.obj.slot) is Slot:
                self.obj.slot = SlotM10()
                self.obj.slot._set_None()
        elif isinstance(self.obj, LamSlotMagNS):
            self.c_NS_type.setCurrentIndex(1)
            # If the Slot are not set, initialize them with a SlotM10
            if self.obj.slot is None or type(self.obj.slot) is Slot:  # north slot
                self.obj.slot = SlotM10()
                self.obj.slot._set_None()
            if self.obj.slot_south is None or type(self.obj.slot_south) is Slot:
                self.obj.slot_south = SlotM10()
                self.obj.slot_south._set_None()

        # Initialize tab widget
        self.update_tab()

        self.set_slot_pitch(self.obj.slot.Zs)

        # Set Help URL
        self.b_help.hide()

        # Connect the slot
        self.c_NS_type.currentIndexChanged.connect(self.set_lam_type)
        self.b_plot.clicked.connect(self.s_plot)

    def update_tab(self):
        """Update the tab widget with one or two tabs

        Parameters
        ----------
        self : SMSlot
            a SMSlot object
        """
        self.tab_slot.clear()  # remove previous tabs
        if isinstance(self.obj, LamSlotMag):  # one pole
            tab = WSlotMag(lam=self.obj, material_dict=self.material_dict)
            tab.saveNeeded.connect(self.emit_save)
            self.tab_slot.addTab(tab, "Pole")
        elif isinstance(self.obj, LamSlotMagNS):  # two poles
            # Adding north pole
            lam_north = LamSlotMag(init_dict=self.obj.as_dict())
            lam_north.slot = self.obj.slot
            lam_north.magnet = self.obj.magnet_north
            tab_north = WSlotMag(
                lam=lam_north,
                material_dict=self.material_dict,
            )
            tab_north.typeSlotShanged.connect(self.update_slot_type)
            tab_north.saveNeeded.connect(self.emit_save)
            self.tab_slot.addTab(tab_north, "North Pole")
            # Adding south pole
            lam_south = LamSlotMag(init_dict=self.obj.as_dict())
            lam_south.slot = self.obj.slot_south
            lam_south.magnet = self.obj.magnet_south
            tab_south = WSlotMag(
                lam=lam_south,
                material_dict=self.material_dict,
            )
            tab_south.typeSlotShanged.connect(self.update_slot_type)
            tab_south.saveNeeded.connect(self.emit_save)
            self.tab_slot.addTab(tab_south, "South Pole")
        self.tab_slot.setCurrentIndex(0)
        if self.obj.slot.Zs is not None:
            self.set_slot_pitch(self.obj.slot.Zs)

    def update_slot_type(self):
        """Update the slot in the lamination when it changed in tab (for uneven case only)

        Parameters
        ----------
        self : SMSlot
            a SMSlot object
        """
        if not isinstance(self.obj, LamSlotMagNS):
            return

        if self.tab_slot.currentIndex() == 0:  # north pole
            self.obj.slot = self.tab_slot.currentWidget().lam.slot
        else:  # south pole
            self.obj.slot_south = self.tab_slot.currentWidget().lam.slot

    def set_lam_type(self):
        "Update the type of lamination according to the combobox to allow/disallow uneven pole pairs"

        # From even to uneven
        if self.c_NS_type.currentIndex() == 1:
            if not isinstance(self.obj, LamSlotMagNS):
                # Keeping the same slot if switching from even to uneven
                previous_slot = self.obj.slot
                # Keeping the same magnet if switching from even to uneven
                previous_magnet = self.obj.magnet
                # Changing the class of the lamination to have uneven pole pairs
                self.obj = LamSlotMagNS(init_dict=self.obj.as_dict())
                # Updating slots and magnets of the lamination
                self.obj.slot = previous_slot.copy()  # north slot
                self.obj.slot_south = previous_slot.copy()
                self.obj.magnet_north = previous_magnet.copy()
                self.obj.magnet_south = previous_magnet.copy()

                self.emit_save()

            # if slots are not set, initialize them with a North SlotM10 and a South SlotM10
            if self.obj.slot is None:
                self.obj.slot = SlotM10()
            if self.obj.slot_south is None:
                self.obj.slot_south = SlotM10()

        # From uneven to even
        else:
            if not isinstance(self.obj, LamSlotMag):
                # Keeping the north slot
                previous_slot = self.obj.slot
                # Keeping the north magnet
                previous_magnet = self.obj.magnet_north
                # Changing the class of the lamination to have even pole pairs
                self.obj = LamSlotMag(init_dict=self.obj.as_dict())
                # Updating slot and magnet of the lamination
                self.obj.slot = previous_slot.copy()
                self.obj.magnet = previous_magnet.copy()

                self.emit_save()

            # # If the slot is not set, initialize it with a SlotM10
            if self.obj.slot is None:
                self.obj.slot = SlotM10()
        # Updating the lamination
        if self.is_stator:
            self.machine.stator = self.obj
        else:
            self.machine.rotor = self.obj
        # Updating tab widget
        self.update_tab()

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
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
            + " [°] ("
            + "%.4g" % (Slot_pitch_rad)
            + " [rad])"
        )

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : SMSlot
            A SMSlot object
        """
        # We have to make sure the slot is right before trying to plot it
        error = self.check(self.obj)
        if self.obj.is_stator:
            name = "Stator"
        else:
            name = "Rotor"

        if error:  # Error => Display it
            self.test_err_msg = "Error in " + name + " Slot definition:\n" + error
            getLogger(GUI_LOG_NAME).debug(self.test_err_msg)
            QMessageBox().critical(self, self.tr("Error"), self.test_err_msg)
        else:  # No error => Plot the lamination
            try:
                self.obj.plot(is_show_fig=not self.is_test, is_add_arrow=True)
                set_plot_gui_icon()
            except Exception as e:
                if self.is_stator:
                    self.test_err_msg = (
                        "Error while plotting Lamination in Stator Magnet step:\n"
                        + str(e)
                    )
                else:
                    self.test_err_msg = (
                        "Error while plotting Lamination in Rotor Magnet step:\n"
                        + str(e)
                    )
                log_error(self, self.test_err_msg)

    @staticmethod
    def check(lamination):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        self: SMSlot
            A SMSlot object

        lamination: Lamination
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        err_msg = None
        if isinstance(lamination, LamSlotMag):  # even case
            # Check that the slot is correctly set
            try:
                index = INIT_INDEX.index(type(lamination.slot))
                err_msg = WIDGET_LIST[index].check(lamination)
                if err_msg is not None:
                    return err_msg
            except SlotCheckError as error:
                return str(error)
        elif isinstance(lamination, LamSlotMagNS):  # uneven case
            # Check that the slot for the north pole is correctly set
            try:
                index = INIT_INDEX.index(type(lamination.slot))
                err_msg = WIDGET_LIST[index].check(lamination)
                if err_msg is not None:
                    return f"North Pole: {err_msg}"
            except SlotCheckError as error:
                return f"North Pole: {error}"
            # Check that the slot for the south pole is correctly set
            try:
                # Create a LamSlotMag with the south pole of lamination
                lamination_south = LamSlotMag(init_dict=lamination.as_dict())
                lamination_south.slot = lamination.slot_south
                lamination_south.magnet = lamination.magnet_south
                index = INIT_INDEX.index(type(lamination_south.slot))
                err_msg = WIDGET_LIST[index].check(lamination_south)
                if err_msg is not None:
                    return f"South Pole: {err_msg}"
            except SlotCheckError as error:
                return f"South Pole: {error}"
