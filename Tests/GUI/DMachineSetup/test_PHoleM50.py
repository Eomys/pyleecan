# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM50.PHoleM50 import PHoleM50
from Tests.GUI import gui_option  # Set unit to m
from pyleecan.Classes.Material import Material


import pytest


class TestPHoleM50(object):
    """Test that the widget PHoleM50 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamHole(Rint=0.1, Rext=0.2)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                H0=0.10,
                H1=0.11,
                H2=0.12,
                W0=0.13,
                W1=0.14,
                W2=0.15,
                H3=0.16,
                W3=0.17,
                H4=0.18,
                W4=0.19,
            )
        )
        test_obj.hole[0].magnet_0.mat_type.name = "Magnet3"
        test_obj.hole[0].magnet_1.mat_type.name = "Magnet2"

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        widget = PHoleM50(test_obj.hole[0], material_dict)

        yield {"widget": widget, "test_obj": test_obj, "material_dict": material_dict}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W0.value() == 0.13
        assert setup["widget"].lf_W1.value() == 0.14
        assert setup["widget"].lf_W2.value() == 0.15
        assert setup["widget"].lf_H3.value() == 0.16
        assert setup["widget"].lf_W3.value() == 0.17
        assert setup["widget"].lf_H4.value() == 0.18
        assert setup["widget"].lf_W4.value() == 0.19
        # Check material
        assert not setup["widget"].w_mat_1.isHidden()
        assert setup["widget"].w_mat_1.c_mat_type.currentText() == "Magnet3"
        assert setup["widget"].w_mat_1.c_mat_type.currentIndex() == 2
        assert not setup["widget"].w_mat_2.isHidden()
        assert setup["widget"].w_mat_2.c_mat_type.currentText() == "Magnet2"
        assert setup["widget"].w_mat_2.c_mat_type.currentIndex() == 1

        setup["test_obj"].hole[0] = HoleM50(
            H0=0.20,
            H1=0.21,
            H2=0.22,
            W0=0.23,
            W1=0.24,
            W2=0.25,
            H3=0.26,
            W3=0.27,
            H4=0.28,
            W4=0.29,
        )
        setup["widget"] = PHoleM50(setup["test_obj"].hole[0], setup["material_dict"])
        assert setup["widget"].lf_H0.value() == 0.20
        assert setup["widget"].lf_H1.value() == 0.21
        assert setup["widget"].lf_H2.value() == 0.22
        assert setup["widget"].lf_W0.value() == 0.23
        assert setup["widget"].lf_W1.value() == 0.24
        assert setup["widget"].lf_W2.value() == 0.25
        assert setup["widget"].lf_H3.value() == 0.26
        assert setup["widget"].lf_W3.value() == 0.27
        assert setup["widget"].lf_H4.value() == 0.28
        assert setup["widget"].lf_W4.value() == 0.29

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        setup["widget"].lf_W0.clear()
        QTest.keyClicks(setup["widget"].lf_W0, "0.31")
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W0 == 0.31
        assert setup["test_obj"].hole[0].W0 == 0.31

    def test_set_W1(self, setup):
        """Check that the Widget allow to update W1"""
        # Clear the field before writing the new value
        setup["widget"].lf_W1.clear()
        QTest.keyClicks(setup["widget"].lf_W1, "0.32")
        setup["widget"].lf_W1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W1 == 0.32
        assert setup["test_obj"].hole[0].W1 == 0.32

    def test_set_W2(self, setup):
        """Check that the Widget allow to update W2"""
        setup["widget"].lf_W2.clear()
        QTest.keyClicks(setup["widget"].lf_W2, "0.33")
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W2 == 0.33
        assert setup["test_obj"].hole[0].W2 == 0.33

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        setup["widget"].lf_W3.clear()
        QTest.keyClicks(setup["widget"].lf_W3, "0.323")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W3 == 0.323
        assert setup["test_obj"].hole[0].W3 == 0.323

    def test_set_W4(self, setup):
        """Check that the Widget allow to update W4"""
        setup["widget"].lf_W4.clear()
        QTest.keyClicks(setup["widget"].lf_W4, "0.334")
        setup["widget"].lf_W4.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W4 == 0.334
        assert setup["test_obj"].hole[0].W4 == 0.334

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        setup["widget"].lf_H0.clear()
        QTest.keyClicks(setup["widget"].lf_H0, "0.34")
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H0 == 0.34
        assert setup["test_obj"].hole[0].H0 == 0.34

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        setup["widget"].lf_H1.clear()
        QTest.keyClicks(setup["widget"].lf_H1, "0.35")
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H1 == 0.35
        assert setup["test_obj"].hole[0].H1 == 0.35

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()
        QTest.keyClicks(setup["widget"].lf_H2, "0.36")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H2 == 0.36
        assert setup["test_obj"].hole[0].H2 == 0.36

    def test_set_H3(self, setup):
        """Check that the Widget allow to update H3"""
        setup["widget"].lf_H3.clear()
        QTest.keyClicks(setup["widget"].lf_H3, "0.363")
        setup["widget"].lf_H3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H3 == 0.363
        assert setup["test_obj"].hole[0].H3 == 0.363

    def test_set_H4(self, setup):
        """Check that the Widget allow to update H4"""
        setup["widget"].lf_H4.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].lf_H4, str(value))
        setup["widget"].lf_H4.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H4 == value
        assert setup["test_obj"].hole[0].H4 == value

    def test_set_material_0(self, setup):
        """Check that you can change the material of magnet_0"""
        setup["widget"].w_mat_0.c_mat_type.setCurrentIndex(0)

        assert setup["widget"].w_mat_0.c_mat_type.currentText() == "Magnet1"
        assert setup["test_obj"].hole[0].mat_void.name == "Magnet1"

        setup["widget"].w_mat_0.c_mat_type.setCurrentIndex(1)

        assert setup["widget"].w_mat_0.c_mat_type.currentText() == "Magnet2"
        assert setup["test_obj"].hole[0].mat_void.name == "Magnet2"

    def test_set_material_1(self, setup):
        """Check that you can change the material of magnet_1"""
        setup["widget"].w_mat_1.c_mat_type.setCurrentIndex(0)

        assert setup["widget"].w_mat_1.c_mat_type.currentText() == "Magnet1"
        assert setup["test_obj"].hole[0].magnet_0.mat_type.name == "Magnet1"

    def test_set_material_2(self, setup):
        """Check that you can change the material of magnet_2"""
        setup["widget"].w_mat_2.c_mat_type.setCurrentIndex(0)

        assert setup["widget"].w_mat_2.c_mat_type.currentText() == "Magnet1"
        assert setup["test_obj"].hole[0].magnet_1.mat_type.name == "Magnet1"

    def test_comp_output(self, setup):
        """Check that you can compute the output only if the hole is correctly set"""
        setup["test_obj"] = LamHole(Rint=0.1, Rext=0.2)
        setup["test_obj"].hole = list()
        setup["test_obj"].hole.append(
            HoleM50(
                H0=0.20,
                H1=0.11,
                H2=0.12,
                W0=0.23,
                W1=0.14,
                W2=0.15,
                H3=0.16,
                W3=0.27,
                H4=0.18,
                W4=0.19,
            )
        )
        setup["widget"].hole = setup["test_obj"].hole[0]
        setup["widget"].comp_output()

        # Nan are there because the value are not correct for the sin, cos and tan methods. But with true values, it works.

        assert setup["widget"].out_slot_surface.text() == "Slot surface: nan [m²]"
        assert setup["widget"].out_magnet_surface.text() == "Magnet surf.: 0.0608 [m²]"
        assert setup["widget"].out_alpha.text() == "alpha: nan [rad] (nan°)"
        assert setup["widget"].out_W5.text() == "W5: nan [m]"
