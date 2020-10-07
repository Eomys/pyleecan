# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.GUI.Dialog.DMachineSetup.SMachineDimension.SMachineDimension import (
    SMachineDimension,
)


import pytest


@pytest.mark.GUI
class TestSMachineDimension(object):
    """Test that the widget SMachineDimension behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = MachineSCIM()
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )
        self.test_obj.frame = Frame(Rint=0.22, Rext=0.24, Lfra=0.25)
        self.test_obj.shaft = Shaft(Lshaft=0.333, Drsh=self.test_obj.rotor.Rint * 2)

        self.matlib = MatLib()
        self.matlib.list_mat = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]
        self.matlib.index_first_mat_mach = 3

        self.widget = SMachineDimension(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test SMachineDimension")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_SRint.value() == 0.21
        assert self.widget.lf_SRext.value() == 0.22
        assert self.widget.lf_RRint.value() == 0.11
        assert self.widget.lf_RRext.value() == 0.12
        assert round(abs(self.widget.lf_Wfra.value() - 0.02), 7) == 0
        assert self.widget.lf_Lfra.value() == 0.25
        assert self.widget.g_frame.isChecked() == True
        assert self.widget.g_shaft.isChecked() == True
        assert self.widget.out_Drsh.text() == "Drsh = 2*Rotor.Rint = 220.0 mm"

    def test_init_no_shaft(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.test_obj.shaft = None
        self.widget = SMachineDimension(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )
        assert self.widget.g_shaft.isChecked() == False
        self.test_obj.shaft = Shaft(Drsh=None)
        self.widget = SMachineDimension(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )
        assert self.widget.g_shaft.isChecked() == False
        self.test_obj.shaft = Shaft(Drsh=0)
        self.widget = SMachineDimension(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )
        assert self.widget.g_shaft.isChecked() == False

    def test_set_SRint(self):
        """Check that the Widget allow to update SRint"""
        # Clear the field before writing the new value
        self.widget.lf_SRint.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_SRint, str(value))
        self.widget.lf_SRint.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.Rint == value

    def test_set_SRext(self):
        """Check that the Widget allow to update SRext"""
        # Clear the field before writing the new value
        self.widget.lf_SRext.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_SRext, str(value))
        self.widget.lf_SRext.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.stator.Rext == value

    def test_set_RRint(self):
        """Check that the Widget allow to update RRint"""
        # Clear the field before writing the new value
        self.widget.lf_RRint.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_RRint, str(value))
        self.widget.lf_RRint.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.Rint == value

    def test_set_RRext(self):
        """Check that the Widget allow to update RRext"""
        # Clear the field before writing the new value
        self.widget.lf_RRext.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_RRext, str(value))
        self.widget.lf_RRext.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.rotor.Rext == value

    def test_set_Wfra(self):
        """Check that the Widget allow to update Wfra"""
        # Clear the field before writing the new value
        self.widget.lf_Wfra.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Wfra, str(value))
        self.widget.lf_Wfra.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.frame.Rint == self.test_obj.stator.Rext
        assert self.test_obj.frame.Rext == self.test_obj.stator.Rext + value

    def test_set_Lfra(self):
        """Check that the Widget allow to update Lfra"""
        # Clear the field before writing the new value
        self.widget.lf_Lfra.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_Lfra, str(value))
        self.widget.lf_Lfra.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.frame.Lfra == value
