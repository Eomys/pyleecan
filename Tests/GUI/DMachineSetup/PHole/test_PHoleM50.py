# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM50.PHoleM50 import PHoleM50
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY


class TestPHoleM50(object):
    """Test that the widget PHoleM50 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPHoleM50")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
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
        self.test_obj.hole[0].magnet_0.mat_type.name = "Magnet3"
        self.test_obj.hole[0].magnet_1.mat_type.name = "Magnet2"

        self.material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        self.material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        self.widget = PHoleM50(self.test_obj.hole[0], self.material_dict)

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        assert self.widget.lf_H3.value() == 0.16
        assert self.widget.lf_W3.value() == 0.17
        assert self.widget.lf_H4.value() == 0.18
        assert self.widget.lf_W4.value() == 0.19
        # Check material
        assert not self.widget.w_mat_1.isHidden()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet3"
        assert self.widget.w_mat_1.c_mat_type.currentIndex() == 2
        assert not self.widget.w_mat_2.isHidden()
        assert self.widget.w_mat_2.c_mat_type.currentText() == "Magnet2"
        assert self.widget.w_mat_2.c_mat_type.currentIndex() == 1

        self.test_obj.hole[0] = HoleM50(
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
        self.widget = PHoleM50(self.test_obj.hole[0], self.material_dict)
        assert self.widget.lf_H0.value() == 0.20
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W0.value() == 0.23
        assert self.widget.lf_W1.value() == 0.24
        assert self.widget.lf_W2.value() == 0.25
        assert self.widget.lf_H3.value() == 0.26
        assert self.widget.lf_W3.value() == 0.27
        assert self.widget.lf_H4.value() == 0.28
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
        # Clear the field before writing the new value
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

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H0 == 0.34
        assert self.test_obj.hole[0].H0 == 0.34

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

    def test_set_H3(self):
        """Check that the Widget allow to update H3"""
        self.widget.lf_H3.clear()
        QTest.keyClicks(self.widget.lf_H3, "0.363")
        self.widget.lf_H3.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H3 == 0.363
        assert self.test_obj.hole[0].H3 == 0.363

    def test_set_H4(self):
        """Check that the Widget allow to update H4"""
        self.widget.lf_H4.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H4, str(value))
        self.widget.lf_H4.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H4 == value
        assert self.test_obj.hole[0].H4 == value

    def test_set_material_0(self):
        """Check that you can change the material of magnet_0"""
        self.widget.w_mat_0.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_0.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].mat_void.name == "Magnet1"

        self.widget.w_mat_0.c_mat_type.setCurrentIndex(1)

        assert self.widget.w_mat_0.c_mat_type.currentText() == "Magnet2"
        assert self.test_obj.hole[0].mat_void.name == "Magnet2"

    def test_set_material_1(self):
        """Check that you can change the material of magnet_1"""
        self.widget.w_mat_1.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].magnet_0.mat_type.name == "Magnet1"

    def test_set_material_2(self):
        """Check that you can change the material of magnet_2"""
        self.widget.w_mat_2.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_2.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].magnet_1.mat_type.name == "Magnet1"

    def test_comp_output(self):
        """Check that you can compute the output only if the hole is correctly set"""
        self.test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.hole = list()
        self.test_obj.hole.append(
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
        self.widget.hole = self.test_obj.hole[0]
        self.widget.comp_output()

        # Nan are there because the value are not correct for the sin, cos and tan methods. But with true values, it works.

        assert self.widget.out_slot_surface.text() == "Hole surface: nan [m²]"
        assert self.widget.out_magnet_surface.text() == "Magnet surf.: 0.0608 [m²]"
        assert self.widget.out_alpha.text() == "alpha: nan [rad] (nan°)"
        assert self.widget.out_W5.text() == "Max magnet width: nan [m]"


if __name__ == "__main__":
    a = TestPHoleM50()
    a.setup_class()
    a.setup_method()
    a.test_comp_output()
    a.teardown_class()
    print("Done")
