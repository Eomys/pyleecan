# -*- coding: utf-8 -*-

import sys
from os import mkdir
from os.path import join, isdir, isfile
import mock
from shutil import rmtree, copyfile
from random import uniform
from numpy import array
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QMessageBox
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.Material import Material
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib, LIB_KEY, MACH_KEY
from Tests import save_load_path as save_path, TEST_DATA_DIR

import pytest

work_path = join(save_path, "Material")


class TestDMatSetup(object):
    """Test that the widget DMatSetup behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestDMatSetup")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        rmtree(work_path)
        cls.app.quit()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""

        # Delete old test if needed
        if isdir(work_path):
            rmtree(work_path)
        mkdir(work_path)
        copyfile(
            join(TEST_DATA_DIR, "Material", "Magnet1.json"),
            join(work_path, "Magnet1.json"),
        )

        test_obj = Material()
        test_obj.name = "Magnet1"
        test_obj.path = join(work_path, "Magnet1.json")
        test_obj.is_isotropic = True
        test_obj.elec.rho = 0.11
        test_obj.mag = MatMagnetics(mur_lin=0.12, Wlam=0.13)
        test_obj.mag.BH_curve = ImportMatrixVal(
            value=array([[0, 1], [2, 100], [3, 300], [4, 450]])
        )
        test_obj.struct.rho = 0.14
        test_obj.struct.Ex = 0.15
        test_obj.struct.Ey = 0.152
        test_obj.struct.Ez = 0.153
        test_obj.struct.nu_xy = 0.16
        test_obj.struct.nu_yz = 0.162
        test_obj.struct.nu_xz = 0.163
        test_obj.struct.Gxy = 0.17
        test_obj.struct.Gyz = 0.172
        test_obj.struct.Gxz = 0.173
        test_obj.HT.lambda_x = 0.18
        test_obj.HT.lambda_y = 0.182
        test_obj.HT.lambda_z = 0.183
        test_obj.HT.Cp = 0.19
        test_obj.HT.alpha = 0.20
        test_obj.eco.cost_unit = 0.21

        material_dict = {LIB_KEY: [test_obj], MACH_KEY: []}
        widget = DMatLib(material_dict=material_dict)

        self.widget = widget
        self.material_dict = material_dict
        self.work_path = work_path
        self.test_obj = test_obj

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""
        assert self.widget.w_setup.nav_ther.currentIndex() == 1
        assert self.widget.w_setup.nav_meca.currentIndex() == 1
        assert self.widget.w_setup.le_name.text() == "Magnet1"
        assert self.widget.w_setup.is_isotropic.checkState() == Qt.Checked
        assert self.widget.w_setup.lf_rho_elec.value() == 0.11
        assert self.widget.w_setup.lf_mur_lin.value() == 0.12
        assert self.widget.w_setup.lf_Wlam.value() == 0.13
        assert self.widget.w_setup.lf_rho_meca.value() == 0.14
        assert self.widget.w_setup.lf_E.value() == 0.15
        assert self.widget.w_setup.lf_nu.value() == 0.16
        assert self.widget.w_setup.lf_G.value() == 0.17
        assert self.widget.w_setup.lf_L.value() == 0.18
        assert self.widget.w_setup.lf_Cp.value() == 0.19
        assert self.widget.w_setup.lf_alpha.value() == 0.2
        assert self.widget.w_setup.lf_cost_unit.value() == 0.21
        assert self.widget.w_setup.w_BH_import.w_import.in_matrix.text() == (
            "Matrix size: (4, 2)"
        )

        # Test Raw Material
        self.material_dict[LIB_KEY][0].mag = None
        self.widget = DMatLib(material_dict=self.material_dict)

        assert self.widget.w_setup.nav_ther.currentIndex() == 1
        assert self.widget.w_setup.nav_meca.currentIndex() == 1
        assert self.widget.w_setup.le_name.text() == "Magnet1"
        assert self.widget.w_setup.is_isotropic.checkState() == Qt.Checked
        assert self.widget.w_setup.lf_rho_elec.value() == 0.11
        assert self.widget.w_setup.lf_rho_meca.value() == 0.14
        assert self.widget.w_setup.lf_E.value() == 0.15
        assert self.widget.w_setup.lf_nu.value() == 0.16
        assert self.widget.w_setup.lf_G.value() == 0.17
        assert self.widget.w_setup.lf_L.value() == 0.18
        assert self.widget.w_setup.lf_Cp.value() == 0.19
        assert self.widget.w_setup.lf_alpha.value() == 0.2
        assert self.widget.w_setup.lf_cost_unit.value() == 0.21

        # Test Magnet material Non isotropic
        self.material_dict[LIB_KEY][0].is_isotropic = False
        self.material_dict[LIB_KEY][0].mag = MatMagnetics(
            mur_lin=0.22, Brm20=0.23, alpha_Br=0.24
        )
        self.widget = DMatLib(material_dict=self.material_dict)

        assert self.widget.w_setup.nav_ther.currentIndex() == 0
        assert self.widget.w_setup.nav_meca.currentIndex() == 0
        assert self.widget.w_setup.le_name.text() == "Magnet1"
        assert self.widget.w_setup.is_isotropic.checkState() == Qt.Unchecked
        assert self.widget.w_setup.lf_rho_elec.value() == 0.11
        assert self.widget.w_setup.lf_mur_lin.value() == 0.22
        assert self.widget.w_setup.lf_Brm20.value() == 0.23
        assert self.widget.w_setup.lf_alpha_Br.value() == 0.24
        assert self.widget.w_setup.lf_rho_meca.value() == 0.14

        assert self.widget.w_setup.lf_Ex.value() == 0.15
        assert self.widget.w_setup.lf_Ey.value() == 0.152
        assert self.widget.w_setup.lf_Ez.value() == 0.153

        assert self.widget.w_setup.lf_nu_xy.value() == 0.16
        assert self.widget.w_setup.lf_nu_yz.value() == 0.162
        assert self.widget.w_setup.lf_nu_xz.value() == 0.163

        assert self.widget.w_setup.lf_Gxy.value() == 0.17
        assert self.widget.w_setup.lf_Gyz.value() == 0.172
        assert self.widget.w_setup.lf_Gxz.value() == 0.173

        assert self.widget.w_setup.lf_Lx.value() == 0.18
        assert self.widget.w_setup.lf_Ly.value() == 0.182
        assert self.widget.w_setup.lf_Lz.value() == 0.183

        assert self.widget.w_setup.lf_Cp.value() == 0.19
        assert self.widget.w_setup.lf_alpha.value() == 0.2
        assert self.widget.w_setup.lf_cost_unit.value() == 0.21

        # Test Magnet material None elec
        self.material_dict[LIB_KEY][0].elec = None
        self.widget = DMatLib(material_dict=self.material_dict)
        assert self.widget.w_setup.mat.elec is not None

        # Test Magnet material None eco
        self.material_dict[LIB_KEY][0].eco = None
        self.widget = DMatLib(material_dict=self.material_dict)

        assert self.widget.w_setup.mat.eco is not None

        # Test Magnet material None HT
        self.material_dict[LIB_KEY][0].HT = None
        self.widget = DMatLib(material_dict=self.material_dict)

        assert self.widget.w_setup.mat.HT is not None

        # Test Magnet material None struct
        self.material_dict[LIB_KEY][0].struct = None
        self.widget = DMatLib(material_dict=self.material_dict)

        assert self.widget.w_setup.mat.struct is not None

    def test_set_name(self):
        """Check that you can change the name and the path"""
        self.widget.w_setup.le_name.setText("Magnet2")
        with mock.patch(
                "PySide2.QtWidgets.QMessageBox.question",
                return_value=QMessageBox.Yes,
            ):
            self.widget.w_setup.le_name.editingFinished.emit()
        assert self.widget.w_setup.mat.name == "Magnet2"
        assert self.widget.w_setup.mat.path == join(self.work_path, "Magnet2.json")

    def test_set_rho_elec(self):
        """Check that the Widget allow to update rho_elec"""
        self.widget.w_setup.lf_rho_elec.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_rho_elec, str(value))
        self.widget.w_setup.lf_rho_elec.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.elec.rho == value

    def test_set_mur_lin(self):
        """Check that the Widget allow to update mur_lin"""
        self.widget.w_setup.lf_mur_lin.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_mur_lin, str(value))
        self.widget.w_setup.lf_mur_lin.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.mag.mur_lin == value
        self.material_dict[LIB_KEY][0].mag = MatMagnetics()
        self.widget = DMatLib(material_dict=self.material_dict)
        self.widget.w_setup.lf_mur_lin.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_mur_lin, str(value))
        self.widget.w_setup.lf_mur_lin.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.mag.mur_lin == value

    def test_set_Wlam(self):
        """Check that the Widget allow to update Wlam"""
        self.widget.w_setup.lf_Wlam.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Wlam, str(value))
        self.widget.w_setup.lf_Wlam.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.mag.Wlam == value

    def test_set_Brm20(self):
        """Check that the Widget allow to update Brm20"""
        self.material_dict[LIB_KEY][0].mag = MatMagnetics()
        self.widget = DMatLib(material_dict=self.material_dict)
        self.widget.w_setup.lf_Brm20.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Brm20, str(value))
        self.widget.w_setup.lf_Brm20.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.mag.Brm20 == value

    def test_set_alpha_Br(self):
        """Check that the Widget allow to update alpha_Br"""
        # Set Material for Magnet
        self.material_dict[LIB_KEY][0].mag = MatMagnetics()
        self.widget = DMatLib(material_dict=self.material_dict)
        self.widget.w_setup.lf_alpha_Br.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_alpha_Br, str(value))
        self.widget.w_setup.lf_alpha_Br.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.mag.alpha_Br == value

    def test_set_rho_meca(self):
        """Check that the Widget allow to update rho_meca"""
        self.widget.w_setup.lf_rho_meca.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_rho_meca, str(value))
        self.widget.w_setup.lf_rho_meca.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.rho == value

    def test_set_E(self):
        """Check that the Widget allow to update E"""
        self.widget.w_setup.lf_E.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_E, str(value))
        self.widget.w_setup.lf_E.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Ex == value
        assert self.widget.w_setup.mat.struct.Ey == value
        assert self.widget.w_setup.mat.struct.Ez == value

    def test_set_Ex(self):
        """Check that the Widget allow to update Ex"""
        self.widget.w_setup.lf_Ex.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Ex, str(value))
        self.widget.w_setup.lf_Ex.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Ex == value

    def test_set_Ey(self):
        """Check that the Widget allow to update Ey"""
        self.widget.w_setup.lf_Ey.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Ey, str(value))
        self.widget.w_setup.lf_Ey.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Ey == value

    def test_set_Ez(self):
        """Check that the Widget allow to update Ez"""
        self.widget.w_setup.lf_Ez.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Ez, str(value))
        self.widget.w_setup.lf_Ez.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Ez == value

    def test_set_nu(self):
        """Check that the Widget allow to update nu"""
        self.widget.w_setup.lf_nu.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_nu, str(value))
        self.widget.w_setup.lf_nu.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.nu_xy == value
        assert self.widget.w_setup.mat.struct.nu_yz == value
        assert self.widget.w_setup.mat.struct.nu_xz == value

    def test_set_nu_xy(self):
        """Check that the Widget allow to update nu_xy"""
        self.widget.w_setup.lf_nu_xy.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_nu_xy, str(value))
        self.widget.w_setup.lf_nu_xy.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.nu_xy == value

    def test_set_nu_xz(self):
        """Check that the Widget allow to update nu_xz"""
        self.widget.w_setup.lf_nu_xz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_nu_xz, str(value))
        self.widget.w_setup.lf_nu_xz.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.nu_xz == value

    def test_set_nu_yz(self):
        """Check that the Widget allow to update nu_yz"""
        self.widget.w_setup.lf_nu_yz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_nu_yz, str(value))
        self.widget.w_setup.lf_nu_yz.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.nu_yz == value

    def test_set_G(self):
        """Check that the Widget allow to update G"""
        self.widget.w_setup.lf_G.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_G, str(value))
        self.widget.w_setup.lf_G.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Gxy == value
        assert self.widget.w_setup.mat.struct.Gyz == value
        assert self.widget.w_setup.mat.struct.Gxz == value

    def test_set_Gxy(self):
        """Check that the Widget allow to update Gxy"""
        self.widget.w_setup.lf_Gxy.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Gxy, str(value))
        self.widget.w_setup.lf_Gxy.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Gxy == value

    def test_set_Gyz(self):
        """Check that the Widget allow to update Gyz"""
        self.widget.w_setup.lf_Gyz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Gyz, str(value))
        self.widget.w_setup.lf_Gyz.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Gyz == value

    def test_set_Gxz(self):
        """Check that the Widget allow to update Gxz"""
        self.widget.w_setup.lf_Gxz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.w_setup.lf_Gxz, str(value))
        self.widget.w_setup.lf_Gxz.editingFinished.emit()  # To trigger the slot

        assert self.widget.w_setup.mat.struct.Gxz == value

    def test_set_is_isotropic(self):
        """Check that the Widget allow to change value of is_isotropic"""
        QTest.mouseClick(
            self.widget.w_setup.is_isotropic, Qt.LeftButton
        )  # Clicking the checkbox with the leftbutton

        assert self.widget.w_setup.is_isotropic.isChecked() == False
        assert self.widget.w_setup.nav_meca.currentIndex() == 0
        assert self.widget.w_setup.nav_ther.currentIndex() == 0

        QTest.mouseClick(self.widget.w_setup.is_isotropic, Qt.LeftButton)

        assert self.widget.w_setup.is_isotropic.isChecked() == True
        assert self.widget.w_setup.nav_meca.currentIndex() == 1
        assert self.widget.w_setup.nav_ther.currentIndex() == 1

    def test_set_cost_unit(self):
        """Check that the Widget allow to update cost_unit"""
        self.widget.w_setup.lf_cost_unit.clear()
        value = 0.4548
        QTest.keyClicks(self.widget.w_setup.lf_cost_unit, str(value))
        self.widget.w_setup.lf_cost_unit.editingFinished.emit()

        assert self.widget.w_setup.mat.eco.cost_unit == value

    def test_set_CP(self):
        """Check that the Widget allow to update mat.HT.Cp"""
        self.widget.w_setup.lf_Cp.clear()
        value = 0.4548
        QTest.keyClicks(self.widget.w_setup.lf_Cp, str(value))
        self.widget.w_setup.lf_Cp.editingFinished.emit()

        assert self.widget.w_setup.mat.HT.Cp == value

    def test_set_alpha(self):
        """Check that the Widget allow to update mat.HT.alpha"""
        self.widget.w_setup.lf_alpha.clear()
        value = 0.4548
        QTest.keyClicks(self.widget.w_setup.lf_alpha, str(value))
        self.widget.w_setup.lf_alpha.editingFinished.emit()

        assert self.widget.w_setup.mat.HT.alpha == value

    def test_set_lambda(self):
        """Check that the Widget allow to update mat.HT.lambda"""
        self.widget.w_setup.lf_L.clear()
        value = 0.4548
        QTest.keyClicks(self.widget.w_setup.lf_L, str(value))
        self.widget.w_setup.lf_L.editingFinished.emit()

        assert self.widget.w_setup.mat.HT.lambda_x == value
        assert self.widget.w_setup.mat.HT.lambda_y == value
        assert self.widget.w_setup.mat.HT.lambda_z == value

    def test_set_lambda_x_y_z(self):
        """Check that the Widget allow to update mat.HT.lambda_x_y_z"""
        self.widget.w_setup.lf_Lx.clear()
        value = 0.4548
        QTest.keyClicks(self.widget.w_setup.lf_Lx, str(value))
        self.widget.w_setup.lf_Lx.editingFinished.emit()

        assert self.widget.w_setup.mat.HT.lambda_x == value

        self.widget.w_setup.lf_Ly.clear()
        value = 0.4548
        QTest.keyClicks(self.widget.w_setup.lf_Ly, str(value))
        self.widget.w_setup.lf_Ly.editingFinished.emit()

        assert self.widget.w_setup.mat.HT.lambda_y == value

        self.widget.w_setup.lf_Lz.clear()
        value = 0.4548
        QTest.keyClicks(self.widget.w_setup.lf_Lz, str(value))
        self.widget.w_setup.lf_Lz.editingFinished.emit()

        assert self.widget.w_setup.mat.HT.lambda_z == value

    def test_BH_setup(self):
        """Check that the BH curve behave have expected"""
        w_imp = self.widget.w_setup.w_BH_import.w_import
        assert self.widget.w_setup.w_BH_import.c_type_import.currentIndex() == 1
        self.widget.w_setup.w_BH_import.w_import.in_matrix.text()
        # Open table to check BH values
        assert w_imp.tab_window is None
        w_imp.b_tab.clicked.emit()
        w_imp.tab_window.si_row.value() == 4
        w_imp.tab_window.si_col.value() == 2
        w_imp.tab_window.w_tab.cellWidget(0, 0).value() == 0
        w_imp.tab_window.w_tab.cellWidget(0, 1).value() == 1
        w_imp.tab_window.w_tab.cellWidget(1, 0).value() == 2
        w_imp.tab_window.w_tab.cellWidget(1, 1).value() == 100
        w_imp.tab_window.w_tab.cellWidget(2, 0).value() == 3
        w_imp.tab_window.w_tab.cellWidget(2, 1).value() == 300
        w_imp.tab_window.w_tab.cellWidget(3, 0).value() == 4
        w_imp.tab_window.w_tab.cellWidget(3, 1).value() == 450
        # Edit table
        w_imp.tab_window.w_tab.cellWidget(3, 0).setValue(5)
        w_imp.tab_window.w_tab.cellWidget(3, 1).setValue(800)
        w_imp.tab_window.b_close.accepted.emit()
        w_imp.tab_window.close()
        self.widget.w_setup.mat.mag.BH_curve.value[3, 0] == 5
        self.widget.w_setup.mat.mag.BH_curve.value[3, 0] == 800
        # Export to excel
        excel_path = join(save_path, "DMatSetup_excel_export.xls").replace("\\", "/")
        assert not isfile(excel_path)
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getSaveFileName",
            return_value=(excel_path, "Excel file (*.xls .*xlsx)"),
        ):
            w_imp.b_convert.clicked.emit()
        assert isfile(excel_path)
        # Convert to excel import
        self.widget.w_setup.w_BH_import.c_type_import.setCurrentIndex(0)
        assert (
            self.widget.w_setup.w_BH_import.c_type_import.currentText()
            == "Import from Excel"
        )
        w_imp = self.widget.w_setup.w_BH_import.w_import
        # Import the excel file
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName",
            return_value=(excel_path, "Excel file (*.xls .*xlsx)"),
        ):
            w_imp.w_file_path.b_path.clicked.emit()
        assert w_imp.w_file_path.le_path.text() == excel_path
        # Check table
        assert w_imp.tab_window is None
        w_imp.b_tab.clicked.emit()
        assert w_imp.tab_window.si_row.value() == 4
        assert w_imp.tab_window.si_col.value() == 2
        assert w_imp.tab_window.w_tab.cellWidget(0, 0).value() == 0
        assert w_imp.tab_window.w_tab.cellWidget(0, 1).value() == 1
        assert w_imp.tab_window.w_tab.cellWidget(1, 0).value() == 2
        assert w_imp.tab_window.w_tab.cellWidget(1, 1).value() == 100
        assert w_imp.tab_window.w_tab.cellWidget(2, 0).value() == 3
        assert w_imp.tab_window.w_tab.cellWidget(2, 1).value() == 300
        assert w_imp.tab_window.w_tab.cellWidget(3, 0).value() == 5
        assert w_imp.tab_window.w_tab.cellWidget(3, 1).value() == 800
        w_imp.tab_window.close()
