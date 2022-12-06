# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QWidget, QFileDialog
from logging import getLogger
from .....loggers import GUI_LOG_NAME
from .....Classes.Winding import Winding
from .....Classes.WindingUD import WindingUD
from .....Classes.MachineSRM import MachineSRM
from .....Classes.MachineWRSM import MachineWRSM
from .....GUI.Dialog.DMachineSetup.SWinding.Gen_SWinding import Gen_SWinding
from .....Methods.Machine.Winding import WindingError
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon


class SWinding(Gen_SWinding, QWidget):
    """Step to define the winding pattern & circuit"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for DMachineSetup nav
    step_name = "Winding"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWinding
            A SWinding widget
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

        # Fill the fields with the machine values (if they're filled)
        if self.is_stator:
            self.obj = machine.stator
            self.b_plot_mmf.setText("Plot Stator Unit MMF")
        else:
            self.obj = machine.rotor
            self.b_plot_mmf.setText("Plot Rotor Unit MMF")
        self.in_Zs.setText("Slot number=" + str(self.obj.get_Zs()))
        if isinstance(machine, MachineSRM):
            self.in_p.hide()  # p is not meaningful for SRM
        else:
            self.in_p.setText(
                "Pole pair number=" + str(self.obj.get_pole_pair_number())
            )

        if isinstance(machine, MachineWRSM) and not self.is_stator:
            # Enforce tooth winding for WRSM rotor
            self.si_qs.setEnabled(False)
            self.obj.winding.qs = 1
            # Two tangential layer enforce
            self.si_Nlayer.setEnabled(False)
            self.obj.winding.Nlayer = 2
            self.obj.winding.is_change_layer = False
            self.is_change_layer.setEnabled(False)
            self.obj.winding.coil_pitch = 1
            self.si_coil_pitch.setEnabled(False)
            self.in_Zs.hide()  # =2*p
            self.b_preview.setEnabled(False)
            # Enforce star of slot
            self.c_wind_type.setEnabled(False)
            self.c_wind_type.setCurrentIndex(0)
            # No plot_mmf
            self.b_plot_mmf.hide()

        # Pattern Group setup
        if self.obj.winding is None:
            self.obj.winding = Winding()  # Default is Star of Slot
        if type(self.obj.winding) is Winding:  # Star of Slot
            self.c_wind_type.setCurrentIndex(0)
            self.hide_star_widget(False)
            # qs
            if self.obj.winding.qs is None:  # default value
                self.obj.winding.qs = 3
            self.si_qs.setValue(self.obj.winding.qs)
            # Nlayer
            if self.obj.winding.Nlayer is None:
                self.obj.winding.Nlayer = 1
            self.si_Nlayer.setValue(self.obj.winding.Nlayer)
            # Coil_pitch
            self.show_layer_widget()
            # Ntcoil
            if self.obj.winding.Ntcoil is None:
                self.obj.winding.Ntcoil = 1
            self.si_Ntcoil.setValue(self.obj.winding.Ntcoil)
        elif type(self.obj.winding) is WindingUD:  # WindingUD
            self.c_wind_type.setCurrentIndex(1)
            self.hide_star_widget(True)
        # Npcp
        if self.obj.winding.Npcp is None:
            self.obj.winding.Npcp = 1  # Default value
        self.si_Npcp.setValue(self.obj.winding.Npcp)

        # Edit Group setup
        if self.obj.winding.is_reverse_wind is None:
            self.obj.winding.is_reverse_wind = False
        if self.obj.winding.is_reverse_wind:
            self.is_reverse.setCheckState(Qt.Checked)
        else:
            self.is_reverse.setCheckState(Qt.Unchecked)
        # Nslot_shift_wind
        if self.obj.winding.Nslot_shift_wind is None:
            self.obj.winding.Nslot_shift_wind = 0
        self.si_Nslot.setValue(self.obj.winding.Nslot_shift_wind)
        # is_reverse_layer
        if self.obj.winding.is_reverse_layer is None:
            self.obj.winding.is_reverse_layer = False
        if self.obj.winding.is_reverse_layer:
            self.is_reverse_layer.setCheckState(Qt.Checked)
        else:
            self.is_reverse_layer.setCheckState(Qt.Unchecked)
        # is_change_layer
        if self.obj.winding.is_change_layer is None:
            self.obj.winding.is_change_layer = False
        if self.obj.winding.is_change_layer:
            self.is_change_layer.setCheckState(Qt.Checked)
        else:
            self.is_change_layer.setCheckState(Qt.Unchecked)
        # is_permute_B_C
        if self.obj.winding.is_permute_B_C is None:
            self.obj.winding.is_permute_B_C = False
        if self.obj.winding.is_permute_B_C:
            self.is_permute_B_C.setCheckState(Qt.Checked)
        else:
            self.is_permute_B_C.setCheckState(Qt.Unchecked)

        # Update the GUI
        self.update_graph()
        self.comp_output()

        # Connect the signal/slot
        self.c_wind_type.currentIndexChanged.connect(self.set_type)
        self.si_Nlayer.valueChanged.connect(self.show_layer_widget)
        self.si_Npcp.editingFinished.connect(self.set_Npcp)
        self.si_Nslot.valueChanged.connect(self.set_Nslot)
        self.si_Ntcoil.valueChanged.connect(self.set_Ntcoil)
        self.is_reverse.stateChanged.connect(self.set_is_reverse_wind)
        self.is_reverse_layer.stateChanged.connect(self.set_is_reverse_layer)
        self.is_change_layer.stateChanged.connect(self.set_is_change_layer)
        self.is_permute_B_C.stateChanged.connect(self.set_is_permute_B_C)
        self.si_qs.valueChanged.connect(self.refresh_needed)
        self.si_Nlayer.valueChanged.connect(self.refresh_needed)
        self.si_coil_pitch.valueChanged.connect(self.refresh_needed)
        self.si_Ntcoil.valueChanged.connect(self.refresh_needed)
        self.si_Npcp.valueChanged.connect(self.refresh_needed)

        # self.b_edit_wind_mat.clicked.connect(self.s_edit_wind_mat)
        self.b_import.clicked.connect(self.s_import_csv)
        self.b_export.clicked.connect(self.s_export_csv)
        self.b_edit_wind_mat.hide()
        self.b_generate.clicked.connect(self.s_generate)
        self.b_preview.clicked.connect(self.s_plot)
        self.b_plot_mmf.clicked.connect(self.s_plot_mmf)

    def hide_star_widget(self, is_hide=True):
        """To display/hide the star of slot widgets"""
        if is_hide:
            self.in_Nlayer.hide()
            self.in_Ntcoil.hide()
            self.in_coil_pitch.hide()
            self.in_qs.hide()
            self.si_Nlayer.hide()
            self.si_Ntcoil.hide()
            self.si_coil_pitch.hide()
            self.si_qs.hide()
            self.b_generate.hide()
            self.b_import.show()
        else:
            self.in_Nlayer.show()
            self.in_Ntcoil.show()
            self.in_coil_pitch.show()
            self.in_qs.show()
            self.si_Nlayer.show()
            self.si_Ntcoil.show()
            self.si_coil_pitch.show()
            self.si_qs.show()
            self.b_generate.show()
            self.b_import.hide()

    def show_layer_widget(self):

        # Coil pitch (or coil span)
        if self.obj.winding.coil_pitch in [0, None]:
            if self.obj.winding.p is None:  # SRM
                self.obj.winding.coil_pitch = 1  # Tooth winding
            else:
                Zs = self.obj.slot.Zs
                qs = self.obj.winding.qs
                p = self.obj.winding.p
                # Number of slots per pole and per phase
                spp = Zs / (2 * p * qs)
                if spp > 0.5:
                    # distributed winding
                    self.obj.winding.coil_pitch = int(qs * spp)
                else:
                    # tooth concentrated winding
                    self.obj.winding.coil_pitch = 1
        self.si_coil_pitch.setValue(self.obj.winding.coil_pitch)

        if self.si_Nlayer.value() == 1:
            self.is_reverse_layer.hide()
            self.is_change_layer.hide()
        else:
            self.is_reverse_layer.show()
            self.is_change_layer.show()
            # is_reverse_layer
            if self.obj.winding.is_reverse_layer is None:
                self.obj.winding.is_reverse_layer = False
            if self.obj.winding.is_reverse_layer:
                self.is_reverse_layer.setCheckState(Qt.Checked)
            else:
                self.is_reverse_layer.setCheckState(Qt.Unchecked)
            # is_change_layer
            if self.obj.winding.is_change_layer is None:
                self.obj.winding.is_change_layer = False
            if self.obj.winding.is_change_layer:
                self.is_change_layer.setCheckState(Qt.Checked)
            else:
                self.is_change_layer.setCheckState(Qt.Unchecked)

    def refresh_needed(self):
        self.b_generate.setEnabled(True)

    def s_generate(self):
        # Update winding object
        self.obj.winding.qs = self.si_qs.value()
        self.obj.winding.Nlayer = self.si_Nlayer.value()
        self.obj.winding.coil_pitch = self.si_coil_pitch.value()
        self.obj.winding.Ntcoil = self.si_Ntcoil.value()
        if isinstance(self.machine, MachineSRM):
            if self.obj.slot.Zs % self.obj.winding.qs != 0:
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    "Error while creating the winding:\nZs must be a multiple of qs for SRM machine",
                )
                return
            # p is not defined for SRM => enforced to p=Zs/qs
            self.obj.winding.p = self.obj.slot.Zs // self.obj.winding.qs
        self.obj.winding.clean()  # Enforce now computation
        # Check winding
        try:
            self.obj.winding.get_connection_mat()
            self.b_generate.setEnabled(False)
        except Exception as e:
            QMessageBox().critical(
                self, self.tr("Error"), "Error while creating the winding:\n" + str(e)
            )
            self.comp_output()
            self.update_graph(is_lam_only=True)
            self.b_generate.setEnabled(True)
            return

        # Update GUI
        self.comp_output()
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_type(self, index):
        """Signal to update the winding type

        Parameters
        ----------
        self : SWinding
            A SWinding object
        index : int
            Index of selected type
        """

        init_dict = self.obj.winding.as_dict()
        if index == 0:  # Star of Slot
            self.obj.winding = Winding(init_dict=init_dict)
            # coil_pitch
            if self.obj.winding.coil_pitch is None:
                self.obj.winding.coil_pitch = 0
            self.si_coil_pitch.setValue(self.obj.winding.coil_pitch)
            # qs
            if self.obj.winding.qs is None:
                self.obj.winding.qs = 3
            self.si_qs.setValue(self.obj.winding.qs)
            # Ntcoil
            if self.obj.winding.Ntcoil is None:
                self.obj.winding.Ntcoil = 1
            self.si_Ntcoil.setValue(self.obj.winding.Ntcoil)

            self.si_Nlayer.setValue(self.obj.winding.Nlayer)
            self.obj.winding.clean()  # ­ Enforce new computation
            self.hide_star_widget(False)
        else:  # User Defined
            self.obj.winding = WindingUD(init_dict=init_dict)
            self.hide_star_widget(True)
        self.obj.winding.Npcp = self.si_Npcp.value()

    def set_Ntcoil(self):
        """Signal to update the value of Ntcoil according to the
        spinbox

        Parameters
        ----------
        self : SWinding
            A SWinding object
        """
        self.obj.winding.Ntcoil = self.si_Ntcoil.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Nslot(self):
        """Signal to update the value of Nslot_shift_wind according to the
        spinbox

        Parameters
        ----------
        self : SWinding
            A SWinding object
        """
        self.obj.winding.Nslot_shift_wind = self.si_Nslot.value()
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_reverse_wind(self, value):
        """Signal to update the value of is_reverse_wind according to the
        widget

        Parameters
        ----------
        self : SWinding
            A SWinding object
        value :
            New value of is_reverse_wind
        """

        value = self.is_reverse.isChecked()
        self.obj.winding.is_reverse_wind = value
        self.update_graph()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_reverse_layer(self, value):
        """Signal to update the value of is_reverse_layer according to the
        widget

        Parameters
        ----------
        self : SWinding
            A SWinding object
        value :
            New value of is_reverse_layer
        """

        value = self.is_reverse_layer.isChecked()
        self.obj.winding.is_reverse_layer = value
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_permute_B_C(self, value):
        """Signal to update the value of is_permute_B_C according to the
        widget

        Parameters
        ----------
        self : SWinding
            A SWinding object
        value :
            New value of is_permute_B_C
        """

        value = self.is_permute_B_C.isChecked()
        self.obj.winding.is_permute_B_C = value
        self.update_graph()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_change_layer(self, value):
        """Signal to update the value of is_change_layer according to the
        widget

        Parameters
        ----------
        self : SWinding
            A SWinding object
        value :
            New value of is_change_layer
        """

        value = self.is_change_layer.isChecked()
        self.obj.winding.is_change_layer = value
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Npcp(self):
        """Signal to update the value of Npcp according to the line edit

        Parameters
        ----------
        self : SWindParam
            A SWindParam object
        """
        self.obj.winding.Npcp = self.si_Npcp.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_export_csv(self):
        """Export the winding matrix to csv"""
        if self.machine.name is not None:
            name = self.machine.name + "_Winding.csv"
        else:
            name = "Winding.csv"
        save_file_path = QFileDialog.getSaveFileName(
            self, self.tr("Save file"), name, "CSV (*.csv);;All files (*.*)"
        )[0]
        try:
            self.obj.winding.export_to_csv(
                file_path=save_file_path, is_add_header=True, is_skip_empty=False
            )
        except Exception as e:
            QMessageBox().critical(
                self, self.tr("Error"), "Error while exporting the winding:\n" + str(e)
            )
            return

    def s_import_csv(self):
        """Import the winding matrix to csv"""
        load_path = str(
            QFileDialog.getOpenFileName(
                self, self.tr("Load file"), None, "CSV (*.csv);;All files (*.*)"
            )[0]
        )
        if load_path != "":
            try:
                self.obj.winding.import_from_csv(file_path=load_path)
                # Update GUI
                self.comp_output()
                self.update_graph()
                # Notify the machine GUI that the machine has changed
                self.saveNeeded.emit()
            except Exception as e:
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    "Error while importing the winding:\n" + str(e),
                )
                return

    def comp_output(self):
        """Update the shape and period Label to match the current winding setup

        Parameters
        ----------
        self : SWinding
            a SWinding object
        """

        wind = self.obj.winding  # For readability

        try:
            mmf_dir = self.obj.comp_mmf_dir()
            if mmf_dir == 1:
                mmf_dir = "CCW"
            elif mmf_dir == -1:
                mmf_dir = "CW"
            else:
                mmf_dir = "?"
        except Exception:  # Unable to compution the connection matrix
            mmf_dir = "?"
        self.out_rot_dir.setText(self.tr("Rotation direction: ") + mmf_dir)

        try:
            ms = str(self.obj.slot.Zs / (wind.p * wind.qs * 2.0))
        except TypeError:  # One of the value is None
            ms = "?"
        self.out_ms.setText(self.tr("Number of slots/pole/phase: ") + ms)
        if self.obj.is_stator:
            self.out_ms.setToolTip(self.tr("Zs / (2*p*qs)"))
        else:
            self.out_ms.setToolTip(self.tr("Zr / (2*p*qr)"))

        try:
            Nperw, _ = wind.get_periodicity()

        except Exception:  # Unable to compution the connection matrix
            Nperw = "?"

        self.out_Nperw.setText(self.tr("Winding periodicity: ") + str(Nperw))

        try:
            Ntspc = str(self.obj.winding.comp_Ntsp(self.obj.slot.Zs))
            Ntspc = Ntspc[:-2] if Ntspc[-2:] == ".0" else Ntspc
        except:
            Ntspc = "?"
        try:
            Ncspc = str(self.obj.winding.comp_Ncspc(self.obj.slot.Zs))
            Ncspc = Ncspc[:-2] if Ncspc[-2:] == ".0" else Ncspc
        except:
            Ncspc = "?"
        self.out_Ncspc.setText(self.tr("Number of coils Ncspc: ") + Ncspc)
        self.out_Ntspc.setText(self.tr("Number of turns Ntspc: ") + Ntspc)

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
                is_add_sign=True,
            )
        except Exception as e:
            if self.obj.is_stator:  # Adapt the text to the current lamination
                err_msg = "Error while plotting machine in Stator Winding:\n" + str(e)
            else:
                err_msg = "Error while plotting machine in Rotor Winding:\n" + str(e)
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

    def s_plot(self):
        """Plot a preview of the winding in a popup

        Parameters
        ----------
        self : SWinding
            A SWinding object
        """
        try:
            self.obj.plot_winding()
            set_plot_gui_icon()
        except (AssertionError, WindingError) as e:
            if self.obj.is_stator:  # Adapt the text to the current lamination
                err_msg = "Error while plotting winding in Stator Winding:\n" + str(e)
            else:
                err_msg = "Error while plotting winding in Rotor Winding:\n" + str(e)
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(self, self.tr("Error"), err_msg)

    def s_plot_mmf(self):
        """Plot the unit mmf of the stator"""
        if self.machine is not None:
            try:
                self.obj.plot_mmf_unit()
            except Exception as e:
                if self.obj.is_stator:  # Adapt the text to the current lamination
                    err_msg = "Error while plotting Stator mmf unit:\n" + str(e)
                else:
                    err_msg = "Error while plotting Rotor mmf unit:\n" + str(e)
                getLogger(GUI_LOG_NAME).error(err_msg)
                QMessageBox().critical(self, self.tr("Error"), err_msg)

    @staticmethod
    def check(lamination):
        """Check that the lamination have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        try:
            wind_mat = lamination.winding.get_connection_mat()
        except Exception as e:
            return "Error in winding matrix generation:\n" + str(e)
        try:
            # Check that everything is set
            if wind_mat is None:
                return "You must set the winding connection matrix !"
            if lamination.winding.qs is None:
                return "You must set qs !"
            if lamination.winding.Nslot_shift_wind is None:
                lamination.winding.Nslot_shift_wind = 0
            if lamination.winding.is_reverse_wind is None:
                lamination.winding.is_reverse_wind = False
            if lamination.winding.Ntcoil is None:
                return "You must set Ntcoil !"
            if lamination.winding.Npcp is None:
                return "You must set Npcp !"
        except Exception as e:
            return str(e)
