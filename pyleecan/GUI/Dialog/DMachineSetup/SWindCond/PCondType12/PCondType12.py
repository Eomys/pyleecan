# -*- coding: utf-8 -*-

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from ......Classes.CondType12 import CondType12
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWindCond.PCondType12.Gen_PCondType12 import (
    Gen_PCondType12,
)


class PCondType12(Gen_PCondType12, QWidget):
    """Page to set the Conductor Type 12"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for SWindCond combobox
    cond_type = CondType12
    cond_name = "Random Round Wire"

    def __init__(self, lamination=None):
        """Initialize the GUI according to conductor

        Parameters
        ----------
        self : PCondType12
            A PCondType12 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set FloatEdit unit
        self.lf_Wwire.unit = "m"
        self.lf_Wins_wire.unit = "m"
        self.lf_Wins_cond.unit = "m"
        self.lf_Lewout.unit = "m"
        self.u = gui_option.unit

        # Set unit name (m ou mm)
        wid_list = [
            self.unit_Wwire,
            self.unit_Wins_cond,
            self.unit_Wins_wire,
            self.unit_Lewout,
        ]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lam = lamination
        if self.lam.winding.conductor is None:
            self.lam.winding.conductor = CondType12()
            self.lam.winding.conductor._set_None()
        self.cond = self.lam.winding.conductor

        # Make sure that isinstance(cond, CondType12)
        if self.cond is None or not isinstance(self.cond, CondType12):
            self.cond = CondType12()
            self.cond._set_None()

        if self.cond.Nwppc is None:
            self.cond.Nwppc = 1  # Default value
        self.si_Nwpc1.setValue(self.cond.Nwppc)

        self.lf_Wwire.setValue(self.cond.Wwire)
        if self.cond.Wins_wire is None:
            self.cond.Wins_wire = 0  # Default value
        else:
            self.g_ins.setChecked(True)
        self.lf_Wins_wire.setValue(self.cond.Wins_wire)
        self.lf_Wins_cond.setValue(self.cond.Wins_cond)
        self.lf_Lewout.validator().setBottom(0)
        if self.lam.winding.Lewout is None:
            self.lam.winding.Lewout = 0
        self.lf_Lewout.setValue(self.lam.winding.Lewout)

        self.update_ins_layout()

        # Display the conductor main output
        self.w_out.comp_output()

        # Connect the signal/slot
        self.g_ins.toggled.connect(self.update_ins_layout)
        self.si_Nwpc1.editingFinished.connect(self.set_Nwppc)
        self.lf_Wwire.editingFinished.connect(self.set_Wwire)
        self.lf_Wins_wire.editingFinished.connect(self.set_Wins_wire)
        self.lf_Wins_cond.editingFinished.connect(self.set_Wins_cond)
        self.lf_Lewout.editingFinished.connect(self.set_Lewout)

    def update_ins_layout(self):
        if self.g_ins.isChecked():
            self.in_Wins_cond.show()
            self.lf_Wins_cond.show()
            self.unit_Wins_cond.show()
            self.in_Wins_wire.show()
            self.lf_Wins_wire.show()
            self.unit_Wins_wire.show()
            self.set_Wins_wire()
            self.set_Wins_cond()
        else:
            self.in_Wins_cond.hide()
            self.lf_Wins_cond.hide()
            self.unit_Wins_cond.hide()
            self.in_Wins_wire.hide()
            self.lf_Wins_wire.hide()
            self.unit_Wins_wire.hide()
            self.set_Wins_wire(Wins_wire=0)
            if self.lf_Wwire.value() is not None:
                self.set_Wins_cond(Wins_cond=3 * self.lf_Wwire.value())

    def set_Nwppc(self):
        """Signal to update the value of Nwppc according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        self.cond.Nwppc = self.si_Nwpc1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wwire(self):
        """Signal to update the value of Wwire according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        self.cond.Wwire = self.lf_Wwire.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wins_wire(self, Wins_wire=None):
        """Signal to update the value of Wins_wire according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        if Wins_wire is None:
            Wins_wire = self.lf_Wins_wire.value()
        self.cond.Wins_wire = Wins_wire
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wins_cond(self, Wins_cond=None):
        """Signal to update the value of Wins_cond according to the line edit

        Parameters
        ----------
        self : PCondType12
            A PCondType12 object
        """
        if Wins_cond is None:
            Wins_cond = self.lf_Wins_cond.value()
        self.cond.Wins_cond = Wins_cond
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
        if cond.Nwppc is None:
            return "You must set Nwppc !"
        elif cond.Wwire is None:
            return "You must set Wwire !"
        elif cond.Wins_wire is None:
            return "You must set Wins_wire !"
        elif cond.Wins_cond is None:
            return "You must set Wins_cond !"
        elif cond.Wins_cond < cond.Wwire:
            return "You must have Wins_cond >= Wwire !"
        elif lam.winding.Lewout is None:
            return "You must set Lewout !"
