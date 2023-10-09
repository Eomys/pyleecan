# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM17 import SlotM17
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot17.PMSlot17 import PMSlot17
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY


import pytest


class TestPMSlot17(object):
    """Test that the widget PMSlot17 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM17(Zs=2)
        self.test_obj.magnet.Lmag = 0.12

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        self.material_dict = material_dict

        self.widget = PMSlot17(self.test_obj, self.material_dict)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot17")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_Lmag.value() == 0.12

    def test_set_Lmag(self):
        """Check that the Widget allow to update Lmag"""
        # Check Unit
        assert self.widget.unit_Lmag.text() == "[m]"
        # Change value in GUI
        self.widget.lf_Lmag.clear()
        QTest.keyClicks(self.widget.lf_Lmag, "0.34")
        self.widget.lf_Lmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.lamination.magnet.Lmag == 0.34
        assert self.test_obj.magnet.Lmag == 0.34

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.9)
        # p check
        self.test_obj.slot = SlotM17(Zs=4)
        self.widget = PMSlot17(self.test_obj, self.material_dict)
        assert self.widget.check(self.test_obj) == "SlotM17 must have p=1"

    def test_set_material(self):
        """Check that you can change the material"""
        self.widget.w_mag.w_mat.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.magnet.mat_type.name == "test1"
        assert self.test_obj.magnet.mat_type.elec.rho == 0.31
        self.widget.w_mag.w_mat.c_mat_type.setCurrentIndex(2)
        assert self.test_obj.magnet.mat_type.name == "test3"
        assert self.test_obj.magnet.mat_type.elec.rho == 0.33

    def test_set_type_magnetization(self):
        """Check that you can change tha magnetization"""
        # type_magnetization set test
        self.widget.w_mag.c_type_magnetization.setCurrentIndex(2)
        assert self.test_obj.magnet.type_magnetization == 2
        self.widget.w_mag.c_type_magnetization.setCurrentIndex(0)
        assert self.test_obj.magnet.type_magnetization == 0


if __name__ == "__main__":
    a = TestPMSlot17()
    a.setup_class()
    a.setup_method()
    a.test_check()
    a.teardown_class()
    print("Done")
