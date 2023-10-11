# -*- coding: utf-8 -*-

import PySide2.QtCore
from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap
from ......Classes.SlotW23 import SlotW23
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlot23.Gen_PWSlot23 import Gen_PWSlot23
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Resources import pixmap_dict


translate = PySide2.QtCore.QCoreApplication.translate


class PWSlot23(Gen_PWSlot23, QWidget):
    """Page to set the Slot Type 23"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Slot Type 23"
    slot_type = SlotW23

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 widget
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
        self.lf_W3.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H2.unit = "m"

        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_W1,
            self.unit_W2,
            self.unit_W3,
            self.unit_H0,
            self.unit_H2,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_H2.setValue(self.slot.H2)

        if self.slot.W3 is None:
            self.lf_W3.clear()
            self.lf_W3.setEnabled(False)
            self.lf_W1.setEnabled(True)
            self.lf_W2.setEnabled(True)

            # No W3 => Constant slot
            self.lf_W1.setValue(self.slot.W1)
            self.lf_W2.setValue(self.slot.W2)

        else:  # Cste tooth
            self.lf_W3.setValue(self.slot.W3)
            # W3 is set => constant Tooth so W1 and W2 should be disabled
            self.is_cst_tooth.setChecked(True)

            self.lf_W1.clear()
            self.lf_W2.clear()
            self.lf_W3.setEnabled(True)
            self.lf_W1.setEnabled(False)
            self.lf_W2.setEnabled(False)

            self.slot.W1 = None
            self.slot.W2 = None

        if self.slot.H1_is_rad is None:
            self.slot.H1_is_rad = False
        if self.slot.H1_is_rad:
            self.lf_H1.setValue(self.slot.H1)
        else:  # convert m unit
            self.lf_H1.setValue(gui_option.unit.get_m(self.slot.H1))

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

        # Update the unit combobox with the current m unit name
        self.c_H1_unit.clear()
        self.c_H1_unit.addItems(
            ["[" + gui_option.unit.get_m_name() + "]", "[rad]", "[°]"]
        )
        if self.slot.H1_is_rad:
            self.c_H1_unit.setCurrentIndex(1)  # Rad
        else:
            self.c_H1_unit.setCurrentIndex(0)  # m

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.c_H1_unit.currentIndexChanged.connect(self.set_H1_unit)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.is_cst_tooth.toggled.connect(self.set_is_cst_tooth)
        self.g_wedge.toggled.connect(self.set_wedge)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 object
        """
        self.slot.W1 = self.lf_W1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 object
        """
        self.slot.W2 = self.lf_W2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 object
        """
        self.slot.W3 = self.lf_W3.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 object
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
        self : PWSlot23
            A PWSlot23 object
        value : int
            current index of the combobox
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
        self : PWSlot23
            A PWSlot23 object
        """
        self.slot.H2 = self.lf_H2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_schematics(self):
        """Select the correct schematics according to wedge and constant tooth/slot"""
        if self.g_wedge.isChecked():
            if self.is_cst_tooth.isChecked():
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotW23_wedge_full_ext_stator_constant_tooth"])
                )

            else:
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotW23_wedge_full_ext_stator"])
                )

        else:
            if self.is_cst_tooth.isChecked():
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotW23_wind_ext_stator_constant_tooth"])
                )
            else:
                self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotW23_wind_ext_stator"]))

    def set_wedge(self):
        """Setup the slot wedge according to the GUI"""
        if self.g_wedge.isChecked():
            self.w_wedge_mat.update(self.slot, "wedge_mat", self.material_dict)

        else:
            self.slot.wedge_mat = None

        # Select the correct schematics
        self.update_schematics()

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_cst_tooth(self, is_checked):
        """Signal to set the correct mode (constant tooth or slot) according to
        the checkbox

        Parameters
        ----------
        self : PWSlot23
            A PWSlot23 object
        is_checked : bool
            State of the checkbox
        """

        self.slot.is_cstt_tooth = is_checked
        if is_checked:
            self.slot.W1 = None
            self.slot.W2 = None
            self.lf_W1.setEnabled(False)
            self.lf_W2.setEnabled(False)
            self.lf_W3.setEnabled(True)

        else:
            self.slot.W3 = None
            self.lf_W3.setEnabled(False)
            self.lf_W1.setEnabled(True)
            self.lf_W2.setEnabled(True)

        # Select the correct schematics
        self.update_schematics()

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
        elif lam.slot.H0 is None:
            return "You must set H0 !"
        elif lam.slot.H1 is None:
            return "You must set H1 !"
        elif lam.slot.H2 is None:
            return "You must set H2 !"
        # elif self.is_cst_tooth.isChecked() and self.slot.W3 is None:
        #     return translate("In constant tooth mode, you must set W3 !")
        # elif (not self.is_cst_tooth.isChecked()) and self.slot.W1 is None:
        #     return translate("In constant slot mode, you must set W1 !")
        # elif (not self.is_cst_tooth.isChecked()) and self.slot.W2 is None:
        #     return translate("In constant slot mode, you must set W2 !")

        # Check that everything is set right
        if lam.slot.W3 is not None:
            lam.slot._comp_W()

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
