# -*- coding: utf-8 -*-

from matplotlib.pyplot import gcf
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget

from .....Classes.LamHole import LamHole
from .....Classes.Lamination import Lamination
from .....Classes.LamSlotMag import LamSlotMag
from .....GUI import gui_option
from .....GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.DAVDuct import DAVDuct
from .....GUI.Dialog.DMachineSetup.SLamParam.Gen_SLamParam import Gen_SLamParam


class SLamParam(Gen_SLamParam, QWidget):
    """Step to setup the main lamination parameters
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for the DMachineSetup nav
    step_name = "Lamination"

    def __init__(self, machine, matlib=[], is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SLamParam
            A SLamParam widget
        machine : Machine
            current machine to edit
        matlib : list
            List of available Material
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.matlib = matlib
        self.is_stator = is_stator

        # Set FloatEdit unit
        self.lf_L1.unit = "m"
        self.lf_Wrvd.unit = "m"
        self.u = gui_option.unit
        self.unit_L1.setText(self.u.get_m_name())
        self.unit_Wrvd.setText(self.u.get_m_name())

        # Get the correct object to set
        if self.is_stator:
            self.obj = machine.stator
            if self.obj.Kf1 is None:
                self.obj.Kf1 = 0.95  # Defaut value
        else:
            self.obj = machine.rotor
            if self.obj.L1 is None:
                # Default value for rotor is the stator one
                self.obj.L1 = self.machine.stator.L1
            if self.obj.Kf1 is None:
                # Default value for rotor is the stator one
                self.obj.Kf1 = self.machine.stator.Kf1

        self.w_mat.update(self.obj, "mat_type", matlib)

        self.lf_L1.setValue(self.obj.L1)
        self.lf_Kf1.setValue(self.obj.Kf1)

        # Ventilation setup
        self.update_avd_text()
        if len(self.obj.axial_vent) > 0 and self.obj.axial_vent[0].Zh > 0:
            self.g_ax_vent.setChecked(True)

        if self.obj.Nrvd is None or self.obj.Nrvd == 0:
            self.si_Nrvd.setValue(0)
        else:
            self.si_Nrvd.setValue(self.obj.Nrvd)
            self.g_rad_vent.setChecked(True)

        if self.obj.Wrvd is None or self.obj.Wrvd == 0:
            self.lf_Wrvd.setValue(0)
        else:
            self.lf_Wrvd.setValue(self.obj.Wrvd)
            self.g_rad_vent.setChecked(True)

        self.update_lenght()  # Update out_length if possible

        # Connecting the signal
        self.lf_L1.editingFinished.connect(self.set_L1)
        self.lf_Kf1.editingFinished.connect(self.set_Kf1)
        self.g_rad_vent.toggled.connect(self.enable_rad_vent)
        self.g_ax_vent.toggled.connect(self.enable_ax_vent)
        self.b_axial_duct.clicked.connect(self.set_avd)
        self.si_Nrvd.editingFinished.connect(self.set_Nrvd)
        self.lf_Wrvd.editingFinished.connect(self.set_Wrvd)
        self.b_plot.clicked.connect(self.s_plot)
        self.w_mat.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        self.saveNeeded.emit()

    def set_L1(self):
        """Signal to update the value of L1 according to the line edit

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        if self.lf_L1.value() != self.obj.L1:
            self.obj.L1 = self.lf_L1.value()
            self.update_lenght()
            # Notify the machine GUI that the machine has changed
            self.saveNeeded.emit()

    def set_Kf1(self):
        """Signal to update the value of Kf1 according to the line edit

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        self.obj.Kf1 = self.lf_Kf1.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def enable_rad_vent(self, is_checked):
        """Clear radial vent value if g_rad_vent is unselected

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        is_checked : bool
            State of the g_rad_vent checkbox
        """
        if not is_checked:
            self.lf_Wrvd.setValue(0)
            self.si_Nrvd.setValue(0)
            self.set_Nrvd()
            self.set_Wrvd()
            self.update_lenght()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def enable_ax_vent(self, is_checked):
        """Clear axial vent value if g_ax_vent is unselected

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        is_checked : bool
            State of the g_ax_vent checkbox
        """
        if not is_checked:
            self.obj.axial_vent = list()  # Default empty
            self.update_avd_text()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_avd(self):
        """Open the GUI to allow the edition of the axial ventilation duct

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        self.avd_win = DAVDuct(self.obj)
        return_code = self.avd_win.exec_()
        if return_code == QDialog.Accepted:
            # self.obj.axial_vent = self.avd_win.vent
            self.update_avd_text()
            # Notify the machine GUI that the machine has changed
            self.saveNeeded.emit()

    def update_avd_text(self):
        """Update the text with the current number of axial vent

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        Nset = 0
        Nduct = 0
        for vent in self.obj.axial_vent:
            Nset += 1
            Nduct += vent.Zh
        self.out_axial_duct.setText(
            self.tr("Axial: ", "Part of Axial: X set (Y ducts)")
            + str(Nset)
            + self.tr(" set (", "Part of Axial: X set (Y ducts)")
            + str(Nduct)
            + self.tr(" ducts)", "Part of Axial: X set (Y ducts)")
        )

    def set_Nrvd(self):
        """Signal to update the value of Nrvd according to the spinbox

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        self.obj.Nrvd = self.si_Nrvd.value()
        self.update_lenght()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wrvd(self):
        """Signal to update the value of Wrvd according to the line edit

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        self.obj.Wrvd = self.lf_Wrvd.value()
        self.update_lenght()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_lenght(self):
        """Update the text of out_length

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        if self.obj.is_stator:  # Adapt the text to the current lamination
            lam_txt = self.tr("Stator total length = L1 + Nrvd * Wrvd = ")
        else:
            lam_txt = self.tr("Rotor total length = L1 + Nrvd * Wrvd = ")

        if self.obj.L1 is None or self.obj.Nrvd is None or self.obj.Wrvd is None:
            self.out_length.setText(lam_txt + "?")
        else:
            length = format(
                self.u.get_m(self.obj.L1 + self.obj.Nrvd * self.obj.Wrvd), ".4g"
            )
            self.out_length.setText(lam_txt + length + " " + self.u.get_m_name())

    @staticmethod
    def check(lamination):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lamination.L1 is None:
            return "You must set L1 !"
        elif lamination.Kf1 is None:
            return "You must set Kf1 !"

    def check_gui(self):
        """Check that the widget are set right according to the current machine

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """
        if self.g_rad_vent.isChecked() and self.obj.Nrvd is None:
            return self.tr("You must set Nrvd or unchecked " "radial Ventilation !")
        if self.g_rad_vent.isChecked() and self.obj.Wrvd is None:
            return self.tr("You must set Wrvd or unchecked " "radial Ventilation !")
        if self.g_ax_vent.isChecked() and len(self.obj.axial_vent) == 0:
            return self.tr(
                "You must add some Axial Ventilation Ducts or "
                "unchecked Axial Ventilation !"
            )

        if not self.g_rad_vent.isChecked():
            self.obj.Nrvd = 0
            self.obj.Wrvd = 0
        if not self.g_ax_vent.isChecked():
            self.obj.axial_vent = list()  # Default empty

    def s_plot(self):
        """Plot the lamination (radial and axial) if possible

        Parameters
        ----------
        self : SLamParam
            A SLamParam object
        """

        # We use an empty lamination for the plot to avoid problem with magnet
        # or winding which are not setup yet
        if self.obj.Rint is None:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Unable to plot the lamination " "(Rint missing)"),
            )
        elif self.obj.Rext is None:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Unable to plot the lamination " "(Rext missing)"),
            )
        else:
            plot_obj = Lamination(
                Rint=self.obj.Rint, Rext=self.obj.Rext, axial_vent=self.obj.axial_vent
            )
            if self.obj.is_stator is not None:
                plot_obj.is_stator = self.obj.is_stator
            plot_obj.plot()
            gcf().canvas.set_window_title(
                self.tr("Lamination (without slots) Front view")
            )
