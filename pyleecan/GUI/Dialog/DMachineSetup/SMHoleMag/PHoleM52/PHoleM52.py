# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from ......Classes.HoleM52 import HoleM52
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52.Gen_PHoleM52 import Gen_PHoleM52
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Dialog.DMachineSetup.SMHoleMag import DEFAULT_MAG_MAT


class PHoleM52(Gen_PHoleM52, QWidget):
    """Page to set the Hole Type 52"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Hole Type 52"
    hole_type = HoleM52

    def __init__(self, hole=None, material_dict=None):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget
        hole : HoleM52
            current hole to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.material_dict = material_dict
        self.hole = hole

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_W3.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_H2.unit = "m"

        # Set default materials
        self.w_mat_0.setText("mat_void")
        self.w_mat_0.def_mat = "Air"
        self.w_mat_0.is_hide_button = True

        self.w_mat_1.setText("magnet_0")
        self.w_mat_1.def_mat = DEFAULT_MAG_MAT
        self.w_mat_1.is_hide_button = True

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [
            self.unit_W0,
            self.unit_W3,
            self.unit_H0,
            self.unit_H1,
            self.unit_H2,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        # Adapt GUI with/without magnet
        if hole.magnet_0 is None:  # SyRM
            self.img_slot.setPixmap(
                QPixmap(":/images/images/MachineSetup/SMHoleMag/HoleM52_no_mag.png")
            )
            self.w_mat_0.update(self.hole, "mat_void", self.material_dict)
            self.w_mat_1.hide()
        else:
            self.w_mat_0.update(self.hole, "mat_void", self.material_dict)
            self.w_mat_1.update(self.hole.magnet_0, "mat_type", self.material_dict)

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.hole.W0)
        self.lf_W3.setValue(self.hole.W3)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)
        self.lf_H2.setValue(self.hole.H2)

        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)

        self.w_mat_0.saveNeeded.connect(self.emit_save)
        self.w_mat_1.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget
        """
        self.hole.W0 = self.lf_W0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget
        """
        self.hole.W3 = self.lf_W3.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget
        """
        self.hole.H0 = self.lf_H0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget
        """
        self.hole.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget
        """
        self.hole.H2 = self.lf_H2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget
        """
        if self.check() is None:
            # We compute the output only if the hole is correctly set
            # Compute all the needed output as string
            s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")
            m_surf = format(self.u.get_m2(self.hole.comp_surface_magnets()), ".4g")
            alpha = self.hole.comp_alpha()
            alpha_rad = "%.4g" % alpha
            alpha_deg = "%.4g" % (alpha * 180 / pi)
            W1 = format(self.u.get_m(self.hole.comp_W1()), ".4g")

            # Update the GUI to display the Output
            self.out_slot_surface.setText(
                "Slot suface: " + s_surf + " " + self.u.get_m2_name()
            )
            self.out_magnet_surface.setText(
                "Magnet surface: " + m_surf + " " + self.u.get_m2_name()
            )
            self.out_alpha.setText("alpha: " + alpha_rad + " rad (" + alpha_deg + "°)")
            self.out_W1.setText("W1: " + W1 + " " + self.u.get_m_name())

        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_slot_surface.setText("Slot suface: ?")
            self.out_magnet_surface.setText("Magnet surface: ?")
            self.out_alpha.setText("alpha: ?")
            self.out_W1.setText("W1: ?")

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PHoleM52
            A PHoleM52 widget

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        # Constraints and None
        try:
            self.hole.check()
        except SlotCheckError as error:
            return str(error)
