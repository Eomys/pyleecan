# -*- coding: utf-8 -*-

from numpy import pi
from qtpy.QtCore import Signal
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QWidget

from ......Classes.HoleM50 import HoleM50
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM50.Gen_PHoleM50 import Gen_PHoleM50
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Dialog.DMachineSetup.SMHoleMag import DEFAULT_MAG_MAT
from ......GUI.Resources import pixmap_dict


class PHoleM50(Gen_PHoleM50, QWidget):
    """Page to set the Hole Type 50"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Hole Type 50"
    hole_type = HoleM50

    def __init__(self, hole=None, material_dict=None):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        hole : HoleM50
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
        self.lf_W1.unit = "m"
        self.lf_W2.unit = "m"
        self.lf_W3.unit = "m"
        self.lf_W4.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_H2.unit = "m"
        self.lf_H3.unit = "m"
        self.lf_H4.unit = "m"

        # Set default materials
        self.w_mat_0.setText("mat_void")
        self.w_mat_0.def_mat = "Air"
        self.w_mat_0.is_hide_button = True
        self.w_mat_1.setText("magnet_0")
        self.w_mat_1.def_mat = DEFAULT_MAG_MAT
        self.w_mat_1.is_hide_button = True
        self.w_mat_2.setText("magnet_1")
        self.w_mat_2.def_mat = DEFAULT_MAG_MAT
        self.w_mat_2.is_hide_button = True

        # Adapt GUI with/without magnet
        if hole.magnet_0 is None:  # SyRM
            self.img_slot.setPixmap(QPixmap(pixmap_dict["HoleM50_empty_int_rotor"]))
            self.w_mat_0.update(self.hole, "mat_void", self.material_dict)
            self.w_mat_1.hide()
            self.w_mat_2.hide()
        else:
            # Set current material
            self.w_mat_0.update(self.hole, "mat_void", self.material_dict)
            self.w_mat_1.update(self.hole.magnet_0, "mat_type", self.material_dict)
            self.w_mat_2.update(self.hole.magnet_1, "mat_type", self.material_dict)

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [
            self.unit_W0,
            self.unit_W1,
            self.unit_W2,
            self.unit_W3,
            self.unit_W4,
            self.unit_H0,
            self.unit_H1,
            self.unit_H2,
            self.unit_H3,
            self.unit_H4,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.hole.W0)
        self.lf_W1.setValue(self.hole.W1)
        self.lf_W2.setValue(self.hole.W2)
        self.lf_W3.setValue(self.hole.W3)
        self.lf_W4.setValue(self.hole.W4)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)
        self.lf_H2.setValue(self.hole.H2)
        self.lf_H3.setValue(self.hole.H3)
        self.lf_H4.setValue(self.hole.H4)

        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_W4.editingFinished.connect(self.set_W4)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.lf_H3.editingFinished.connect(self.set_H3)
        self.lf_H4.editingFinished.connect(self.set_H4)
        self.w_mat_0.saveNeeded.connect(self.emit_save)
        self.w_mat_1.saveNeeded.connect(self.emit_save)
        self.w_mat_2.saveNeeded.connect(self.emit_save)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.W0 = self.lf_W0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.W1 = self.lf_W1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.W2 = self.lf_W2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.W3 = self.lf_W3.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W4(self):
        """Signal to update the value of W4 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.W4 = self.lf_W4.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.H0 = self.lf_H0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.H2 = self.lf_H2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H3(self):
        """Signal to update the value of H3 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.H3 = self.lf_H3.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H4(self):
        """Signal to update the value of H4 according to the line edit

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        self.hole.H4 = self.lf_H4.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget
        """
        # Hole surface
        try:
            s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")
            self.out_slot_surface.setText(
                "Hole surface: " + s_surf + " [" + self.u.get_m2_name() + "]"
            )
        except:
            self.out_slot_surface.setText("Hole surface: ?")

        # Magnet surface
        try:
            m_surf = format(self.u.get_m2(self.hole.comp_surface_magnets()), ".4g")
            self.out_magnet_surface.setText(
                "Magnet surf.: " + m_surf + " [" + self.u.get_m2_name() + "]"
            )
        except:
            self.out_magnet_surface.setText("Magnet surf.: ?")

        # Alpha
        try:
            alpha = self.hole.comp_alpha()
            alpha_rad = "%.4g" % alpha
            alpha_deg = "%.4g" % (alpha * 180 / pi)
            self.out_alpha.setText(
                "alpha: " + alpha_rad + " [rad] (" + alpha_deg + "°)"
            )
        except:
            self.out_alpha.setText("alpha: ?")

        # Magnet width
        try:
            Mag_width = format(
                self.u.get_m(self.hole.W2 + self.hole.W4 + self.hole.comp_W5()),
                ".4g",
            )
            # Update the GUI to display the Output
            self.out_W5.setText(
                "Max magnet width: " + Mag_width + " [" + self.u.get_m_name() + "]"
            )
        except:
            self.out_W5.setText("Max magnet width: ?")

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PHoleM50
            A PHoleM50 widget

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
