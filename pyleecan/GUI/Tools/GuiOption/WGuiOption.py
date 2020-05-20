from os import getcwd, rename, remove
from os.path import join, dirname, abspath, split
from re import match

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from ....Functions.load import load_matlib
from ....Functions.Material.compare_material import compare_material
from ....Functions.Material.replace_material_pyleecan_obj import (
    replace_material_pyleecan_obj,
)
from ....GUI.Tools.GuiOption.Ui_GuiOption import Ui_GUIOption
from ....GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from ....definitions import DATA_DIR
from ....GUI import GUI_logger, gui_option
from ....Functions.path_tools import abs_file_path
from ....definitions import edit_config_dict, MATLIB_DIR
from ....Functions.load import load_matlib
from ....Classes.Material import Material


class WGuiOption(Ui_GUIOption, QDialog):
    def __init__(self, machine_setup, dmatlib):
        """
        WGuiOption enable to modify some option in the GUI such as:
            - units
            - material library folder
        
        Parameters:
        machine_setup: DMachineSetup
            Machine widget
        dmatlib: DMatlib 
            Material library widget
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.le_matlib_path.setText(MATLIB_DIR)
        self.machine_setup = machine_setup  # DMachineSetup to access to the machine
        self.dmatlib = dmatlib  # dmatlib to access to the material library
        self.c_unit_m.setCurrentIndex(gui_option.unit.unit_m)
        self.c_unit_m2.setCurrentIndex(gui_option.unit.unit_m2)

        # Connections
        self.b_matlib_path.clicked.connect(self.b_define_matlib_dir)
        self.le_matlib_path.textChanged.connect(self.change_matlib_dir)
        self.c_unit_m.currentTextChanged.connect(lambda: self.change_unit(unit="m"))
        self.c_unit_m2.currentTextChanged.connect(lambda: self.change_unit(unit="m2"))

    def b_define_matlib_dir(self):
        """
        b_define_matlib_dir open a dialog to select the matlib directory 
        """
        folder = QFileDialog.getExistingDirectory(self, "Select MatLib directory")
        if folder != self.dmatlib.matlib_path and folder:
            self.dmatlib.matlib_path = folder
            self.le_matlib_path.setText(folder)

    def change_matlib_dir(self):
        """
        Change the matlib directory and load the new matlib
        """
        matlib_path = self.le_matlib_path.text()
        edit_config_dict("MATLIB_DIR", matlib_path)
        new_matlib = load_matlib(matlib_path)

        # Get the current machine matlib
        machine_matlib = self.dmatlib.matlib[self.dmatlib.index_first_matlib_mach :]

        # Add the machine material in case one of them has been add to the previous MatLib
        current_machine_mat = self.machine_setup.machine.get_material_list()

        for mat in current_machine_mat:
            if mat.is_isotropic != None and mat not in machine_matlib:
                machine_matlib.append(mat)

        self.dmatlib.index_first_matlib_mach = len(new_matlib)
        self.dmatlib.matlib = new_matlib

        # Copy the new matlib and remove material name and path to compare material
        matlib_without_name = [
            Material(init_dict=material.as_dict()) for material in new_matlib
        ]
        for mat in matlib_without_name:
            mat.name = ""
            mat.path = ""

        # Check if the machine material are in the new MatLib
        default_mat = Material()
        for mat in machine_matlib:
            name = mat.name
            path = mat.path
            mat.name = ""
            mat.path = ""
            if mat not in matlib_without_name:
                mat.name = name
                mat.path = path
                if mat != default_mat:
                    self.dmatlib.matlib.append(mat)
                    self.dmatlib.check_duplicated_material(len(self.dmatlib.matlib) - 1)
            # Else replace the machine material by the matlib one
            else:
                for matlib_material in self.dmatlib.matlib:
                    # Find the material in the matlib
                    if compare_material(mat, matlib_material):
                        replace_material_pyleecan_obj(
                            self.machine_setup.machine, mat, matlib_material
                        )
                        break

        self.dmatlib.update_mat_list()

    def change_unit(self, unit="m"):
        """
        change_unit changes the unit in the gui options and save this change in the 
        pyleecan default configuration

        unit : str
            unit to update
        """
        global gui_option
        if unit == "m":  # Length unit
            key = "UNIT_M"
            value = self.c_unit_m.currentIndex()
            gui_option.unit.unit_m = value
        elif unit == "m2":  # Surface unit
            key = "UNIT_M2"
            value = self.c_unit_m2.currentIndex()
            gui_option.unit.unit_m2 = value
        else:
            raise ValueError("Unexpected argument in change_unit, unit=" + str(unit))

        edit_config_dict(key, value)
