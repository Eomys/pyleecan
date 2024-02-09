# -*- coding: utf-8 -*-

import sys
import os
from os.path import isdir, isfile, join
from os import makedirs, listdir
import pytest
from numpy import pi
from numpy.testing import assert_almost_equal
import mock

import numpy as np
from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.GUI.Dialog.DMachineSetup.SSimu.SSimu import SSimu
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from pyleecan.Classes.LossFEA import LossFEA

from Tests import save_gui_path as save_path

save_path = join(save_path, "Test_SSimu")
if not isdir(save_path):
    makedirs(save_path)


class TestSSimu(object):
    """Test that the widget SSimu behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Create widget before each test"""
        self.machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
        self.test_config_dict = {"GUI": {}, "MAIN": {}, "PLOT": {}}
        self.widget = SSimu(
            machine=self.machine,
            material_dict=None,
            is_stator=None,
            test_config_dict=self.test_config_dict,
        )

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_set_N0(self):
        """Check that the Widget allow to update N0"""
        assert self.widget.lf_N0.value() == 1000
        assert self.widget.simu.input.OP.N0 == 1000

        self.widget.lf_N0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_N0, "4000")
        self.widget.lf_N0.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_N0.value() == 4000
        assert self.widget.simu.input.OP.N0 == 4000

    def test_set_Id(self):
        """Check that the Widget allow to update Id"""
        assert self.widget.lf_I1.value() == 0
        assert self.widget.simu.input.OP.Id_ref == 0

        self.widget.lf_I1.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_I1, "3.14")
        self.widget.lf_I1.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_I1.value() == 3.14
        assert self.widget.simu.input.OP.Id_ref == 3.14

    def test_set_Iq(self):
        """Check that the Widget allow to update Iq"""
        assert self.widget.lf_I2.value() == 0
        assert self.widget.simu.input.OP.Iq_ref == 0

        self.widget.lf_I2.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_I2, "2.5")
        self.widget.lf_I2.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_I2.value() == 2.5
        assert self.widget.simu.input.OP.Iq_ref == 2.5

    def test_set_T_mag(self):
        """Check that the Widget allow to update T_mag"""
        assert self.widget.lf_T_mag.value() == 20
        assert self.widget.simu.mag.T_mag == 20

        self.widget.lf_T_mag.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_T_mag, "25")
        self.widget.lf_T_mag.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_T_mag.value() == 25
        assert self.widget.simu.mag.T_mag == 25

    def test_set_si_Na_tot(self):
        """Check that the Widget allow to update si_Na_tot"""
        assert self.widget.si_Na_tot.value() == 1680
        assert self.widget.simu.input.Na_tot == 1680

        self.widget.si_Na_tot.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.si_Na_tot, "354")
        self.widget.si_Na_tot.editingFinished.emit()  # To trigger the slot

        assert self.widget.si_Na_tot.value() == 354
        assert self.widget.simu.input.Na_tot == 354

    def test_set_si_Nt_tot(self):
        """Check that the Widget allow to update si_Nt_tot"""
        assert self.widget.si_Nt_tot.value() == 480
        assert self.widget.simu.input.Nt_tot == 480

        self.widget.si_Nt_tot.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.si_Nt_tot, "256")
        self.widget.si_Nt_tot.editingFinished.emit()  # To trigger the slot

        assert self.widget.si_Nt_tot.value() == 256
        assert self.widget.simu.input.Nt_tot == 256

    def test_set_kmesh(self):
        """Check that the Widget allow to update si_Nt_tot"""
        assert self.widget.lf_Kmesh.value() == 1
        assert self.widget.simu.mag.Kmesh_fineness == 1

        self.widget.lf_Kmesh.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_Kmesh, "2")
        self.widget.lf_Kmesh.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_Kmesh.value() == 2
        assert self.widget.simu.mag.Kmesh_fineness == 2

    def test_set_nb_worker(self):
        """Check that the Widget allow to update nb_worker"""
        assert self.widget.si_nb_worker.value() == 8
        assert self.widget.simu.mag.nb_worker == 8

        self.widget.si_nb_worker.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.si_nb_worker, "4")
        self.widget.si_nb_worker.editingFinished.emit()  # To trigger the slot

        assert self.widget.si_nb_worker.value() == 4
        assert self.widget.simu.mag.nb_worker == 4

    def test_set_Tsta(self):
        """Check that the Widget allow to update lf_Tsta"""
        assert self.widget.simu.loss is None

        self.widget.g_losses_model.setChecked(True)
        assert self.widget.g_losses_model.isChecked()
        assert self.widget.is_mesh_sol.isChecked()
        assert isinstance(self.widget.simu.loss, LossFEA)
        assert self.widget.simu.mag.is_get_meshsolution == True

        self.widget.g_losses_model.setChecked(False)
        assert not self.widget.g_losses_model.isChecked()
        assert self.widget.simu.loss == None

        self.widget.g_losses_model.setChecked(True)

        self.widget.lf_Tsta.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_Tsta, "130")
        self.widget.lf_Tsta.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_Tsta.value() == 130
        assert self.widget.simu.loss.Tsta == 130

    def test_set_Trot(self):
        """Check that the Widget allow to update lf_Trot"""
        assert self.widget.simu.loss is None
        self.widget.g_losses_model.setChecked(True)
        assert self.widget.g_losses_model.isChecked()
        assert self.widget.is_mesh_sol.isChecked()
        assert isinstance(self.widget.simu.loss, LossFEA)
        assert self.widget.simu.mag.is_get_meshsolution == True

        self.widget.g_losses_model.setChecked(False)
        assert not self.widget.g_losses_model.isChecked()
        assert self.widget.simu.loss == None

        self.widget.g_losses_model.setChecked(True)

        self.widget.lf_Trot.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_Trot, "130")
        self.widget.lf_Trot.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_Trot.value() == 130
        assert self.widget.simu.loss.Trot == 130

    def test_set_save_mesh_solution(self):
        """Check that the Widget allow to update mesh solution"""
        assert self.widget.simu.mag.is_get_meshsolution == False

        self.widget.is_mesh_sol.setChecked(True)
        assert self.widget.is_mesh_sol.isChecked()
        assert self.widget.simu.mag.is_get_meshsolution == True

        self.widget.is_mesh_sol.setChecked(False)
        assert not self.widget.is_mesh_sol.isChecked()
        assert self.widget.simu.mag.is_get_meshsolution == False

    def test_simu(self):
        """Check the simu"""
        self.widget.si_Nt_tot.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.si_Nt_tot, "4")
        self.widget.si_Nt_tot.editingFinished.emit()  # To trigger the slot

        self.widget.si_nb_worker.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.si_nb_worker, "4")
        self.widget.si_nb_worker.editingFinished.emit()  # To trigger the slot

        self.widget.lf_Kmesh.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_Kmesh, "0.3")
        self.widget.lf_Kmesh.editingFinished.emit()  # To trigger the slot

        # set Loss
        self.widget.g_losses_model.setChecked(True)

        self.widget.lf_Trot.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_Trot, "20")
        self.widget.lf_Trot.editingFinished.emit()  # To trigger the slot

        self.widget.lf_Tsta.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_Tsta, "20")
        self.widget.lf_Tsta.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_path_result.le_path.text() == ""
        assert "RESULT_DIR" not in self.test_config_dict["MAIN"]
        res_path = join(save_path, "Simu_Results")
        makedirs(res_path)
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getExistingDirectory", return_value=res_path
        ):
            # To trigger the slot
            self.widget.w_path_result.b_path.clicked.emit()
        res_path = res_path.replace("\\", "/")
        assert self.widget.w_path_result.le_path.text() == res_path

        assert self.widget.test_err_msg is None
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.information",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.b_next.clicked.emit()
        assert (
            self.widget.test_err_msg
            == "Simulation "
            + self.widget.simu.name
            + " is finished.\nResults available at "
            + self.widget.simu.path_result
        )
        # result dir is updated during run
        dir_path_result = os.path.dirname(self.widget.simu.path_result)
        assert dir_path_result == res_path
        assert self.test_config_dict["MAIN"]["RESULT_DIR"] == res_path

        path_result = self.widget.simu.path_result

        os.path.dirname(path_result)
        assert os.path.exists(path_result)

        list_file = os.listdir(path_result)
        assert len(list_file) == 25

        list_file_expected = [
            "B_meshsolution.png",
            "Femm",
            "FEMM_Toyota_Prius.json",
            "FEMM_Toyota_Prius.log",
            "flux 3D FFT_radial.png",
            "flux 3D FFT_tangential.png",
            "flux as fct of angle_radial.png",
            "flux as fct of angle_tangential.png",
            "flux as fct of time_radial.png",
            "flux as fct of time_tangential.png",
            "flux FFT over freq_radial.png",
            "flux FFT over freq_tangential.png",
            "flux FFT over wavenumber_radial.png",
            "flux FFT over wavenumber_tangential.png",
            "Losses.png",
            "Losses_meshsolution_rotor.png",
            "Losses_meshsolution_stator.png",
            "MagMesh.vtk",
            "MagMeshSolution.mat",
            "Result.h5",
            "Result.mat",
            "Stator winding flux.png",
            "torque as fct of time.png",
            "torque FFT over freq.png",
            "Toyota_Prius.png",
        ]

        assert list_file == list_file_expected


if __name__ == "__main__":
    a = TestSSimu()
    a.setup_class()
    a.setup_method()
    a.test_set_N0()
    a.test_set_Tsta()
    a.test_simu()

    print("Done")
