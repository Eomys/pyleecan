# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY
from pyleecan.Classes.Shaft import Shaft
from pyleecan.GUI.Dialog.DMachineSetup.SMachineDimension.SMachineDimension import (
    SMachineDimension,
)


class TestSMachineDimension(object):
    """Test that the widget SMachineDimension behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )
        test_obj.frame = Frame(Rint=0.22, Rext=0.24, Lfra=0.25)
        test_obj.shaft = Shaft(Lshaft=0.333, Drsh=test_obj.rotor.Rint * 2)

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        widget = SMachineDimension(
            machine=test_obj, material_dict=material_dict, is_stator=False
        )

        yield {"widget": widget, "test_obj": test_obj, "material_dict": material_dict}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_SRint.value() == 0.21
        assert setup["widget"].lf_SRext.value() == 0.22
        assert setup["widget"].lf_RRint.value() == 0.11
        assert setup["widget"].lf_RRext.value() == 0.12
        assert round(abs(setup["widget"].lf_Wfra.value() - 0.02), 7) == 0
        assert setup["widget"].lf_Lfra.value() == 0.25
        assert setup["widget"].g_frame.isChecked() == True
        assert setup["widget"].g_shaft.isChecked() == True
        assert setup["widget"].out_Drsh.text() == "Drsh = 0.22 [m]"

    def test_init_no_shaft(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        setup["test_obj"].shaft = None
        setup["widget"] = SMachineDimension(
            machine=setup["test_obj"],
            material_dict=setup["material_dict"],
            is_stator=False,
        )
        assert setup["widget"].g_shaft.isChecked() == False
        setup["test_obj"].shaft = Shaft(Drsh=None)
        setup["widget"] = SMachineDimension(
            machine=setup["test_obj"],
            material_dict=setup["material_dict"],
            is_stator=False,
        )
        assert setup["widget"].g_shaft.isChecked() == False
        setup["test_obj"].shaft = Shaft(Drsh=0)
        setup["widget"] = SMachineDimension(
            machine=setup["test_obj"],
            material_dict=setup["material_dict"],
            is_stator=False,
        )
        assert setup["widget"].g_shaft.isChecked() == False

    def test_set_SRint(self, setup):
        """Check that the Widget allow to update SRint"""
        # Clear the field before writing the new value
        setup["widget"].lf_SRint.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_SRint, str(value))
        setup["widget"].lf_SRint.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.Rint == value

    def test_set_SRext(self, setup):
        """Check that the Widget allow to update SRext"""
        # Clear the field before writing the new value
        setup["widget"].lf_SRext.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_SRext, str(value))
        setup["widget"].lf_SRext.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.Rext == value

    def test_set_RRint(self, setup):
        """Check that the Widget allow to update RRint"""
        # Clear the field before writing the new value
        setup["widget"].lf_RRint.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_RRint, str(value))
        setup["widget"].lf_RRint.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.Rint == value

    def test_set_RRext(self, setup):
        """Check that the Widget allow to update RRext"""
        # Clear the field before writing the new value
        setup["widget"].lf_RRext.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_RRext, str(value))
        setup["widget"].lf_RRext.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.Rext == value

    def test_set_Wfra(self, setup):
        """Check that the Widget allow to update Wfra"""
        # Clear the field before writing the new value
        setup["widget"].lf_Wfra.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Wfra, str(value))
        setup["widget"].lf_Wfra.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].frame.Rint == setup["test_obj"].stator.Rext
        assert setup["test_obj"].frame.Rext == setup["test_obj"].stator.Rext + value

    def test_set_Lfra(self, setup):
        """Check that the Widget allow to update Lfra"""
        # Clear the field before writing the new value
        setup["widget"].lf_Lfra.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_Lfra, str(value))
        setup["widget"].lf_Lfra.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].frame.Lfra == value
