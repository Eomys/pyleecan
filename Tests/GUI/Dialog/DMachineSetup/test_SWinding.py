# -*- coding: utf-8 -*-

import sys
from os.path import join, isfile
from random import uniform
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
import mock
import pytest
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.GUI.Dialog.DMachineSetup.SWinding.SWinding import SWinding

from Tests import save_gui_path


class TestSWinding(object):
    """Test that the widget SWinding behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestSWinding")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""

        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind()
        test_obj.stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.stator.winding = Winding(p=3)
        test_obj.stator.winding.qs = 6
        test_obj.stator.winding.coil_pitch = 8
        test_obj.stator.winding.Nlayer = 2
        test_obj.stator.winding.Nslot_shift_wind = 10
        test_obj.stator.winding.Npcp = 2
        test_obj.stator.winding.is_reverse_wind = True
        test_obj.stator.winding.is_reverse_layer = True
        test_obj.stator.winding.is_change_layer = True
        test_obj.stator.winding.is_permute_B_C = True

        self.widget = SWinding(machine=test_obj, material_dict=dict(), is_stator=True)
        self.test_obj = test_obj.copy()

        self.test_obj_2 = test_obj.copy()
        self.test_obj.stator.winding = WindingUD()
        self.widget_2 = SWinding(
            machine=self.test_obj_2, material_dict=dict(), is_stator=True
        )

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    @pytest.mark.SCIM
    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""
        assert self.widget.in_Zs.text() == "Slot number: 36"
        assert self.widget.in_p.text() == "Pole pair number: 3"
        assert self.widget.si_qs.value() == 6
        assert self.widget.c_layer_def.currentIndex() == 2
        assert self.widget.si_coil_pitch.value() == 8
        assert self.widget.si_Nslot.value() == 10
        assert self.widget.si_Npcp.value() == 2
        assert self.widget.c_wind_type.currentIndex() == 0
        assert self.widget.c_wind_type.currentText() == "Star of Slot"
        assert self.widget.is_reverse.checkState() == Qt.Checked
        assert self.widget.is_reverse_layer.checkState() == Qt.Checked
        assert self.widget.is_permute_B_C.checkState() == Qt.Checked
        assert self.widget.out_rot_dir.text() == "Rotation direction: CW"

        self.test_obj = MachineSCIM()
        self.test_obj.stator = LamSlotWind()
        self.test_obj.stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.stator.winding = None
        self.widget = SWinding(
            machine=self.test_obj, material_dict=dict(), is_stator=True
        )

        assert self.widget.c_wind_type.currentIndex() == 0
        assert type(self.test_obj.stator.winding) == Winding

        self.test_obj = MachineSCIM()
        self.test_obj.stator = LamSlotWind()
        self.test_obj.stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        self.test_obj.stator.winding = Winding()
        self.test_obj.stator.winding.qs = None
        self.test_obj.stator.winding.coil_pitch = None
        self.test_obj.stator.winding.Nslot_shift_wind = None
        self.test_obj.stator.winding.Ntcoil = None
        self.test_obj.stator.winding.is_reverse_wind = None

        self.widget = SWinding(
            machine=self.test_obj, material_dict=dict(), is_stator=True
        )

        # The GUI define a default winding
        assert self.test_obj.stator.winding.qs == 3
        assert self.widget.si_qs.value() == 3
        assert self.test_obj.stator.winding.coil_pitch == 6
        assert self.widget.si_coil_pitch.value() == 6
        assert self.widget.si_Nslot.value() == 0
        assert self.widget.c_layer_def.currentIndex() == 0
        assert self.widget.machine.stator.winding.Ntcoil == 1
        assert not self.widget.machine.stator.winding.is_reverse_wind

    @pytest.mark.SCIM
    def test_set_wind_type(self):
        """Check that the Widget allow to update type_winding"""

        self.widget.c_wind_type.setCurrentIndex(1)
        assert type(self.widget.obj.winding) == WindingUD

        self.widget.c_wind_type.setCurrentIndex(0)
        assert type(self.widget.obj.winding) == Winding

    @pytest.mark.SCIM
    def test_generate(self):
        """Check that the Widget allow to update qs"""
        self.widget.si_qs.setValue(3)
        self.widget.c_layer_def.setCurrentIndex(2)
        self.widget.si_coil_pitch.setValue(5)
        self.widget.si_Ntcoil.setValue(9)
        self.widget.si_Npcp.setValue(2)

        self.widget.b_generate.clicked.emit()
        assert self.widget.obj.winding.wind_mat.shape == (2, 1, 36, 3)
        assert self.widget.out_rot_dir.text() == "Rotation direction: CCW"
        assert self.widget.out_ms.text() == "Slots per pole per phase: 2.0"
        assert self.widget.out_Nperw.text() == "Winding periodicity: 6"
        assert self.widget.out_Ncspc.text() == "Coils in series per parallel circuit: 6"
        assert self.widget.out_Ntspc.text() == "Turns in series per phase: 54"

    @pytest.mark.SCIM
    def test_export_import(self):
        return_value = (
            join(save_gui_path, "test_SWinding_export.csv"),
            "CSV (*.csv)",
        )

        assert not isfile(return_value[0])
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.b_export.clicked.emit()

        assert isfile(return_value[0])

        self.widget.c_wind_type.setCurrentIndex(1)
        assert not self.widget.b_import.isHidden()
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.b_import.clicked.emit()

    @pytest.mark.SCIM
    def test_set_is_reverse(self):
        """Check that the Widget allow to update is_reverse_wind"""
        self.widget.is_reverse.setCheckState(Qt.Unchecked)
        assert not self.widget.obj.winding.is_reverse_wind
        self.widget.is_reverse.setCheckState(Qt.Checked)
        assert self.widget.obj.winding.is_reverse_wind

    @pytest.mark.SCIM
    def test_set_is_reverse_layer(self):
        """Check that the Widget allow to update is_reverse_layer"""
        self.widget.is_reverse_layer.setCheckState(Qt.Unchecked)
        assert not self.widget.obj.winding.is_reverse_layer
        self.widget.is_reverse_layer.setCheckState(Qt.Checked)
        assert self.widget.obj.winding.is_reverse_layer

    @pytest.mark.SCIM
    def test_set_is_permute_B_C(self):
        """Check that the Widget allow to update is_permute_B_C"""
        self.widget.is_permute_B_C.setCheckState(Qt.Unchecked)
        assert not self.widget.obj.winding.is_permute_B_C
        self.widget.is_permute_B_C.setCheckState(Qt.Checked)
        assert self.widget.obj.winding.is_permute_B_C

    @pytest.mark.SCIM
    def test_set_c_layer_def(self):
        """Check that the Widget allow to update layer definition"""

        # First state: machine has two layers
        assert self.widget.obj.winding.Nlayer == 2

        # Second state: Machine has one layer
        self.widget.c_layer_def.setCurrentIndex(0)
        self.widget.b_generate.clicked.emit()
        assert self.widget.obj.winding.Nlayer == 1

        # Third state: Machine has double layer radial
        self.widget.c_layer_def.setCurrentIndex(1)
        self.widget.b_generate.clicked.emit()
        assert self.widget.obj.winding.Nlayer == 2
        assert not self.widget.obj.winding.is_change_layer

        # Fourth state: machine has double layer tangential
        self.widget.c_layer_def.setCurrentIndex(2)
        self.widget.b_generate.clicked.emit()
        assert self.widget.obj.winding.Nlayer == 2
        assert self.widget.obj.winding.is_change_layer

    @pytest.mark.SCIM
    def test_set_Nslot(self):
        """Check that the Widget allow to update Nslot"""
        self.widget.si_Nslot.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        self.widget.si_Nslot.setValue(value)

        assert self.widget.obj.winding.Nslot_shift_wind == value

    @pytest.mark.SCIM
    def test_set_Npcp(self):
        """Check that the Widget allow to update Npcp"""
        self.widget.si_Npcp.clear()  # Clear the field before writing
        value = int(uniform(1, 3))
        self.widget.si_Npcp.setValue(value)

        assert self.widget.obj.winding.Npcp == value

    @pytest.mark.SCIM
    def test_check(self):
        """Check that the check works correctly"""
        rotor = LamSlotWind()
        rotor.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(p=8, qs=None)

        assert "Error in winding matrix gen" in self.widget.check(rotor)


if __name__ == "__main__":
    a = TestSWinding()
    a.setup_class()
    a.setup_method()
    # a.test_init()
    # a.test_set_wind_type()
    # a.test_generate()
    # a.test_export_import()
    # a.test_set_is_reverse()
    # a.test_set_is_reverse_layer()
    # a.test_set_is_permute_B_C()
    # a.test_set_Nslot()
    a.test_set_Npcp()
    # a.test_check()
    # a.test_set_c_layer_def()
    a.teardown_class()
    print("Done")
