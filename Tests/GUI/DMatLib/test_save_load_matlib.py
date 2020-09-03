# -*- coding: utf-8 -*-

import sys
from os import listdir, mkdir, remove
from os.path import abspath, basename, isdir, isfile, join
from shutil import copyfile, rmtree

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QDialogButtonBox

from pyleecan.Functions.load import load
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from Tests import TEST_DATA_DIR
from Tests import save_load_path as save_path


import pytest


@pytest.mark.GUI
class Testsave_load_matlib(object):
    """Test that the widget DMachineSetup and DMatLib can save/load the MatLib (old and new)
    """

    def setup_method(self, method):
        """Run at the begining of every test to create the workspace
        """
        self.work_path = join(save_path, "Material")
        # Delete old test if needed
        if isdir(self.work_path):
            rmtree(self.work_path)
        mkdir(self.work_path)

    def teardown(self):
        """Delete the workspace at the end of the tests
        """
        rmtree(self.work_path)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test Save/Load MatLib")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()


    def test_load_save_several_file(self):
        """Check that you can load/save several machine files
            """
        # Copy the matlib
        mkdir(join(self.work_path, "Lamination"))
        mkdir(join(self.work_path, "Magnet"))
        copyfile(    
            join(TEST_DATA_DIR, "Material", "Magnet1.json"),    
            join(self.work_path, "Magnet", "Magnet1.json"),    
        )
        cop_path = join(self.work_path, "Copper1.json")
        copyfile(join(TEST_DATA_DIR, "Material", "Copper1.json"), cop_path)
        copyfile(    
            join(TEST_DATA_DIR, "Material", "Insulator1.json"),    
            join(self.work_path, "Insulator1.json"),    
        )
        lam_path = join(self.work_path, "Lamination", "M400-50A.json")
        copyfile(join(TEST_DATA_DIR, "Material", "M400-50A.json"), lam_path)
        nb_file = len(    
            [    
                name    
                for name in listdir(self.work_path)    
                if isfile(join(self.work_path, name)) and name[-5:] == ".json"    
            ]    
        )
        assert nb_file == 2

        # Start the GUI
        self.matlib = MatLib(self.work_path)
        self.mat_widget = DMatLib(matlib=self.matlib)
        self.widget = DMachineSetup(    
            dmatlib=self.mat_widget, machine=None, machine_path=self.work_path    
        )
        # Check load of the matlib
        assert len(self.matlib.dict_mat["RefMatLib"]) == 4
        assert ["Copper1", "Insulator1", "M400-50A", "Magnet1"] == [mat.name for mat in self.matlib.dict_mat["RefMatLib"]]

        assert self.matlib.dict_mat["RefMatLib"][0].elec.rho == 1.73e-8
        assert self.matlib.dict_mat["RefMatLib"][0].HT.alpha == 0.00393
        assert self.matlib.dict_mat["RefMatLib"][0].path == join(self.work_path, "Copper1.json").replace("\\", "/")

        assert self.matlib.dict_mat["RefMatLib"][2].mag.mur_lin == 2500
        assert self.matlib.dict_mat["RefMatLib"][2].struct.rho == 7650
        assert self.matlib.dict_mat["RefMatLib"][2].struct.Ex == 215000000000
        assert self.matlib.dict_mat["RefMatLib"][2].path ==    join(self.work_path, "Lamination", "M400-50A.json").replace("\\", "/")
        # Change value of materials
        self.matlib.dict_mat["RefMatLib"][0].elec.rho = 1.74e-8
        self.matlib.dict_mat["RefMatLib"][0].HT.alpha = 0.00555
        self.matlib.dict_mat["RefMatLib"][2].mag.mur_lin = 2501.2
        self.matlib.dict_mat["RefMatLib"][2].struct.rho = 76
        # Save matlib
        for mat in self.matlib.dict_mat["RefMatLib"]:
            mat.save(mat.path)
            mat2 = load(mat.path)
            assert mat.as_dict() == mat2.as_dict()


def compare_file(file_path1, file_path2):
    # name1 = basename(file_path1)
    # name2 = basename(file_path2)
    # if name1 != name2:
    #     return "Different file name: (" + name1 + ", " + name2 + ")"
    with open(file_path1) as file1:
        with open(file_path2) as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            if len(lines1) != len(lines2):
                return (
                    "Different file length: ("
                    + str(len(lines1))
                    + ", "
                    + str(len(lines2))
                    + ")"
                )
            for ii in range(len(lines1)):
                if lines1[ii] != lines2[ii]:
                    return (
                        "Different line "
                        + str(ii)
                        + ":\n"
                        + lines1[ii]
                        + "\n"
                        + lines2[ii]
                    )
    return None
