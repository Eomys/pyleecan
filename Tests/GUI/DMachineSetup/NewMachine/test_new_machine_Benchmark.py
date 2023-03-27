import sys
from os.path import join

from PySide2 import QtWidgets
import pytest
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape
from pyleecan.GUI.Dialog.DMachineSetup.SMachineDimension.SMachineDimension import (
    SMachineDimension,
)
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.SMSlot import SMSlot
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from pyleecan.GUI.Dialog.DMachineSetup.SSimu.SSimu import SSimu
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType11.PCondType11 import PCondType11
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.GUI.Dialog.DMachineSetup.SWinding.SWinding import SWinding
from pyleecan.GUI.Dialog.DMachineSetup.SPreview.SPreview import SPreview
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.SWSlot import SWSlot
from pyleecan.GUI.Dialog.DMachineSetup.SSkew.SSkew import SSkew

from Tests.GUI import gui_option  # Set unit as [m]

from pyleecan.Functions.load import load_matlib

from pyleecan.definitions import DATA_DIR

import logging

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)

matlib_path = join(DATA_DIR, "Material")


class TestNewMachineBenchmark(object):
    """Test that you can create the Benchmark"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test NewMachineBenchmark")
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
    def test_Benchmark(self):
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
        index_SPMSM = self.widget.w_step.c_type.findText("SPMSM")
        self.widget.w_step.c_type.setCurrentIndex(index_SPMSM)
        assert self.widget.w_step.c_type.currentText() == "SPMSM"
        self.widget.w_step.le_name.setText("Benchmark_Test")
        self.widget.w_step.le_name.editingFinished.emit()
        self.widget.w_step.si_p.setValue(5)
        self.widget.w_step.si_p.editingFinished.emit()
        assert self.widget.w_step.si_p.value() == 5
        ## Check modif
        assert isinstance(self.widget.machine, MachineSIPMSM)
        assert self.widget.machine.name == "Benchmark_Test"
        assert self.widget.machine.stator.winding.p == 5

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
        self.widget.w_step.lf_SRext.setText("0.073")
        self.widget.w_step.lf_SRext.editingFinished.emit()
        self.widget.w_step.lf_SRint.setText("0.048")
        self.widget.w_step.lf_SRint.editingFinished.emit()
        self.widget.w_step.lf_RRext.setText("0.04")
        self.widget.w_step.lf_RRext.editingFinished.emit()
        self.widget.w_step.g_shaft.setChecked(True)
        assert self.widget.w_step.lf_RRint.isEnabled()
        self.widget.w_step.lf_RRint.setText("0.0095")
        self.widget.w_step.lf_RRint.editingFinished.emit()
        ## Check modif
        assert self.widget.machine.stator.Rext == pytest.approx(0.073)
        assert self.widget.machine.stator.Rint == pytest.approx(0.048)
        assert self.widget.machine.rotor.Rext == pytest.approx(0.04)
        assert self.widget.machine.rotor.Rint == pytest.approx(0.0095)
        assert self.widget.w_step.out_Drsh.text() == "Drsh = 0.019 [m]"
        assert self.widget.w_step.out_airgap.text() == "Airgap magnetic width = 8 [mm]"
        assert isinstance(self.widget.machine.shaft, Shaft)
        assert self.widget.machine.frame is None

        #####################
        # 3 Stator Slot
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 3: Stator Slot"
        assert isinstance(self.widget.w_step, SWSlot)

        self.widget.w_step.si_Zs.setValue(12)
        self.widget.w_step.si_Zs.editingFinished.emit()
        index_slot22 = self.widget.w_step.c_slot_type.findText("Slot Type 22")
        self.widget.w_step.c_slot_type.setCurrentIndex(index_slot22)
        self.widget.w_step.w_slot.lf_W0.setValue(0.3142)
        self.widget.w_step.w_slot.lf_W0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_W2.setValue(0.3142)
        self.widget.w_step.w_slot.lf_W2.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H0.setValue(0)
        self.widget.w_step.w_slot.lf_H0.editingFinished.emit()
        self.widget.w_step.w_slot.lf_H2.setValue(0.02)
        self.widget.w_step.w_slot.lf_H2.editingFinished.emit()
        ## Check modif
        self.widget.w_step.b_plot.clicked.emit()
        assert self.widget.w_step.machine.stator.slot.W0 == pytest.approx(0.3142)
        assert self.widget.w_step.machine.stator.slot.W2 == pytest.approx(0.3142)
        assert self.widget.w_step.machine.stator.slot.H0 == pytest.approx(0)
        assert self.widget.w_step.machine.stator.slot.H2 == pytest.approx(0.02)
        assert self.widget.w_step.out_Slot_pitch.text() == "Slot pitch = 360 / Zs = 30 [°] (0.5236 [rad])"
        assert (
            self.widget.w_step.w_slot.w_out.out_Wlam.text() == "Stator width: 0.025 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_slot_height.text() == "Slot height: 0.02 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_yoke_height.text() == "Yoke height: 0.005 [m]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_wind_surface.text()
            == "Active surface: 0.0003645 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_tot_surface.text()
            == "Slot surface: 0.0003645 [m²]"
        )
        assert (
            self.widget.w_step.w_slot.w_out.out_op_angle.text()
            == "Opening angle: 0.3142 [rad]"
        )

        #####################
        # 4 Stator Lamination
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 4: Stator Lamination"
        assert isinstance(self.widget.w_step, SLamShape)

        assert self.widget.w_step.lf_L1.value() is None
        assert self.widget.w_step.lf_Kf1.value() == 0.95

        assert not self.widget.w_step.g_axial.isChecked()
        assert not self.widget.w_step.g_radial.isChecked()
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.lf_L1.setValue(0.14)
        self.widget.w_step.lf_L1.editingFinished.emit()

        assert self.widget.w_step.lf_L1.value() == 0.14
        # ? -> Because Radial cooling duct hasn't been activated once
        assert self.widget.w_step.out_length.text() == "Stator total length = ?"

        assert self.widget.w_step.machine.stator.L1 == 0.14
        assert self.widget.w_step.machine.stator.Kf1 == 0.95

        #####################
        # 5 Stator Winding
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 5: Stator Winding"
        assert isinstance(self.widget.w_step, SWinding)

        assert self.widget.w_step.c_wind_type.currentText() == "Star of Slot"
        assert self.widget.w_step.in_Zs.text() == "Slot number=12"
        assert self.widget.w_step.in_p.text() == "Pole pair number=5"
        assert self.widget.w_step.si_qs.value() == 3
        assert self.widget.w_step.si_Nlayer.value() == 1
        assert self.widget.w_step.si_coil_pitch.value() == 1
        assert self.widget.w_step.si_Ntcoil.value() == 1
        assert self.widget.w_step.si_Npcp.value() == 1
        assert self.widget.w_step.si_Nslot.value() == 0
        assert not self.widget.w_step.is_reverse.isChecked()
        assert not self.widget.w_step.is_permute_B_C.isChecked()
        assert not self.widget.w_step.is_reverse_layer.isChecked()
        assert not self.widget.w_step.is_change_layer.isChecked()

        self.widget.w_step.si_Nlayer.setValue(2)
        self.widget.w_step.si_Nlayer.editingFinished.emit()

        self.widget.w_step.b_generate.clicked.emit()

        assert self.widget.w_step.si_Nlayer.value() == 2
        # TODO BUG find why the Rotation direction does not setup as a CCW rotation (In an imported Benchmark, it does.)
        assert self.widget.w_step.out_rot_dir.text() == "Rotation direction: ?"
        assert self.widget.w_step.out_ms.text() == "Number of slots/pole/phase: 0.4"
        assert self.widget.w_step.out_Nperw.text() == "Winding periodicity: 2"
        assert self.widget.w_step.out_Ntspc.text() == "Number of turns Ntspc: 4"
        assert self.widget.w_step.out_Ncspc.text() == "Number of coils Ncspc: 4"


        # Is the stator winding well defined ?
        assert self.widget.w_step.machine.stator.winding.qs == 3
        assert self.widget.w_step.machine.stator.winding.Nlayer == 2
        assert self.widget.w_step.machine.stator.winding.coil_pitch == 1
        assert self.widget.w_step.machine.stator.winding.Ntcoil == 1
        assert self.widget.w_step.machine.stator.winding.Npcp == 1
        assert self.widget.w_step.machine.stator.winding.Nslot_shift_wind == 0
        assert not self.widget.w_step.machine.stator.winding.is_reverse_wind
        assert not self.widget.w_step.machine.stator.winding.is_permute_B_C
        assert not self.widget.w_step.machine.stator.winding.is_reverse_layer
        assert not self.widget.w_step.machine.stator.winding.is_change_layer

        #####################
        # 6 Stator Conductor
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 6: Stator Conductor"
        assert isinstance(self.widget.w_step, SWindCond)

        # Initial state
        assert self.widget.w_step.c_cond_type.currentText() == "Preformed Rectangular"
        assert self.widget.w_step.w_mat_0.c_mat_type.currentText() == "Copper1"
        assert self.widget.w_step.w_mat_1.c_mat_type.currentText() == "Insulator1"
        assert isinstance(self.widget.w_step.w_cond, PCondType11)
        assert not self.widget.w_step.w_cond.g_ins.isChecked()
        assert self.widget.w_step.w_cond.si_Nwpc1_rad.value() == 1
        assert self.widget.w_step.w_cond.si_Nwpc1_tan.value() == 1
        assert self.widget.w_step.w_cond.lf_Wwire.value() is None
        assert self.widget.w_step.w_cond.lf_Hwire.value() is None
        assert self.widget.w_step.w_cond.lf_Lewout.value() == 0

        self.widget.w_step.w_cond.g_ins.setChecked(True)

        self.widget.w_step.w_cond.si_Nwpc1_rad.setValue(10)
        self.widget.w_step.w_cond.si_Nwpc1_rad.editingFinished.emit()
        self.widget.w_step.w_cond.si_Nwpc1_tan.setValue(5)
        self.widget.w_step.w_cond.si_Nwpc1_tan.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wwire.setValue(0.001)
        self.widget.w_step.w_cond.lf_Wwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Hwire.setValue(0.001)
        self.widget.w_step.w_cond.lf_Hwire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Wins_wire.setValue(0.0005)
        self.widget.w_step.w_cond.lf_Wins_wire.editingFinished.emit()
        self.widget.w_step.w_cond.lf_Lewout.setValue(0)
        self.widget.w_step.w_cond.lf_Lewout.editingFinished.emit()

        assert self.widget.w_step.w_cond.w_out.out_H.text() == "Hcond = 0.02 [m]"
        assert self.widget.w_step.w_cond.w_out.out_W.text() == "Wcond = 0.01 [m]"
        assert self.widget.w_step.w_cond.w_out.out_S.text() == "Scond = 0.0002 [m²]"
        assert self.widget.w_step.w_cond.w_out.out_Sact.text() == "Scond_active = 5e-05 [m²]"
        assert self.widget.w_step.w_cond.w_out.out_K.text() == "Ksfill = 27.44 %"
        assert self.widget.w_step.w_cond.w_out.out_MLT.text() == "Mean Length Turn = 0.28 [m]"
        assert self.widget.w_step.w_cond.w_out.out_Rwind.text() == "Rwind 20°C = 0.0003875 [Ohm]"

        # Is the stator winding conductors well defined ?
        assert isinstance(self.widget.w_step.machine.stator.winding.conductor, CondType11)
        assert self.widget.w_step.machine.stator.winding.conductor.Nwppc_tan == 5
        assert self.widget.w_step.machine.stator.winding.conductor.Nwppc_rad == 10
        assert self.widget.w_step.machine.stator.winding.conductor.Wwire == 0.001
        assert self.widget.w_step.machine.stator.winding.conductor.Hwire == 0.001
        assert self.widget.w_step.machine.stator.winding.conductor.Wins_wire == 0.0005
        assert self.widget.w_step.machine.stator.winding.Lewout == 0

        #####################
        # 7 Rotor Magnet
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 7: Rotor Magnet"
        assert isinstance(self.widget.w_step, SMSlot)

        assert self.widget.w_step.out_Slot_pitch.text() == "p = 5 / Slot pitch = 36 [°] (0.6283 [rad])"
        assert self.widget.w_step.c_slot_type.currentText() == "Rectangular Magnet"
        assert self.widget.w_step.c_type_magnetization.currentText() == "Radial"
        assert self.widget.w_step.w_mat.c_mat_type.currentText() == "Magnet1"

        index_polar_magnet = self.widget.w_step.c_slot_type.findText("Polar Magnet")
        self.widget.w_step.c_slot_type.setCurrentIndex(index_polar_magnet)
        index_magnetPrius = self.widget.w_step.w_mat.c_mat_type.findText("MagnetPrius")
        self.widget.w_step.w_mat.c_mat_type.setCurrentIndex(index_magnetPrius)

        wid_slot = self.widget.w_step.w_slot
        assert isinstance(wid_slot, PMSlot11)

        assert wid_slot.lf_W0.value() is None
        assert wid_slot.lf_Wmag.value() is None
        assert wid_slot.lf_H0.value() is None
        assert wid_slot.lf_Hmag.value() is None

        wid_slot.lf_W0.setValue(0.6048)
        wid_slot.lf_W0.editingFinished.emit()
        wid_slot.lf_Wmag.setValue(0.6048)
        wid_slot.lf_Wmag.editingFinished.emit()
        wid_slot.lf_H0.setValue(0)
        wid_slot.lf_H0.editingFinished.emit()
        wid_slot.lf_Hmag.setValue(0.005)
        wid_slot.lf_Hmag.editingFinished.emit()

        assert wid_slot.w_out.out_Wlam.text() == "Rotor width: 0.0305 [m]"
        assert wid_slot.w_out.out_slot_height.text() == "Slot height: 0 [m]"
        assert wid_slot.w_out.out_yoke_height.text() == "Yoke height: 0.0305 [m]"
        assert wid_slot.w_out.out_wind_surface.text() == "Active surface: 0.0001285 [m²]"
        assert wid_slot.w_out.out_tot_surface.text() == "Slot surface: 0 [m²]"
        assert wid_slot.w_out.out_op_angle.text() == "Opening angle: 0.6048 [rad]"

        assert self.widget.w_step.machine.rotor.slot.W0 == 0.6048
        assert self.widget.w_step.machine.rotor.slot.Wmag == 0.6048
        assert self.widget.w_step.machine.rotor.slot.H0 == 0
        assert self.widget.w_step.machine.rotor.slot.Hmag == 0.005

        #####################
        # 8 Rotor Lamination
        self.widget.w_step.b_next.clicked.emit()
        assert self.widget.nav_step.currentItem().text() == " 8: Rotor Lamination"
        assert isinstance(self.widget.w_step, SLamShape)

        assert self.widget.w_step.lf_L1.value() == 0.14
        assert self.widget.w_step.lf_Kf1.value() == 0.95

        assert not self.widget.w_step.g_axial.isChecked()
        assert not self.widget.w_step.g_radial.isChecked()
        assert not self.widget.w_step.g_notches.isChecked()

        assert self.widget.w_step.machine.rotor.L1 == 0.14
        assert self.widget.w_step.machine.rotor.Kf1 == 0.95

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

        assert self.widget.w_step.tab_machine.tab_param.item(0,0).text() == "Machine Type"
        assert self.widget.w_step.tab_machine.tab_param.item(0,1).text() == "SIPMSM"
        assert self.widget.w_step.tab_machine.tab_param.item(1,0).text() == "Stator slot number"
        assert self.widget.w_step.tab_machine.tab_param.item(1,1).text() == "12"
        assert self.widget.w_step.tab_machine.tab_param.item(2,0).text() == "Pole pair number"
        assert self.widget.w_step.tab_machine.tab_param.item(2,1).text() == "5"
        assert self.widget.w_step.tab_machine.tab_param.item(3,0).text() == "Topology"
        assert self.widget.w_step.tab_machine.tab_param.item(3,1).text() == "Internal Rotor"
        assert self.widget.w_step.tab_machine.tab_param.item(4,0).text() == "Stator phase number"
        assert self.widget.w_step.tab_machine.tab_param.item(4,1).text() == "3"
        assert self.widget.w_step.tab_machine.tab_param.item(5,0).text() == "Stator winding resistance"
        assert self.widget.w_step.tab_machine.tab_param.item(5,1).text() == "0.0003875 Ohm"

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
        assert self.widget.w_step.si_Na_tot.value() == 2100
        assert self.widget.w_step.si_Nt_tot.value() == 120
        assert self.widget.w_step.is_per_a.isChecked()
        assert self.widget.w_step.is_per_t.isChecked()
        assert self.widget.w_step.lf_Kmesh.value() == 1
        assert self.widget.w_step.si_nb_worker.value() == 12
        assert self.widget.w_step.le_name.text() == "FEMM_Benchmark_Test"

if __name__ == "__main__":
    a = TestNewMachineBenchmark()
    a.setup_class()
    a.setup_method()
    a.test_Benchmark()
    print("Done")