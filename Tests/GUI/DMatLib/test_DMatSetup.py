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

from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.Material import Material
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from Tests import save_load_path as save_path, TEST_DATA_DIR

import pytest


class TestDMatSetup(object):
    """Test that the widget DMatSetup behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        work_path = join(save_path, "Material")
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
        widget = DMatSetup(material=test_obj)

        yield {"widget": widget, "work_path": work_path, "test_obj": test_obj}

        self.app.quit()

        rmtree(work_path)

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""
        assert setup["widget"].nav_ther.currentIndex() == 1
        assert setup["widget"].nav_meca.currentIndex() == 1
        assert setup["widget"].le_name.text() == "Magnet1"
        assert setup["widget"].is_isotropic.checkState() == Qt.Checked
        assert setup["widget"].lf_rho_elec.value() == 0.11
        assert setup["widget"].lf_mur_lin.value() == 0.12
        assert setup["widget"].lf_Wlam.value() == 0.13
        assert setup["widget"].lf_rho_meca.value() == 0.14
        assert setup["widget"].lf_E.value() == 0.15
        assert setup["widget"].lf_nu.value() == 0.16
        assert setup["widget"].lf_G.value() == 0.17
        assert setup["widget"].lf_L.value() == 0.18
        assert setup["widget"].lf_Cp.value() == 0.19
        assert setup["widget"].lf_alpha.value() == 0.2
        assert setup["widget"].lf_cost_unit.value() == 0.21
        assert setup["widget"].w_BH_import.w_import.in_matrix.text() == (
            "Matrix size: (4, 2)"
        )

        # Test Raw Material
        setup["test_obj"].mag = None
        setup["widget"] = DMatSetup(material=setup["test_obj"])

        assert setup["widget"].nav_ther.currentIndex() == 1
        assert setup["widget"].nav_meca.currentIndex() == 1
        assert setup["widget"].le_name.text() == "Magnet1"
        assert setup["widget"].is_isotropic.checkState() == Qt.Checked
        assert setup["widget"].lf_rho_elec.value() == 0.11
        assert setup["widget"].lf_rho_meca.value() == 0.14
        assert setup["widget"].lf_E.value() == 0.15
        assert setup["widget"].lf_nu.value() == 0.16
        assert setup["widget"].lf_G.value() == 0.17
        assert setup["widget"].lf_L.value() == 0.18
        assert setup["widget"].lf_Cp.value() == 0.19
        assert setup["widget"].lf_alpha.value() == 0.2
        assert setup["widget"].lf_cost_unit.value() == 0.21

        # Test Magnet material Non isotropic
        setup["test_obj"].is_isotropic = False
        setup["test_obj"].mag = MatMagnetics(mur_lin=0.22, Brm20=0.23, alpha_Br=0.24)
        setup["widget"] = DMatSetup(material=setup["test_obj"])

        assert setup["widget"].nav_ther.currentIndex() == 0
        assert setup["widget"].nav_meca.currentIndex() == 0
        assert setup["widget"].le_name.text() == "Magnet1"
        assert setup["widget"].is_isotropic.checkState() == Qt.Unchecked
        assert setup["widget"].lf_rho_elec.value() == 0.11
        assert setup["widget"].lf_mur_lin.value() == 0.22
        assert setup["widget"].lf_Brm20.value() == 0.23
        assert setup["widget"].lf_alpha_Br.value() == 0.24
        assert setup["widget"].lf_rho_meca.value() == 0.14

        assert setup["widget"].lf_Ex.value() == 0.15
        assert setup["widget"].lf_Ey.value() == 0.152
        assert setup["widget"].lf_Ez.value() == 0.153

        assert setup["widget"].lf_nu_xy.value() == 0.16
        assert setup["widget"].lf_nu_yz.value() == 0.162
        assert setup["widget"].lf_nu_xz.value() == 0.163

        assert setup["widget"].lf_Gxy.value() == 0.17
        assert setup["widget"].lf_Gyz.value() == 0.172
        assert setup["widget"].lf_Gxz.value() == 0.173

        assert setup["widget"].lf_Lx.value() == 0.18
        assert setup["widget"].lf_Ly.value() == 0.182
        assert setup["widget"].lf_Lz.value() == 0.183

        assert setup["widget"].lf_Cp.value() == 0.19
        assert setup["widget"].lf_alpha.value() == 0.2
        assert setup["widget"].lf_cost_unit.value() == 0.21

        # Test Magnet material None elec
        setup["test_obj"].elec = None
        setup["widget"] = DMatSetup(material=setup["test_obj"])

        assert setup["widget"].mat.elec is not None

        # Test Magnet material None eco
        setup["test_obj"].eco = None
        setup["widget"] = DMatSetup(material=setup["test_obj"])

        assert setup["widget"].mat.eco is not None

        # Test Magnet material None HT
        setup["test_obj"].HT = None
        setup["widget"] = DMatSetup(material=setup["test_obj"])

        assert setup["widget"].mat.HT is not None

        # Test Magnet material None struct
        setup["test_obj"].struct = None
        setup["widget"] = DMatSetup(material=setup["test_obj"])

        assert setup["widget"].mat.struct is not None

    def test_set_name(self, setup):
        """Check that you can change the name and the path"""
        setup["widget"].le_name.setText("Magnet2")
        setup["widget"].le_name.editingFinished.emit()
        assert setup["widget"].mat.name == "Magnet2"
        assert setup["widget"].mat.path == join(setup["work_path"], "Magnet2.json")

    def test_set_rho_elec(self, setup):
        """Check that the Widget allow to update rho_elec"""
        setup["widget"].lf_rho_elec.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_rho_elec, str(value))
        setup["widget"].lf_rho_elec.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.elec.rho == value

    def test_set_mur_lin(self, setup):
        """Check that the Widget allow to update mur_lin"""
        setup["widget"].lf_mur_lin.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_mur_lin, str(value))
        setup["widget"].lf_mur_lin.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.mag.mur_lin == value
        setup["test_obj"].mag = MatMagnetics()
        setup["widget"] = DMatSetup(material=setup["test_obj"])
        setup["widget"].lf_mur_lin.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_mur_lin, str(value))
        setup["widget"].lf_mur_lin.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.mag.mur_lin == value

    def test_set_Wlam(self, setup):
        """Check that the Widget allow to update Wlam"""
        setup["widget"].lf_Wlam.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Wlam, str(value))
        setup["widget"].lf_Wlam.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.mag.Wlam == value

    def test_set_Brm20(self, setup):
        """Check that the Widget allow to update Brm20"""
        setup["test_obj"].mag = MatMagnetics()
        setup["widget"] = DMatSetup(material=setup["test_obj"])
        setup["widget"].lf_Brm20.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Brm20, str(value))
        setup["widget"].lf_Brm20.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.mag.Brm20 == value

    def test_set_alpha_Br(self, setup):
        """Check that the Widget allow to update alpha_Br"""
        # Set Material for Magnet
        setup["test_obj"].mag = MatMagnetics()
        setup["widget"] = DMatSetup(material=setup["test_obj"])
        setup["widget"].lf_alpha_Br.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_alpha_Br, str(value))
        setup["widget"].lf_alpha_Br.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.mag.alpha_Br == value

    def test_set_rho_meca(self, setup):
        """Check that the Widget allow to update rho_meca"""
        setup["widget"].lf_rho_meca.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_rho_meca, str(value))
        setup["widget"].lf_rho_meca.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.rho == value

    def test_set_E(self, setup):
        """Check that the Widget allow to update E"""
        setup["widget"].lf_E.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_E, str(value))
        setup["widget"].lf_E.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Ex == value
        assert setup["widget"].mat.struct.Ey == value
        assert setup["widget"].mat.struct.Ez == value

    def test_set_Ex(self, setup):
        """Check that the Widget allow to update Ex"""
        setup["widget"].lf_Ex.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Ex, str(value))
        setup["widget"].lf_Ex.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Ex == value

    def test_set_Ey(self, setup):
        """Check that the Widget allow to update Ey"""
        setup["widget"].lf_Ey.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Ey, str(value))
        setup["widget"].lf_Ey.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Ey == value

    def test_set_Ez(self, setup):
        """Check that the Widget allow to update Ez"""
        setup["widget"].lf_Ez.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Ez, str(value))
        setup["widget"].lf_Ez.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Ez == value

    def test_set_nu(self, setup):
        """Check that the Widget allow to update nu"""
        setup["widget"].lf_nu.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_nu, str(value))
        setup["widget"].lf_nu.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.nu_xy == value
        assert setup["widget"].mat.struct.nu_yz == value
        assert setup["widget"].mat.struct.nu_xz == value

    def test_set_nu_xy(self, setup):
        """Check that the Widget allow to update nu_xy"""
        setup["widget"].lf_nu_xy.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_nu_xy, str(value))
        setup["widget"].lf_nu_xy.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.nu_xy == value

    def test_set_nu_xz(self, setup):
        """Check that the Widget allow to update nu_xz"""
        setup["widget"].lf_nu_xz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_nu_xz, str(value))
        setup["widget"].lf_nu_xz.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.nu_xz == value

    def test_set_nu_yz(self, setup):
        """Check that the Widget allow to update nu_yz"""
        setup["widget"].lf_nu_yz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_nu_yz, str(value))
        setup["widget"].lf_nu_yz.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.nu_yz == value

    def test_set_G(self, setup):
        """Check that the Widget allow to update G"""
        setup["widget"].lf_G.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_G, str(value))
        setup["widget"].lf_G.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Gxy == value
        assert setup["widget"].mat.struct.Gyz == value
        assert setup["widget"].mat.struct.Gxz == value

    def test_set_Gxy(self, setup):
        """Check that the Widget allow to update Gxy"""
        setup["widget"].lf_Gxy.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Gxy, str(value))
        setup["widget"].lf_Gxy.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Gxy == value

    def test_set_Gyz(self, setup):
        """Check that the Widget allow to update Gyz"""
        setup["widget"].lf_Gyz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Gyz, str(value))
        setup["widget"].lf_Gyz.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Gyz == value

    def test_set_Gxz(self, setup):
        """Check that the Widget allow to update Gxz"""
        setup["widget"].lf_Gxz.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Gxz, str(value))
        setup["widget"].lf_Gxz.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].mat.struct.Gxz == value

    def test_set_is_isotropic(self, setup):
        """Check that the Widget allow to change value of is_isotropic"""
        QTest.mouseClick(
            setup["widget"].is_isotropic, Qt.LeftButton
        )  # Clicking the checkbox with the leftbutton

        assert setup["widget"].is_isotropic.isChecked() == False
        assert setup["widget"].nav_meca.currentIndex() == 0
        assert setup["widget"].nav_ther.currentIndex() == 0

        QTest.mouseClick(setup["widget"].is_isotropic, Qt.LeftButton)

        assert setup["widget"].is_isotropic.isChecked() == True
        assert setup["widget"].nav_meca.currentIndex() == 1
        assert setup["widget"].nav_ther.currentIndex() == 1

    def test_set_cost_unit(self, setup):
        """Check that the Widget allow to update cost_unit"""
        setup["widget"].lf_cost_unit.clear()
        value = 0.4548
        QTest.keyClicks(setup["widget"].lf_cost_unit, str(value))
        setup["widget"].lf_cost_unit.editingFinished.emit()

        assert setup["widget"].mat.eco.cost_unit == value

    def test_set_CP(self, setup):
        """Check that the Widget allow to update mat.HT.Cp"""
        setup["widget"].lf_Cp.clear()
        value = 0.4548
        QTest.keyClicks(setup["widget"].lf_Cp, str(value))
        setup["widget"].lf_Cp.editingFinished.emit()

        assert setup["widget"].mat.HT.Cp == value

    def test_set_alpha(self, setup):
        """Check that the Widget allow to update mat.HT.alpha"""
        setup["widget"].lf_alpha.clear()
        value = 0.4548
        QTest.keyClicks(setup["widget"].lf_alpha, str(value))
        setup["widget"].lf_alpha.editingFinished.emit()

        assert setup["widget"].mat.HT.alpha == value

    def test_set_lambda(self, setup):
        """Check that the Widget allow to update mat.HT.lambda"""
        setup["widget"].lf_L.clear()
        value = 0.4548
        QTest.keyClicks(setup["widget"].lf_L, str(value))
        setup["widget"].lf_L.editingFinished.emit()

        assert setup["widget"].mat.HT.lambda_x == value
        assert setup["widget"].mat.HT.lambda_y == value
        assert setup["widget"].mat.HT.lambda_z == value

    def test_set_lambda_x_y_z(self, setup):
        """Check that the Widget allow to update mat.HT.lambda_x_y_z"""
        setup["widget"].lf_Lx.clear()
        value = 0.4548
        QTest.keyClicks(setup["widget"].lf_Lx, str(value))
        setup["widget"].lf_Lx.editingFinished.emit()

        assert setup["widget"].mat.HT.lambda_x == value

        setup["widget"].lf_Ly.clear()
        value = 0.4548
        QTest.keyClicks(setup["widget"].lf_Ly, str(value))
        setup["widget"].lf_Ly.editingFinished.emit()

        assert setup["widget"].mat.HT.lambda_y == value

        setup["widget"].lf_Lz.clear()
        value = 0.4548
        QTest.keyClicks(setup["widget"].lf_Lz, str(value))
        setup["widget"].lf_Lz.editingFinished.emit()

        assert setup["widget"].mat.HT.lambda_z == value

    def test_BH_setup(self, setup):
        """Check that the BH curve behave have expected"""
        w_imp = setup["widget"].w_BH_import.w_import
        assert setup["widget"].w_BH_import.c_type_import.currentIndex() == 1
        setup["widget"].w_BH_import.w_import.in_matrix.text()
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
        setup["widget"].mat.mag.BH_curve.value[3, 0] == 5
        setup["widget"].mat.mag.BH_curve.value[3, 0] == 800
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
        setup["widget"].w_BH_import.c_type_import.setCurrentIndex(0)
        assert (
            setup["widget"].w_BH_import.c_type_import.currentText()
            == "Import from Excel"
        )
        w_imp = setup["widget"].w_BH_import.w_import
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
        w_imp.tab_window.si_row.value() == 4
        w_imp.tab_window.si_col.value() == 2
        w_imp.tab_window.w_tab.cellWidget(0, 0).value() == 0
        w_imp.tab_window.w_tab.cellWidget(0, 1).value() == 1
        w_imp.tab_window.w_tab.cellWidget(1, 0).value() == 2
        w_imp.tab_window.w_tab.cellWidget(1, 1).value() == 100
        w_imp.tab_window.w_tab.cellWidget(2, 0).value() == 3
        w_imp.tab_window.w_tab.cellWidget(2, 1).value() == 300
        w_imp.tab_window.w_tab.cellWidget(3, 0).value() == 5
        w_imp.tab_window.w_tab.cellWidget(3, 1).value() == 800
