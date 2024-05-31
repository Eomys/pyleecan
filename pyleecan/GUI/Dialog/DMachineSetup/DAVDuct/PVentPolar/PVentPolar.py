# -*- coding: utf-8 -*-

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget

from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.DAVDuct.PVentPolar.Gen_PVentPolar import (
    Gen_PVentPolar,
)
from ......Classes.VentilationPolar import VentilationPolar
from numpy import pi


class PVentPolar(Gen_PVentPolar, QWidget):
    """Page to setup the Ventilation Polar"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Hole combobox
    hole_name = "Polar"
    hole_type = VentilationPolar

    def __init__(self, lam=None, vent=None):
        """Initialize the widget according the current lamination

        Parameters
        ----------
        self : PVentPolar
            A PVentPolar widget
        lam : Lamination
            current lamination to edit
        vent : VentPolar
            current ventilation to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set FloatEdit unit
        self.lf_H0.unit = "m"
        self.lf_D0.unit = "m"

        self.lam = lam
        self.vent = vent

        # Fill the fields with the machine values (if they're filled)
        if self.vent.Zh is None:
            self.vent.Zh = 8
        self.si_Zh.setValue(self.vent.Zh)
        self.lf_H0.setValue(self.vent.H0)
        self.lf_D0.setValue(self.vent.D0)
        self.lf_W1.setValue(self.vent.W1)  # default unit is rad

        # Display the main output of the vent
        self.w_out.comp_output()

        # Set unit name (m ou mm)
        wid_list = [self.unit_H0, self.unit_D0]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Connect the signal
        self.si_Zh.valueChanged.connect(self.set_Zh)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_D0.editingFinished.connect(self.set_D0)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.c_W1_unit.currentIndexChanged.connect(self.set_W1_unit)

    def set_Zh(self):
        """Signal to update the value of Zh according to the line edit

        Parameters
        ----------
        self : PVentPolar
            A PVentPolar object
        """
        self.vent.Zh = self.si_Zh.value()
        self.w_out.comp_output()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PVentPolar
            A PVentPolar object
        """
        self.vent.H0 = self.lf_H0.value()
        self.w_out.comp_output()

    def set_D0(self):
        """Signal to update the value of D0 according to the line edit

        Parameters
        ----------
        self : PVentPolar
            A PVentPolar object
        """
        self.vent.D0 = self.lf_D0.value()
        self.w_out.comp_output()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PVentPolar
            A PVentPolar object
        """
        if self.lf_W1.value() is None:
            self.vent.W1 = 0
        elif self.c_W1_unit.currentText() == "[rad]":
            self.vent.W1 = self.lf_W1.value()
        else:
            self.vent.W1 = self.lf_W1.value() * pi / 180
        self.w_out.comp_output()

    def set_W1_unit(self):
        """Change current unit of W1"""
        if self.c_W1_unit.currentText() == "[rad]":
            self.lf_W1.validator().setTop(6.29)
        else:
            self.lf_W1.validator().setTop(360)
        self.set_W1()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PVentPolar
            A PVentPolar object

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if self.vent.Zh is None:
            return self.tr("You must set Zh !")
        elif self.vent.H0 is None:
            return self.tr("You must set H0 !")
        elif self.vent.D0 is None:
            return self.tr("You must set D0 !")
        elif self.vent.W1 is None:
            return self.tr("You must set W1 !")
        elif self.vent.Alpha0 is None:
            self.vent.Alpha0 = 0
        return None
