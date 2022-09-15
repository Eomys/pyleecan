# -*- coding: utf-8 -*-

import PySide2.QtCore
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap
from ......Classes.BoreFlower import BoreFlower
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.DBore.PBoreFlower.Gen_PBoreFlower import (
    Gen_PBoreFlower,
)
from numpy import pi

translate = PySide2.QtCore.QCoreApplication.translate


class PBoreFlower(Gen_PBoreFlower, QWidget):
    """Page to set the BoreFlower"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for bore combobox
    bore_name = "Bore Flower"
    bore_type = BoreFlower

    def __init__(self, lamination=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PBoreFlower
            A PBoreFlower widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.lamination = lamination
        self.bore = lamination.bore
        self.bore.N = self.lamination.get_pole_pair_number() *2

        # Set FloatEdit unit
        self.lf_Rarc.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_Rarc,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_Rarc.setValue(self.bore.Rarc)
        self.lf_alpha.setValue(self.bore.alpha)

        # Display the main output of the bore (surface, height...)
        self.w_out.comp_output()

        # Connect the signal/bore
        self.lf_Rarc.editingFinished.connect(self.set_Rarc)
        self.lf_alpha.editingFinished.connect(self.set_alpha)
        self.c_alpha_unit.currentIndexChanged.connect(self.set_alpha)

    def set_Rarc(self):
        """Signal to update the value of Rarc according to the line edit

        Parameters
        ----------
        self : PBoreFlower
            A PBoreFlower object
        """
        self.bore.Rarc = self.lf_Rarc.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_alpha(self):
        """Signal to update the value of alpha according to the line edit

        Parameters
        ----------
        self : PBoreFlower
            A PBoreFlower object
        """
        if self.c_alpha_unit.currentIndex() == 0:  # rad
            self.bore.alpha = self.lf_alpha.value()
        else:  # deg
            self.bore.alpha = self.lf_alpha.value() * pi / 180
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamboreWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.bore.Rarc is None:
            return "You must set Rarc !"
        elif lam.bore.alpha is None:
            return "You must set alpha !"

        # Check that everything is set right
        # Constraints
        try:
            lam.bore.get_bore_line()
        except Exception as error:
            return str(error)
