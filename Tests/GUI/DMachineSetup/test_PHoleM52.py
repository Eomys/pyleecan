# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52.PHoleM52 import PHoleM52
from pyleecan.Classes.Material import Material


import pytest


class TestPHoleM52(object):
    """Test that the widget PHoleM52 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamHole(Rint=0.1, Rext=0.2)
        test_obj.hole = list()
        test_obj.hole.append(HoleM52(H0=0.10, H1=0.11, H2=0.12, W0=0.13, W3=0.17))
        test_obj.hole[0].magnet_0.mat_type.name = "Magnet2"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        widget = PHoleM52(test_obj.hole[0], material_dict)

        yield {"widget": widget, "test_obj": test_obj, "material_dict": material_dict}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W0.value() == 0.13
        assert setup["widget"].lf_W3.value() == 0.17
        # Check material
        assert not setup["widget"].w_mat_1.isHidden()
        assert setup["widget"].w_mat_1.c_mat_type.currentText() == "Magnet2"
        assert setup["widget"].w_mat_1.c_mat_type.currentIndex() == 1

        setup["test_obj"] = LamHole(Rint=0.1, Rext=0.2)
        setup["test_obj"].hole = list()
        setup["test_obj"].hole.append(
            HoleM52(H0=0.10, H1=0.11, H2=0.12, W0=0.13, W3=0.17)
        )
        setup["test_obj"].hole[0].magnet_0 == None

        setup["widget"] = PHoleM52(setup["test_obj"].hole[0], setup["material_dict"])
        assert not setup["widget"].w_mat_1.isHidden()

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        setup["widget"].lf_W0.clear()
        QTest.keyClicks(setup["widget"].lf_W0, "0.31")
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W0 == 0.31
        assert setup["test_obj"].hole[0].W0 == 0.31

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        # Clear the field before writing the new value
        setup["widget"].lf_W3.clear()
        QTest.keyClicks(setup["widget"].lf_W3, "0.323")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W3 == 0.323
        assert setup["test_obj"].hole[0].W3 == 0.323

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        # Clear the field before writing the new value
        setup["widget"].lf_H0.clear()
        QTest.keyClicks(setup["widget"].lf_H0, "0.34")
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H0 == 0.34
        assert setup["test_obj"].hole[0].H0 == 0.34

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        # Clear the field before writing the new value
        setup["widget"].lf_H1.clear()
        QTest.keyClicks(setup["widget"].lf_H1, "0.35")
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H1 == 0.35
        assert setup["test_obj"].hole[0].H1 == 0.35

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        # Clear the field before writing the new value
        setup["widget"].lf_H2.clear()
        QTest.keyClicks(setup["widget"].lf_H2, "0.36")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H2 == 0.36
        assert setup["test_obj"].hole[0].H2 == 0.36

    def test_set_material_0(self, setup):
        """Check that you can change the material of mat_void"""
        setup["widget"].w_mat_0.c_mat_type.setCurrentIndex(0)

        assert setup["widget"].w_mat_0.c_mat_type.currentText() == "Magnet1"
        assert setup["test_obj"].hole[0].mat_void.name == "Magnet1"

    def test_set_material_1(self, setup):
        """Check that you can change the material of magnet_0"""
        setup["widget"].w_mat_1.c_mat_type.setCurrentIndex(0)

        assert setup["widget"].w_mat_1.c_mat_type.currentText() == "Magnet1"
        assert setup["test_obj"].hole[0].magnet_0.mat_type.name == "Magnet1"

    def test_comp_output(self, setup):
        """Check that you can compute the output only if the hole is correctly set"""
        setup["test_obj"] = LamHole(Rint=0.1, Rext=0.2)
        setup["test_obj"].hole = list()
        setup["test_obj"].hole.append(
            HoleM52(H0=0.0010, H1=0.11, H2=0.00012, W0=0.0013, W3=0.0017)
        )
        setup["widget"].hole = setup["test_obj"].hole[0]
        setup["widget"].comp_output()

        # Nan are there because the value are not correct for the sin, cos and tan methods. But with true values, it works.

        assert setup["widget"].out_slot_surface.text() == "Slot suface: 0.002569 m²"
        assert (
            setup["widget"].out_magnet_surface.text() == "Magnet surface: 0.000143 m²"
        )
        assert setup["widget"].out_alpha.text() == "alpha: 0.166 rad (9.511°)"
        assert setup["widget"].out_W1.text() == "W1: 0.006234 m"
