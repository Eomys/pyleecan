# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
from qtpy import QtWidgets
from qtpy.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Material import Material
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape


class TestSLamShape(object):
    """Test that the widget SLamShape behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind(
            is_stator=True, L1=0.11, Kf1=0.12, Nrvd=12, Wrvd=0.13
        )
        test_obj.stator.mat_type.name = "test3"
        test_obj.rotor = LamSlotWind(
            is_stator=False, L1=0.21, Kf1=0.22, Nrvd=22, Wrvd=0.23
        )
        test_obj.rotor.mat_type.name = "test2"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        widget_1 = SLamShape(
            machine=test_obj, material_dict=material_dict, is_stator=True
        )
        widget_2 = SLamShape(
            machine=test_obj, material_dict=material_dict, is_stator=False
        )

        yield {
            "widget": widget_1,
            "widget2": widget_2,
            "test_obj": test_obj,
            "material_dict": material_dict,
        }

        self.app.quit()

    @pytest.mark.SCIM
    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_L1.value() == 0.11
        assert setup["widget"].lf_Kf1.value() == 0.12
        assert setup["widget"].lf_Wrvd.value() == 0.13
        assert setup["widget"].si_Nrvd.value() == 12
        assert setup["widget"].w_mat.c_mat_type.currentIndex() == 2

        assert setup["widget2"].lf_L1.value() == 0.21
        assert setup["widget2"].lf_Kf1.value() == 0.22
        assert setup["widget2"].lf_Wrvd.value() == 0.23
        assert setup["widget2"].si_Nrvd.value() == 22
        assert setup["widget2"].w_mat.c_mat_type.currentIndex() == 1

    @pytest.mark.SCIM
    def test_set_L1(self, setup):
        """Check that the Widget allow to update L1"""
        # Clear the field before writing the new value
        setup["widget"].lf_L1.clear()
        value_1 = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_L1, str(value_1))
        setup["widget"].lf_L1.editingFinished.emit()  # To trigger the slot

        # Clear the field before writing the new value
        setup["widget2"].lf_L1.clear()
        value_2 = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget2"].lf_L1, str(value_2))
        setup["widget2"].lf_L1.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.L1 == value_1
        assert setup["test_obj"].rotor.L1 == value_2

    @pytest.mark.SCIM
    def test_set_Kf1(self, setup):
        """Check that the Widget allow to update Kf1"""
        # Clear the field before writing the new value
        setup["widget"].lf_Kf1.clear()
        value_1 = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Kf1, str(value_1))
        setup["widget"].lf_Kf1.editingFinished.emit()  # To trigger the slot

        # Clear the field before writing the new value
        setup["widget2"].lf_Kf1.clear()
        value_2 = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget2"].lf_Kf1, str(value_2))
        setup["widget2"].lf_Kf1.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.Kf1 == value_1
        assert setup["test_obj"].rotor.Kf1 == value_2

    @pytest.mark.SCIM
    def test_set_Wrvd(self, setup):
        """Check that the Widget allow to update Wrvd"""
        # Clear the field before writing the new value
        setup["widget"].lf_Wrvd.clear()
        value_1 = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Wrvd, str(value_1))
        setup["widget"].lf_Wrvd.editingFinished.emit()  # To trigger the slot

        # Clear the field before writing the new value
        setup["widget2"].lf_Wrvd.clear()
        value_2 = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget2"].lf_Wrvd, str(value_2))
        setup["widget2"].lf_Wrvd.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.Wrvd == value_1
        assert setup["test_obj"].rotor.Wrvd == value_2

    @pytest.mark.SCIM
    def test_set_Nrvd(self, setup):
        """Check that the Widget allow to update Nrvd"""
        # Clear the field before writing the new value
        setup["widget"].si_Nrvd.clear()
        value_1 = int(uniform(1, 10))
        setup["widget"].si_Nrvd.setValue(value_1)

        # Clear the field before writing the new value
        setup["widget2"].si_Nrvd.clear()
        value_2 = int(uniform(1, 10))
        setup["widget2"].si_Nrvd.setValue(value_2)

        assert setup["test_obj"].stator.Nrvd == value_1
        assert setup["test_obj"].rotor.Nrvd == value_2

    @pytest.mark.SCIM
    def test_set_material(self, setup):
        """Check that the combobox update the material"""
        setup["widget"].w_mat.c_mat_type.setCurrentIndex(0)
        assert setup["test_obj"].stator.mat_type.name == "test1"
        assert setup["test_obj"].stator.mat_type.elec.rho == 0.31

        setup["widget2"].w_mat.c_mat_type.setCurrentIndex(2)
        assert setup["test_obj"].rotor.mat_type.name == "test3"
        assert setup["test_obj"].rotor.mat_type.elec.rho == 0.33

    @pytest.mark.SCIM
    def test_clean_vent(self, setup):
        """Test that you can clean the ventilation"""

        assert not setup["widget"].g_axial.isChecked()

        setup["test_obj"].stator.axial_vent = list()
        setup["test_obj"].stator.axial_vent.append(VentilationCirc(Zh=8))
        setup["test_obj"].stator.axial_vent.append(VentilationCirc(Zh=10))
        setup["widget"] = SLamShape(
            machine=setup["test_obj"],
            material_dict=setup["material_dict"],
            is_stator=True,
        )
        assert setup["widget"].g_axial.isChecked()

        setup["widget"].g_axial.setChecked(False)
        assert setup["test_obj"].stator.axial_vent == list()

    @pytest.mark.SCIM
    def test_text_vent(self, setup):
        """Test the text avd"""
        assert setup["widget"].out_axial_duct.text() == "Axial: 0 set (0 ducts)"

        setup["test_obj"].stator.axial_vent = list()
        setup["test_obj"].stator.axial_vent.append(VentilationCirc(Zh=8))
        setup["test_obj"].stator.axial_vent.append(VentilationCirc(Zh=10))
        setup["widget"] = SLamShape(
            machine=setup["test_obj"],
            material_dict=setup["material_dict"],
            is_stator=True,
        )
        assert setup["widget"].out_axial_duct.text() == "Axial: 2 set (18 ducts)"

        setup["test_obj"].stator.axial_vent = list()
        setup["test_obj"].stator.axial_vent.append(VentilationTrap(Zh=20))
        setup["widget"] = SLamShape(
            machine=setup["test_obj"],
            material_dict=setup["material_dict"],
            is_stator=True,
        )
        assert setup["widget"].out_axial_duct.text() == "Axial: 1 set (20 ducts)"
