# -*- coding: utf-8 -*-

from qtpy.QtCore import Signal
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QWidget
from pyleecan.Classes.HoleM63 import HoleM63
from pyleecan.GUI import gui_option
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM63.Gen_PHoleM63 import (
    Gen_PHoleM63,
)
from pyleecan.Methods.Slot.Slot import SlotCheckError
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag import DEFAULT_MAG_MAT
from .....Resources import pixmap_dict
from numpy import pi


class PHoleM63(Gen_PHoleM63, QWidget):
    """Page to set the Hole Type 63"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Hole Type 63"
    hole_type = HoleM63

    def __init__(self, hole=None, material_dict=None):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleM63
            A PHoleM63 widget
        hole : HoleM63
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
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_W0.unit = "m"

        # Set default materials
        self.w_mat_0.setText("magnet_0")
        self.w_mat_0.def_mat = DEFAULT_MAG_MAT
        self.w_mat_0.is_hide_button = True

        if hole.magnet_0 is None:  # SyRM
            self.img_slot.setPixmap(QPixmap(pixmap_dict["HoleM63_empty_int_rotor"]))
            self.w_mat_0.hide()
        else:
            # Set current material
            self.w_mat_0.update(self.hole.magnet_0, "mat_type", self.material_dict)

        if self.hole.top_flat is None:
            self.hole.top_flat = False

        elif self.hole.top_flat == True:
            self.img_slot.setPixmap(
                QPixmap(pixmap_dict["HoleM63_mag_int_rotor_top_flat"])
            )

        self.ck_is_top_flat.setChecked(self.hole.top_flat)

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [
            self.unit_H0,
            self.unit_H1,
            self.unit_W0,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)
        self.lf_W0.setValue(self.hole.W0)

        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.ck_is_top_flat.toggled.connect(self.set_ck_is_top_flat)

        self.w_mat_0.saveNeeded.connect(self.emit_save)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM63
            A PHoleM63 object
        """
        self.hole.W0 = self.lf_W0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PHoleM63
            A PHoleM63 widget
        """
        self.hole.H0 = self.lf_H0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PHoleM63
            A PHoleM63 widget
        """
        self.hole.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_ck_is_top_flat(self):
        """Signal to set the correct mode (top_flat or hole) according to
        the checkbox

        Parameters
        ----------
        self : PHoleM63
            A PHoleM63 object

        """
        if self.ck_is_top_flat.isChecked():
            self.img_slot.setPixmap(
                QPixmap(pixmap_dict["HoleM63_mag_int_rotor_top_flat"])
            )
        else:
            self.img_slot.setPixmap(QPixmap(pixmap_dict["HoleM63_mag_int_rotor"]))
        self.hole.top_flat = self.ck_is_top_flat.isChecked()

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleM63
            A PHoleM63 widget
        """
        is_set = False
        if self.check() is None:
            try:
                # We compute the output only if the hole is correctly set
                # Compute all the needed output as string
                s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")

                # Update the GUI to display the Output
                self.out_slot_surface.setText(
                    f"Slot suface (2 part): {s_surf} {self.u.get_m2_name()}"
                )
                self.out_magnet_surface.setText(
                    f"Magnet surface:  {s_surf} {self.u.get_m2_name()}"
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
        self : PHoleM63
            A PHoleM63 widget

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
