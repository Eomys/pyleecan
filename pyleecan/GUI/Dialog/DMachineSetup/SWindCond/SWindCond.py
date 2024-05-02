# -*- coding: utf-8 -*-


from qtpy.QtCore import Signal
from qtpy.QtWidgets import QMessageBox, QWidget, QListView

from .....Classes.CondType11 import CondType11
from .....Classes.CondType12 import CondType12
from .....GUI.Dialog.DMachineSetup.SWindCond.PCondType11.PCondType11 import PCondType11
from .....GUI.Dialog.DMachineSetup.SWindCond.PCondType12.PCondType12 import PCondType12
from .....GUI.Dialog.DMachineSetup.SWindCond.Ui_SWindCond import Ui_SWindCond

# For the Conductor combobox
wid_list = [PCondType11, PCondType12]
type_list = [wid.cond_type for wid in wid_list]
name_list = [wid.cond_name for wid in wid_list]


class SWindCond(Ui_SWindCond, QWidget):
    """Step to define the winding conductor"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Conductor"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWindCond
            A SWindCond widget
        machine : Machine
            current machine to edit
        material_dict : list
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

        # Fill the fields with the machine values (if they're filled)
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor

        # Fill the combobox with the available conductor
        self.c_cond_type.clear()
        listView = QListView(self.c_cond_type)
        for cond in name_list:
            self.c_cond_type.addItem(cond)
        self.c_cond_type.setView(listView)
        # Set default conductor if conductor not set
        if (
            self.obj.winding.conductor is None
            or type(self.obj.winding.conductor) not in type_list
        ):
            # CondType11 is the default
            self.obj.winding.conductor = CondType11()
            self.obj.winding.conductor._set_None()

        # Initialize the needed conductor widget
        index = type_list.index(type(self.obj.winding.conductor))
        self.s_update(index)
        self.c_cond_type.setCurrentIndex(index)

        # Connect the widget
        self.c_cond_type.currentIndexChanged.connect(self.s_set_cond_type)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def s_set_cond_type(self, index):
        """Setup the Gui for the selected conductor type

        Parameters
        ----------
        self : SWindCond
            A SWindCond object
        index : int
            Index of the selected conductor type
        """

        # Initialize the new one and keep materials
        cond_mat = self.obj.winding.conductor.cond_mat
        ins_mat = self.obj.winding.conductor.ins_mat

        self.obj.winding.conductor = type_list[index]()
        self.obj.winding.conductor._set_None()

        self.obj.winding.conductor.cond_mat = cond_mat
        self.obj.winding.conductor.ins_mat = ins_mat
        # Update the GUI
        self.s_update(index)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_update(self, index):
        """Update the GUI to show the current conductor widget

        Parameters
        ----------
        self : SWindCond
            a SWindCond object
        index : int
            Index of the selected conductor type
        """
        # Regenerate the pages with the new values
        self.w_cond.setParent(None)
        self.w_cond = wid_list[index](self.obj, self.material_dict)
        self.w_cond.saveNeeded.connect(self.emit_save)

        # Refresh the GUI
        self.main_layout.removeWidget(self.w_cond)
        self.main_layout.insertWidget(1, self.w_cond)

    @staticmethod
    def check(lamination):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        try:
            # Call the check method of the conductor (every cond type have a
            # different check method)
            index = type_list.index(type(lamination.winding.conductor))
            return wid_list[index].check(lamination)
        except Exception as e:
            return str(e)
