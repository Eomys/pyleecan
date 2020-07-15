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
from ....GUI import GUI_logger, gui_option
from ....Functions.path_tools import abs_file_path
from ....Functions.init_environment import save_config_dict
from ....definitions import config_dict
from ....Functions.load import load_matlib
from ....Classes.Material import Material


class WGuiOption(Ui_GUIOption, QDialog):
    def __init__(self, machine_setup, matlib):
        """
        WGuiOption enable to modify some option in the GUI such as:
            - units
            - material library folder
        
        Parameters:
        machine_setup: DMachineSetup
            Machine widget
        matlib : MatLib
            Material Library 
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.le_matlib_path.setText(config_dict["MAIN"]["MATLIB_DIR"])
        self.machine_setup = machine_setup  # DMachineSetup to access to the machine
        self.matlib = matlib  # dmatlib to access to the material library
        self.c_unit_m.setCurrentIndex(gui_option.unit.unit_m)
        self.c_unit_m2.setCurrentIndex(gui_option.unit.unit_m2)

        # Connections
        self.b_matlib_path.clicked.connect(self.b_define_matlib_dir)
        self.le_matlib_path.textChanged.connect(self.change_matlib_dir)
        self.c_unit_m.currentTextChanged.connect(self.set_unit_m)
        self.c_unit_m2.currentTextChanged.connect(self.set_unit_m2)

    def b_define_matlib_dir(self):
        """
        b_define_matlib_dir open a dialog to select the matlib directory 
        """
        folder = QFileDialog.getExistingDirectory(self, "Select MatLib directory")
        if folder != self.matlib.ref_path and folder:
            self.le_matlib_path.setText(folder)
        GUI_logger.info("message")

    def change_matlib_dir(self):
        """
        Change the matlib directory and load the new matlib
        """
        matlib_path = self.le_matlib_path.text()
        config_dict["MAIN"]["MATLIB_DIR"] = matlib_path
        save_config_dict(config_dict)

        self.matlib.load_mat_ref(matlib_path)
        self.matlib.add_machine_mat(self.machine_setup.machine)

    def set_unit_m(self):
        """Update the value of unit_m
        """
        global gui_option
        gui_option.unit.unit_m = self.c_unit_m.currentIndex()
        config_dict["GUI"]["UNIT_M"] = gui_option.unit.unit_m
        save_config_dict(config_dict)

    def set_unit_m2(self):
        """Update the value of unit_m2
        """
        global gui_option
        gui_option.unit.unit_m2 = self.c_unit_m2.currentIndex()
        config_dict["GUI"]["UNIT_M2"] = gui_option.unit.unit_m2
        save_config_dict(config_dict)
