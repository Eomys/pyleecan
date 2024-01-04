# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotW11_2 import SlotW11_2
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot11.PWSlot11 import PWSlot11
from pyleecan.Classes.Notch import Notch
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY

import pytest


class TestPWSlot11_2:
    """Test that the widget PWSlot11 behave like it should when using SlotW11_2"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot11")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        self.material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        self.mat1 = Material(name="Mat1")
        self.mat2 = Material(name="Mat2")
        self.mat3 = Material(name="M400-50A")
        self.mat4 = Material(name="Mat4")
        self.material_dict[LIB_KEY] = [
            self.mat1,
            self.mat2,
            self.mat3,
        ]
        self.material_dict[MACH_KEY] = [
            self.mat4,
        ]

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2, mat_type=self.mat3)
        self.test_obj.slot = SlotW11_2(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            R1=0.16,
            H1_is_rad=False,
        )
        self.widget = PWSlot11(self.test_obj, self.material_dict)

    def test_slot_type_unchanged(self):
        # Set Wedge
        self.widget.g_wedge.setChecked(True)
        self.widget.w_wedge_mat.c_mat_type.setCurrentIndex(0)

        # Remove wedge
        self.widget.g_wedge.setChecked(False)
        self.assert_slot_type()

        # Set W0
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set W1
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set W2
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set W3
        self.widget.lf_W3.setEnabled(True)
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.99")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set H0
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set H1 in mm
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set H1 in deg
        self.widget.c_H1_unit.setCurrentIndex(2)

        self.widget.lf_H1.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H1, str(1.4))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set H1 in rad
        self.widget.c_H1_unit.setCurrentIndex(1)
        self.assert_slot_type()

        # Set H2
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set R1
        self.widget.lf_R1.clear()
        QTest.keyClicks(self.widget.lf_R1, "0.37")
        self.widget.lf_R1.editingFinished.emit()  # To trigger the slot
        self.assert_slot_type()

        # Set constant tooth
        self.widget.is_cst_tooth.setChecked(True)
        self.assert_slot_type()
        self.widget.is_cst_tooth.setChecked(False)
        self.assert_slot_type()

    def assert_slot_type(self):
        assert isinstance(self.test_obj.slot, SlotW11_2)
        assert isinstance(self.widget.lamination.slot, SlotW11_2)
