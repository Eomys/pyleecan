# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWidget
from logging import getLogger


from .....loggers import GUI_LOG_NAME
from .....GUI import gui_option
from .....Classes.MachineIPMSM import MachineIPMSM
from .....GUI.Dialog.DMachineSetup.DBore.DBore import DBore
from .....GUI.Dialog.DMachineSetup.DNotchTab.DNotchTab import DNotchTab
from .....GUI.Dialog.DMachineSetup.DAVDuct.DAVDuct import DAVDuct
from .....GUI.Dialog.DMachineSetup.SLamShape.Gen_SLamShape import Gen_SLamShape


class SLamShape(Gen_SLamShape, QWidget):
    """Step to define the Lamination Shape and parameters"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Lamination"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SLamShape
            A SLamShape widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set Help URL
        # self.b_help.url = "https://pyleecan.org/winding.convention.html"

        # Saving arguments
        self.machine = machine
        self.material_dict = material_dict
        self.is_stator = is_stator

        # Set FloatEdit unit
        self.lf_L1.unit = "m"
        self.lf_Wrvd.unit = "m"
        self.u = gui_option.unit
        self.unit_L1.setText("[" + self.u.get_m_name() + "]")
        self.unit_Wrvd.setText("[" + self.u.get_m_name() + "]")

        # Get the correct object to set
        if self.is_stator:
            self.obj = machine.stator
            if self.obj.Kf1 is None:
                self.obj.Kf1 = 0.95  # Defaut value
        else:  # Rotor use Stator parameters as default
            self.obj = machine.rotor
            if self.obj.L1 is None:
                # Default value for rotor is the stator one
                self.obj.L1 = self.machine.stator.L1
            if self.obj.Kf1 is None:
                # Default value for rotor is the stator one
                self.obj.Kf1 = self.machine.stator.Kf1
        self.lf_L1.setValue(self.obj.L1)
        self.lf_Kf1.setValue(self.obj.Kf1)

        # Material setup
        self.w_mat.setText("Lamination Material")
        self.w_mat.def_mat = "M400-50A"
        self.w_mat.update(self.obj, "mat_type", self.material_dict)

        # Ventilation setup
        if self.obj.axial_vent is None:
            self.obj.axial_vent = list()
        self.update_avd_text()
        if len(self.obj.axial_vent) > 0 and self.obj.axial_vent[0].Zh > 0:
            self.g_axial.setChecked(True)

        if self.obj.Nrvd is None or self.obj.Nrvd == 0:
            self.si_Nrvd.setValue(0)
        else:
            self.si_Nrvd.setValue(self.obj.Nrvd)
            self.g_radial.setChecked(True)

        if self.obj.Wrvd is None or self.obj.Wrvd == 0:
            self.lf_Wrvd.setValue(0)
        else:
            self.lf_Wrvd.setValue(self.obj.Wrvd)
            self.g_radial.setChecked(True)

        # Notches setup
        if self.obj.notch is None:
            self.obj.notch = list()
        if len(self.obj.notch) > 0:
            self.g_notches.setChecked(True)
        self.update_notches_text()

        # Bore Setup
        if self.obj.bore is not None:
            self.g_bore.setChecked(True)

        # Only for IPMSM rotor
        if not is_stator and isinstance(self.machine, MachineIPMSM):
            self.g_bore.show()
        else:
            self.g_bore.hide()

        # Setup Output
        self.update_graph()
        self.update_lenght()  # Update out_length if possible

        # Connecting the signal
        self.lf_L1.editingFinished.connect(self.set_L1)
        self.lf_Kf1.editingFinished.connect(self.set_Kf1)
        self.g_radial.toggled.connect(self.enable_rad_vent)
        self.g_axial.toggled.connect(self.enable_ax_vent)
        self.b_axial_duct.clicked.connect(self.set_avd)
        self.g_notches.toggled.connect(self.enable_notches)
        self.b_notch.clicked.connect(self.set_notches)
        self.g_bore.toggled.connect(self.enable_bore)
        self.b_bore.clicked.connect(self.set_bore)
        self.si_Nrvd.editingFinished.connect(self.set_Nrvd)
        self.lf_Wrvd.editingFinished.connect(self.set_Wrvd)
        self.w_mat.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        self.saveNeeded.emit()

    def set_L1(self):
        """Signal to update the value of L1 according to the line edit

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
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
        self : SLamShape
            A SLamShape object
        """
        self.obj.Kf1 = self.lf_Kf1.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def enable_rad_vent(self, is_checked):
        """Clear radial vent value if g_radial is unselected

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        is_checked : bool
            State of the g_radial checkbox
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
        """Clear axial vent value if g_axial is unselected

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        is_checked : bool
            State of the g_axial checkbox
        """
        if not is_checked:
            self.obj.axial_vent = list()  # Default empty
            self.update_avd_text()
            self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_avd(self):
        """Open the GUI to allow the edition of the axial ventilation duct

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        self.avd_win = DAVDuct(self.obj)
        self.avd_win.show()
        self.avd_win.accepted.connect(self.validate_avd)

    def validate_avd(self):
        """Validate the ventilation

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        # self.obj.axial_vent = self.avd_win.vent
        self.update_avd_text()
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_avd_text(self):
        """Update the text with the current number of axial vent

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
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
        self : SLamShape
            A SLamShape object
        """
        self.obj.Nrvd = self.si_Nrvd.value()
        self.update_lenght()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wrvd(self):
        """Signal to update the value of Wrvd according to the line edit

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        self.obj.Wrvd = self.lf_Wrvd.value()
        self.update_lenght()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def enable_notches(self):
        """Clear notches values if g_notches is unselected"""
        if not self.g_notches.isChecked():
            # remove notches
            self.obj.notch = list()
            self.update_notches_text()
            self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_notches(self):
        """Opens widget to define notches to add to the lamination

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        self.notches_win = DNotchTab(self.machine, self.is_stator)
        self.notches_win.show()
        self.notches_win.accepted.connect(self.validate_notches)

    def validate_notches(self):
        """validates the notches defined by the user
        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        self.obj.notch = self.notches_win.obj.notch
        self.notches_win = None
        self.update_notches_text()
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_notches_text(self):
        """Update the text with the current number of notches

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        Nset = len(self.obj.notch)
        Nnotch = 0
        for notch in self.obj.notch:
            Nnotch += notch.notch_shape.Zs
        self.out_notch.setText(str(Nset) + " set (" + str(Nnotch) + " notches)")

    def enable_bore(self):
        """Clear bore if g_bore is unselected"""
        if not self.g_notches.isChecked():
            self.obj.bore = None
            self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_bore(self):
        """Opens widget to define bore to add to the lamination

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        self.bore_win = DBore(self.obj)
        self.bore_win.show()
        self.bore_win.accepted.connect(self.validate_bore)

    def validate_bore(self):
        """validates the bore shape defined by the user
        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        self.obj.bore = self.bore_win.lam.bore
        self.bore_win = None
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_lenght(self):
        """Update the text of out_length

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        if self.obj.is_stator:  # Adapt the text to the current lamination
            lam_txt = self.tr("Stator total length = ")
        else:
            lam_txt = self.tr("Rotor total length = ")

        if self.obj.L1 is None or self.obj.Nrvd is None or self.obj.Wrvd is None:
            self.out_length.setText(lam_txt + "?")
        else:
            length = format(
                self.u.get_m(self.obj.L1 + self.obj.Nrvd * self.obj.Wrvd), ".4g"
            )
            self.out_length.setText(lam_txt + length + " [" + self.u.get_m_name() + "]")

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
        try:
            if lamination.L1 is None:
                return "You must set L1 !"
            elif lamination.Kf1 is None:
                return "You must set Kf1 !"
        except Exception as e:
            return str(e)

    def check_gui(self):
        """Check that the widget are set right according to the current machine

        Parameters
        ----------
        self : SLamShape
            A SLamShape object
        """
        if self.g_radial.isChecked() and self.obj.Nrvd is None:
            return self.tr("You must set Nrvd or unchecked " "radial Ventilation !")
        if self.g_radial.isChecked() and self.obj.Wrvd is None:
            return self.tr("You must set Wrvd or unchecked " "radial Ventilation !")
        if self.g_axial.isChecked() and len(self.obj.axial_vent) == 0:
            return self.tr(
                "You must add some Axial Ventilation Ducts or "
                "unchecked Axial Ventilation !"
            )

        if not self.g_radial.isChecked():
            self.obj.Nrvd = 0
            self.obj.Wrvd = 0
        if not self.g_axial.isChecked():
            self.obj.axial_vent = list()  # Default empty

    def update_graph(self, is_lam_only=False):
        """Plot the lamination with/without the winding"""
        self.w_viewer.axes.clear()
        # Plot the lamination in the viewer fig
        try:
            self.obj.plot(
                fig=self.w_viewer.fig,
                ax=self.w_viewer.axes,
                is_show_fig=False,
                is_lam_only=is_lam_only,
            )
        except Exception as e:
            if self.obj.is_stator:  # Adapt the text to the current lamination
                err_msg = "Error while plotting machine in Stator Lamination:\n" + str(
                    e
                )
            else:
                err_msg = "Error while plotting machine in Rotor Lamination:\n" + str(e)
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(
                self,
                self.tr("Error"),
                err_msg,
            )

        # Update the Graph
        self.w_viewer.axes.set_axis_off()
        self.w_viewer.axes.axis("equal")
        self.w_viewer.draw()
