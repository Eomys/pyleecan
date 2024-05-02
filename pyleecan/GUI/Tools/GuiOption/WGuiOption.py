from os import getcwd, rename, remove
from os.path import join, dirname, abspath, split
from re import match

from qtpy.QtWidgets import QDialog, QFileDialog, QMessageBox

from ....Functions.load import load_matlib
from ....GUI.Tools.GuiOption.Ui_GuiOption import Ui_GUIOption
from ....GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from ....GUI import gui_option
from ....Functions.path_tools import abs_file_path
from ....Functions.init_environment import save_config_dict
from ....definitions import config_dict
from ....Functions.load import load_matlib
from ....Classes.Material import Material


class WGuiOption(Ui_GUIOption, QDialog):
    def __init__(self, machine_setup=None, matlib=None):
        """
        WGuiOption enable to modify some option in the GUI such as:
            - units
            - material library folder

        Parameters:
        machine_setup: DMachineSetup
            Machine widget
        matlib : DMatLib
            Material Library Dialog
        """
        QDialog.__init__(self)
        self.setupUi(self)
        # Matlib path selector setup
        self.w_matlib_path.verbose_name = "Matlib directory"
        self.w_matlib_path.is_file = False
        self.w_matlib_path.set_path_txt(config_dict["MAIN"]["MATLIB_DIR"])
        self.w_matlib_path.update()

        self.machine_setup = machine_setup  # DMachineSetup to access to the machine
        self.matlib = matlib  # dmatlib to access to the material library

        self.c_unit_m.setCurrentIndex(gui_option.unit.unit_m)
        self.c_unit_m2.setCurrentIndex(gui_option.unit.unit_m2)

        # Connections
        self.w_matlib_path.pathChanged.connect(self.change_matlib_dir)
        self.c_unit_m.currentTextChanged.connect(self.set_unit_m)
        self.c_unit_m2.currentTextChanged.connect(self.set_unit_m2)

    def change_matlib_dir(self):
        """
        Change the matlib directory and load the new matlib
        """
        matlib_path = self.w_matlib_path.get_path()
        config_dict["MAIN"]["MATLIB_DIR"] = matlib_path
        save_config_dict(config_dict)

        if self.matlib is not None:
            self.matlib.load_mat_ref(matlib_path)
            if self.machine_setup is not None:
                self.matlib.add_machine_mat(self.machine_setup.machine)

    def set_unit_m(self):
        """Update the value of unit_m"""
        global gui_option
        gui_option.unit.unit_m = self.c_unit_m.currentIndex()
        config_dict["GUI"]["UNIT_M"] = gui_option.unit.unit_m
        save_config_dict(config_dict)

    def set_unit_m2(self):
        """Update the value of unit_m2"""
        global gui_option
        gui_option.unit.unit_m2 = self.c_unit_m2.currentIndex()
        config_dict["GUI"]["UNIT_M2"] = gui_option.unit.unit_m2
        save_config_dict(config_dict)
