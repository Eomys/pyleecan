import sys
from os import makedirs, listdir
from numpy import max as np_max
from os.path import isdir, isfile, join
from shutil import rmtree
from multiprocessing import cpu_count
import matplotlib.pyplot as plt

from PySide2 import QtWidgets
import mock
import pytest
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape
from pyleecan.GUI.Dialog.DMachineSetup.SMachineDimension.SMachineDimension import (
    SMachineDimension,
)
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.GUI.Dialog.DMachineSetup.SBar.SBar import SBar
from pyleecan.GUI.Dialog.DMachineSetup.SSimu.SSimu import SSimu
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType11.PCondType11 import (
    PCondType11,
)
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType21.PCondType21 import PCondType21
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.GUI.Dialog.DMachineSetup.SWinding.SWinding import SWinding
from pyleecan.GUI.Dialog.DMachineSetup.SPreview.SPreview import SPreview
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.SWSlot import SWSlot
from pyleecan.GUI.Dialog.DMachineSetup.SSkew.SSkew import SSkew

from Tests.GUI import gui_option  # Set unit as [m]

from pyleecan.Functions.load import load_matlib
from Tests import save_gui_path as save_path

from pyleecan.definitions import DATA_DIR

import logging

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)

matlib_path = join(DATA_DIR, "Material")
save_path = join(save_path, "Test_New_RT")
if not isdir(save_path):
    makedirs(save_path)


