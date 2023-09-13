# -*- coding: utf-8 -*-

import PySide2.QtCore
from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap
from ......Classes.SlotW21 import SlotW21
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlot21.Gen_PWSlot21 import Gen_PWSlot21
from ......Methods.Slot.Slot import SlotCheckError

translate = PySide2.QtCore.QCoreApplication.translate


class PWSlot21(Gen_PWSlot21, QWidget):
    """Page to set the Slot Type 21"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Slot Type 21"
    slot_type = SlotW21

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 widget
        lamination : Lamination
            current lamination to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.lamination = lamination
        self.slot = lamination.slot
        self.material_dict = material_dict

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_W1.unit = "m"
        self.lf_W2.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H2.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_W1,
            self.unit_W2,
            self.unit_H0,
            self.unit_H2,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_W1.setValue(self.slot.W1)
        self.lf_W2.setValue(self.slot.W2)
        self.lf_H0.setValue(self.slot.H0)
        if self.slot.H1_is_rad is None:
            self.slot.H1_is_rad = False
        if self.slot.H1_is_rad:
            self.lf_H1.setValue(self.slot.H1)
        else:  # convert m unit
            self.lf_H1.setValue(gui_option.unit.get_m(self.slot.H1))
        self.lf_H2.setValue(self.slot.H2)

        # Update the unit combobox with the current m unit name
        self.c_H1_unit.clear()
        self.c_H1_unit.addItems(
            ["[" + gui_option.unit.get_m_name() + "]", "[rad]", "[°]"]
        )
        if self.slot.H1_is_rad:  # rad
            self.c_H1_unit.setCurrentIndex(1)
        else:  # m
            self.c_H1_unit.setCurrentIndex(0)

        # Wedge setup
        self.g_wedge.setChecked(self.slot.wedge_mat is not None)
        self.w_wedge_mat.setText("Wedge Material")
        if lamination.mat_type is not None and lamination.mat_type.name not in [
            "",
            None,
        ]:
            self.w_wedge_mat.def_mat = lamination.mat_type.name
        else:
            self.w_wedge_mat.def_mat = "M400-50A"
        self.set_wedge()

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.c_H1_unit.currentIndexChanged.connect(self.set_H1_unit)
        self.g_wedge.toggled.connect(self.set_wedge)

    def set_wedge(self):
        """Setup the slot wedge according to the GUI"""
        if self.g_wedge.isChecked():
            self.w_wedge_mat.show()
            self.img_slot.setPixmap(
                QPixmap(":/images/images/MachineSetup/WSlot/SlotW21_wedge_full.png")
            )
            self.w_wedge_mat.update(self.slot, "wedge_mat", self.material_dict)
        else:
            self.w_wedge_mat.hide()
            self.slot.wedge_mat = None
            self.img_slot.setPixmap(
                QPixmap(":/images/images/MachineSetup/WSlot/SlotW21_wind.png")
            )
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 object
        """
        self.slot.W1 = self.lf_W1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 object
        """
        self.slot.W2 = self.lf_W2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 object
        """
        if self.lf_H1.value() is not None:
            if self.c_H1_unit.currentIndex() == 0:  # m or mm
                self.slot.H1 = gui_option.unit.set_m(self.lf_H1.value())
            elif self.c_H1_unit.currentIndex() == 1:  # rad
                self.slot.H1 = self.lf_H1.value()
            else:  # °
                self.slot.H1 = self.lf_H1.value() / 180 * pi
        else:
            self.slot.H1 = None
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1_unit(self, value):
        """Signal to update the value of H1_unit according to the combobox

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 object
        value : int
            Current index of the combobox
        """
        self.slot.H1_is_rad = bool(value)
        if self.lf_H1.text() != "":
            self.set_H1()  # Update for ° if needed and call comp_output
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PWSlot21
            A PWSlot21 object
        """
        self.slot.H2 = self.lf_H2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.W0 is None:
            return "You must set W0 !"
        elif lam.slot.W1 is None:
            return "You must set W1 !"
        elif lam.slot.W2 is None:
            return "You must set W2 !"
        elif lam.slot.H0 is None:
            return "You must set H0 !"
        elif lam.slot.H1 is None:
            return "You must set H1 !"
        elif lam.slot.H2 is None:
            return "You must set H2 !"
        elif lam.slot.H1 >= pi / 2:
            return "You must have H1 < 90°"

        # Check that everything is set right
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
