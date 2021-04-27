# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QWidget

from .....Classes.Winding import Winding
from .....Classes.WindingUD import WindingUD
from .....Functions.Winding.comp_wind_periodicity import comp_wind_periodicity
from .....GUI.Dialog.DMachineSetup.SWinding.Gen_SWinding import Gen_SWinding
from .....Methods.Machine.Winding import WindingError


class SWinding(Gen_SWinding, QWidget):
    """Step to define the winding pattern & circuit"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Winding"

    def __init__(self, machine, matlib, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWinding
            A SWinding widget
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

        # Set Help URL
        self.b_help.url = "https://pyleecan.org/winding.convention.html"

        # Saving arguments
        self.machine = machine
        self.matlib = matlib
        self.is_stator = is_stator

        # Fill the fields with the machine values (if they're filled)
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor
        self.in_Zsp.setText(
            "Slot number="
            + str(self.obj.get_Zs())
            + ", Pole pair numer="
            + str(self.obj.get_pole_pair_number())
        )

        # if machine.type_machine == 9 and not self.is_stator:
        #     # Enforce tooth winding for WRSM rotor
        #     self.obj.winding = WindingCW2LT(init_dict=self.obj.winding.as_dict())
        #     self.obj.winding.qs = 1
        #     self.b_preview.setEnabled(False)
        #     self.si_qs.setEnabled(False)
        #     self.c_wind_type.setEnabled(False)
        #     self.c_wind_type.setCurrentIndex(0)

        # Set the current Winding pattern
        if self.obj.winding is None:
            self.obj.winding = Winding()
        if type(self.obj.winding) is Winding:
            self.c_wind_type.setCurrentIndex(0)
            self.stack_wind_type.setCurrentIndex(0)
            if self.obj.winding.coil_pitch is None:
                self.obj.winding.coil_pitch = 0
            self.si_coil_pitch.setValue(self.obj.winding.coil_pitch)
            if self.obj.winding.qs is None:  # default value
                self.obj.winding.qs = 3
            self.si_qs.setValue(self.obj.winding.qs)
        else:  # WindingUD
            self.c_wind_type.setCurrentIndex(0)
            self.stack_wind_type.setCurrentIndex(1)

        if self.obj.winding.is_reverse_wind is None:
            self.obj.winding.is_reverse_wind = False
        if self.obj.winding.is_reverse_wind:
            self.is_reverse.setCheckState(Qt.Checked)
        else:
            self.is_reverse.setCheckState(Qt.Unchecked)
        if self.obj.winding.Nslot_shift_wind is None:
            self.obj.winding.Nslot_shift_wind = 0
        self.si_Nslot.setValue(self.obj.winding.Nslot_shift_wind)

        # Circuit parameter setup
        if self.obj.winding.Ntcoil is None:
            self.obj.winding.Ntcoil = 1
        self.si_Ntcoil.setValue(self.obj.winding.Ntcoil)
        if self.obj.winding.Npcpp is None:
            self.obj.winding.Npcpp = 1  # Default value
        self.si_Npcpp.setValue(self.obj.winding.Npcpp)

        # Update the GUI
        self.update_graph()
        self.comp_output()

        # Connect the signal/slot
        self.c_wind_type.currentIndexChanged.connect(self.set_type)
        self.si_qs.editingFinished.connect(self.set_qs)
        self.si_coil_pitch.editingFinished.connect(self.set_coil_pitch)
        self.si_Ntcoil.editingFinished.connect(self.set_Ntcoil)
        self.si_Npcpp.editingFinished.connect(self.set_Npcp)
        self.si_Nslot.valueChanged.connect(self.set_Nslot)
        self.is_reverse.stateChanged.connect(self.set_is_reverse_wind)

        # self.b_edit_wind_mat.clicked.connect(self.s_edit_wind_mat)
        # self.b_import_csv.clicked.connect(self.s_import_csv)
        # self.b_export_csv.clicked.connect(self.s_export_csv)
        self.b_edit_wind_mat.setEnabled(False)
        self.b_import_csv.setEnabled(False)
        self.b_export_csv.setEnabled(False)
        self.b_preview.clicked.connect(self.s_plot)

    def set_type(self, index):
        """Signal to update the winding type

        Parameters
        ----------
        self : SWinding
            A SWinding object
        index : int
            Index of selected type
        """

        init_dict = self.obj.winding.as_dict()
        if index == 0:
            self.obj.winding = Winding(init_dict=init_dict)
            if self.obj.winding.coil_pitch is None:
                self.obj.winding.coil_pitch = 0
            self.si_coil_pitch.setValue(self.obj.winding.coil_pitch)
            if self.obj.winding.qs is None:  # default value
                self.obj.winding.qs = 3
            self.si_qs.setValue(self.obj.winding.qs)
            self.stack_wind_type.setCurrentIndex(0)
        else:
            self.obj.winding = WindingUD(init_dict=init_dict)
            self.stack_wind_type.setCurrentIndex(1)
        self.obj.winding.Ntcoil = self.si_Ntcoil.value()
        self.obj.winding.Npcpp = self.si_Npcpp.value()

        # Update out_shape
        self.comp_output()
        # Update image
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_qs(self):
        """Signal to update the value of qs according to the spinbox

        Parameters
        ----------
        self : SWinding
            A SWinding object
        """
        self.obj.winding.qs = self.si_qs.value()
        self.comp_output()
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_coil_pitch(self):
        """Signal to update the value of coil_pitch according to the spinbox

        Parameters
        ----------
        self : SWinding
            A SWinding object
        """
        self.obj.winding.coil_pitch = self.si_coil_pitch.value()
        self.comp_output()
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Nslot(self):
        """Signal to update the value of Nslot_shift_wind according to the
        spinbox

        Parameters
        ----------
        self : SWinding
            A SWinding object
        """
        self.obj.winding.Nslot_shift_wind = self.si_Nslot.value()
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_reverse_wind(self, value):
        """Signal to update the value of is_reverse_wind according to the
        widget

        Parameters
        ----------
        self : SWinding
            A SWinding object
        value :
            New value of is_reverse_wind
        """

        value = self.is_reverse.isChecked()
        self.update_graph()
        self.obj.winding.is_reverse_wind = value
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Ntcoil(self):
        """Signal to update the value of Ntcoil according to the line edit

        Parameters
        ----------
        self : SWindParam
            A SWindParam object
        """
        self.obj.winding.Ntcoil = self.si_Ntcoil.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Npcp(self):
        """Signal to update the value of Npcp according to the line edit

        Parameters
        ----------
        self : SWindParam
            A SWindParam object
        """
        self.obj.winding.Npcpp = self.si_Npcpp.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Update the shape and period Label to match the current winding setup

        Parameters
        ----------
        self : SWinding
            a SWinding object
        """

        wind = self.obj.winding  # For readability
        # Wind_matrix is a matrix of dimension [Nlay_rad, Nlay_tan, Zs, qs]
        # Nlay_rad and Nlay_tan depend of the winding type
        (Nrad, Ntan) = wind.get_dim_wind()
        Nlay = str(Nrad) + ", " + str(Ntan) + ", "

        # Zs should be set, but to be sure:
        if self.obj.slot.Zs is None:
            Zs = "?, "
        else:
            Zs = str(self.obj.slot.Zs) + ", "

        if wind.qs is None:
            qs = "?]"
        else:
            qs = str(wind.qs) + "]"

        self.out_shape.setText(self.tr("Matrix shape [") + Nlay + Zs + qs)

        try:
            ms = str(self.obj.slot.Zs / (wind.p * wind.qs * 2.0))
        except TypeError:  # One of the value is None
            ms = "?"
        if self.obj.is_stator:
            self.out_ms.setText(self.tr("ms = Zs / (2*p*qs) = ") + ms)
        else:
            self.out_ms.setText(self.tr("ms = Zr / (2*p*qr) = ") + ms)

        try:
            wind_mat = wind.comp_connection_mat(self.obj.slot.Zs)
            Nperw = str(comp_wind_periodicity(wind_mat)[0])
        except Exception:  # Unable to compution the connection matrix
            Nperw = "?"
        self.out_Nperw.setText(self.tr("Nperw: ") + Nperw)

        try:
            Ntspc = str(self.obj.winding.comp_Ntspc(Zs))
        except:
            Ntspc = "?"
        try:
            Ncspc = str(self.obj.winding.comp_Ncspc(Zs))
        except:
            Ncspc = "?"
        self.out_Ncspc.setText(self.tr("Ncspc: ") + Ncspc)
        self.out_Ntspc.setText(self.tr("Ntspc: ") + Ntspc)

    def update_graph(self):
        """Plot the lamination with/without the winding"""
        # Plot the lamination in the viewer fig
        try:
            self.obj.plot(fig=self.w_viewer.fig, is_show_fig=False)
        except:
            pass

        # Update the Graph
        self.w_viewer.axes.set_axis_off()
        self.w_viewer.axes.axis("equal")
        if self.w_viewer.axes.get_legend() is not None:
            self.w_viewer.axes.get_legend().remove()
        self.w_viewer.draw()

    def s_plot(self):
        """Plot a preview of the winding in a popup

        Parameters
        ----------
        self : SWinding
            A SWinding object
        """
        try:
            self.obj.plot_winding()
        except (AssertionError, WindingError) as e:
            QMessageBox().critical(self, self.tr("Error"), str(e))

    @staticmethod
    def check(lamination):
        """Check that the lamination have all the needed field set

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
            # Check that everything is set
            if lamination.winding.qs is None:
                return "You must set qs !"
            if lamination.winding.Nslot_shift_wind is None:
                lamination.winding.Nslot_shift_wind = 0
            if lamination.winding.is_reverse_wind is None:
                lamination.winding.is_reverse_wind = False
            if lamination.Ntcoil is None:
                return "You must set Ntcoil !"
            if lamination.Npcpp is None:
                return "You must set Npcpp !"
        except Exception as e:
            return str(e)
