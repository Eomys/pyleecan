# -*- coding: utf-8 -*-

from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QMessageBox, QWidget, QApplication
from numpy import pi, floor
import matplotlib.pyplot as plt
from logging import getLogger

from .....Functions.Load.import_class import import_class
from .....loggers import GUI_LOG_NAME
from .....Classes.LamSlotWind import LamSlotWind
from .....Classes.LamSquirrelCage import LamSquirrelCage
from .....Classes.Slot import Slot
from .....Classes.SlotUD import SlotUD
from .....Classes.SlotUD2 import SlotUD2
from .....Classes.Slot import Slot
from .....Classes.LamSquirrelCage import LamSquirrelCage
from .....GUI.Dialog.DMachineSetup.SWSlot.Gen_SWSlot import Gen_SWSlot
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlotUD.PWSlotUD import PWSlotUD
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot10.PWSlot10 import PWSlot10
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot11.PWSlot11 import PWSlot11
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot12.PWSlot12 import PWSlot12
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot13.PWSlot13 import PWSlot13
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.PWSlot14 import PWSlot14
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot15.PWSlot15 import PWSlot15
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot16.PWSlot16 import PWSlot16
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot21.PWSlot21 import PWSlot21
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.PWSlot22 import PWSlot22
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot23.PWSlot23 import PWSlot23
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot24.PWSlot24 import PWSlot24
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.PWSlot25 import PWSlot25
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot26.PWSlot26 import PWSlot26
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot27.PWSlot27 import PWSlot27
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.PWSlot28 import PWSlot28
from .....GUI.Dialog.DMachineSetup.SWSlot.PWSlot29.PWSlot29 import PWSlot29
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon

# List to convert index of combobox to slot type
WIDGET_LIST = [
    PWSlotUD,
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
    """Step to set the slot with winding"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Slot"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWSlot
            A SWSlot widget
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
        self.is_test = False  # To avoid call to show in plot
        self.test_err_msg = None  # To store error message for testing

        self.b_help.hide()

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
            self.out_Slot_pitch.setText(self.out_Slot_pitch.text().replace("Zs", "Zr"))
            self.in_Zs.setText(self.in_Zs.text().replace("Zs", "Zr"))

        # If the Slot is not set, initialize it with a UD
        if self.obj.slot is None or type(self.obj.slot) is Slot:
            self.obj.slot = SlotUD()
            self.obj.slot._set_None()

        if self.obj.slot.Zs is None:
            self.si_Zs.clear()
        else:
            self.si_Zs.setValue(self.obj.slot.Zs)

        self.set_slot_pitch(self.obj.slot.Zs)

        # Set the correct index for the type checkbox and display the object
        if isinstance(self.obj.slot, SlotUD2):
            index = 0
        else:
            index = INIT_INDEX.index(type(self.obj.slot))
        self.c_slot_type.setCurrentIndex(index)

        # Update the slot widget
        self.s_update_slot()

        # Connect the slot
        self.c_slot_type.currentIndexChanged.connect(self.s_change_slot)
        self.si_Zs.valueChanged.connect(self.set_Zs)
        self.b_plot.clicked.connect(self.s_plot)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
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
        wedge_mat = self.obj.slot.wedge_mat
        if self.previous_slot[INIT_INDEX[index]] is None:
            # No previous slot of this type
            self.obj.slot = INIT_INDEX[index]()
            self.obj.slot._set_None()  # No default value
            self.obj.slot.Zs = Zs
            self.obj.slot.wedge_mat = wedge_mat
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
        # Clear previous winding matrix (if needed)
        if hasattr(self.obj, "winding"):
            self.obj.winding.clean()
        # If we are working on a SCIM then we also need to update the value of qs
        if isinstance(self.obj, LamSquirrelCage):
            self.obj.winding.qs = value

        self.set_slot_pitch(value)
        self.w_slot.w_out.comp_output()
        if isinstance(self.w_slot, PWSlotUD):
            self.w_slot.update_graph()

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
        sp_txt = self.tr("Slot pitch: 360 / Zs = ")

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
        self : SWSlot
            A SWSlot object
        """

        # Regenerate the pages with the new values
        self.w_slot.setParent(None)
        self.w_slot = WIDGET_LIST[self.c_slot_type.currentIndex()](
            self.obj, material_dict=self.material_dict
        )
        self.w_slot.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_slot)
        self.main_layout.insertWidget(1, self.w_slot)
        # Update Zs for PWSlotUD
        if isinstance(self.w_slot, PWSlotUD):
            self.w_slot.ZsChanged.connect(self.set_Zs_UD)

    def set_Zs_UD(self):
        self.si_Zs.blockSignals(True)
        self.obj.slot = self.w_slot.slot  # Update pointer
        self.si_Zs.setValue(self.obj.slot.Zs)
        self.si_Zs.blockSignals(False)

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
                self.obj.plot(
                    is_lam_only=not (type(self.obj) is LamSlotWind),
                    is_show_fig=not self.is_test,
                )
                set_plot_gui_icon()
            except Exception as e:
                if self.is_stator:
                    self.test_err_msg = (
                        "Error while plotting Lamination in Stator Slot step:\n"
                        + str(e)
                    )
                else:
                    self.test_err_msg = (
                        "Error while plotting Lamination in Rotor Slot step:\n" + str(e)
                    )
                getLogger(GUI_LOG_NAME).error(self.test_err_msg)
                QMessageBox().warning(
                    self,
                    self.tr("Error while plotting"),
                    self.tr(self.test_err_msg),
                )

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
        try:
            # Check that everything is set
            if lam.slot.Zs is None:
                return "You must set Zs !"

            # Call the check method of the slot (every slot type have a
            # different check method)
            if isinstance(lam.slot, SlotUD2):
                index = 0
            else:
                index = INIT_INDEX.index(type(lam.slot))
            return WIDGET_LIST[index].check(lam)
        except Exception as e:
            return str(e)
