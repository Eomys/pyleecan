# -*- coding: utf-8 -*-

import PySide2.QtCore
from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap
from ......Classes.SlotW11 import SlotW11
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlot11.Gen_PWSlot11 import Gen_PWSlot11
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Resources import pixmap_dict

translate = PySide2.QtCore.QCoreApplication.translate


class PWSlot11(Gen_PWSlot11, QWidget):
    """Page to set the Slot Type 11"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Slot Type 11"
    slot_type = SlotW11

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 widget
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
        self.lf_R1.unit = "m"

        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_W1,
            self.unit_W2,
            self.unit_W3,
            self.unit_H0,
            self.unit_H2,
            self.unit_R1,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_H2.setValue(self.slot.H2)
        if self.slot.W3 is None:
            self.lf_W3.clear()
            self.is_cst_tooth.setChecked(False)
            self.lf_W3.setEnabled(False)
            # No W3 => Constant slot
            self.lf_W1.setValue(self.slot.W1)
            self.lf_W2.setValue(self.slot.W2)
        else:  # Cste tooth
            self.lf_W3.setValue(self.slot.W3)
            # W3 is set => constant Tooth so W1 and W2 should be disabled
            self.is_cst_tooth.setChecked(True)
            self.slot.W1 = None
            self.slot.W2 = None
            self.lf_W1.clear()
            self.lf_W2.clear()
            self.lf_W1.setEnabled(False)
            self.lf_W2.setEnabled(False)
        if self.slot.H1_is_rad is None:
            self.slot.H1_is_rad = False
        if self.slot.H1_is_rad:
            self.lf_H1.setValue(self.slot.H1)
        else:  # convert m unit
            self.lf_H1.setValue(gui_option.unit.get_m(self.slot.H1))
        self.lf_R1.setValue(self.slot.R1)

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
        self.lf_R1.editingFinished.connect(self.set_R1)
        self.is_cst_tooth.toggled.connect(self.set_is_cst_tooth)
        self.g_wedge.toggled.connect(self.set_wedge)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
        """
        self.slot.W1 = self.lf_W1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
        """
        self.slot.W2 = self.lf_W2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
        """
        self.slot.W3 = self.lf_W3.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R1(self):
        """Signal to update the value of R1 according to the line edit

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
        """
        self.slot.R1 = self.lf_R1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
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
        self : PWSlot11
            A PWSlot11 object
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
        self : PWSlot11
            A PWSlot11 object
        """
        self.slot.H2 = self.lf_H2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    # setup slot schematics
    def update_schematics(self):
        if self.g_wedge.isChecked():
            if self.is_cst_tooth.isChecked():
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotW11_constant_tooth_wedge_full"])
                )

            else:
                self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotW11_wedge_full"]))

        else:
            if self.is_cst_tooth.isChecked():
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotW11_constant_tooth_wind"])
                )
            else:
                self.img_slot.setPixmap(QPixmap(pixmap_dict["SlotW11_wind"]))

    def set_wedge(self):
        """Setup the slot wedge according to the GUI"""
        if self.g_wedge.isChecked():
            self.w_wedge_mat.show()
            self.w_wedge_mat.update(self.slot, "wedge_mat", self.material_dict)

        else:
            self.w_wedge_mat.hide()
            self.slot.wedge_mat = None

        # setup the picture
        self.update_schematics()

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_cst_tooth(self, is_checked):
        """Signal to set the correct mode (constant tooth or slot) according to
        the checkbox

        Parameters
        ----------
        self : PWSlot11
            A PWSlot11 object
        is_checked : bool
            State of the checkbox
        """
        self.slot.is_cstt_tooth = is_checked
        if is_checked:
            self.w_wedge_mat.update(self.slot, "wedge_mat", self.material_dict)
            self.slot.W1 = None
            self.slot.W2 = None
            self.lf_W1.clear()
            self.lf_W2.clear()
            self.lf_W1.setEnabled(False)
            self.lf_W2.setEnabled(False)
            self.lf_W3.setEnabled(True)
            self.w_wedge_mat.show()

        else:
            self.slot.W3 = None
            self.lf_W3.clear()
            self.lf_W3.setEnabled(False)
            self.lf_W1.setEnabled(True)
            self.lf_W2.setEnabled(True)
            self.w_wedge_mat.show()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

        """setup the picture"""
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

        # Check that everything is set and Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Check that everything is set right
        if lam.slot.W3 is not None:
            lam.slot._comp_W()

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return "Unable to compute yoke height:" + str(error)
        if yoke_height <= 0:
            return "The slot height is greater than the lamination !"
