import sys
from Tests.GUI import gui_option  # Set unit as [m]
import pytest
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from pyleecan.Classes.Material import Material
from pyleecan.Classes.HoleM63 import HoleM63
from pyleecan.Classes.LamHole import LamHole
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM63.PHoleM63 import PHoleM63
from numpy import pi


class TestPHoleM63(object):
    """Test that the widget PHoleM63 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPHoleM63")
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
        test_obj = LamHole(Rint=0.1, Rext=0.5)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM63(
                H0=0.11,
                H1=0.12,
                W0=0.13,
            )
        )

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet0"),
        ]

        self.widget = PHoleM63(test_obj.hole[0], material_dict)
        self.test_obj = test_obj
        self.material_dict = material_dict

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.11
        assert self.widget.lf_H1.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13

        self.test_obj.hole[0] = HoleM63(H0=0.21, H1=0.22, W0=0.8, top_flat=True)
        self.widget = PHoleM63(self.test_obj.hole[0], self.material_dict)
        assert self.widget.lf_H0.value() == 0.21
        assert self.widget.lf_H1.value() == 0.22
        assert self.widget.lf_W0.value() == 0.8
        assert self.widget.ck_is_top_flat.isChecked() == True

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Clear the field before writing the new value
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.W0 == 0.31
        assert self.test_obj.hole[0].W0 == 0.31

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.35")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H0 == 0.35
        assert self.test_obj.hole[0].H0 == 0.35

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.36")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.hole.H1 == 0.36
        assert self.test_obj.hole[0].H1 == 0.36

    def test_set_top_flat(self):
        """Check that the Widget allow to update top_flat"""
        assert not self.test_obj.hole[0].top_flat
        self.widget.ck_is_top_flat.setChecked(True)
        assert self.test_obj.hole[0].top_flat


if __name__ == "__main__":
    a = TestPHoleM63()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    print("Done")
