# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from PyQt5 import QtWidgets

from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib


class test_DMatLib(TestCase):
    """Test that the widget DMatLib behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""
        mat_lib = list()
        mat_lib.append(Material())
        mat_lib[0].name = "test_material_1"
        mat_lib[0].is_isotropic = True
        mat_lib[0].elec.rho = 0.11
        mat_lib[0].mag = MatMagnetics(mur_lin=0.12, Wlam=0.13)
        mat_lib[0].struct.rho = 0.14
        mat_lib[0].struct.Ex = 0.15
        mat_lib[0].struct.Ey = 0.152
        mat_lib[0].struct.Ez = 0.153
        mat_lib[0].struct.nu_xy = 0.16
        mat_lib[0].struct.nu_yz = 0.162
        mat_lib[0].struct.nu_xz = 0.163
        mat_lib[0].struct.Gxy = 0.17
        mat_lib[0].struct.Gyz = 0.172
        mat_lib[0].struct.Gxz = 0.173
        mat_lib[0].HT.lambda_x = 0.18
        mat_lib[0].HT.lambda_y = 0.182
        mat_lib[0].HT.lambda_z = 0.183
        mat_lib[0].HT.Cp = 0.19
        mat_lib[0].HT.alpha = 0.20
        mat_lib[0].eco.cost_unit = 0.21

        mat_lib.append(Material(name="test_material_2"))
        mat_lib.append(Material(name="test_material_3"))
        mat_lib.append(Material(name="test_material_4"))
        mat_lib.append(Material(name="test_material_5"))
        mat_lib.append(Material(name="test_material_6"))
        mat_lib.append(Material(name="test_material_7"))

        self.widget = DMatLib(matlib=mat_lib)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test DMatLib")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""
        self.assertEqual(self.widget.out_name.text(), "name: test_material_1")
        self.assertEqual(self.widget.out_iso.text(), "type: isotropic")
        self.assertEqual(self.widget.out_rho_elec.text(), "rho = 0.11 ohm.m")
        self.assertEqual(self.widget.out_cost_unit.text(), u"cost_unit = 0.21 €/kg")
        self.assertEqual(self.widget.out_Cp.text(), "Cp = 0.19 W/kg/K")
        self.assertEqual(self.widget.out_alpha.text(), "alpha = 0.2")
        self.assertEqual(self.widget.out_L.text(), "Lambda = 0.18 W/K")
        self.assertEqual(self.widget.out_rho_meca.text(), "rho = 0.14 kg/m^3")
        self.assertEqual(self.widget.out_E.text(), "E = 0.15 Pa")
        self.assertEqual(self.widget.out_G.text(), "G = 0.17 Pa")
        self.assertEqual(self.widget.out_nu.text(), "nu = 0.16")
        self.assertEqual(self.widget.out_mur_lin.text(), "mur_lin = 0.12")
        self.assertEqual(self.widget.out_wlam.text(), "wlam = 0.13 m")

        # Check list
        self.assertEqual(self.widget.nav_mat.count(), 7)
        for ii in range(0, self.widget.nav_mat.count()):
            self.assertEqual(
                self.widget.nav_mat.item(ii).text(),
                "00" + str(ii + 1) + " - test_material_" + str(ii + 1),
            )
