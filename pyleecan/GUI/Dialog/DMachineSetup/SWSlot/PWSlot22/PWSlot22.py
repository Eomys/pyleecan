# -*- coding: utf-8 -*-

import PySide2.QtCore
from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget, QListView
from PySide2.QtGui import QPixmap
from ......Classes.SlotW22 import SlotW22
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.Gen_PWSlot22 import Gen_PWSlot22
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Resources import pixmap_dict


translate = PySide2.QtCore.QCoreApplication.translate


class PWSlot22(Gen_PWSlot22, QWidget):
    """Page to set the Slot Type 22"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Slot Type 22"
    slot_type = SlotW22

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 widget
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
        self.lf_H0.unit = "m"
        self.lf_H2.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [self.unit_H0, self.unit_H2]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_W2.setValue(self.slot.W2)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_H2.setValue(self.slot.H2)

        listView = QListView(self.c_W0_unit)
        self.c_W0_unit.setView(listView)

        listView = QListView(self.c_W2_unit)
        self.c_W2_unit.setView(listView)

        self.c_W0_unit.setCurrentIndex(0)  # rad
        self.c_W2_unit.setCurrentIndex(0)  # rad

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
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.c_W0_unit.currentIndexChanged.connect(self.set_W0_unit)
        self.c_W2_unit.currentIndexChanged.connect(self.set_W2_unit)
        self.g_wedge.toggled.connect(self.set_wedge)

    def set_wedge(self):
        """Setup the slot wedge according to the GUI"""
        if self.g_wedge.isChecked():
            self.img_slot.setPixmap(
                QPixmap(pixmap_dict["SlotW22_wedge_full_ext_stator"])
            )
            self.w_wedge_mat.update(self.slot, "wedge_mat", self.material_dict)
        else:
            self.slot.wedge_mat = None
            self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotW22_wind_ext_stator"]))
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        if self.lf_W0.value() is not None:
            if self.c_W0_unit.currentIndex() == 0:  # Rad
                self.slot.W0 = self.lf_W0.value()
            else:
                self.slot.W0 = self.lf_W0.value() / 180 * pi
        else:
            self.slot.W0 = None
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        if self.lf_W2.value() is not None:
            if self.c_W2_unit.currentIndex() == 0:  # Rad
                self.slot.W2 = self.lf_W2.value()
            else:
                self.slot.W2 = self.lf_W2.value() / 180 * pi
        else:
            self.slot.W2 = None
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        self.slot.H2 = self.lf_H2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W0_unit(self, value):
        """Signal to convert the value of W0 according to the combobox unit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        value : int
            Current index of combobox
        """
        if self.lf_W0.text() != "":
            self.set_W0()  # Update for ° if needed and call comp_output
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2_unit(self, value):
        """Signal to convert the value of W2 according to the combobox unit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        value : int
            Current index of combobox
        """
        if self.lf_W2.text() != "":
            self.set_W2()  # Update for ° if needed and call comp_output
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
        if lam.slot.Zs is None:
            return "You must set Zs !"
        elif lam.slot.W0 is None:
            return "You must set W0 !"
        elif lam.slot.W2 is None:
            return "You must set W2 !"
        elif lam.slot.H0 is None:
            return "You must set H0 !"
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
