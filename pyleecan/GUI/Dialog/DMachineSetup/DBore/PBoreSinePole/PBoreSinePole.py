# -*- coding: utf-8 -*-

import qtpy.QtCore
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget
from qtpy.QtGui import QPixmap
from ......Classes.BoreSinePole import BoreSinePole
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.DBore.PBoreSinePole.Gen_PBoreSinePole import (
    Gen_PBoreSinePole,
)
from numpy import pi

translate = qtpy.QtCore.QCoreApplication.translate


class PBoreSinePole(Gen_PBoreSinePole, QWidget):
    """Page to set the BoreSinePole"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for bore combobox
    bore_name = "Bore Sine Pole"
    bore_type = BoreSinePole

    def __init__(self, lamination=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PBoreSinePole
            A PBoreSinePole widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.lamination = lamination
        self.bore = lamination.bore
        if self.bore.N is None or self.bore.N == 0:
            self.bore.N = 2 * lamination.get_pole_pair_number()

        if self.bore.k is None or self.bore.k == 0:
            self.bore.k = 1
        if self.bore.alpha is None:
            self.bore.alpha = 0

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_delta_d.unit = "m"
        self.lf_delta_q.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_delta_d,
            self.unit_delta_q,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.si_N.setValue(self.bore.N)
        self.lf_W0.setValue(self.bore.W0)
        self.lf_k.setValue(self.bore.k if self.bore.k else 1)
        self.lf_delta_d.setValue(self.bore.delta_d)
        self.lf_delta_q.setValue(self.bore.delta_q)

        # Display the main output of the bore (surface, height...)
        self.w_out.comp_output()

        # Connect the signal/bore
        self.si_N.editingFinished.connect(self.set_N)
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_k.editingFinished.connect(self.set_k)
        self.lf_delta_d.editingFinished.connect(self.set_delta_d)
        self.lf_delta_q.editingFinished.connect(self.set_delta_q)

    def set_N(self):
        """Signal to update the value of N according to the line edit

        Parameters
        ----------
        self : PBoreFlower
            A PBoreFlower object
        """
        self.bore.N = self.si_N.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PBoreSinePole
            A PBoreSinePole object
        """
        self.bore.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_k(self):
        """Signal to update the value of k according to the line edit

        Parameters
        ----------
        self : PBoreSinePole
            A PBoreSinePole object
        """
        self.bore.k = self.lf_k.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_delta_d(self):
        """Signal to update the value of delta_d according to the line edit

        Parameters
        ----------
        self : PBoreSinePole
            A PBoreSinePole object
        """
        self.bore.delta_d = self.lf_delta_d.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_delta_q(self):
        """Signal to update the value of delta_q according to the line edit

        Parameters
        ----------
        self : PBoreSinePole
            A PBoreSinePole object
        """
        self.bore.delta_q = self.lf_delta_q.value()
        self.w_out.comp_output()
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
        if lam.bore.W0 is None:
            return "You must set W0 !"
        elif lam.bore.k is None:
            return "You must set k !"
        elif lam.bore.delta_d is None:
            return "You must set delta_d !"
        elif lam.bore.delta_q is None:
            return "You must set delta_q !"
        elif lam.bore.alpha is None:
            lam.bore.alpha = 0

        # Check that everything is set right
        # Constraints
        try:
            lam.bore.get_bore_line()
        except Exception as error:
            return str(error)
