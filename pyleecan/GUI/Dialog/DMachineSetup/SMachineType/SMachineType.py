# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QWidget

from .....GUI.Dialog.DMachineSetup.SMachineType.Gen_SMachineType import Gen_SMachineType
from .....Classes.Winding import Winding
from .....Classes.MachineSRM import MachineSRM
from .....Classes.MachineWRSM import MachineWRSM
from .....definitions import PACKAGE_NAME


class SMachineType(Gen_SMachineType, QWidget):
    """First Step to setup the Machine Type"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for the DMachineSetup nav
    step_name = "Machine Type"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SMachineType
            A SMachineType widget
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

        # Dynamic import to avoid import loop
        module = __import__(
            PACKAGE_NAME + ".GUI.Dialog.DMachineSetup", fromlist=["DMachineSetup"]
        )
        self.mach_list = getattr(module, "mach_list")
        self.mach_index = getattr(module, "mach_index")

        # Fill the combobox
        self.c_type.clear()
        self.c_type.addItems(
            [self.mach_dict["name"] for self.mach_dict in self.mach_list]
        )
        # Update the GUI to the current machine type
        index = self.mach_index.index(type(self.machine))
        self.mach_dict = self.mach_list[index]
        self.img_type_machine.setPixmap(QPixmap(self.mach_dict["img"]))
        # Initialize the machine description
        if machine.desc not in [None, ""]:
            self.in_machine_desc.setPlainText(machine.desc)
        else:
            self.in_machine_desc.setPlaceholderText(self.mach_dict["txt"])
        self.c_type.setCurrentIndex(index)
        if isinstance(self.machine, MachineSRM):
            # p is not meaningful for SRM
            self.si_p.hide()
            self.in_p.hide()
        elif machine.stator.get_pole_pair_number() is not None:
            self.si_p.setValue(machine.stator.winding.p)
        else:
            self.si_p.clear()  # Empty spinbox

        # Set default values
        self.machine.stator.is_stator = True
        self.machine.rotor.is_stator = False

        if machine.rotor.is_internal is None:
            self.machine.rotor.is_internal = True
            self.machine.stator.is_internal = False
            self.c_topology.setCurrentText("Internal Rotor")
        elif machine.rotor.is_internal:
            self.c_topology.setCurrentText("Internal Rotor")
        else:
            self.c_topology.setCurrentText("External Rotor")

        # WRSM can only have Internal Rotor
        if self.machine.type_machine == 9:
            self.c_topology.setEnabled(False)
        else:
            self.c_topology.setEnabled(True)

        if machine.name not in [None, ""]:
            self.le_name.setText(machine.name)

        # Connect the slot/signal
        self.si_p.valueChanged.connect(self.set_p)
        self.c_topology.currentIndexChanged.connect(self.set_inner_rotor)
        self.le_name.editingFinished.connect(self.s_set_name)
        self.in_machine_desc.textChanged.connect(self.set_desc)
        self.c_type.currentIndexChanged.connect(self.set_machine_type)

    def set_desc(self):
        """Set the description of the machine

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        """
        self.machine.desc = self.in_machine_desc.toPlainText()
        self.saveNeeded.emit()

    def s_set_name(self):
        """Set the name of the machine

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        """
        self.machine.name = str(self.le_name.text())
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_p(self):
        """Signal to update the value of p according to the spinbox

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        """
        value = self.si_p.value()
        if self.machine.stator.winding is None:
            self.machine.stator.winding = Winding()
            self.machine.stator.winding._set_None()
        else:
            # If a winding is defined, clearing it as it will have to be re-generated
            self.machine.stator.winding.clean()

        self.machine.set_pole_pair_number(value)
        if isinstance(self.machine, MachineWRSM):
            self.machine.rotor.slot.Zs = value

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_inner_rotor(self):
        """Signal to update the value of is_internal according to the widget

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        is_checked : bool
            State of is_internal
        """
        self.machine.stator.is_internal = (
            not self.c_topology.currentText() == "Internal Rotor"
        )
        self.machine.rotor.is_internal = (
            self.c_topology.currentText() == "Internal Rotor"
        )
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_machine_type(self, index):
        """Change the machine type according to the combobox

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        index : int
            Selected machine type index
        """
        p = self.machine.stator.get_pole_pair_number()
        # Get the correct machine class
        mach = self.mach_list[index]["init_machine"]
        self.machine = type(mach)(init_dict=mach.as_dict())
        self.in_machine_desc.setPlaceholderText(self.mach_list[index]["txt"])
        if p is not None:
            self.si_p.setValue(p)
            self.set_p()
        # Update the GUI with the new machine
        self.parent().machine = self.machine
        self.parent().update_nav(next_step=0)
        if self.parent() is not None:
            self.parent().main_layout.removeWidget(self)

    @staticmethod
    def check(machine):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        machine : Machine
            Machine to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        try:
            if machine.stator.winding is None:
                return "Missing stator winding"
            if not isinstance(
                machine, MachineSRM
            ) and machine.stator.get_pole_pair_number() in [None, 0]:
                return "p must be >0 !"
            if machine.name in [None, ""]:
                return "name of the machine is missing"
        except Exception as e:
            return str(e)
