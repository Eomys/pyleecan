# -*- coding: utf-8 -*-

from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QWidget

from .....Classes.Shaft import Shaft
from .....Classes.Frame import Frame
from .....Classes.LamSlotMag import LamSlotMag
from .....GUI import gui_option
from .....GUI.Dialog.DMachineSetup.SMachineDimension.Ui_SMachineDimension import (
    Ui_SMachineDimension,
)
from .....GUI.Resources import pixmap_dict


class SMachineDimension(Ui_SMachineDimension, QWidget):
    """Step to setup the Machine dimension"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for the DMachineSetup nav
    step_name = "Machine Dimensions"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension widget
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
        self.lf_SRint.unit = "m"
        self.lf_SRext.unit = "m"
        self.lf_RRext.unit = "m"
        self.lf_RRint.unit = "m"
        self.lf_Wfra.unit = "m"
        self.lf_Lfra.unit = "m"
        self.lf_Lshaft.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_SRint,
            self.unit_SRext,
            self.unit_RRext,
            self.unit_RRint,
            self.unit_Wfra,
            self.unit_Lfra,
            self.unit_Lshaft,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Initialize the GUI with the current machine value
        self.lf_SRint.setValue(machine.stator.Rint)
        self.lf_SRext.setValue(machine.stator.Rext)
        self.lf_RRint.setValue(machine.rotor.Rint)
        self.lf_RRext.setValue(machine.rotor.Rext)

        self.set_airgap()  # Update out_airgap if possible

        # Set default materials
        self.w_mat_0.setText("Shaft Material")
        self.w_mat_0.def_mat = "M400-50A"
        self.w_mat_1.setText("Frame Material")
        self.w_mat_1.def_mat = "M400-50A"

        # Make sure that the Shaft/Frame is cleaned for External Rotor
        if not machine.rotor.is_internal:
            machine.shaft = None
            machine.frame = None

        if (
            machine.frame is None
            or machine.frame.Rint is None
            or machine.frame.Rext is None
            or machine.frame.comp_height_eq() == 0
        ):
            machine.frame = None
            self.g_frame.setChecked(False)
            self.lf_Wfra.clear()  # Empty spinbox
            self.lf_Lfra.clear()  # Empty spinbox
        else:
            self.g_frame.setChecked(True)
            self.lf_Wfra.setValue(machine.frame.comp_height_eq())
            if machine.frame.Lfra is not None:
                self.lf_Lfra.setValue(machine.frame.Lfra)
            self.w_mat_1.update(self.machine.frame, "mat_type", self.material_dict)

        # Adapt the GUI to the topology of the machine
        self.out_Drsh.hide()  # Never show Drsh, internal parameter
        if not machine.rotor.is_internal:  # External Rotor
            if isinstance(self.machine.rotor, LamSlotMag):
                self.img_machine.setPixmap(QPixmap(pixmap_dict["Dim_Ext_Rotor_mag"]))
            else:
                self.img_machine.setPixmap(QPixmap(pixmap_dict["Dim_Ext_Rotor"]))
            self.g_shaft.hide()
            self.g_frame.hide()
        elif (
            machine.shaft is None
            or machine.shaft.Drsh is None
            or machine.shaft.Drsh == 0
        ):
            # Internal Rotor without shaft
            machine.shaft = None
            self.g_shaft.show()
            self.g_frame.show()
            if isinstance(self.machine.rotor, LamSlotMag):
                self.img_machine.setPixmap(
                    QPixmap(pixmap_dict["Dim_In_Rotor_No_Shaft_mag"])
                )
            else:
                self.img_machine.setPixmap(
                    QPixmap(pixmap_dict["Dim_In_Rotor_No_Shaft"])
                )
            self.g_shaft.setChecked(False)
            # If there is no shaft, the rotor doesn't have internal radius
            self.lf_RRint.setValue(0)
            self.lf_RRint.setEnabled(False)
            self.machine.rotor.Rint = 0
        else:  # Internal Rotor with shaft
            self.g_shaft.show()
            self.g_frame.show()
            if isinstance(self.machine.rotor, LamSlotMag):
                self.img_machine.setPixmap(
                    QPixmap(pixmap_dict["Dim_In_Rotor_Shaft_mag"])
                )
            else:
                self.img_machine.setPixmap(QPixmap(pixmap_dict["Dim_In_Rotor_Shaft"]))
            self.g_shaft.setChecked(True)
            self.machine.shaft.Drsh = self.machine.rotor.Rint * 2
            self.out_Drsh.setText(
                self.tr("Drsh = ")
                + format(gui_option.unit.get_m(self.machine.shaft.Drsh), ".4g")
                + " ["
                + gui_option.unit.get_m_name()
                + "]"
            )
            self.w_mat_0.update(self.machine.shaft, "mat_type", self.material_dict)
            if self.machine.shaft.Lshaft is None:
                Lshaft = 0
            else:
                Lshaft = self.machine.shaft.Lshaft
            self.lf_Lshaft.setValue(Lshaft)

        # Connect the widget
        self.lf_SRint.editingFinished.connect(self.set_stator_Rint)
        self.lf_SRext.editingFinished.connect(self.set_stator_Rext)
        self.lf_RRint.editingFinished.connect(self.set_rotor_Rint)
        self.lf_RRext.editingFinished.connect(self.set_rotor_Rext)
        self.lf_Lshaft.editingFinished.connect(self.set_Lshaft)
        self.lf_Wfra.editingFinished.connect(self.set_Wfra)
        self.lf_Lfra.editingFinished.connect(self.set_Lfra)

        self.g_shaft.toggled.connect(self.set_Drsh)
        self.g_frame.toggled.connect(self.clear_frame)

        self.w_mat_0.saveNeeded.connect(self.emit_save)
        self.w_mat_1.saveNeeded.connect(self.emit_save)

    def set_stator_Rint(self):
        """Signal to update the value of stator.Rint according to the line edit

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        if self.machine.stator.Rint != self.lf_SRint.value():
            self.machine.stator.Rint = self.lf_SRint.value()
            self.set_airgap()  # Update out_airgap if possible
            # Notify the machine GUI that the machine has changed
            self.saveNeeded.emit()

    def set_stator_Rext(self):
        """Signal to update the value of stator.Rext according to the line edit

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        if self.machine.stator.Rext != self.lf_SRext.value():
            Rext = self.lf_SRext.value()
            self.machine.stator.Rext = Rext
            if self.machine.frame is not None:
                try:  # Fail if lf_Wfra empty
                    self.machine.frame.Rext = Rext + self.lf_Wfra.value()
                    self.machine.frame.Rint = Rext
                except TypeError:  # Wfra is None
                    self.machine.frame.Rext = Rext
                    self.machine.frame.Rint = Rext
            self.set_airgap()  # Update out_airgap if possible
            # Notify the machine GUI that the machine has changed
            self.saveNeeded.emit()

    def set_rotor_Rint(self):
        """Signal to update the value of rotor.Rint according to the line edit

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        self.machine.rotor.Rint = self.lf_RRint.value()
        if self.machine.rotor.is_internal:  # Update out_Drsh if needed
            self.set_Drsh(self.g_shaft.isChecked())
        self.set_airgap()  # Update out_airgap if possible
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_rotor_Rext(self):
        """Signal to update the value of rotor.Rext according to the line edit

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        self.machine.rotor.Rext = self.lf_RRext.value()
        self.set_airgap()  # Update out_airgap if possible
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_airgap(self):
        """Signal to update the value of airgap according to the line edit

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        # For readibility
        rotor = self.machine.rotor
        stator = self.machine.stator
        gap_txt = self.tr("Airgap magnetic width = ")
        # Airgap definition change accoding to Topology
        if rotor.is_internal:
            # Update only if the needed parameters are set
            if rotor.Rext is not None and stator.Rint is not None:
                gap = stator.Rint - rotor.Rext
                airgap = format(gap * 1000, ".6g")
                self.out_airgap.setText(gap_txt + airgap + " [mm]")
            else:
                self.out_airgap.setText(gap_txt + "?")
        else:
            # Update only if the needed parameters are set
            if rotor.Rint is not None and stator.Rext is not None:
                airgap = format((rotor.Rint - stator.Rext) * 1000, ".6g")
                self.out_airgap.setText(gap_txt + airgap + " [mm]")
            else:
                self.out_airgap.setText(gap_txt + "?")

    def set_Lshaft(self):
        """Signal to update the value of shaft.Lshaft according to the line edit

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        self.machine.shaft.Lshaft = self.lf_Lshaft.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wfra(self):
        """Signal to update the value of Wfra according to the spinbox

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        if self.machine.stator.Rext is not None:
            Wfra = self.lf_Wfra.value()
            self.machine.frame.Rint = self.machine.stator.Rext
            self.machine.frame.Rext = self.machine.stator.Rext + Wfra
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Lfra(self):
        """Signal to update the value of Lfra according to the line edit

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        self.machine.frame.Lfra = self.lf_Lfra.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def clear_frame(self, is_checked):
        """Signal to remove the frame if the checkbox is unchecked

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        is_checked : bool
            State of the g_frame checkbox
        """
        if is_checked:
            self.machine.frame = Frame()
            self.machine.frame._set_None()
            if self.machine.stator.Rext is not None:
                self.machine.frame.Rint = self.machine.stator.Rext
                self.machine.frame.Rext = self.machine.stator.Rext
            else:
                self.machine.frame.Rint = None
                self.machine.frame.Rext = None
            self.w_mat_1.update(self.machine.frame, "mat_type", self.material_dict)
            self.lf_Wfra.clear()
            self.lf_Lfra.clear()
        else:
            self.machine.frame = None
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Drsh(self, is_checked):
        """Signal to set Drsh according to the page context

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        is_checked : bool
            State of g_shaft
        """

        if is_checked:  # If there is a shaft
            # Set the corresponding image
            if isinstance(self.machine.rotor, LamSlotMag):
                self.img_machine.setPixmap(
                    QPixmap(pixmap_dict["Dim_In_Rotor_Shaft_mag"])
                )
            else:
                self.img_machine.setPixmap(QPixmap(pixmap_dict["Dim_In_Rotor_Shaft"]))
            # Set Drsh if machine.rotor.Rint is set
            if self.machine.rotor.Rint is not None:
                if self.machine.shaft is None:
                    self.machine.shaft = Shaft()
                    self.machine.shaft._set_None()
                self.machine.shaft.Drsh = self.machine.rotor.Rint * 2
                self.out_Drsh.setText(
                    self.tr("Drsh = ")
                    + format(gui_option.unit.get_m(self.machine.shaft.Drsh), ".4g")
                    + " ["
                    + gui_option.unit.get_m_name()
                    + "]"
                )
            else:
                self.out_Drsh.setText(self.tr("Drsh = "))
                self.machine.shaft.Drsh = None
            self.w_mat_0.update(self.machine.shaft, "mat_type", self.material_dict)
            # machine.rotor.Rint editable only if there is a shaft
            self.lf_RRint.setEnabled(True)

        else:  # If there is no shaft
            # Set the corresponding image
            if isinstance(self.machine.rotor, LamSlotMag):
                self.img_machine.setPixmap(
                    QPixmap(pixmap_dict["Dim_In_Rotor_No_Shaft_mag"])
                )
            else:
                self.img_machine.setPixmap(
                    QPixmap(pixmap_dict["Dim_In_Rotor_No_Shaft"])
                )

            self.machine.shaft = None
            self.machine.rotor.Rint = 0
            self.lf_RRint.setValue(0)

            # machine.rotor.Rint editable only if there is a shaft
            self.lf_RRint.setEnabled(False)
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(machine):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        machine : Machine
            Machine to check

        Returns
        -------
        error : str
            Error message (return None if no error)

        """
        try:
            # Check that everything is set
            if machine.stator.Rint is None:
                return "You must set Stator.Rint !"
            if machine.stator.Rext is None:
                return "You must set Stator.Rext !"
            if machine.rotor.Rint is None:
                return "You must set Rotor.Rint !"
            if machine.rotor.Rext is None:
                return "You must set Rotor.Rext !"
            if machine.shaft is not None and machine.shaft.mat_type is None:
                return "You must set the shaft material !"
            if machine.frame is not None and machine.frame.mat_type is None:
                return "You must set the frame material !"

            # Check that everything is set right
            if machine.stator.Rext <= machine.stator.Rint:
                return "The Stator can't have an internal radius greater than the external one !"
            if machine.rotor.Rext <= machine.rotor.Rint:
                return "The Rotor can't have an internal radius greater than the external one !"
            if machine.rotor.is_internal and machine.stator.Rint <= machine.rotor.Rext:
                return "For Internal Rotor machine, you must have: Rotor.Rext < Stator.Rint !"
            if (
                not machine.rotor.is_internal
                and machine.stator.Rext >= machine.rotor.Rint
            ):
                return "For External Rotor machine, you must have: Stator.Rext < Rotor.Rint !"
        except Exception as e:
            return str(e)

    def check_gui(self):
        """Check that the widget are set right according to the current machine

        Parameters
        ----------
        self : SMachineDimension
            A SMachineDimension object
        """
        machine = self.machine

        if machine.rotor.Rint is None and self.g_shaft.isChecked():
            return self.tr("You must set Rotor.Rint !")
        if machine.rotor.Rint is None and not self.g_shaft.isChecked():
            machine.rotor.Rint = 0
            machine.shaft = None
        if self.g_frame.isChecked() and machine.frame.Rint is None:
            return self.tr("You must set Wfra or unchecked Frame !")
        if not self.g_frame.isChecked():
            self.machine.frame = None

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
