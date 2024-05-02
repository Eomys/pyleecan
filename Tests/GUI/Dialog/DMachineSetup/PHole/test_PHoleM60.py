import sys
from Tests.GUI import gui_option  # Set unit as [m]
import pytest
from qtpy import QtWidgets
from qtpy.QtTest import QTest
from pyleecan.Classes.Material import Material
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.LamHole import LamHole
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM60.PHoleM60 import PHoleM60


class TestPHoleM60(object):
    """Test that the widget PHoleM60 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPHoleM60")
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
            HoleM60(H0=0.11, H1=0.12, W0=0.13, W1=0.14, W2=0.15, W3=0.17)
        )
        test_obj.hole.append(
            HoleM60(
                H0=0.11,
                H1=0.12,
                W0=0.13,
                W1=0.14,
                W2=0.15,
                W3=0.17,
                magnet_0=None,
            )
        )

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        self.widget = PHoleM60(test_obj.hole[0], material_dict)
        self.widget2 = PHoleM60(test_obj.hole[1], material_dict)
        self.test_obj = test_obj
        self.material_dict = material_dict

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.11
        assert self.widget.lf_H1.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        assert self.widget.lf_W3.value() == 0.17

        assert self.widget.w_mat_1.isHidden() == False

        self.test_obj.hole[0] = HoleM60(
            H0=0.21, H1=0.22, W0=0.23, W1=0.24, W2=0.25, W3=0.27
        )
        self.widget = PHoleM60(self.test_obj.hole[0], self.material_dict)
        assert self.widget.lf_H0.value() == 0.21
        assert self.widget.lf_H1.value() == 0.22
        assert self.widget.lf_W0.value() == 0.23
        assert self.widget.lf_W1.value() == 0.24
        assert self.widget.lf_W2.value() == 0.25
        assert self.widget.lf_W3.value() == 0.27

        assert self.widget2.w_mat_1.isHidden() == True

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


if __name__ == "__main__":
    a = TestPHoleM60()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    print("Done")
