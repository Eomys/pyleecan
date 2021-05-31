# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 20 14:10:24 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from pyleecan.Classes.Material import Material
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib, LIB_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM57.PHoleM57 import PHoleM57
from Tests.GUI import gui_option  # Set unit to m

import pytest


class TestPHoleM57(object):
    """Test that the widget PHoleM57 behave like it should"""

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
            HoleM57(H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.17, W4=0.19)
        )
        test_obj.hole.append(
            HoleM57(
                H1=0.11,
                H2=0.12,
                W0=0.13,
                W1=0.14,
                W2=0.15,
                W3=0.17,
                W4=0.19,
                magnet_0=None,
            )
        )

        matlib = DMatLib()
        matlib.dict_mat[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        widget = PHoleM57(test_obj.hole[0], matlib)
        widget2 = PHoleM57(test_obj.hole[1], matlib)

        yield {
            "widget": widget,
            "widget2": widget2,
            "test_obj": test_obj,
            "matlib": matlib,
        }

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].lf_H1.value() == 0.11
        assert setup["widget"].lf_H2.value() == 0.12
        assert setup["widget"].lf_W0.value() == 0.13
        assert setup["widget"].lf_W1.value() == 0.14
        assert setup["widget"].lf_W2.value() == 0.15
        assert setup["widget"].lf_W3.value() == 0.17
        assert setup["widget"].lf_W4.value() == 0.19

        assert setup["widget"].w_mat_1.isHidden() == False

        setup["test_obj"].hole[0] = HoleM57(
            H1=0.21, H2=0.22, W0=0.23, W1=0.24, W2=0.25, W3=0.27, W4=0.29
        )
        setup["widget"] = PHoleM57(setup["test_obj"].hole[0], setup["matlib"])
        assert setup["widget"].lf_H1.value() == 0.21
        assert setup["widget"].lf_H2.value() == 0.22
        assert setup["widget"].lf_W0.value() == 0.23
        assert setup["widget"].lf_W1.value() == 0.24
        assert setup["widget"].lf_W2.value() == 0.25
        assert setup["widget"].lf_W3.value() == 0.27
        assert setup["widget"].lf_W4.value() == 0.29

        assert setup["widget2"].w_mat_1.isHidden() == True

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
