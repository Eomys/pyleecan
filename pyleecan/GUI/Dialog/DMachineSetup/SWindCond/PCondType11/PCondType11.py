# -*- coding: utf-8 -*-

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap

from ......Classes.CondType11 import CondType11
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWindCond.PCondType11.Gen_PCondType11 import (
    Gen_PCondType11,
)
from ......GUI.Resources import pixmap_dict


class PCondType11(Gen_PCondType11, QWidget):
    """Page to set the Conductor Type 11"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for SWindCond combobox
    cond_type = CondType11
    cond_name = "Form wound"

    def __init__(self, lamination=None, material_dict=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PCondType11
            A PCondType11 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.material_dict = material_dict

        self.w_mat_0.setText("Conductor material")
        self.w_mat_0.def_mat = "Copper1"
        self.w_mat_0.setWhatsThis("Conductor material")
        self.w_mat_0.setToolTip("Conductor material")

        self.w_mat_1.setText("Insulator material")
        self.w_mat_1.def_mat = "Insulator1"
        self.w_mat_1.setText("Insulator material")
        self.w_mat_1.setWhatsThis("Insulator material")
        self.w_mat_1.setToolTip("Insulator material")

        # Set FloatEdit unit
        self.lf_Wwire.unit = "m"
        self.lf_Hwire.unit = "m"
        self.lf_Wins_wire.unit = "m"
        self.lf_Lewout.unit = "m"
        self.u = gui_option.unit

        # Set unit name (m ou mm)
        wid_list = [
            self.unit_Wwire,
            self.unit_Hwire,
            self.unit_Wins_wire,
            self.unit_Lewout,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lam = lamination
        self.cond = self.lam.winding.conductor

        # Make sure that isinstance(cond, CondType11)
        if self.cond is None or not isinstance(self.cond, CondType11):
            self.cond = CondType11()
            self.cond._set_None()

        if self.cond.Nwppc_tan is None:
            self.cond.Nwppc_tan = 1  # Default value
        self.si_Nwpc1_tan.setValue(self.cond.Nwppc_tan)

        if self.cond.Nwppc_rad is None:
            self.cond.Nwppc_rad = 1  # Default value
        self.si_Nwpc1_rad.setValue(self.cond.Nwppc_rad)

        self.lf_Wwire.setValue(self.cond.Wwire)
        self.lf_Hwire.setValue(self.cond.Hwire)
        if self.cond.Wins_wire is None:
            self.cond.Wins_wire = 0  # Default value
        if self.cond.Wins_wire != 0:
            self.g_ins.setChecked(True)
            self.lf_Wins_wire.setValue(self.cond.Wins_wire)
        self.lf_Lewout.validator().setBottom(0)
        if self.lam.winding.Lewout is None:
            self.lam.winding.Lewout = 0
        self.lf_Lewout.setValue(self.lam.winding.Lewout)

        self.set_Nwppc()
        self.set_Nwppc()
        self.update_ins_layout()

        # Set conductor and insulator material
        self.w_mat_0.update(self.lam.winding.conductor, "cond_mat", self.material_dict)
        self.w_mat_1.update(self.lam.winding.conductor, "ins_mat", self.material_dict)

        # Display the conductor main output
        self.w_out.comp_output()

        # Connect the slot/signal
        self.g_ins.toggled.connect(self.update_ins_layout)
        self.si_Nwpc1_tan.valueChanged.connect(self.set_Nwppc)
        self.si_Nwpc1_rad.valueChanged.connect(self.set_Nwppc)
        self.lf_Wwire.editingFinished.connect(self.set_Wwire)
        self.lf_Hwire.editingFinished.connect(self.set_Hwire)
        self.lf_Wins_wire.editingFinished.connect(self.set_Wins_wire)
        self.lf_Lewout.editingFinished.connect(self.set_Lewout)
        self.w_mat_0.saveNeeded.connect(self.emit_save)
        self.w_mat_1.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def update_ins_layout(self):
        if self.g_ins.isChecked():
            self.set_Wins_wire()
        else:
            self.set_Wins_wire(Wins_wire=None)

    def set_Nwppc(self):
        """Signal to update the value of Nwppc_tan and rad according to the line edit

        Parameters
        ----------
        self : PCondType11
            A PCondType11 object
        """
        self.cond.Nwppc_tan = self.si_Nwpc1_tan.value()
        self.cond.Nwppc_rad = self.si_Nwpc1_rad.value()
        if self.si_Nwpc1_tan.value() * self.si_Nwpc1_rad.value() > 1:
            self.in_Wwire.setText("Strand width")
            self.in_Hwire.setText("Strand height")
            self.img_cond.setPixmap(QPixmap(pixmap_dict["Cond11"]))
            self.w_mat_0.setText("Strand material")
        else:
            self.in_Wwire.setText("Conductor width")
            self.in_Hwire.setText("Conductor height")
            self.img_cond.setPixmap(QPixmap(pixmap_dict["Cond11_single"]))
            self.w_mat_0.setText("Conductor material")
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Nwppc_rad(self):
        """Signal to update the value of Nwppc_rad according to the line edit

        Parameters
        ----------
        self : PCondType11
            A PCondType11 object
        """
        self.cond.Nwppc_rad = self.si_Nwpc1_rad.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wwire(self):
        """Signal to update the value of Wwire according to the line edit

        Parameters
        ----------
        self : PCondType11
            A PCondType11 object
        """
        self.cond.Wwire = self.lf_Wwire.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Hwire(self):
        """Signal to update the value of Hwire according to the line edit

        Parameters
        ----------
        self : PCondType11
            A PCondType11 object
        """
        self.cond.Hwire = self.lf_Hwire.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wins_coil(self):
        """Signal to update the value of Wins_coil according to the line edit

        Parameters
        ----------
        self : PCondType11
            A PCondType11 object
        """
        self.cond.Wins_coil = self.lf_Wins_coil.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wins_wire(self, Wins_wire=-1):
        """Signal to update the value of Wwire according to the line edit

        Parameters
        ----------
        self : PCondType11
            A PCondType11 object
        """
        if Wins_wire == -1:
            Wins_wire = self.lf_Wins_wire.value()
        self.cond.Wins_wire = Wins_wire
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Lewout(self):
        """Signal to update the value of Lewout according to the line edit

        Parameters
        ----------
        self : PCondType11
            A PCondType11 object
        """
        self.lam.winding.Lewout = self.lf_Lewout.value()
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

        cond = lam.winding.conductor
        # Check that everything is set
        if cond.Nwppc_tan is None:
            return "Strands in tangential direction must be set"
        elif cond.Nwppc_rad is None:
            return "Strands in radial direction must be set"
        elif cond.Wwire is None:
            if cond.Nwppc_tan * cond.Nwppc_rad > 1:
                return "Strand width must be set"
            else:
                return "Conductor width must be set"
        elif cond.Hwire is None:
            if cond.Nwppc_tan * cond.Nwppc_rad > 1:
                return "Strand height must be set"
            else:
                return "Conductor height must be set"
        elif lam.winding.Lewout is None:
            return "End winding length must be set"
