# -*- coding: utf-8 -*-

from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget
from pyleecan.Classes.HoleM62 import HoleM62
from pyleecan.GUI import gui_option
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM62.Gen_PHoleM62 import (
    Gen_PHoleM62,
)
from pyleecan.Methods.Slot.Slot import SlotCheckError
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag import DEFAULT_MAG_MAT
from .....Resources import pixmap_dict


class PHoleM62(Gen_PHoleM62, QWidget):
    """Page to set the Hole Type 62"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Hole Type 62"
    hole_type = HoleM62

    def __init__(self, hole=None, material_dict=None):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 widget
        hole : HoleM62
            current hole to edit
        material_dict : list
            Materials dictionary (library + machine)
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.material_dict = material_dict
        self.hole = hole

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"

        # Set default materials
        self.w_mat_0.setText("magnet_0")
        self.w_mat_0.def_mat = DEFAULT_MAG_MAT
        self.w_mat_0.is_hide_button = True

        if hole.magnet_0 is None:  # SyRM
            self.img_slot.setPixmap(QPixmap(pixmap_dict["HoleM62_no_mag"]))
            self.w_mat_0.hide()
        else:
            # Set current material
            self.w_mat_0.update(self.hole.magnet_0, "mat_type", self.material_dict)

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [
            self.unit_W0,
            self.unit_H0,
            self.unit_H1,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.hole.W0)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)

        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)

        self.w_mat_0.saveNeeded.connect(self.emit_save)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 widget
        """
        self.hole.W0 = self.lf_W0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 widget
        """
        self.hole.H0 = self.lf_H0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 widget
        """
        self.hole.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 widget
        """
        is_set = False
        if self.check() is None:
            try:
                # We compute the output only if the hole is correctly set
                # Compute all the needed output as string
                s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")
                m_surf = format(self.u.get_m2(self.hole.comp_surface_magnets()), ".4g")

                # Update the GUI to display the Output
                self.out_slot_surface.setText(
                    "Slot suface (2 part): " + s_surf + " " + self.u.get_m2_name()
                )
                self.out_magnet_surface.setText(
                    "Magnet surface: " + m_surf + " " + self.u.get_m2_name()
                )
                is_set = True
            except:
                pass

        if not is_set:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_slot_surface.setText("Slot suface (2 part): ?")
            self.out_magnet_surface.setText("Magnet surface: ?")

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 widget

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

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
