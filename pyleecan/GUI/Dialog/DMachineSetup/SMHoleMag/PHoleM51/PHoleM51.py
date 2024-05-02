# -*- coding: utf-8 -*-

from numpy import pi
from qtpy.QtCore import Signal
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QWidget

from ......Classes.MachineIPMSM import MachineIPMSM
from ......Classes.HoleM51 import HoleM51
from ......Classes.Magnet import Magnet
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM51.Gen_PHoleM51 import Gen_PHoleM51
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Dialog.DMachineSetup.SMHoleMag import DEFAULT_MAG_MAT
from ......GUI.Resources import pixmap_dict


class PHoleM51(Gen_PHoleM51, QWidget):
    """Page to set the Hole Type 51"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Hole Type 51"
    hole_type = HoleM51

    def __init__(self, hole=None, material_dict=None):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        hole : HoleM51
            current hole to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.material_dict = material_dict

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_W1.unit = "rad"
        self.lf_W2.unit = "m"
        self.lf_W3.unit = "m"
        self.lf_W4.unit = "m"
        self.lf_W5.unit = "m"
        self.lf_W6.unit = "m"
        self.lf_W7.unit = "m"
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

        self.w_mat_2.setText("magnet_1")
        self.w_mat_2.def_mat = DEFAULT_MAG_MAT
        self.w_mat_2.is_hide_button = True

        self.w_mat_3.setText("magnet_2")
        self.w_mat_3.def_mat = DEFAULT_MAG_MAT
        self.w_mat_3.is_hide_button = True

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [
            self.unit_W0,
            self.unit_W2,
            self.unit_W3,
            self.unit_W4,
            self.unit_W5,
            self.unit_W6,
            self.unit_W7,
            self.unit_H0,
            self.unit_H1,
            self.unit_H2,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        self.hole = hole

        # Adapt GUI with/without magnet
        if not isinstance(hole.parent.parent, MachineIPMSM):  # SyRM
            self.img_slot.setPixmap(QPixmap(pixmap_dict["HoleM51_empty_int_rotor"]))
            # Disable magnet only parameters
            hole.W2 = 0
            hole.W3 = 0
            hole.W4 = 0
            hole.W5 = 0
            hole.W6 = 0
            hole.W7 = 0
            self.lf_W2.setEnabled(False)
            self.lf_W3.setEnabled(False)
            self.lf_W4.setEnabled(False)
            self.lf_W5.setEnabled(False)
            self.lf_W6.setEnabled(False)
            self.lf_W7.setEnabled(False)
            self.w_mat_0.update(self.hole, "mat_void", self.material_dict)
            self.w_mat_1.hide()
            self.w_mat_2.hide()
            self.w_mat_3.hide()
        else:
            self.w_mat_0.update(self.hole, "mat_void", self.material_dict)
            self.w_mat_1.update(self.hole.magnet_0, "mat_type", self.material_dict)
            self.w_mat_2.update(self.hole.magnet_1, "mat_type", self.material_dict)
            self.w_mat_3.update(self.hole.magnet_2, "mat_type", self.material_dict)
            if self.hole.magnet_0 is None:
                self.w_mat_1.setEnabled(False)
            if self.hole.magnet_1 is None:
                self.w_mat_2.setEnabled(False)
            if self.hole.magnet_2 is None:
                self.w_mat_3.setEnabled(False)

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.hole.W0)
        self.lf_W1.setValue(self.hole.W1)
        self.lf_W2.setValue(self.hole.W2)
        self.lf_W3.setValue(self.hole.W3)
        self.lf_W4.setValue(self.hole.W4)
        self.lf_W5.setValue(self.hole.W5)
        self.lf_W6.setValue(self.hole.W6)
        self.lf_W7.setValue(self.hole.W7)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)
        self.lf_H2.setValue(self.hole.H2)

        self.is_magnet_0.setChecked(self.hole.magnet_0 is not None)
        self.is_magnet_1.setChecked(self.hole.magnet_1 is not None)
        self.is_magnet_2.setChecked(self.hole.magnet_2 is not None)
        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_W4.editingFinished.connect(self.set_W4)
        self.lf_W5.editingFinished.connect(self.set_W5)
        self.lf_W6.editingFinished.connect(self.set_W6)
        self.lf_W7.editingFinished.connect(self.set_W7)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.w_mat_0.saveNeeded.connect(self.emit_save)
        self.w_mat_1.saveNeeded.connect(self.emit_save)
        self.w_mat_2.saveNeeded.connect(self.emit_save)
        self.w_mat_3.saveNeeded.connect(self.emit_save)
        self.is_magnet_0.stateChanged.connect(self.change_magnet_0)
        self.is_magnet_1.stateChanged.connect(self.change_magnet_1)
        self.is_magnet_2.stateChanged.connect(self.change_magnet_2)

    def change_magnet_0(self):
        """Set/Remove magnet_0 according to checkbox"""
        if self.is_magnet_0.isChecked():
            self.hole.magnet_0 = Magnet()
            self.hole.magnet_0._set_None()
            self.w_mat_1.setEnabled(True)
            self.w_mat_1.update(self.hole.magnet_0, "mat_type", self.material_dict)
            self.w_mat_1.set_mat_type()
        else:
            self.hole.magnet_0 = None
            self.w_mat_1.setEnabled(False)

    def change_magnet_1(self):
        """Set/Remove magnet_1 according to checkbox"""
        if self.is_magnet_1.isChecked():
            self.hole.magnet_1 = Magnet()
            self.hole.magnet_1._set_None()
            self.w_mat_2.setEnabled(True)
            self.w_mat_2.update(self.hole.magnet_1, "mat_type", self.material_dict)
            self.w_mat_2.set_mat_type()
        else:
            self.hole.magnet_1 = None
            self.w_mat_2.setEnabled(False)

    def change_magnet_2(self):
        """Set/Remove magnet_2 according to checkbox"""
        if self.is_magnet_2.isChecked():
            self.hole.magnet_2 = Magnet()
            self.hole.magnet_2._set_None()
            self.w_mat_3.setEnabled(True)
            self.w_mat_3.update(self.hole.magnet_2, "mat_type", self.material_dict)
            self.w_mat_3.set_mat_type()
        else:
            self.hole.magnet_2 = None
            self.w_mat_3.setEnabled(False)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W0 = self.lf_W0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W1 = self.lf_W1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W2 = self.lf_W2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W3 = self.lf_W3.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W4(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W4 = self.lf_W4.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W5(self):
        """Signal to update the value of W5 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W5 = self.lf_W5.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W6(self):
        """Signal to update the value of W6 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W6 = self.lf_W6.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W7(self):
        """Signal to update the value of W7 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.W7 = self.lf_W7.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.H0 = self.lf_H0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        self.hole.H2 = self.lf_H2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget
        """
        if self.check() is None:
            # We compute the output only if the hole is correctly set
            # Compute all the needed output as string
            try:
                s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")
                m_surf = format(self.u.get_m2(self.hole.comp_surface_magnets()), ".4g")
                alpha = self.hole.comp_alpha()
                alpha_rad = "%.4g" % alpha
                alpha_deg = "%.4g" % (alpha * 180 / pi)
                Ws = format(self.u.get_m(self.hole.comp_width()), ".4g")

                # Update the GUI to display the Output
                self.out_slot_surface.setText(
                    "Slot suface: " + s_surf + " " + self.u.get_m2_name()
                )
                self.out_magnet_surface.setText(
                    "Magnet surface: " + m_surf + " " + self.u.get_m2_name()
                )
                self.out_alpha.setText(
                    "alpha: " + alpha_rad + " rad (" + alpha_deg + "°)"
                )
                self.out_Whole.setText("Wslot: " + Ws + " " + self.u.get_m_name())
            except:
                # We can't compute the output => We erase the previous version
                # (that way the user know that something is wrong)
                self.out_slot_surface.setText("Slot suface: ?")
                self.out_magnet_surface.setText("Magnet surface: ?")
                self.out_alpha.setText("alpha: ?")
                self.out_Whole.setText("Wslot: ?")
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_slot_surface.setText("Slot suface: ?")
            self.out_magnet_surface.setText("Magnet surface: ?")
            self.out_alpha.setText("alpha: ?")
            self.out_Whole.setText("Wslot: ?")

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PHoleM51
            A PHoleM51 widget

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
