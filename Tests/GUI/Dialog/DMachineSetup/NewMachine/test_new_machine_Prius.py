import sys
from os.path import isdir, isfile, join
from shutil import rmtree
from multiprocessing import cpu_count
import matplotlib.pyplot as plt
from os import makedirs, listdir
from numpy import max as np_max

from qtpy import QtWidgets
import mock
import pytest
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape
from pyleecan.GUI.Dialog.DMachineSetup.SMachineDimension.SMachineDimension import (
    SMachineDimension,
)
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.WHoleMag.WHoleMag import WHoleMag
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM50.PHoleM50 import PHoleM50
from pyleecan.GUI.Dialog.DMachineSetup.SSimu.SSimu import SSimu
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType11.PCondType11 import (
    PCondType11,
)
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType12.PCondType12 import (
    PCondType12,
)
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
save_path = join(save_path, "Test_New_Prius")
if not isdir(save_path):
    makedirs(save_path)


class TestNewMachinePrius(object):
    """Test that you can create the Toyota prius"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test NewMachinePrius")
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
    def test_Toyota_Prius(self):
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
        index_IPMSM = self.widget.w_step.c_type.findText("IPMSM")
        self.widget.w_step.c_type.setCurrentIndex(index_IPMSM)
        assert self.widget.w_step.c_type.currentText() == "IPMSM"
        self.widget.w_step.le_name.setText("Prius_Test")
        self.widget.w_step.le_name.editingFinished.emit()
        self.widget.w_step.si_p.setValue(4)
        self.widget.w_step.si_p.editingFinished.emit()
        assert self.widget.w_step.si_p.value() == 4
        ## Check modif
        assert isinstance(self.widget.machine, MachineIPMSM)
        assert self.widget.machine.name == "Prius_Test"
        assert not self.widget.machine.stator.is_internal
        assert self.widget.machine.rotor.is_internal
        assert self.widget.machine.stator.winding.p == 4
        assert self.widget.machine.rotor.hole[0].Zh == 8

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
        self.widget.w_step.lf_SRext.setText("134.62e-3")
        self.widget.w_step.lf_SRext.editingFinished.emit()
        self.widget.w_step.lf_SRint.setText("80.95e-3")
        self.widget.w_step.lf_SRint.editingFinished.emit()
        self.widget.w_step.lf_RRext.setText("80.2e-3")
        self.widget.w_step.lf_RRext.editingFinished.emit()
        self.widget.w_step.g_shaft.setChecked(True)
        self.widget.w_step.lf_Lshaft.setText("0.1")
        self.widget.w_step.lf_Lshaft.editingFinished.emit()
        assert self.widget.w_step.lf_RRint.isEnabled()
        self.widget.w_step.lf_RRint.setText("55.32e-3")
        self.widget.w_step.lf_RRint.editingFinished.emit()
        assert self.widget.w_step.w_mat_0.c_mat_type.currentText() == "M400-50A"
        ## Check modif
        assert self.widget.machine.stator.Rext == pytest.approx(134.62e-3)
        assert self.widget.machine.stator.Rint == pytest.approx(80.95e-3)
        assert self.widget.machine.rotor.Rext == pytest.approx(80.2e-3)
        assert self.widget.machine.rotor.Rint == pytest.approx(55.32e-3)
        assert self.widget.machine.shaft.Lshaft == pytest.approx(0.1)
        assert self.widget.w_step.out_Drsh.text() == "Drsh = 0.1106 [m]"
        assert (
            self.widget.w_step.out_airgap.text() == "Airgap magnetic width = 0.75 [mm]"
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
            "qtpy.QtWidgets.QMessageBox.critical",
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
            == "Stator width: 0.05367 [m]"
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
        self.widget.w_step.si_Zs.setValue(48)
        self.widget.w_step.si_Zs.editingFinished.emit()
        index_slot11 = self.widget.w_step.c_slot_type.findText("Slot Type 11")
        self.widget.w_step.c_slot_type.setCurrentIndex(index_slot11)
        self.widget.w_step.w_slot.lf_W0.setValue(1.93e-3)
        self.widget.w_step.w_slot.lf_W0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W1.setValue(5e-3)
        self.widget.w_step.w_slot.lf_W1.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W2.setValue(8e-3)
        self.widget.w_step.w_slot.lf_W2.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H0.setValue(1e-3)
        self.widget.w_step.w_slot.lf_H0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H1.setValue(0)
        self.widget.w_step.w_slot.lf_H1.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H2.setValue(33.3e-3)
        self.widget.w_step.w_slot.lf_H2.editingFinished.emit()
        self.widget.w_step.w_slot.lf_R1.setValue(4e-3)
        self.widget.w_step.w_slot.lf_R1.editingFinished.emit()
        ## Check modif
        self.widget.w_step.b_plot.clicked.emit()
        assert self.widget.w_step.machine.stator.slot.W0 == pytest.approx(1.93e-3)
        assert self.widget.w_step.machine.stator.slot.W1 == pytest.approx(5e-3)
        assert self.widget.w_step.machine.stator.slot.W2 == pytest.approx(8e-3)
        assert self.widget.w_step.machine.stator.slot.H0 == pytest.approx(1e-3)
        assert self.widget.w_step.machine.stator.slot.H1 == pytest.approx(0)
        assert self.widget.w_step.machine.stator.slot.H2 == pytest.approx(33.3e-3)
        assert self.widget.w_step.machine.stator.slot.R1 == pytest.approx(4e-3)
        assert (
            self.widget.w_step.out_Slot_pitch.text()
            == "Slot pitch: 360 / Zs = 7.5 [°] (0.1309 [rad])"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_slot_height.text()
            == "Slot height: 0.03429 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_yoke_height.text()
            == "Yoke height: 0.01938 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_wind_surface.text()
            == "Active surface: 0.0002156 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_tot_surface.text()
            == "Slot surface: 0.0002175 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_op_angle.text()
            == "Opening angle: 0.02384 [rad]"
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

        self.widget.w_step.lf_L1.setValue(0.08382)
        self.widget.w_step.lf_L1.editingFinished.emit()

        assert self.widget.w_step.lf_L1.value() == 0.08382
        # ? -> Because Radial cooling duct hasn't been activated once
        assert self.widget.w_step.out_length.text() == "Stator total length = ?"

        assert self.widget.w_step.machine.stator.L1 == 0.08382
        assert self.widget.w_step.machine.stator.Kf1 == 0.95
        assert self.widget.machine.stator.mat_type.name == "M400-50A"

        #####################
        # 5 Stator Winding
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 5: Stator Winding"
        assert isinstance(self.widget.w_step, SWinding)
        self.widget.w_step.is_test = True  # To hide the plots

        assert self.widget.w_step.c_wind_type.currentText() == "Star of Slot"
        assert self.widget.w_step.in_Zs.text() == "Slot number: 48"
        assert self.widget.w_step.in_p.text() == "Pole pair number: 4"
        assert self.widget.w_step.si_qs.value() == 3
        assert self.widget.w_step.c_layer_def.currentText() == "Single Layer"
        assert self.widget.w_step.si_coil_pitch.value() == 6
        assert self.widget.w_step.si_Ntcoil.value() == 1
        assert self.widget.w_step.si_Npcp.value() == 1
        assert self.widget.w_step.si_Nslot.value() == 0
        assert not self.widget.w_step.is_reverse.isChecked()
        assert not self.widget.w_step.is_permute_B_C.isChecked()

        self.widget.w_step.si_Ntcoil.setValue(9)
        self.widget.w_step.si_Ntcoil.editingFinished.emit()

        self.widget.w_step.b_generate.clicked.emit()

        assert self.widget.w_step.si_Ntcoil.value() == 9
        assert self.widget.w_step.out_rot_dir.text() == "Rotation direction: CCW"
        assert self.widget.w_step.out_ms.text() == "Slots per pole per phase: 2.0"
        assert self.widget.w_step.out_Nperw.text() == "Winding periodicity: 8"
        assert self.widget.w_step.out_Ntspc.text() == "Turns in series per phase: 72"
        assert (
            self.widget.w_step.out_Ncspc.text()
            == "Coils in series per parallel circuit: 8"
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
            "qtpy.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.w_step.b_export.clicked.emit()
        assert isfile(file_path)

        # Is the stator winding well defined ?
        assert self.widget.w_step.machine.stator.winding.qs == 3
        assert self.widget.w_step.machine.stator.winding.Nlayer == 1
        assert self.widget.w_step.machine.stator.winding.coil_pitch == 6
        assert self.widget.w_step.machine.stator.winding.Ntcoil == 9
        assert self.widget.w_step.machine.stator.winding.Npcp == 1
        assert self.widget.w_step.machine.stator.winding.Nslot_shift_wind == 0
        assert not self.widget.w_step.machine.stator.winding.is_reverse_wind
        assert not self.widget.w_step.machine.stator.winding.is_permute_B_C

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

        assert isinstance(
            self.widget.w_step.machine.stator.winding.conductor, CondType11
        )

        self.widget.w_step.c_cond_type.setCurrentIndex(1)

        assert self.widget.w_step.c_cond_type.currentText() == "Stranded"
        assert isinstance(self.widget.w_step.w_cond, PCondType12)
        assert self.widget.w_step.w_cond.w_mat_0.c_mat_type.currentText() == "Copper1"
        assert not self.widget.w_step.w_cond.g_ins.isChecked()
        assert self.widget.w_step.w_cond.si_Nwpc1.value() == 1
        assert self.widget.w_step.w_cond.lf_Wwire.value() is None
        assert self.widget.w_step.w_cond.lf_Lewout.value() == 0

        self.widget.w_step.w_cond.g_ins.setChecked(True)
        assert (
            self.widget.w_step.w_cond.w_mat_1.c_mat_type.currentText() == "Insulator1"
        )

        assert self.widget.w_step.w_cond.lf_Wins_cond.value() is None
        assert self.widget.w_step.w_cond.lf_Wins_wire.value() is None

        self.widget.w_step.w_cond.si_Nwpc1.setValue(13)
        self.widget.w_step.w_cond.si_Nwpc1.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wwire.setValue(0.000912)
        self.widget.w_step.w_cond.lf_Wwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wins_cond.setValue(0.015)
        self.widget.w_step.w_cond.lf_Wins_cond.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wins_wire.setValue(1e-06)
        self.widget.w_step.w_cond.lf_Wins_wire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Lewout.setValue(0.019366)
        self.widget.w_step.w_cond.lf_Lewout.editingFinished.emit()

        assert (
            self.widget.w_step.w_cond.w_out.out_Sslot.text()
            == "Slot surface: 0.0002175 [m²]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Saslot.text()
            == "Slot active surface: 0.0002156 [m²]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Sact.text()
            == "Conductor active surface: 8.492e-06 [m²]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Ncps.text() == "Conductors per slot: 9"
        )
        assert self.widget.w_step.w_cond.w_out.out_K.text() == "Fill factor: 35.45 %"
        assert (
            self.widget.w_step.w_cond.w_out.out_MLT.text()
            == "Mean Length Turn: 0.2451 [m]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_Rwind.text()
            == "Phase resistance at 20°C: 0.036 [Ohm]"
        )
        assert (
            self.widget.w_step.w_cond.w_out.out_RwindLL.text()
            == "Line-to-line resistance at 20°C: 0.072 [Ohm]"
        )

        # Is the stator winding conductors well defined ?
        assert isinstance(
            self.widget.w_step.machine.stator.winding.conductor, CondType12
        )
        assert (
            self.widget.w_step.machine.stator.winding.conductor.cond_mat.name
            == "Copper1"
        )
        assert (
            self.widget.w_step.machine.stator.winding.conductor.ins_mat.name
            == "Insulator1"
        )
        assert self.widget.w_step.machine.stator.winding.conductor.Nwppc == 13
        assert self.widget.w_step.machine.stator.winding.conductor.Wwire == 0.000912
        assert self.widget.w_step.machine.stator.winding.conductor.Wins_wire == 1e-06
        assert self.widget.w_step.machine.stator.winding.conductor.Wins_cond == 0.015
        assert self.widget.w_step.machine.stator.winding.Lewout == 0.019366

        #####################
        # 7 Rotor Hole
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 7: Rotor Hole"
        assert isinstance(self.widget.w_step, SMHoleMag)
        self.widget.w_step.is_test = True  # To hide the plot

        assert (
            self.widget.w_step.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )

        wid_hole = self.widget.w_step.tab_hole.currentWidget()
        assert isinstance(wid_hole, WHoleMag)

        assert wid_hole.c_hole_type.count() == 12
        assert wid_hole.c_hole_type.currentText() == "Hole Type 50"
        assert isinstance(wid_hole.w_hole, PHoleM50)

        assert self.widget.w_step.test_err_msg is None
        with mock.patch(
            "qtpy.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.w_step.b_plot.clicked.emit()
        assert (
            self.widget.w_step.test_err_msg
            == "Error in Hole definition:\nYou must set W0 !"
        )

        assert wid_hole.w_hole.lf_W0.value() is None
        assert wid_hole.w_hole.lf_W1.value() is None
        assert wid_hole.w_hole.lf_W2.value() is None
        assert wid_hole.w_hole.lf_W3.value() is None
        assert wid_hole.w_hole.lf_W4.value() is None
        assert wid_hole.w_hole.lf_H0.value() is None
        assert wid_hole.w_hole.lf_H1.value() is None
        assert wid_hole.w_hole.lf_H2.value() is None
        assert wid_hole.w_hole.lf_H3.value() is None
        assert wid_hole.w_hole.lf_H4.value() is None
        assert wid_hole.w_hole.w_mat_0.c_mat_type.currentText() == "Air"
        assert wid_hole.w_hole.w_mat_1.c_mat_type.currentText() == "MagnetPrius"
        assert wid_hole.w_hole.w_mat_2.c_mat_type.currentText() == "MagnetPrius"
        assert wid_hole.w_hole.out_slot_surface.text() == "Hole surface: ?"
        assert wid_hole.w_hole.out_magnet_surface.text() == "Magnet surf.: ?"
        assert wid_hole.w_hole.out_alpha.text() == "alpha: ?"
        assert wid_hole.w_hole.out_W5.text() == "Max magnet width: ?"

        wid_hole.w_hole.lf_H0.setValue(0.01096)
        wid_hole.w_hole.lf_H0.editingFinished.emit()
        wid_hole.w_hole.lf_H1.setValue(0.0015)
        wid_hole.w_hole.lf_H1.editingFinished.emit()
        wid_hole.w_hole.lf_H2.setValue(0.001)
        wid_hole.w_hole.lf_H2.editingFinished.emit()
        wid_hole.w_hole.lf_H3.setValue(0.0065)
        wid_hole.w_hole.lf_H3.editingFinished.emit()
        wid_hole.w_hole.lf_H4.setValue(0)
        wid_hole.w_hole.lf_H4.editingFinished.emit()
        wid_hole.w_hole.lf_W0.setValue(0.042)
        wid_hole.w_hole.lf_W0.editingFinished.emit()
        wid_hole.w_hole.lf_W1.setValue(0)
        wid_hole.w_hole.lf_W1.editingFinished.emit()
        wid_hole.w_hole.lf_W2.setValue(0)
        wid_hole.w_hole.lf_W2.editingFinished.emit()
        wid_hole.w_hole.lf_W3.setValue(0.014)
        wid_hole.w_hole.lf_W3.editingFinished.emit()
        wid_hole.w_hole.lf_W4.setValue(0.0189)
        wid_hole.w_hole.lf_W4.editingFinished.emit()

        assert wid_hole.w_hole.out_slot_surface.text() == "Hole surface: 0.0002968 [m²]"
        assert (
            wid_hole.w_hole.out_magnet_surface.text() == "Magnet surf.: 0.0002457 [m²]"
        )
        assert wid_hole.w_hole.out_alpha.text() == "alpha: 0.3048 [rad] (17.46°)"
        assert wid_hole.w_hole.out_W5.text() == "Max magnet width: 0.02201 [m]"

        assert self.widget.w_step.machine.rotor.hole[0].H0 == 0.01096
        assert self.widget.w_step.machine.rotor.hole[0].H1 == 0.0015
        assert self.widget.w_step.machine.rotor.hole[0].H2 == 0.001
        assert self.widget.w_step.machine.rotor.hole[0].H3 == 0.0065
        assert self.widget.w_step.machine.rotor.hole[0].H4 == 0
        assert self.widget.w_step.machine.rotor.hole[0].W0 == 0.042
        assert self.widget.w_step.machine.rotor.hole[0].W1 == 0
        assert self.widget.w_step.machine.rotor.hole[0].W2 == 0
        assert self.widget.w_step.machine.rotor.hole[0].W3 == 0.014
        assert self.widget.w_step.machine.rotor.hole[0].W4 == 0.0189
        self.widget.w_step.b_plot.clicked.emit()

        #####################
        # 8 Rotor Lamination
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 8: Rotor Lamination"
        assert isinstance(self.widget.w_step, SLamShape)

        assert self.widget.w_step.lf_L1.value() == 0.08382
        assert self.widget.w_step.lf_Kf1.value() == 0.95
        assert self.widget.w_step.w_mat.c_mat_type.currentText() == "M400-50A"

        assert not self.widget.w_step.g_axial.isChecked()
        assert not self.widget.w_step.g_radial.isChecked()
        assert not self.widget.w_step.g_notches.isChecked()

        assert self.widget.w_step.machine.rotor.L1 == 0.08382
        assert self.widget.w_step.machine.rotor.Kf1 == 0.95
        assert self.widget.w_step.machine.rotor.mat_type.name == "M400-50A"

        #####################
        # 9 Rotor Skew
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 9: Rotor Skew"
        assert isinstance(self.widget.w_step, SSkew)

        assert not self.widget.w_step.g_activate.isChecked()

        #####################
        # 10 Machine Summary
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "10: Machine Summary"
        assert isinstance(self.widget.w_step, SPreview)
        self.widget.w_step.tab_machine.is_test = True  # To hide the plots

        assert (
            self.widget.w_step.tab_machine.tab_param.item(0, 0).text() == "Machine Type"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(0, 1).text() == "IPMSM"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(1, 0).text()
            == "Stator slot number"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(1, 1).text() == "48"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(2, 0).text()
            == "Pole pair number"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(2, 1).text() == "4"
        assert self.widget.w_step.tab_machine.tab_param.item(3, 0).text() == "Topology"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(3, 1).text()
            == "Internal Rotor"
        )
        assert (
            self.widget.w_step.tab_machine.tab_param.item(4, 0).text()
            == "Stator phase number"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(4, 1).text() == "3"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(5, 0).text()
            == "Stator winding resistance"
        )
        assert (
            self.widget.w_step.tab_machine.tab_param.item(5, 1).text() == "0.03595 Ohm"
        )
        assert (
            self.widget.w_step.tab_machine.tab_param.item(6, 0).text()
            == "Machine total mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(6, 1).text() == "33.38 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(7, 0).text()
            == "Stator lamination mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(7, 1).text() == "15.78 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(8, 0).text()
            == "Stator winding mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(8, 1).text() == "4.001 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(9, 0).text()
            == "Rotor lamination mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(9, 1).text() == "5.006 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(10, 0).text()
            == "Rotor magnet mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(10, 1).text() == "1.236 kg"
        assert (
            self.widget.w_step.tab_machine.tab_param.item(11, 0).text() == "Shaft mass"
        )
        assert self.widget.w_step.tab_machine.tab_param.item(11, 1).text() == "7.355 kg"
        assert self.widget.w_step.tab_machine.tab_param.rowCount() == 12

        self.widget.w_step.tab_machine.b_plot_machine.clicked.emit()
        self.widget.w_step.tab_machine.b_mmf.clicked.emit()

        #####################
        # 11 FEMM Simulation
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == "11: FEMM Simulation"
        assert isinstance(self.widget.w_step, SSimu)

        assert self.widget.w_step.lf_N0.value() == 1000
        assert self.widget.w_step.lf_I1.value() == 0
        assert self.widget.w_step.lf_I2.value() == 0
        assert self.widget.w_step.lf_T_mag.value() == 20
        assert self.widget.w_step.si_Na_tot.value() == 1680
        assert self.widget.w_step.si_Nt_tot.value() == 480
        assert self.widget.w_step.is_per_a.isChecked()
        assert self.widget.w_step.is_per_t.isChecked()
        assert self.widget.w_step.lf_Kmesh.value() == 1
        assert self.widget.w_step.si_nb_worker.value() == cpu_count()
        assert self.widget.w_step.le_name.text() == "FEMM_Prius_Test"

        ## Define
        res_path = join(save_path, "Simu_Results")
        makedirs(res_path)
        with mock.patch(
            "qtpy.QtWidgets.QFileDialog.getExistingDirectory", return_value=res_path
        ):
            # To trigger the slot
            self.widget.w_step.w_path_result.b_path.clicked.emit()
        self.widget.w_step.si_Nt_tot.setValue(1)
        self.widget.w_step.si_Nt_tot.editingFinished.emit()
        self.widget.w_step.lf_Kmesh.setValue(0.6)
        self.widget.w_step.lf_Kmesh.editingFinished.emit()

        ## Run
        assert len(listdir(res_path)) == 0
        with mock.patch("qtpy.QtWidgets.QMessageBox.information", return_value=None):
            self.widget.w_step.b_next.clicked.emit()
        # Run creates a new results folder with execution time in the name
        assert len(listdir(res_path)) == 1
        assert len(listdir(join(res_path, listdir(res_path)[0]))) == 18
        assert np_max(
            self.widget.w_step.last_out.mag.B.components["radial"].values
        ) == pytest.approx(0.548, rel=0.1)


if __name__ == "__main__":
    a = TestNewMachinePrius()
    a.setup_class()
    a.setup_method()
    a.test_Toyota_Prius()
    print("Done")
