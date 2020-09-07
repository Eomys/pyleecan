# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 20 14:10:24 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

import sys
from random import uniform

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM57.PHoleM57 import PHoleM57
from Tests.GUI import gui_option  # Set unit to m

import pytest


@pytest.mark.GUI
class TestPHoleM57(object):
    """Test that the widget PHoleM57 behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
            HoleM57(H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.17, W4=0.19)
        )
        self.widget = PHoleM57(self.test_obj.hole[0])

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PHoleM57")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        assert self.widget.lf_W3.value() == 0.17
        assert self.widget.lf_W4.value() == 0.19

        self.test_obj.hole[0] = HoleM57(
            H1=0.21, H2=0.22, W0=0.23, W1=0.24, W2=0.25, W3=0.27, W4=0.29
        )
        self.widget = PHoleM57(self.test_obj.hole[0])
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W0.value() == 0.23
        assert self.widget.lf_W1.value() == 0.24
        assert self.widget.lf_W2.value() == 0.25
        assert self.widget.lf_W3.value() == 0.27
        assert self.widget.lf_W4.value() == 0.29

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W0 == 0.31
        assert self.test_obj.hole[0].W0 == 0.31

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W1 == 0.32
        assert self.test_obj.hole[0].W1 == 0.32

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W2 == 0.33
        assert self.test_obj.hole[0].W2 == 0.33

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.323")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W3 == 0.323
        assert self.test_obj.hole[0].W3 == 0.323

    def test_set_W4(self):
        """Check that the Widget allow to update W4"""
        self.widget.lf_W4.clear()
        QTest.keyClicks(self.widget.lf_W4, "0.334")
        self.widget.lf_W4.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W4 == 0.334
        assert self.test_obj.hole[0].W4 == 0.334

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H1 == 0.35
        assert self.test_obj.hole[0].H1 == 0.35

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H2 == 0.36
        assert self.test_obj.hole[0].H2 == 0.36
