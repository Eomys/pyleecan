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
from numpy import pi


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
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"

        # Set default materials
        self.w_mat_0.setText("magnet_0")
        self.w_mat_0.def_mat = DEFAULT_MAG_MAT
        self.w_mat_0.is_hide_button = True

        if hole.magnet_0 is None:  # SyRM
            self.img_slot.setPixmap(QPixmap(pixmap_dict["HoleM62_empty_int_rotor"]))
            self.w_mat_0.hide()
        else:
            # Set current material
            self.w_mat_0.update(self.hole.magnet_0, "mat_type", self.material_dict)

        if self.hole.W0_is_rad is None:
            self.hole.W0_is_rad = False

        if self.hole.W0_is_rad:
            self.lf_W0.setValue(self.hole.W0)
        else:  # convert m unit
            self.lf_W0.setValue(gui_option.unit.get_m(self.hole.W0))

        # Update the unit combobox with the current m unit name
        self.c_W0_unit.clear()
        self.c_W0_unit.addItems(
            ["[" + gui_option.unit.get_m_name() + "]", "[rad]", "[°]"]
        )

        if self.hole.W0_is_rad:
            self.c_W0_unit.setCurrentIndex(1)  # Rad
            self.ck_is_radial.setChecked(True)
        else:
            self.c_W0_unit.setCurrentIndex(0)  # m
            self.ck_is_radial.setChecked(False)

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [
            self.unit_H0,
            self.unit_H1,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)

        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.c_W0_unit.currentIndexChanged.connect(self.set_W0_unit)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.ck_is_radial.toggled.connect(self.set_ck_is_radial)

        self.w_mat_0.saveNeeded.connect(self.emit_save)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 object
        """
        if self.lf_W0.value() is not None:
            if self.c_W0_unit.currentIndex() == 0:  # m or mm
                self.hole.W0 = gui_option.unit.set_m(self.lf_W0.value())
            elif self.c_W0_unit.currentIndex() == 1:  # rad
                self.hole.W0 = self.lf_W0.value()
            else:  # °
                self.hole.W0 = self.lf_W0.value() / 180 * pi
        else:
            self.hole.W0 = None
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W0_unit(self, value):
        """Signal to update the value of W0_unit according to the combobox

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 object
        value : int
            current index of the combobox
        """
        self.hole.W0_is_rad = bool(value)
        if self.lf_W0.text() != "":
            self.set_W0()  # Update for ° if needed and call comp_output
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

        if self.c_W0_unit.currentIndex() == 0:  # m or mm
            self.ck_is_radial.setChecked(False)

        else:
            self.ck_is_radial.setChecked(True)

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

    def set_ck_is_radial(self):
        """Signal to set the correct mode (radial or hole) according to
        the checkbox

        Parameters
        ----------
        self : PHoleM62
            A PHoleM62 object

        """
        if self.ck_is_radial.isChecked():
            self.img_slot.setPixmap(
                QPixmap(pixmap_dict["HoleM62_mag_int_rotor_radial"])
            )
            self.hole.W0_is_rad = True
            self.c_W0_unit.setCurrentIndex(1)

        else:
            self.img_slot.setPixmap(QPixmap(pixmap_dict["HoleM62_mag_int_rotor"]))
            self.hole.W0_is_rad = False
            self.c_W0_unit.setCurrentIndex(0)

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
