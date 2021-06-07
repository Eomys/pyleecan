# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM54.PHoleM54 import PHoleM54
from pyleecan.Classes.Material import Material


import pytest


class TestPHoleM54(object):
    """Test that the widget PHoleM54 behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = LamHole(Rint=0.1, Rext=0.2)
        test_obj.hole = list()
        test_obj.hole.append(HoleM54(H0=0.10, H1=0.11, W0=0.12, R1=0.13))
        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]
        widget = PHoleM54(test_obj.hole[0], material_dict=material_dict)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H0.value() == 0.10
        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_W0.value() == 0.12
        assert setup["widget"].lf_R1.value() == 0.13

    def test_set_W0(self, setup):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        setup["widget"].lf_W0.clear()
        QTest.keyClicks(setup["widget"].lf_W0, "0.31")
        setup["widget"].lf_W0.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.W0 == 0.31
        assert setup["test_obj"].hole[0].W0 == 0.31

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

    def test_set_R1(self, setup):
        """Check that the Widget allow to update R1"""
        setup["widget"].lf_R1.clear()
        QTest.keyClicks(setup["widget"].lf_R1, "0.36")
        setup["widget"].lf_R1.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].hole.R1 == 0.36
        assert setup["test_obj"].hole[0].R1 == 0.36
