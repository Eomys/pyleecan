# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib, LIB_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM53.PHoleM53 import PHoleM53
from pyleecan.Classes.Material import Material


import pytest


class TestPHoleM53(object):
    """Test that the widget PHoleM53 behave like it should"""

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
            HoleM53(
                H0=0.10, H1=0.11, H2=0.12, H3=0.13, W1=0.14, W2=0.15, W3=0.16, W4=0.17
            )
        )
        test_obj.hole[0].magnet_0.mat_type.name = "Magnet3"
        test_obj.hole[0].magnet_1.mat_type.name = "Magnet2"

        matlib = DMatLib()
        matlib.dict_mat[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]
        widget = PHoleM53(test_obj.hole[0], matlib)

        yield {"widget": widget, "test_obj": test_obj, "matlib": matlib}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_H3.value() == 0.13
        assert setup["widget"].lf_W1.value() == 0.14
        assert setup["widget"].lf_W2.value() == 0.15
        assert setup["widget"].lf_W3.value() == 0.16
        assert setup["widget"].lf_W4.value() == 0.17
        # Check material
        assert not setup["widget"].w_mat_1.isHidden()
        assert setup["widget"].w_mat_1.c_mat_type.currentText() == "Magnet3"
        assert setup["widget"].w_mat_1.c_mat_type.currentIndex() == 2
        assert not setup["widget"].w_mat_2.isHidden()
        assert setup["widget"].w_mat_2.c_mat_type.currentText() == "Magnet2"
        assert setup["widget"].w_mat_2.c_mat_type.currentIndex() == 1

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        # Clear the field before writing the new value
        setup["widget"].lf_H0.clear()
        QTest.keyClicks(setup["widget"].lf_H0, "0.311")
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H0 == 0.311
        assert setup["test_obj"].hole[0].H0 == 0.311

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        setup["widget"].lf_H1.clear()
        QTest.keyClicks(setup["widget"].lf_H1, "0.352")
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H1 == 0.352
        assert setup["test_obj"].hole[0].H1 == 0.352

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        setup["widget"].lf_H2.clear()
        QTest.keyClicks(setup["widget"].lf_H2, "0.363")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H2 == 0.363
        assert setup["test_obj"].hole[0].H2 == 0.363

    def test_set_H3(self, setup):
        """Check that the Widget allow to update H3"""
        setup["widget"].lf_H3.clear()
        QTest.keyClicks(setup["widget"].lf_H3, "0.314")
        setup["widget"].lf_H3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H3 == 0.314
        assert setup["test_obj"].hole[0].H3 == 0.314

    def test_set_W1(self, setup):
        """Check that the Widget allow to update W1"""
        setup["widget"].lf_W1.clear()
        QTest.keyClicks(setup["widget"].lf_W1, "0.355")
        setup["widget"].lf_W1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W1 == 0.355
        assert setup["test_obj"].hole[0].W1 == 0.355

    def test_set_W2(self, setup):
        """Check that the Widget allow to update W2"""
        setup["widget"].lf_W2.clear()
        QTest.keyClicks(setup["widget"].lf_W2, "0.366")
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W2 == 0.366
        assert setup["test_obj"].hole[0].W2 == 0.366

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        setup["widget"].lf_W3.clear()
        QTest.keyClicks(setup["widget"].lf_W3, "0.357")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W3 == 0.357
        assert setup["test_obj"].hole[0].W3 == 0.357

    def test_set_W4(self, setup):
        """Check that the Widget allow to update W4"""
        setup["widget"].lf_W4.clear()
        QTest.keyClicks(setup["widget"].lf_W4, "0.368")
        setup["widget"].lf_W4.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W4 == 0.368
        assert setup["test_obj"].hole[0].W4 == 0.368

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

    def test_set_material_2(self, setup):
        """Check that you can change the material of magnet_1"""
        setup["widget"].w_mat_2.c_mat_type.setCurrentIndex(0)

        assert setup["widget"].w_mat_2.c_mat_type.currentText() == "Magnet1"
        assert setup["test_obj"].hole[0].magnet_1.mat_type.name == "Magnet1"

    def test_comp_output(self, setup):
        """Check that comp_output is correctly working"""
        setup["test_obj"].hole[0] = HoleM53(
            H0=0.10,
            H1=0.0000000000011,
            H2=0.12,
            H3=0.0000000000015,
            W4=0.99,
            W1=0.14,
            W2=0.0000015,
            W3=0.0000017,
        )
        setup["widget"].hole = setup["test_obj"].hole[0]
        setup["widget"].comp_output()

        assert (
            setup["widget"].out_slot_surface.text()
            == "Slot suface (2 part): 0.01033 m²"
        )
        assert (
            setup["widget"].out_magnet_surface.text() == "Magnet surface: 4.08e-07 m²"
        )
        assert setup["widget"].out_W5.text() == "W5: 0.01565 m"

    def test_PHoleM53_None_Magnet(self, setup):
        """Check that you can create PHoleM53 with None for magnet_0"""
        setup["test_obj"].hole.append(
            HoleM53(
                H0=0.10,
                H1=0.11,
                H2=0.12,
                W4=0.13,
                W1=0.14,
                W2=0.15,
                W3=0.17,
                magnet_0=None,
            )
        )

        setup["matlib"] = DMatLib()
        setup["matlib"].dict_mat[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        setup["widget"] = PHoleM53(setup["test_obj"].hole[1], setup["matlib"])

        assert setup["widget"].w_mat_1.isHidden()
        assert setup["widget"].w_mat_2.isHidden()