class TestNewMachineRailway(object):
    """Test that you can create the Railway"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test NewMachineRailway")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        # MatLib widget
        material_dict = load_matlib(matlib_path=matlib_path)
        self.widget = DMachineSetup(
            material_dict=material_dict, machine_path=join(DATA_DIR, "Machine")
        )

    @pytest.mark.IPMSM
    def test_Railway(self):
        """Create a new machine"""
        # Load data for readibility
        self.widget.nav_step.count() == 12

        ################
        # 1 Machine Type
        ## Initial state
        assert self.widget.machine.rotor.is_internal is True
        assert self.widget.machine.name is None
        assert self.widget.machine.stator.winding.p is None
        assert self.widget.nav_step.currentRow() == 0
        assert self.widget.nav_step.currentItem().text() == " 1: Machine Type"
        assert isinstance(self.widget.w_step, SMachineType)
        assert self.widget.w_step.c_type.currentText() == "SCIM"
        ## Definition
        self.widget.w_step.le_name.setText("Railway_Test")
        self.widget.w_step.le_name.editingFinished.emit()
        self.widget.w_step.si_p.setValue(3)
        self.widget.w_step.si_p.editingFinished.emit()
        assert self.widget.w_step.si_p.value() == 3
        ## Check modif
        assert isinstance(self.widget.machine, MachineSCIM)
        assert self.widget.machine.name == "Railway_Test"
        assert not self.widget.machine.stator.is_internal
        assert self.widget.machine.rotor.is_internal
        assert self.widget.machine.stator.winding.p == 3
        assert self.widget.machine.rotor.winding.p == 3

        #####################
        # 2 Machine Dimension
        self.widget.w_step.b_next.clicked.emit()
        ## Initial state
        assert self.widget.nav_step.currentRow() == 1
        assert self.widget.nav_step.currentItem().text() == " 2: Machine Dimensions"
        assert isinstance(self.widget.w_step, SMachineDimension)
        assert self.widget.machine.stator.Rint is None
        assert self.widget.machine.stator.Rext is None
        assert self.widget.machine.rotor.Rint == 0
        assert self.widget.machine.rotor.Rext is None
        assert self.widget.machine.shaft is None
        assert self.widget.machine.frame is None
        assert not self.widget.w_step.lf_RRint.isEnabled()
        assert not self.widget.w_step.g_frame.isChecked()
        assert not self.widget.w_step.g_shaft.isChecked()
        ## Definition
        self.widget.w_step.lf_SRext.setText("0.2")
        self.widget.w_step.lf_SRext.editingFinished.emit()
        self.widget.w_step.lf_SRint.setText("0.1325")
        self.widget.w_step.lf_SRint.editingFinished.emit()
        self.widget.w_step.lf_RRext.setText("0.131")
        self.widget.w_step.lf_RRext.editingFinished.emit()
        self.widget.w_step.g_shaft.setChecked(True)
        assert self.widget.w_step.lf_RRint.isEnabled()
        self.widget.w_step.lf_RRint.setText("0.045")
        self.widget.w_step.lf_RRint.editingFinished.emit()
        assert self.widget.w_step.w_mat_0.c_mat_type.currentText() == "M400-50A"
        ## Check modif
        assert self.widget.machine.stator.Rext == pytest.approx(0.2)
        assert self.widget.machine.stator.Rint == pytest.approx(0.1325)
        assert self.widget.machine.rotor.Rext == pytest.approx(0.131)
        assert self.widget.machine.rotor.Rint == pytest.approx(0.045)
        assert self.widget.w_step.out_Drsh.text() == "Drsh = 0.09 [m]"
        assert (
            self.widget.w_step.out_airgap.text() == "Airgap magnetic width = 1.5 [mm]"
        )
        assert isinstance(self.widget.machine.shaft, Shaft)
        assert self.widget.machine.shaft.mat_type.name == "M400-50A"
        assert self.widget.machine.frame is None

        #####################
        # 3 Stator Slot
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 3: Stator Slot"
        assert isinstance(self.widget.w_step, SWSlot)
        self.widget.w_step.is_test = True  # To hide the plots

        ## Initial state
        assert self.widget.w_step.test_err_msg is None
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.w_step.b_plot.clicked.emit()
        assert (
            self.widget.w_step.test_err_msg
            == "Error in Stator Slot definition:\nYou must set Zs !"
        )

        assert self.widget.w_step.out_Slot_pitch.text() == "Slot pitch: 360 / Zs = ?"
        assert (
            self.widget.w_step.w_slot.w_out.out_Wlam.text()
            == "Stator width: 0.0675 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_slot_height.text() == "Slot height: ?"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_yoke_height.text() == "Yoke height: ?"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_wind_surface.text()
            == "Active surface: ?"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_tot_surface.text() == "Slot surface: ?"
        )
        assert self.widget.w_step.w_slot.w_out.out_op_angle.text() == "Opening angle: ?"

        ## Definition
        self.widget.w_step.si_Zs.setValue(36)
        self.widget.w_step.si_Zs.editingFinished.emit()
        index_slot10 = self.widget.w_step.c_slot_type.findText("Slot Type 10")
        self.widget.w_step.c_slot_type.setCurrentIndex(index_slot10)
        self.widget.w_step.w_slot.lf_W0.setValue(0.012)
        self.widget.w_step.w_slot.lf_W0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W1.setValue(0.014)
        self.widget.w_step.w_slot.lf_W1.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W2.setValue(0.012)
        self.widget.w_step.w_slot.lf_W2.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H0.setValue(0.001)
        self.widget.w_step.w_slot.lf_H0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H1.setValue(0.0015)
        self.widget.w_step.w_slot.lf_H1.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H2.setValue(0.03)
        self.widget.w_step.w_slot.lf_H2.editingFinished.emit()

        ## Check modif
        self.widget.w_step.b_plot.clicked.emit()
        assert self.widget.w_step.machine.stator.slot.W0 == pytest.approx(0.012)
        assert self.widget.w_step.machine.stator.slot.W1 == pytest.approx(0.014)
        assert self.widget.w_step.machine.stator.slot.W2 == pytest.approx(0.012)
        assert self.widget.w_step.machine.stator.slot.H0 == pytest.approx(0.001)
        assert self.widget.w_step.machine.stator.slot.H1 == pytest.approx(0.0015)
        assert self.widget.w_step.machine.stator.slot.H2 == pytest.approx(0.03)
        assert (
            self.widget.w_step.out_Slot_pitch.text()
            == "Slot pitch: 360 / Zs = 10 [°] (0.1745 [rad])"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_Wlam.text()
            == "Stator width: 0.0675 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_slot_height.text()
            == "Slot height: 0.03247 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_yoke_height.text()
            == "Yoke height: 0.03503 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_wind_surface.text()
            == "Active surface: 0.00036 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_tot_surface.text()
            == "Slot surface: 0.0003904 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_op_angle.text()
            == "Opening angle: 0.0906 [rad]"
        )

        #####################
        # 4 Stator Lamination
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 4: Stator Lamination"
        assert isinstance(self.widget.w_step, SLamShape)

        assert self.widget.w_step.lf_L1.value() is None
        assert self.widget.w_step.lf_Kf1.value() == 0.95
        assert self.widget.w_step.w_mat.c_mat_type.currentText() == "M400-50A"

        assert not self.widget.w_step.g_axial.isChecked()
        assert not self.widget.w_step.g_radial.isChecked()
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.lf_L1.setValue(0.35)
        self.widget.w_step.lf_L1.editingFinished.emit()

        assert self.widget.w_step.lf_L1.value() == 0.35
        # ? -> Because Radial cooling duct hasn't been activated once
        assert self.widget.w_step.out_length.text() == "Stator total length = ?"

        assert self.widget.w_step.machine.stator.L1 == 0.35
        assert self.widget.w_step.machine.stator.Kf1 == 0.95
        assert self.widget.machine.stator.mat_type.name == "M400-50A"

        #####################
        # 5 Stator Winding
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 5: Stator Winding"
        assert isinstance(self.widget.w_step, SWinding)
        self.widget.w_step.is_test = True  # To hide the plots

        assert self.widget.w_step.c_wind_type.currentText() == "Star of Slot"
        assert self.widget.w_step.in_Zs.text() == "Slot number: 36"
        assert self.widget.w_step.in_p.text() == "Pole pair number: 3"
        assert self.widget.w_step.si_qs.value() == 3
        assert self.widget.w_step.c_layer_def.currentText() == "Single Layer"
        assert self.widget.w_step.si_coil_pitch.value() == 6
        assert self.widget.w_step.si_Ntcoil.value() == 1
        assert self.widget.w_step.si_Npcp.value() == 1
        assert self.widget.w_step.si_Nslot.value() == 0
        assert not self.widget.w_step.is_reverse.isChecked()
        assert not self.widget.w_step.is_permute_B_C.isChecked()
        assert not self.widget.w_step.is_reverse_layer.isChecked()

        self.widget.w_step.c_layer_def.setCurrentIndex(1)
        self.widget.w_step.si_coil_pitch.setValue(5)
        self.widget.w_step.si_coil_pitch.editingFinished.emit()
        self.widget.w_step.si_Ntcoil.setValue(7)
        self.widget.w_step.si_Ntcoil.editingFinished.emit()
        self.widget.w_step.si_Npcp.setValue(2)
        self.widget.w_step.si_Npcp.editingFinished.emit()

        self.widget.w_step.b_generate.clicked.emit()

        assert (
            self.widget.w_step.c_layer_def.currentText() == "Double Layer overlapping"
        )
        assert self.widget.w_step.si_coil_pitch.value() == 5
        assert self.widget.w_step.si_Ntcoil.value() == 7
        assert self.widget.w_step.si_Npcp.value() == 2
        assert self.widget.w_step.out_rot_dir.text() == "Rotation direction: CCW"
        assert self.widget.w_step.out_ms.text() == "Slots per pole per phase: 2.0"
        assert self.widget.w_step.out_Nperw.text() == "Winding periodicity: 6"
        assert self.widget.w_step.out_Ntspc.text() == "Turns in series per phase: 42"
        assert (
            self.widget.w_step.out_Ncspc.text()
            == "Coils in series per parallel circuit: 6"
        )

        # Check plots/export
        assert self.widget.w_step.fig_mmf is None
        self.widget.w_step.b_plot_mmf.clicked.emit()
        assert isinstance(self.widget.w_step.fig_mmf, plt.Figure)

        assert self.widget.w_step.fig_radial is None
        self.widget.w_step.b_plot_radial.clicked.emit()
        assert isinstance(self.widget.w_step.fig_radial, plt.Figure)

        assert self.widget.w_step.fig_linear is None
        self.widget.w_step.b_plot_linear.clicked.emit()
        assert isinstance(self.widget.w_step.fig_linear, plt.Figure)

        file_path = join(save_path, "winding_export.csv")
        return_value = (
            file_path,
            "CSV (*.csv)",
        )
        assert not isfile(file_path)
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.w_step.b_export.clicked.emit()
        assert isfile(file_path)

        # Is the stator winding well defined ?
        assert self.widget.w_step.machine.stator.winding.qs == 3
        assert self.widget.w_step.machine.stator.winding.Nlayer == 2
        assert self.widget.w_step.machine.stator.winding.coil_pitch == 5
        assert self.widget.w_step.machine.stator.winding.Ntcoil == 7
        assert self.widget.w_step.machine.stator.winding.Npcp == 2
        assert self.widget.w_step.machine.stator.winding.Nslot_shift_wind == 0
        assert not self.widget.w_step.machine.stator.winding.is_reverse_wind
        assert not self.widget.w_step.machine.stator.winding.is_permute_B_C
        assert not self.widget.w_step.machine.rotor.winding.is_reverse_layer
        assert not self.widget.w_step.machine.rotor.winding.is_change_layer

        #####################
        # 6 Stator Conductor
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 6: Stator Conductor"
        assert isinstance(self.widget.w_step, SWindCond)

        # Initial state
        assert self.widget.w_step.c_cond_type.currentText() == "Form wound"
        assert isinstance(self.widget.w_step.w_cond, PCondType11)
        assert self.widget.w_step.w_cond.w_mat_0.c_mat_type.currentText() == "Copper1"
        assert not self.widget.w_step.w_cond.g_ins.isChecked()
        assert self.widget.w_step.w_cond.si_Nwpc1_rad.value() == 1
        assert self.widget.w_step.w_cond.si_Nwpc1_tan.value() == 1
        assert self.widget.w_step.w_cond.lf_Wwire.value() is None
        assert self.widget.w_step.w_cond.lf_Hwire.value() is None
        assert self.widget.w_step.w_cond.lf_Lewout.value() == 0

        self.widget.w_step.w_cond.g_ins.setChecked(True)
        assert (
            self.widget.w_step.w_cond.w_mat_1.c_mat_type.currentText() == "Insulator1"
        )

        self.widget.w_step.w_cond.si_Nwpc1_rad.setValue(1)
        self.widget.w_step.w_cond.si_Nwpc1_rad.editingFinished.emit()
        self.widget.w_step.w_cond.si_Nwpc1_tan.setValue(1)
        self.widget.w_step.w_cond.si_Nwpc1_tan.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wwire.setValue(0.01)
        self.widget.w_step.w_cond.lf_Wwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Hwire.setValue(0.002)
        self.widget.w_step.w_cond.lf_Hwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wins_wire.setValue(0)
        self.widget.w_step.w_cond.lf_Wins_wire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Lewout.setValue(0.1541392)
        self.widget.w_step.w_cond.lf_Lewout.editingFinished.emit()

        assert (
            self.widget.w_step.w_cond.w_out.out_Sslot.text()
            == "Slot surface: 0.0003904 [m²]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Saslot.text()
            == "Slot active surface: 0.00036 [m²]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Sact.text()
            == "Conductor active surface: 2e-05 [m²]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Ncps.text() == "Conductors per slot: 14"
        )
        assert self.widget.w_step.w_cond.w_out.out_K.text() == "Fill factor: 77.78 %"
        assert (
            self.widget.w_step.w_cond.w_out.out_MLT.text()
            == "Mean Length Turn: 1.317 [m]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Rwind.text()
            == "Winding resistance at 20°C: 0.024 [Ohm]"
        )

        # Is the stator winding conductors well defined ?
        assert isinstance(
            self.widget.w_step.machine.stator.winding.conductor, CondType11
        )
        assert (
            self.widget.w_step.machine.stator.winding.conductor.cond_mat.name
            == "Copper1"
        )
        assert (
            self.widget.w_step.machine.stator.winding.conductor.ins_mat.name
            == "Insulator1"
        )
        assert self.widget.w_step.machine.stator.winding.conductor.Nwppc_tan == 1
        assert self.widget.w_step.machine.stator.winding.conductor.Nwppc_rad == 1
        assert self.widget.w_step.machine.stator.winding.conductor.Wwire == 0.01
        assert self.widget.w_step.machine.stator.winding.conductor.Hwire == 0.002
        assert self.widget.w_step.machine.stator.winding.conductor.Wins_wire == 0
        assert self.widget.w_step.machine.stator.winding.Lewout == 0.1541392

        #####################
        # 7 Rotor Slot
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 7: Rotor Slot"
        assert isinstance(self.widget.w_step, SWSlot)
        self.widget.w_step.is_test = True  # To hide the plot

        assert self.widget.w_step.test_err_msg is None
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.w_step.b_plot.clicked.emit()
        assert (
            self.widget.w_step.test_err_msg
            == "Error in Rotor Slot definition:\nYou must set Zs !"
        )

        self.widget.w_step.si_Zs.setValue(28)
        self.widget.w_step.si_Zs.editingFinished.emit()
        index_slot21 = self.widget.w_step.c_slot_type.findText("Slot Type 21")
        self.widget.w_step.c_slot_type.setCurrentIndex(index_slot21)
        self.widget.w_step.w_slot.lf_W0.setValue(0.003)
        self.widget.w_step.w_slot.lf_W0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W1.setValue(0.013)
        self.widget.w_step.w_slot.lf_W1.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W2.setValue(0.01)
        self.widget.w_step.w_slot.lf_W2.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H0.setValue(0.003)
        self.widget.w_step.w_slot.lf_H0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H1.setValue(0)
        self.widget.w_step.w_slot.lf_H1.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H2.setValue(0.02)
        self.widget.w_step.w_slot.lf_H2.editingFinished.emit()

        ## Check modif
        self.widget.w_step.b_plot.clicked.emit()
        assert self.widget.w_step.machine.rotor.slot.W0 == pytest.approx(0.003)
        assert self.widget.w_step.machine.rotor.slot.W1 == pytest.approx(0.013)
        assert self.widget.w_step.machine.rotor.slot.W2 == pytest.approx(0.01)
        assert self.widget.w_step.machine.rotor.slot.H0 == pytest.approx(0.003)
        assert self.widget.w_step.machine.rotor.slot.H1 == pytest.approx(0)
        assert self.widget.w_step.machine.rotor.slot.H2 == pytest.approx(0.02)
        assert (
            self.widget.w_step.out_Slot_pitch.text()
            == "Slot pitch: 360 / Zs = 12.86 [°] (0.2244 [rad])"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_Wlam.text() == "Rotor width: 0.086 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_slot_height.text()
            == "Slot height: 0.02301 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_yoke_height.text()
            == "Yoke height: 0.06299 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_wind_surface.text()
            == "Active surface: 0.00023 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_tot_surface.text()
            == "Slot surface: 0.000239 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_op_angle.text()
            == "Opening angle: 0.0229 [rad]"
        )

        #####################
        # 8 Rotor Bar
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 8: Rotor Bar"
        assert isinstance(self.widget.w_step, SBar)

        assert self.widget.w_step.lf_Hscr.value() is None
        assert self.widget.w_step.lf_Lscr.value() is None
        assert self.widget.w_step.lf_Lewout.value() is None
        assert self.widget.w_step.w_mat_scr.c_mat_type.currentText() == "Copper1"
        assert self.widget.w_step.c_bar_type.currentText() == "Rectangular bar"
        assert isinstance(self.widget.w_step.w_bar, PCondType21)
        assert self.widget.w_step.w_bar.lf_Hbar.value() is None
        assert self.widget.w_step.w_bar.lf_Wbar.value() is None
        assert self.widget.w_step.w_bar.w_mat.c_mat_type.currentText() == "Copper1"

        assert self.widget.w_step.w_bar.w_out.out_Sbar.text() == "Sbar: ?"
        assert self.widget.w_step.w_bar.w_out.out_Sslot.text() == "Sslot: 0.000239 [m²]"
        assert self.widget.w_step.w_bar.w_out.out_ratio.text() == "Sbar / Sslot: ?"

        self.widget.w_step.lf_Hscr.setValue(0.02)
        self.widget.w_step.lf_Hscr.editingFinished.emit()
        self.widget.w_step.lf_Lscr.setValue(0.015)
        self.widget.w_step.lf_Lscr.editingFinished.emit()
        self.widget.w_step.lf_Lewout.setValue(0.017)
        self.widget.w_step.lf_Lewout.editingFinished.emit()
        self.widget.w_step.w_bar.lf_Hbar.setValue(0.02)
        self.widget.w_step.w_bar.lf_Hbar.editingFinished.emit()
        self.widget.w_step.w_bar.lf_Wbar.setValue(0.01)
        self.widget.w_step.w_bar.lf_Wbar.editingFinished.emit()

        assert self.widget.w_step.w_bar.w_out.out_Sbar.text() == "Sbar: 0.0002 [m²]"
        assert self.widget.w_step.w_bar.w_out.out_Sslot.text() == "Sslot: 0.000239 [m²]"
        assert (
            self.widget.w_step.w_bar.w_out.out_ratio.text() == "Sbar / Sslot: 83.68 [%]"
        )

        assert self.widget.w_step.machine.rotor.Hscr == pytest.approx(0.02)
        assert self.widget.w_step.machine.rotor.Lscr == pytest.approx(0.015)
        assert self.widget.w_step.machine.rotor.winding.Lewout == pytest.approx(0.017)
        assert self.widget.w_step.machine.rotor.winding.conductor.Hbar == pytest.approx(
            0.02
        )
        assert self.widget.w_step.machine.rotor.winding.conductor.Wbar == pytest.approx(
            0.01
        )
        assert self.widget.w_step.machine.rotor.ring_mat.name == "Copper1"
        assert (
            self.widget.w_step.machine.rotor.winding.conductor.cond_mat.name
            == "Copper1"
        )

        #####################
        # 9 Rotor Lamination
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 9: Rotor Lamination"
        assert isinstance(self.widget.w_step, SLamShape)

        assert self.widget.w_step.lf_L1.value() == 0.35
        assert self.widget.w_step.lf_Kf1.value() == 0.95

        assert not self.widget.w_step.g_axial.isChecked()
        assert not self.widget.w_step.g_radial.isChecked()
        assert not self.widget.w_step.g_notches.isChecked()

        assert self.widget.w_step.machine.rotor.L1 == 0.35
        assert self.widget.w_step.machine.rotor.Kf1 == 0.95

        #####################
        # 10 Rotor Skew
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "10: Rotor Skew"
        assert isinstance(self.widget.w_step, SSkew)

        assert not self.widget.w_step.g_activate.isChecked()

        #####################
        # 11 Machine Summary
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "11: Machine Summary"
        assert isinstance(self.widget.w_step, SPreview)
        self.widget.w_step.tab_machine.is_test = True  # To hide the plots

        assert (
            self.widget.w_step.tab_machine.tab_param.item(0, 0).text() == "Machine Type"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(0, 1).text() == "SCIM"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(1, 0).text()
            == "Stator slot number"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(1, 1).text() == "36"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(2, 0).text()
            == "Rotor slot number"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(2, 1).text() == "28"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(3, 0).text()
            == "Pole pair number"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(3, 1).text() == "3"
        assert self.widget.w_step.tab_machine.tab_param.item(4, 0).text() == "Topology"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(4, 1).text()
            == "Internal Rotor"
        )
        assert (
            self.widget.w_step.tab_machine.tab_param.item(5, 0).text()
            == "Stator phase number"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(5, 1).text() == "3"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(6, 0).text()
            == "Stator winding resistance"
        )
        assert (
            self.widget.w_step.tab_machine.tab_param.item(6, 1).text() == "0.02392 Ohm"
        )
        assert (
            self.widget.w_step.tab_machine.tab_param.item(7, 0).text()
            == "Machine total mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(7, 1).text() == "327.7 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(8, 0).text()
            == "Stator lamination mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(8, 1).text() == "143.6 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(9, 0).text()
            == "Stator winding mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(9, 1).text() == "59.06 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(10, 0).text()
            == "Rotor lamination mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(10, 1).text() == "103.9 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(11, 0).text()
            == "Rotor winding mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(11, 1).text() == "21.12 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(12, 0).text() == "Shaft mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(12, 1).text() == "0 kg"
        assert self.widget.w_step.tab_machine.tab_param.rowCount() == 13

        self.widget.w_step.tab_machine.b_plot_machine.clicked.emit()
        self.widget.w_step.tab_machine.b_mmf.clicked.emit()

        #####################
        # 12 FEMM Simulation
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "12: FEMM Simulation"
        assert isinstance(self.widget.w_step, SSimu)

        assert self.widget.w_step.lf_N0.value() == 1000
        assert self.widget.w_step.lf_I1.value() == 0
        assert self.widget.w_step.lf_I2.value() == 0
        assert self.widget.w_step.si_Na_tot.value() == 1260
        assert self.widget.w_step.si_Nt_tot.value() == 360
        assert self.widget.w_step.is_per_a.isChecked()
        assert self.widget.w_step.is_per_t.isChecked()
        assert self.widget.w_step.lf_Kmesh.value() == 1
        assert self.widget.w_step.si_nb_worker.value() == cpu_count()
        assert self.widget.w_step.le_name.text() == "FEMM_Railway_Test"

        ## Define
        res_path = join(save_path, "Simu_Results")
        makedirs(res_path)
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getExistingDirectory", return_value=res_path
        ):
            # To trigger the slot
            self.widget.w_step.w_path_result.b_path.clicked.emit()
        self.widget.w_step.si_Nt_tot.setValue(1)
        self.widget.w_step.si_Nt_tot.editingFinished.emit()
        self.widget.w_step.lf_Kmesh.setValue(0.6)
        self.widget.w_step.lf_Kmesh.editingFinished.emit()
        self.widget.w_step.lf_I1.setValue(80)
        self.widget.w_step.lf_I1.editingFinished.emit()

        ## Run
        assert len(listdir(res_path)) == 0
        with mock.patch("PySide2.QtWidgets.QMessageBox.information", return_value=None):
            self.widget.w_step.b_next.clicked.emit()
        # Run creates a new results folder with execution time in the name
        assert len(listdir(res_path)) == 1
        assert len(listdir(join(res_path, listdir(res_path)[0]))) == 18
        assert np_max(
            self.widget.w_step.last_out.mag.B.components["radial"].values
        ) == pytest.approx(1.1, rel=0.1)


if __name__ == "__main__":
    a = TestNewMachineRailway()
    a.setup_class()
    a.setup_method()
    a.test_Railway()
    print("Done")
