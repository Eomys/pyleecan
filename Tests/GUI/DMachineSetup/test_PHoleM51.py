# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM51.PHoleM51 import PHoleM51
from pyleecan.Classes.Material import Material


import pytest


@pytest.mark.GUI
class TestPHoleM51(object):
    """Test that the widget PHoleM51 behave like it should"""

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
            HoleM51(
                H0=0.10,
                H1=0.11,
                H2=0.12,
                W0=0.13,
                W1=0.14,
                W2=0.15,
                W3=0.16,
                W4=0.17,
                W5=0.18,
                W6=0.19,
                W7=0.2,
            )
        )
        test_obj.hole[0].magnet_0.mat_type.name = "Magnet3"
        test_obj.hole[0].magnet_1.mat_type.name = "Magnet2"
        test_obj.hole[0].magnet_2.mat_type.name = "Magnet1"

        matlib = MatLib()
        matlib.dict_mat["RefMatLib"] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        widget = PHoleM51(test_obj.hole[0], matlib)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W0.value() == 0.13
        assert setup["widget"].lf_W1.value() == 0.14
        assert setup["widget"].lf_W2.value() == 0.15
        assert setup["widget"].lf_W3.value() == 0.16
        assert setup["widget"].lf_W4.value() == 0.17
        assert setup["widget"].lf_W5.value() == 0.18
        assert setup["widget"].lf_W6.value() == 0.19
        assert setup["widget"].lf_W7.value() == 0.2
        # Check material
        assert not setup["widget"].w_mat_1.isHidden()
        assert setup["widget"].w_mat_1.c_mat_type.currentText() == "Magnet3"
        assert setup["widget"].w_mat_1.c_mat_type.currentIndex() == 2
        assert not setup["widget"].w_mat_2.isHidden()
        assert setup["widget"].w_mat_2.c_mat_type.currentText() == "Magnet2"
        assert setup["widget"].w_mat_2.c_mat_type.currentIndex() == 1
        assert not setup["widget"].w_mat_3.isHidden()
        assert setup["widget"].w_mat_3.c_mat_type.currentText() == "Magnet1"
        assert setup["widget"].w_mat_3.c_mat_type.currentIndex() == 0

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        setup["widget"].lf_W0.clear()
        QTest.keyClicks(setup["widget"].lf_W0, "0.30")
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W0 == 0.30
        assert setup["test_obj"].hole[0].W0 == 0.30

    def test_set_W1(self, setup):
        """Check that the Widget allow to update W1"""
        # Clear the field before writing the new value
        setup["widget"].lf_W1.clear()
        QTest.keyClicks(setup["widget"].lf_W1, "0.31")
        setup["widget"].lf_W1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W1 == 0.31
        assert setup["test_obj"].hole[0].W1 == 0.31

    def test_set_W2(self, setup):
        """Check that the Widget allow to update W2"""
        # Clear the field before writing the new value
        setup["widget"].lf_W2.clear()
        QTest.keyClicks(setup["widget"].lf_W2, "0.32")
        setup["widget"].lf_W2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W2 == 0.32
        assert setup["test_obj"].hole[0].W2 == 0.32

    def test_set_W3(self, setup):
        """Check that the Widget allow to update W3"""
        # Clear the field before writing the new value
        setup["widget"].lf_W3.clear()
        QTest.keyClicks(setup["widget"].lf_W3, "0.33")
        setup["widget"].lf_W3.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W3 == 0.33
        assert setup["test_obj"].hole[0].W3 == 0.33

    def test_set_W4(self, setup):
        """Check that the Widget allow to update W4"""
        # Clear the field before writing the new value
        setup["widget"].lf_W4.clear()
        QTest.keyClicks(setup["widget"].lf_W4, "0.34")
        setup["widget"].lf_W4.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W4 == 0.34
        assert setup["test_obj"].hole[0].W4 == 0.34

    def test_set_W5(self, setup):
        """Check that the Widget allow to update W5"""
        # Clear the field before writing the new value
        setup["widget"].lf_W5.clear()
        QTest.keyClicks(setup["widget"].lf_W5, "0.35")
        setup["widget"].lf_W5.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W5 == 0.35
        assert setup["test_obj"].hole[0].W5 == 0.35

    def test_set_W6(self, setup):
        """Check that the Widget allow to update W6"""
        # Clear the field before writing the new value
        setup["widget"].lf_W6.clear()
        QTest.keyClicks(setup["widget"].lf_W6, "0.36")
        setup["widget"].lf_W6.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W6 == 0.36
        assert setup["test_obj"].hole[0].W6 == 0.36

    def test_set_W7(self, setup):
        """Check that the Widget allow to update W7"""
        # Clear the field before writing the new value
        setup["widget"].lf_W7.clear()
        QTest.keyClicks(setup["widget"].lf_W7, "0.37")
        setup["widget"].lf_W7.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W7 == 0.37
        assert setup["test_obj"].hole[0].W7 == 0.37

    def test_set_H0(self, setup):
        """Check that the Widget allow to update H0"""
        # Clear the field before writing the new value
        setup["widget"].lf_H0.clear()
        QTest.keyClicks(setup["widget"].lf_H0, "0.38")
        setup["widget"].lf_H0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H0 == 0.38
        assert setup["test_obj"].hole[0].H0 == 0.38

    def test_set_H1(self, setup):
        """Check that the Widget allow to update H1"""
        # Clear the field before writing the new value
        setup["widget"].lf_H1.clear()
        QTest.keyClicks(setup["widget"].lf_H1, "0.39")
        setup["widget"].lf_H1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H1 == 0.39
        assert setup["test_obj"].hole[0].H1 == 0.39

    def test_set_H2(self, setup):
        """Check that the Widget allow to update H2"""
        # Clear the field before writing the new value
        setup["widget"].lf_H2.clear()
        QTest.keyClicks(setup["widget"].lf_H2, "0.40")
        setup["widget"].lf_H2.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.H2 == 0.40
        assert setup["test_obj"].hole[0].H2 == 0.40

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

    def test_set_material_3(self, setup):
        """Check that you can change the material of magnet_2"""
        setup["widget"].w_mat_3.c_mat_type.setCurrentIndex(2)

        assert setup["widget"].w_mat_3.c_mat_type.currentText() == "Magnet3"
        assert setup["test_obj"].hole[0].magnet_2.mat_type.name == "Magnet3"

    def test_comp_output(self, setup):
        """Check that comp_output is correctly working"""
        setup["test_obj"].hole[0].W0 = 0.5
        setup["test_obj"].hole[0].H0 = 0.00000001
        setup["widget"].hole = setup["test_obj"].hole[0]
        setup["widget"].comp_output()
        assert not (setup["widget"].out_alpha.text() == "alpha: ?")
        assert not (setup["widget"].out_Whole.text() == "Wslot: ?")
