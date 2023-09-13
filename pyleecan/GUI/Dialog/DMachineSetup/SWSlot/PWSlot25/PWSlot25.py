# -*- coding: utf-8 -*-

import PySide2.QtCore
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap
from ......Classes.SlotW25 import SlotW25
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.Gen_PWSlot25 import Gen_PWSlot25
from ......Methods.Slot.Slot import SlotCheckError

translate = PySide2.QtCore.QCoreApplication.translate


class PWSlot25(Gen_PWSlot25, QWidget):
    """Page to set the Slot Type 25"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Slot Type 25"
    slot_type = SlotW25

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot25
            A PWSlot25 widget
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
        self.lf_W3.unit = "m"
        self.lf_W4.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_H2.unit = "m"

        # Set unit name (m ou mm)
        wid_list = [self.unit_W3, self.unit_W4, self.unit_H1, self.unit_H2]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W3.setValue(self.slot.W3)
        self.lf_W4.setValue(self.slot.W4)
        self.lf_H1.setValue(self.slot.H1)
        self.lf_H2.setValue(self.slot.H2)

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

        # Connect the signal/slot
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_W4.editingFinished.connect(self.set_W4)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.g_wedge.toggled.connect(self.set_wedge)

    def set_wedge(self):
        """Setup the slot wedge according to the GUI"""
        if self.g_wedge.isChecked():
            self.w_wedge_mat.show()
            self.img_slot.setPixmap(
                QPixmap(":/images/images/MachineSetup/WSlot/SlotW25_wedge_full.png")
            )
            self.w_wedge_mat.update(self.slot, "wedge_mat", self.material_dict)
        else:
            self.w_wedge_mat.hide()
            self.slot.wedge_mat = None
            self.img_slot.setPixmap(
                QPixmap(":/images/images/MachineSetup/WSlot/SlotW25_wind.png")
            )
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PWSlot25
            A PWSlot25 object
        """
        self.slot.W3 = self.lf_W3.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W4(self):
        """Signal to update the value of W4 according to the line edit

        Parameters
        ----------
        self : PWSlot25
            A PWSlot25 object
        """
        self.slot.W4 = self.lf_W4.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PWSlot25
            A PWSlot25 object
        """
        self.slot.H1 = self.lf_H1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PWSlot25
            A PWSlot25 object
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
        if lam.slot.W3 is None:
            return "You must set W3 !"
        elif lam.slot.W4 is None:
            return "You must set W4 !"
        elif lam.slot.H1 is None:
            return "You must set H1 !"
        elif lam.slot.H2 is None:
            return "You must set H2 !"

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
