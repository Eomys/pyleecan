# -*- coding: utf-8 -*-

import sys

import pytest
from qtpy import QtWidgets
from qtpy.QtTest import QTest
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM51.PHoleM51 import PHoleM51
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from qtpy.QtCore import Qt


class TestPHoleM51(object):
    """Test that the widget PHoleM51 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPHoleM51")
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

        test_obj = LamHole(Rint=0.1, Rext=0.2)
        self.machine = MachineIPMSM(rotor=test_obj)
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

        self.material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        self.material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        self.widget = PHoleM51(test_obj.hole[0], self.material_dict)

        self.test_obj = test_obj

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        assert self.widget.lf_W3.value() == 0.16
        assert self.widget.lf_W4.value() == 0.17
        assert self.widget.lf_W5.value() == 0.18
        assert self.widget.lf_W6.value() == 0.19
        assert self.widget.lf_W7.value() == 0.2

    def test_init_no_mag(self):
        """Init the widget with all magnets at None"""
        test_obj2 = self.test_obj.copy()
        machine = MachineIPMSM(rotor=test_obj2)
        test_obj2.hole[0].magnet_0 = None
        test_obj2.hole[0].magnet_1 = None
        test_obj2.hole[0].magnet_2 = None

        widget2 = PHoleM51(test_obj2.hole[0], self.material_dict)
        # Check material
        assert not widget2.w_mat_1.isHidden()
        assert not widget2.w_mat_1.isEnabled()
        assert widget2.w_mat_1.c_mat_type.currentText() == ""
        assert widget2.w_mat_1.c_mat_type.currentIndex() == -1
        assert widget2.w_mat_1.c_mat_type.count() == 3
        assert not widget2.is_magnet_0.isChecked()

        assert not widget2.w_mat_2.isHidden()
        assert not widget2.w_mat_2.isEnabled()
        assert widget2.w_mat_2.c_mat_type.currentText() == ""
        assert widget2.w_mat_2.c_mat_type.currentIndex() == -1
        assert widget2.w_mat_2.c_mat_type.count() == 3
        assert not widget2.is_magnet_1.isChecked()

        assert not widget2.w_mat_3.isHidden()
        assert not widget2.w_mat_3.isEnabled()
        assert widget2.w_mat_3.c_mat_type.currentText() == ""
        assert widget2.w_mat_3.c_mat_type.currentIndex() == -1
        assert widget2.w_mat_3.c_mat_type.count() == 3
        assert not widget2.is_magnet_2.isChecked()

    def remove_add_magnet(self):
        """Check that the magnets can be removed and added back"""
        # Check Init state
        assert not self.widget.w_mat_1.isHidden()
        assert self.widget.w_mat_1.isEnabled()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet3"
        assert self.widget.w_mat_1.c_mat_type.currentIndex() == 2
        assert self.widget.is_magnet_0.isChecked()

        assert not self.widget.w_mat_2.isHidden()
        assert self.widget.w_mat_2.isEnabled()
        assert self.widget.w_mat_2.c_mat_type.currentText() == "Magnet2"
        assert self.widget.w_mat_2.c_mat_type.currentIndex() == 1
        assert self.widget.is_magnet_1.isChecked()

        assert not self.widget.w_mat_3.isHidden()
        assert self.widget.w_mat_3.isEnabled()
        assert self.widget.w_mat_3.c_mat_type.currentText() == "Magnet1"
        assert self.widget.w_mat_3.c_mat_type.currentIndex() == 0
        assert self.widget.is_magnet_2.isChecked()

        # Remove Magnet_0
        self.widget.is_magnet_0.setCheckState(Qt.Unchecked)
        assert self.test_obj.hole[0].magnet_0 is None
        assert not self.widget.w_mat_1.isEnabled()

        assert self.test_obj.hole[0].magnet_1 is not None
        assert self.widget.w_mat_2.isEnabled()

        assert self.test_obj.hole[0].magnet_2 is not None
        assert self.widget.w_mat_3.isEnabled()

        # Remove Magnet_1
        self.widget.is_magnet_1.setCheckState(Qt.Unchecked)
        assert self.test_obj.hole[0].magnet_0 is None
        assert not self.widget.w_mat_1.isEnabled()

        assert self.test_obj.hole[0].magnet_1 is None
        assert not self.widget.w_mat_2.isEnabled()

        assert self.test_obj.hole[0].magnet_2 is not None
        assert self.widget.w_mat_3.isEnabled()

        # Remove Magnet_2
        self.widget.is_magnet_2.setCheckState(Qt.Unchecked)
        assert self.test_obj.hole[0].magnet_0 is None
        assert not self.widget.w_mat_1.isEnabled()

        assert self.test_obj.hole[0].magnet_1 is None
        assert not self.widget.w_mat_2.isEnabled()

        assert self.test_obj.hole[0].magnet_2 is None
        assert not self.widget.w_mat_3.isEnabled()

        # Add back Magnet_0 (default material is Magnet1)
        self.widget.is_magnet_0.setCheckState(Qt.Checked)
        assert self.test_obj.hole[0].magnet_0 is not None
        assert self.test_obj.hole[0].magnet_0.mat_type.name == "Magnet1"
        assert self.widget.w_mat_1.isEnabled()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet1"

        assert self.test_obj.hole[0].magnet_1 is None
        assert not self.widget.w_mat_2.isEnabled()

        assert self.test_obj.hole[0].magnet_2 is None
        assert not self.widget.w_mat_3.isEnabled()

        # Add back Magnet_1 (default material is Magnet1)
        self.widget.is_magnet_1.setCheckState(Qt.Checked)
        assert self.test_obj.hole[0].magnet_0 is not None
        assert self.test_obj.hole[0].magnet_0.mat_type.name == "Magnet1"
        assert self.widget.w_mat_1.isEnabled()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet1"

        assert self.test_obj.hole[0].magnet_1 is not None
        assert self.test_obj.hole[0].magnet_1.mat_type.name == "Magnet1"
        assert self.widget.w_mat_2.isEnabled()
        assert self.widget.w_mat_2.c_mat_type.currentText() == "Magnet1"

        assert self.test_obj.hole[0].magnet_2 is None
        assert not self.widget.w_mat_3.isEnabled()

        # Add back Magnet_2 (default material is Magnet1)
        self.widget.is_magnet_2.setCheckState(Qt.Checked)
        assert self.test_obj.hole[0].magnet_0 is not None
        assert self.test_obj.hole[0].magnet_0.mat_type.name == "Magnet1"
        assert self.widget.w_mat_1.isEnabled()
        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet1"

        assert self.test_obj.hole[0].magnet_1 is not None
        assert self.test_obj.hole[0].magnet_1.mat_type.name == "Magnet1"
        assert self.widget.w_mat_2.isEnabled()
        assert self.widget.w_mat_2.c_mat_type.currentText() == "Magnet1"

        assert self.test_obj.hole[0].magnet_2 is not None
        assert self.test_obj.hole[0].magnet_2.mat_type.name == "Magnet1"
        assert self.widget.w_mat_3.isEnabled()
        assert self.widget.w_mat_3.c_mat_type.currentText() == "Magnet1"

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.30")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W0 == 0.30
        assert self.test_obj.hole[0].W0 == 0.30

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        # Clear the field before writing the new value
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.31")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W1 == 0.31
        assert self.test_obj.hole[0].W1 == 0.31

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        # Clear the field before writing the new value
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.32")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W2 == 0.32
        assert self.test_obj.hole[0].W2 == 0.32

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        # Clear the field before writing the new value
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.33")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W3 == 0.33
        assert self.test_obj.hole[0].W3 == 0.33

    def test_set_W4(self):
        """Check that the Widget allow to update W4"""
        # Clear the field before writing the new value
        self.widget.lf_W4.clear()
        QTest.keyClicks(self.widget.lf_W4, "0.34")
        self.widget.lf_W4.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W4 == 0.34
        assert self.test_obj.hole[0].W4 == 0.34

    def test_set_W5(self):
        """Check that the Widget allow to update W5"""
        # Clear the field before writing the new value
        self.widget.lf_W5.clear()
        QTest.keyClicks(self.widget.lf_W5, "0.35")
        self.widget.lf_W5.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W5 == 0.35
        assert self.test_obj.hole[0].W5 == 0.35

    def test_set_W6(self):
        """Check that the Widget allow to update W6"""
        # Clear the field before writing the new value
        self.widget.lf_W6.clear()
        QTest.keyClicks(self.widget.lf_W6, "0.36")
        self.widget.lf_W6.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W6 == 0.36
        assert self.test_obj.hole[0].W6 == 0.36

    def test_set_W7(self):
        """Check that the Widget allow to update W7"""
        # Clear the field before writing the new value
        self.widget.lf_W7.clear()
        QTest.keyClicks(self.widget.lf_W7, "0.37")
        self.widget.lf_W7.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W7 == 0.37
        assert self.test_obj.hole[0].W7 == 0.37

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        # Clear the field before writing the new value
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.38")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H0 == 0.38
        assert self.test_obj.hole[0].H0 == 0.38

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        # Clear the field before writing the new value
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.39")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H1 == 0.39
        assert self.test_obj.hole[0].H1 == 0.39

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        # Clear the field before writing the new value
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.40")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H2 == 0.40
        assert self.test_obj.hole[0].H2 == 0.40

    def test_set_material_0(self):
        """Check that you can change the material of mat_void"""
        self.widget.w_mat_0.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_0.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].mat_void.name == "Magnet1"

    def test_set_material_1(self):
        """Check that you can change the material of magnet_0"""
        self.widget.w_mat_1.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_1.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].magnet_0.mat_type.name == "Magnet1"

    def test_set_material_2(self):
        """Check that you can change the material of magnet_1"""
        self.widget.w_mat_2.c_mat_type.setCurrentIndex(0)

        assert self.widget.w_mat_2.c_mat_type.currentText() == "Magnet1"
        assert self.test_obj.hole[0].magnet_1.mat_type.name == "Magnet1"

    def test_set_material_3(self):
        """Check that you can change the material of magnet_2"""
        self.widget.w_mat_3.c_mat_type.setCurrentIndex(2)

        assert self.widget.w_mat_3.c_mat_type.currentText() == "Magnet3"
        assert self.test_obj.hole[0].magnet_2.mat_type.name == "Magnet3"

    def test_comp_output(self):
        """Check that comp_output is correctly working"""
        self.test_obj.hole[0].W0 = 0.5
        self.test_obj.hole[0].H0 = 0.00000001
        self.widget.hole = self.test_obj.hole[0]
        self.widget.comp_output()
        assert not (self.widget.out_alpha.text() == "alpha: ?")
        assert not (self.widget.out_Whole.text() == "Wslot: ?")


if __name__ == "__main__":
    a = TestPHoleM51()
    a.setup_class()
    a.setup_method()
    a.test_init_no_mag()
    a.teardown_class()
    print("Done")
