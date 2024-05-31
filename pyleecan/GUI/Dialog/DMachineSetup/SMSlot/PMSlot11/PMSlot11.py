# -*- coding: utf-8 -*-

import qtpy.QtCore
from numpy import pi
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget
from qtpy.QtGui import QPixmap
from ......Classes.SlotM11 import SlotM11
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.Gen_PMSlot11 import Gen_PMSlot11
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Resources import pixmap_dict


translate = qtpy.QtCore.QCoreApplication.translate

# Unit combobox
RAD_ID = 0


class PMSlot11(Gen_PMSlot11, QWidget):
    """Page to set the Slot Magnet Type 11"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Polar Magnet"
    notch_name = "Polar"
    slot_type = SlotM11

    def __init__(self, lamination=None, notch_obj=None, material_dict=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PMSlot11
            A PMSlot11 widget
        lamination : Lamination
            current lamination to edit
        notch_obj : notch
            current notch to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.lamination = lamination
        self.slot = lamination.slot
        self.is_notch = notch_obj is not None
        self.notch_obj = notch_obj
        self.material_dict = material_dict

        # Set FloatEdit unit
        self.lf_W0.unit = "rad"
        self.lf_H0.unit = "m"
        self.lf_W1.unit = "rad"
        self.lf_H1.unit = "m"

        # Set unit name (m ou mm)
        self.unit_H0.setText("[" + gui_option.unit.get_m_name() + "]")
        self.unit_H1.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_W1.setValue(self.slot.W1)
        self.lf_H1.setValue(self.slot.H1)

        # Notch setup
        if self.is_notch:
            self.w_mag.hide()  # Hide magnet widgets
            self.g_key.show()  # Setup key widgets
            self.g_key.setChecked(self.notch_obj.key_mat is not None)
            if self.notch_obj.key_mat is None:
                self.slot.W1 = 0  # Clear for check
                self.slot.H1 = 0  # Clear for check
                self.lf_W1.setValue(None)
                self.lf_H1.setValue(None)

            # Material setup
            self.w_key_mat.setText("Key Material")
            self.w_key_mat.def_mat = "Steel1"
            self.set_key()
        else:
            # Setup the widgets according to current values
            self.w_mag.update(lamination, self.material_dict)

            # Use schematics on the inner without magnet
            self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotM11_mag_int_rotor"]))

            self.g_key.hide()

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.c_W0_unit.currentIndexChanged.connect(self.set_W0)
        self.w_mag.saveNeeded.connect(self.emit_save)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.c_W1_unit.currentIndexChanged.connect(self.set_W1)
        self.g_key.toggled.connect(self.set_key)

    def set_key(self):
        """Setup the slot key according to the GUI"""
        widget_list = [self.lf_W1, self.c_W1_unit, self.in_W1]
        widget_list += [self.lf_H1, self.unit_H1, self.in_H1]
        widget_list += [self.w_key_mat]

        if self.g_key.isChecked():
            self.w_key_mat.update(self.notch_obj, "key_mat", self.material_dict)
            if self.lamination.is_internal:
                self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotM11_key_int_rotor"]))
            else:
                self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotM11_key_ext_stator"]))
            is_enabled = True

        else:
            self.notch_obj.key_mat = None
            if self.lamination.is_internal:
                self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotM11_empty_int_rotor"]))
            else:
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotM11_empty_ext_stator"])
                )
            is_enabled = False

        for widget in widget_list:
            widget.setEnabled(is_enabled)
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PMSlot11
            A PMSlot11 object
        """
        if self.lf_W0.value() is not None:
            if self.c_W0_unit.currentIndex() == RAD_ID:
                self.slot.W0 = self.lf_W0.value()
            else:
                self.slot.W0 = self.lf_W0.value() * pi / 180
        else:
            self.slot.W0 = None
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PMSlot11
            A PMSlot11 object
        """
        if self.c_W1_unit.currentIndex() == RAD_ID:
            self.slot.W1 = self.lf_W1.value()
        else:
            self.slot.W1 = self.lf_W1.value() * pi / 180
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PMSlot11
            A PMSlot11 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PMSlot11
            A PMSlot11 object
        """
        self.slot.H1 = self.lf_H1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lam: LamSlotMag
            Lamination to check.

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.W0 is None:
            return "You must set W0 !"
        elif lam.slot.H0 is None:
            return "You must set H0 !"
        if lam.slot.W1 is None:
            return "You must set W1 !"
        elif lam.slot.H1 is None:
            return "You must set H1 !"

        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return "Unable to compute yoke height:" + str(error)

        if yoke_height <= 0:
            return "The slot height is greater than the lamination !"
