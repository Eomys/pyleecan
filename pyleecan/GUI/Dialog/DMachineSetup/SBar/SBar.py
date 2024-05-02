# -*- coding: utf-8 -*-


from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget, QListView

from .....GUI import gui_option
from .....GUI.Dialog.DMachineSetup.SBar.Gen_SBar import Gen_SBar
from .....GUI.Dialog.DMachineSetup.SBar.PCondType21.PCondType21 import PCondType21
from .....GUI.Dialog.DMachineSetup.SBar.PCondType22.PCondType22 import PCondType22
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from .....Functions.GUI.log_error import log_error

# Information to fill the conductor type combobox
WIDGET_LIST = [PCondType21, PCondType22]
INIT_INDEX = [wid.cond_type for wid in WIDGET_LIST]
COND_NAME = [wid.cond_name for wid in WIDGET_LIST]


class SBar(Gen_SBar, QWidget):
    """Step to setup the Rotor Bar for SCIM machine"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for the DMachineSetup nav
    step_name = "Bar"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SBar
            A SBar widget
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

        # Set FloatEdit unit
        self.lf_Hscr.unit = "m"
        self.lf_Lscr.unit = "m"
        self.lf_Lewout.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [self.unit_Hscr, self.unit_Lscr, self.unit_Lewout]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Update winding qs
        if (
            self.machine.rotor.slot.Zs is not None
            and self.machine.rotor.winding.qs is None
        ):
            self.machine.rotor.winding.qs = self.machine.rotor.slot.Zs

        # Update winding
        if (
            self.machine.rotor.slot.Zs is not None
            and self.machine.rotor.winding.qs is None
        ):
            self.machine.rotor.winding.qs = self.machine.rotor.slot.Zs
        if self.machine.rotor.winding.Npcp is None:
            self.machine.rotor.winding.Npcp = 1
        if self.machine.rotor.winding.Ntcoil is None:
            self.machine.rotor.winding.Ntcoil = 1

        # Set materials
        self.w_mat_scr.def_mat = "Copper1"
        self.w_mat_scr.setText("Ring material")
        # self.w_mat_scr.is_hide_button = True
        self.w_mat_scr.update(self.machine.rotor, "ring_mat", self.material_dict)

        # Initialize the GUI with the current machine value
        self.lf_Hscr.setValue(machine.rotor.Hscr)
        self.lf_Lscr.setValue(machine.rotor.Lscr)
        self.lf_Lewout.setValue(machine.rotor.winding.Lewout)

        # Fill the combobox
        listView = QListView(self.c_bar_type)
        self.c_bar_type.clear()
        self.c_bar_type.setView(listView)
        for cond in COND_NAME:
            self.c_bar_type.addItem(cond)
        # Initialize the needed conductor page
        conductor = machine.rotor.winding.conductor
        if type(conductor) in INIT_INDEX:
            index = INIT_INDEX.index(type(conductor))
            self.g_bar.layout().removeWidget(self.w_bar)
            self.w_bar.setParent(None)
            self.w_bar = WIDGET_LIST[index](self.machine, self.material_dict)
            self.g_bar.layout().addWidget(self.w_bar)
            self.c_bar_type.setCurrentIndex(index)
        else:  # Set default conductor
            self.s_set_bar_type(0)
            self.c_bar_type.setCurrentIndex(0)
        self.w_bar.saveNeeded.connect(self.emit_save)

        # Connect the signal/slot
        self.lf_Hscr.editingFinished.connect(self.set_Hscr)
        self.lf_Lscr.editingFinished.connect(self.set_Lscr)
        self.lf_Lewout.editingFinished.connect(self.set_Lewout)
        self.c_bar_type.currentIndexChanged.connect(self.s_set_bar_type)
        self.b_plot.clicked.connect(self.s_plot)
        self.w_mat_scr.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Emit the saveNeeded signal"""
        self.saveNeeded.emit()

    def set_Hscr(self):
        """Signal to update the value of Hscr according to the line edit

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.rotor.Hscr = self.lf_Hscr.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Lscr(self):
        """Signal to update the value of Lscr according to the line edit

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.rotor.Lscr = self.lf_Lscr.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Lewout(self):
        """Signal to update the value of Lewout according to the line edit

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.rotor.winding.Lewout = self.lf_Lewout.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_set_bar_type(self, index):
        """Setup the Gui for the selected conductor type

        Parameters
        ----------
        self : SBar
            A SBar object
        index : int
            Index of the selected conductor type
        """
        try:
            # Remove the old widget
            self.g_bar.layout().removeWidget(self.w_bar)
            self.w_bar.setParent(None)

            # Initialize the new widget and conductor
            self.machine.rotor.winding.conductor = INIT_INDEX[index]()
            self.machine.rotor.winding.conductor._set_None()

            self.w_bar = WIDGET_LIST[index](self.machine, self.material_dict)
            self.w_bar.saveNeeded.connect(self.emit_save)
            # Refresh the GUi
            self.g_bar.layout().addWidget(self.w_bar)
            # Notify the machine GUI that the machine has changed
            self.saveNeeded.emit()
        except Exception as e:
            log_error(self, "Error while selecting bar type:\n" + str(e))

    def s_plot(self):
        """Try to plot the machine

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.plot()
        set_plot_gui_icon()

    @staticmethod
    def check(lamination):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        try:
            # Check that everything is set
            if lamination.Hscr is None:
                return "You must set Hscr !"
            elif lamination.Lscr is None:
                return "You must set Lscr !"
            elif lamination.winding.Lewout is None:
                return "You must set Lewout !"
            elif lamination.ring_mat.name is None:
                return "You must set the ring material !"
            elif lamination.winding.conductor.cond_mat is None:
                return "You must set the bar material !"

            if type(lamination.winding.conductor) is INIT_INDEX[0]:
                if lamination.winding.conductor.Hbar is None:
                    return "You must set Hbar !"
                elif lamination.winding.conductor.Wbar is None:
                    return "You must set Wbar !"
        except Exception as e:
            return str(e)
