import sys
from os import makedirs
from os.path import isdir, join
from shutil import copytree, rmtree

import pytest
from PySide2 import QtWidgets

from Tests import TEST_DATA_DIR, save_gui_path as save_path
from pyleecan.Functions.load import LIB_KEY, MACH_KEY, load, load_matlib
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup

WS_path = join(save_path, "DMatlib_Workspace_test")
Ref_path = join(TEST_DATA_DIR, "Material", "Workflow")


class TestDMatlibWF(object):
    """Check that the GUI enables to set/modified/add/delete material from the
    Material library and the machine.
    The test machine / library has the following characteristics:
    - stator.mat_type, rotor.mat_type, shaft.mat_type == M400-50A same as matlib
    - rotor.hole[0] = Air missing from Reference library
    - rotor.hole[0].magnet_0.mat_type is an altered version of MagnetPrius
    - rotor.hole[0].magnet_1.mat_type matches MagnetPrius from Library
    """

    def setup_method(self):
        """Setup the workspace and the GUI"""

        # Setup workspace with machine and material copy
        if isdir(WS_path):
            rmtree(WS_path)
        copytree(Ref_path, WS_path)

        # Load Machine
        Toyota_Prius = load(join(WS_path, "Toyota_Prius.json"))
        assert Toyota_Prius.rotor.hole[0].magnet_0.mat_type.name == "MagnetPrius"
        # Load Material Library
        material_dict = load_matlib(machine=Toyota_Prius, matlib_path=WS_path)

        # Machine Setup Widget
        self.widget = DMachineSetup(material_dict=material_dict, machine=Toyota_Prius)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test DMachineSelector")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        if isdir(WS_path):
            rmtree(WS_path)
        cls.app.quit()

    def test_init(self):
        """Test that Machine GUI and WMatSelect are correctly loaded"""
        # Check content of MatLib
        assert self.widget.material_dict is not None
        mat_dict = self.widget.material_dict
        assert LIB_KEY in mat_dict
        assert [mat.name for mat in mat_dict[LIB_KEY]] == [
            "Copper1",
            "Insulator1",
            "M400-50A",
            "MagnetPrius",
        ]
        assert MACH_KEY in mat_dict
        assert [mat.name for mat in mat_dict[MACH_KEY]] == ["Air", "MagnetPrius_old"]
        # Check that all the WMatSelect widget are correctly defined
        exp_items = [
            "Copper1",
            "Insulator1",
            "M400-50A",
            "MagnetPrius",
            "Air",
            "MagnetPrius_old",
        ]
        self.widget.nav_step.setCurrentRow(1)  # MachineDimension
        combo = self.widget.w_step.w_mat_0.c_mat_type
        assert combo.currentText() == "M400-50A"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items
        self.widget.nav_step.setCurrentRow(2)  # LamParam Stator
        combo = self.widget.w_step.w_mat.c_mat_type
        assert combo.currentText() == "M400-50A"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items
        self.widget.nav_step.setCurrentRow(5)  # Winding conductor
        combo = self.widget.w_step.w_mat_0.c_mat_type
        assert combo.currentText() == "Copper1"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items
        combo = self.widget.w_step.w_mat_1.c_mat_type
        assert combo.currentText() == "Insulator1"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items
        self.widget.nav_step.setCurrentRow(6)  # LamParam Rotor
        combo = self.widget.w_step.w_mat.c_mat_type
        assert combo.currentText() == "M400-50A"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items
        self.widget.nav_step.setCurrentRow(7)  # Hole material
        combo = self.widget.w_step.tab_hole.widget(0).w_hole.w_mat_0.c_mat_type
        assert combo.currentText() == "Air"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items
        combo = self.widget.w_step.tab_hole.widget(0).w_hole.w_mat_1.c_mat_type
        assert (
            self.widget.machine.rotor.hole[0].magnet_0.mat_type.name
            == "MagnetPrius_old"
        )
        assert combo.currentText() == "MagnetPrius_old"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items
        combo = self.widget.w_step.tab_hole.widget(0).w_hole.w_mat_2.c_mat_type
        assert combo.currentText() == "MagnetPrius"
        assert [combo.itemText(i) for i in range(combo.count())] == exp_items

    def edit_matlib(self):
        """Edit a material in the Library and check changes in machine"""
        # Check initial state
        assert self.widget.machine.stator.mat_type.elec.rho == 1
        assert self.widget.machine.rotor.mat_type.elec.rho == 1
        assert self.widget.machine.shaft.mat_type.elec.rho == 1
        M400 = load(join(WS_path, "M400-50A.json"))
        assert M400.elec.rho == 1
        # Open DMatlib
        self.widget.nav_step.setCurrentRow(2)  # LamParam Stator
        assert self.widget.w_step.w_mat.current_dialog is None
        self.widget.w_step.w_mat.b_matlib.clicked.emit()
        assert isinstance(self.widget.w_step.w_mat.current_dialog, DMatLib)
        dialog = self.widget.w_step.w_mat.current_dialog
        assert dialog.is_lib_mat is True
        assert dialog.nav_mat.currentRow() == 2
        assert dialog.out_rho_elec.text() == "rho = 1 [ohm.m]"
        # Edit M400-50A material
        dialog.b_edit.clicked.emit()
        dialog.current_dialog.lf_rho_elec.setValue(2)
        dialog.current_dialog.lf_rho_elec.editingFinished.emit()
        dialog.current_dialog.b_save.clicked.emit()
        # Check modifications
        assert dialog.nav_mat.currentRow() == 2
        assert dialog.out_rho_elec.text() == "rho = 2.0 [ohm.m]"
        assert self.widget.machine.stator.mat_type.elec.rho == 2
        assert self.widget.machine.rotor.mat_type.elec.rho == 2
        assert self.widget.machine.shaft.mat_type.elec.rho == 2
        M400 = load(join(WS_path, "M400-50A.json"))
        assert M400.elec.rho == 2

    def edit_machine_material(self):
        """Edit a material from the machine"""
        # Check initial state
        assert self.widget.machine.rotor.hole[0].mat_void.struct.rho == 1.2044
        # Open DMatlib
        self.widget.nav_step.setCurrentRow(7)  # Hole material
        w_mat = self.widget.w_step.tab_hole.widget(0).w_hole.w_mat_0
        assert w_mat.current_dialog is None
        w_mat.b_matlib.clicked.emit()
        assert isinstance(w_mat.current_dialog, DMatLib)
        dialog = w_mat.current_dialog
        assert dialog.is_lib_mat is False
        assert dialog.nav_mat_mach.currentRow() == 0
        assert dialog.out_rho_meca.text() == "rho = 1.2044 [kg/m^3]"
        # Edit M400-50A material
        dialog.b_edit.clicked.emit()
        dialog.current_dialog.lf_rho_meca.setValue(2.468)
        dialog.current_dialog.lf_rho_meca.editingFinished.emit()
        dialog.current_dialog.b_save.clicked.emit()
        # Check modifications
        assert dialog.nav_mat_mach.currentRow() == 0
        assert dialog.out_rho_meca.text() == "rho = 2.468 [kg/m^3]"
        assert self.widget.machine.rotor.hole[0].mat_void.struct.rho == 2.468


if __name__ == "__main__":
    a = TestDMatlibWF()
    a.setup_class()
    a.setup_method()
    a.edit_machine_material()
    print("Done")
