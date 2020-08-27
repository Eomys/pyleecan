# -*- coding: utf-8 -*-

import sys
from os import mkdir
from os.path import join, isdir
from shutil import rmtree, copyfile
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from Tests import save_load_path as save_path, TEST_DATA_DIR


class test_DMatSetup(TestCase):
    """Test that the widget DMatSetup behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        self.work_path = join(save_path, "Material")
        # Delete old test if needed
        if isdir(self.work_path):
            rmtree(self.work_path)
        mkdir(self.work_path)
        copyfile(
            join(TEST_DATA_DIR, "Material", "Magnet1.json"),
            join(self.work_path, "Magnet1.json"),
        )

        self.test_obj = Material()
        self.test_obj.name = "Magnet1"
        self.test_obj.path = join(self.work_path, "Magnet1.json")
        self.test_obj.is_isotropic = True
        self.test_obj.elec.rho = 0.11
        self.test_obj.mag = MatMagnetics(mur_lin=0.12, Wlam=0.13)
        self.test_obj.struct.rho = 0.14
        self.test_obj.struct.Ex = 0.15
        self.test_obj.struct.Ey = 0.152
        self.test_obj.struct.Ez = 0.153
        self.test_obj.struct.nu_xy = 0.16
        self.test_obj.struct.nu_yz = 0.162
        self.test_obj.struct.nu_xz = 0.163
        self.test_obj.struct.Gxy = 0.17
        self.test_obj.struct.Gyz = 0.172
        self.test_obj.struct.Gxz = 0.173
        self.test_obj.HT.lambda_x = 0.18
        self.test_obj.HT.lambda_y = 0.182
        self.test_obj.HT.lambda_z = 0.183
        self.test_obj.HT.Cp = 0.19
        self.test_obj.HT.alpha = 0.20
        self.test_obj.eco.cost_unit = 0.21
        self.widget = DMatSetup(material=self.test_obj)

    def teardown(self):
        """Delete the workspace at the end of the tests
        """
        rmtree(self.work_path)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test DMatSetup")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""
        self.assertEqual(self.widget.nav_ther.currentIndex(), 1)
        self.assertEqual(self.widget.nav_meca.currentIndex(), 1)
        self.assertEqual(self.widget.le_name.text(), "Magnet1")
        self.assertEqual(self.widget.is_isotropic.checkState(), Qt.Checked)
        self.assertEqual(self.widget.lf_rho_elec.value(), 0.11)
        self.assertEqual(self.widget.lf_mur_lin.value(), 0.12)
        self.assertEqual(self.widget.lf_Wlam.value(), 0.13)
        self.assertEqual(self.widget.lf_rho_meca.value(), 0.14)
        self.assertEqual(self.widget.lf_E.value(), 0.15)
        self.assertEqual(self.widget.lf_nu.value(), 0.16)
        self.assertEqual(self.widget.lf_G.value(), 0.17)
        self.assertEqual(self.widget.lf_L.value(), 0.18)
        self.assertEqual(self.widget.lf_Cp.value(), 0.19)
        self.assertEqual(self.widget.lf_alpha.value(), 0.2)
        self.assertEqual(self.widget.lf_cost_unit.value(), 0.21)

        # Test Raw Material
        self.test_obj.mag = None
        self.widget = DMatSetup(material=self.test_obj)

        self.assertEqual(self.widget.nav_ther.currentIndex(), 1)
        self.assertEqual(self.widget.nav_meca.currentIndex(), 1)
        self.assertEqual(self.widget.le_name.text(), "Magnet1")
        self.assertEqual(self.widget.is_isotropic.checkState(), Qt.Checked)
        self.assertEqual(self.widget.lf_rho_elec.value(), 0.11)
        self.assertEqual(self.widget.lf_rho_meca.value(), 0.14)
        self.assertEqual(self.widget.lf_E.value(), 0.15)
        self.assertEqual(self.widget.lf_nu.value(), 0.16)
        self.assertEqual(self.widget.lf_G.value(), 0.17)
        self.assertEqual(self.widget.lf_L.value(), 0.18)
        self.assertEqual(self.widget.lf_Cp.value(), 0.19)
        self.assertEqual(self.widget.lf_alpha.value(), 0.2)
        self.assertEqual(self.widget.lf_cost_unit.value(), 0.21)

        # Test Magnet material Non isotropic
        self.test_obj.is_isotropic = False
        self.test_obj.mag = MatMagnetics(mur_lin=0.22, Brm20=0.23, alpha_Br=0.24)
        self.widget = DMatSetup(material=self.test_obj)

        self.assertEqual(self.widget.nav_ther.currentIndex(), 0)
        self.assertEqual(self.widget.nav_meca.currentIndex(), 0)
        self.assertEqual(self.widget.le_name.text(), "Magnet1")
        self.assertEqual(self.widget.is_isotropic.checkState(), Qt.Unchecked)
        self.assertEqual(self.widget.lf_rho_elec.value(), 0.11)
        self.assertEqual(self.widget.lf_mur_lin.value(), 0.22)
        self.assertEqual(self.widget.lf_Brm20.value(), 0.23)
        self.assertEqual(self.widget.lf_alpha_Br.value(), 0.24)
        self.assertEqual(self.widget.lf_rho_meca.value(), 0.14)

        self.assertEqual(self.widget.lf_Ex.value(), 0.15)
        self.assertEqual(self.widget.lf_Ey.value(), 0.152)
        self.assertEqual(self.widget.lf_Ez.value(), 0.153)

        self.assertEqual(self.widget.lf_nu_xy.value(), 0.16)
        self.assertEqual(self.widget.lf_nu_yz.value(), 0.162)
        self.assertEqual(self.widget.lf_nu_xz.value(), 0.163)

        self.assertEqual(self.widget.lf_Gxy.value(), 0.17)
        self.assertEqual(self.widget.lf_Gyz.value(), 0.172)
        self.assertEqual(self.widget.lf_Gxz.value(), 0.173)

        self.assertEqual(self.widget.lf_Lx.value(), 0.18)
        self.assertEqual(self.widget.lf_Ly.value(), 0.182)
        self.assertEqual(self.widget.lf_Lz.value(), 0.183)

        self.assertEqual(self.widget.lf_Cp.value(), 0.19)
        self.assertEqual(self.widget.lf_alpha.value(), 0.2)
        self.assertEqual(self.widget.lf_cost_unit.value(), 0.21)

    def test_set_name(self):
        """Check that you can change the name and the path
        """
        self.widget.le_name.setText("Magnet2")
        self.widget.le_name.editingFinished.emit()
        self.assertEqual(self.widget.mat.name, "Magnet2")
        self.assertEqual(self.widget.mat.path, join(self.work_path, "Magnet2.json"))

    def test_set_rho_elec(self):
        """Check that the Widget allow to update rho_elec"""
        self.widget.lf_rho_elec.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_rho_elec, str(value))
        self.widget.lf_rho_elec.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.elec.rho, value)

    def test_set_mur_lin(self):
        """Check that the Widget allow to update mur_lin"""
        self.widget.lf_mur_lin.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_mur_lin, str(value))
        self.widget.lf_mur_lin.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.mag.mur_lin, value)

        # Test also for Magnet Materials
        self.test_obj.mag = MatMagnetics()
        self.widget = DMatSetup(material=self.test_obj)

        self.widget.lf_mur_lin.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_mur_lin, str(value))
        self.widget.lf_mur_lin.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.mag.mur_lin, value)

    def test_set_Wlam(self):
        """Check that the Widget allow to update Wlam"""
        self.widget.lf_Wlam.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Wlam, str(value))
        self.widget.lf_Wlam.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.mag.Wlam, value)

    def test_set_Brm20(self):
        """Check that the Widget allow to update Brm20"""
        # Set Material for Magnet
        self.test_obj.mag = MatMagnetics()
        self.widget = DMatSetup(material=self.test_obj)

        self.widget.lf_Brm20.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Brm20, str(value))
        self.widget.lf_Brm20.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.mag.Brm20, value)

    def test_set_alpha_Br(self):
        """Check that the Widget allow to update alpha_Br"""
        # Set Material for Magnet
        self.test_obj.mag = MatMagnetics()
        self.widget = DMatSetup(material=self.test_obj)

        self.widget.lf_alpha_Br.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_alpha_Br, str(value))
        self.widget.lf_alpha_Br.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.mag.alpha_Br, value)

    def test_set_rho_meca(self):
        """Check that the Widget allow to update rho_meca"""
        self.widget.lf_rho_meca.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_rho_meca, str(value))
        self.widget.lf_rho_meca.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.rho, value)

    def test_set_E(self):
        """Check that the Widget allow to update E"""
        self.widget.lf_E.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_E, str(value))
        self.widget.lf_E.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Ex, value)
        self.assertEqual(self.widget.mat.struct.Ey, value)
        self.assertEqual(self.widget.mat.struct.Ez, value)

    def test_set_Ex(self):
        """Check that the Widget allow to update Ex"""
        self.widget.lf_Ex.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Ex, str(value))
        self.widget.lf_Ex.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Ex, value)

    def test_set_Ey(self):
        """Check that the Widget allow to update Ey"""
        self.widget.lf_Ey.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Ey, str(value))
        self.widget.lf_Ey.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Ey, value)

    def test_set_Ez(self):
        """Check that the Widget allow to update Ez"""
        self.widget.lf_Ez.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Ez, str(value))
        self.widget.lf_Ez.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Ez, value)

    def test_set_nu(self):
        """Check that the Widget allow to update nu"""
        self.widget.lf_nu.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_nu, str(value))
        self.widget.lf_nu.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.nu_xy, value)
        self.assertEqual(self.widget.mat.struct.nu_yz, value)
        self.assertEqual(self.widget.mat.struct.nu_xz, value)

    def test_set_nu_xy(self):
        """Check that the Widget allow to update nu_xy"""
        self.widget.lf_nu_xy.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_nu_xy, str(value))
        self.widget.lf_nu_xy.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.nu_xy, value)

    def test_set_nu_xz(self):
        """Check that the Widget allow to update nu_xz"""
        self.widget.lf_nu_xz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_nu_xz, str(value))
        self.widget.lf_nu_xz.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.nu_xz, value)

    def test_set_nu_yz(self):
        """Check that the Widget allow to update nu_yz"""
        self.widget.lf_nu_yz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_nu_yz, str(value))
        self.widget.lf_nu_yz.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.nu_yz, value)

    def test_set_G(self):
        """Check that the Widget allow to update G"""
        self.widget.lf_G.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_G, str(value))
        self.widget.lf_G.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Gxy, value)
        self.assertEqual(self.widget.mat.struct.Gyz, value)
        self.assertEqual(self.widget.mat.struct.Gxz, value)

    def test_set_Gxy(self):
        """Check that the Widget allow to update Gxy"""
        self.widget.lf_Gxy.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Gxy, str(value))
        self.widget.lf_Gxy.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Gxy, value)

    def test_set_Gyz(self):
        """Check that the Widget allow to update Gyz"""
        self.widget.lf_Gyz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Gyz, str(value))
        self.widget.lf_Gyz.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Gyz, value)

    def test_set_Gxz(self):
        """Check that the Widget allow to update Gxz"""
        self.widget.lf_Gxz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Gxz, str(value))
        self.widget.lf_Gxz.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.mat.struct.Gxz, value)
