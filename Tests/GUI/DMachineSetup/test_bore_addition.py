from PySide2 import QtWidgets
from os.path import join, isfile
from os import remove
import mock
import sys
import logging
from numpy import pi
from numpy.testing import assert_almost_equal
import pytest
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.BoreFlower import BoreFlower
from pyleecan.Classes.BoreSinePole import BoreSinePole
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.DBore.DBore import DBore
from pyleecan.GUI.Dialog.DMachineSetup.DBore.PBoreSinePole.PBoreSinePole import (
    PBoreSinePole,
)
from pyleecan.GUI.Dialog.DMachineSetup.DBore.PBoreFlower.PBoreFlower import PBoreFlower
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape
from Tests import save_gui_path as save_path

matlib_path = join(DATA_DIR, "Material")
machine_name = "Toyota_Prius"

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)


class TestBoreAddition(object):
    """Test that the widget SLamShape enables to add Bore shape"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestBoreShape")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        # MatLib widget
        material_dict = load_matlib(matlib_path=matlib_path)
        self.widget = DMachineSetup(
            material_dict=material_dict, machine_path=join(DATA_DIR, "Machine")
        )

        # Loading Prius machine
        return_value = (
            join(DATA_DIR, "Machine", machine_name + ".json"),
            "Json (*.json)",
        )
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.b_load.clicked.emit()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_boreflower_addition(self):
        """Checking that the UI allow the definition and the addition to a machine"""

        assert self.widget.machine.name == "Toyota_Prius"

        # Step 1 : Checking bore groupBox and recovering dialog
        self.widget.nav_step.setCurrentRow(5)  # Stator Shape step
        assert isinstance(self.widget.w_step, SLamShape)
        assert self.widget.w_step.g_bore.isHidden()

        self.widget.nav_step.setCurrentRow(7)  # Rotor Shape step
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_bore.isHidden()
        assert not self.widget.w_step.g_bore.isChecked()
        assert self.widget.w_step.obj.bore is None

        self.widget.w_step.g_bore.setChecked(True)

        assert self.widget.w_step.b_bore.isEnabled()
        self.widget.w_step.b_bore.clicked.emit()

        assert isinstance(self.widget.w_step.bore_win, DBore)

        # Check initial state
        BW = self.widget.w_step.bore_win
        assert BW.c_bore_type.currentText() == "Bore Flower"
        assert isinstance(BW.w_bore, PBoreFlower)
        assert BW.w_bore.lf_Rarc.value() == pytest.approx(68.17 * 1e-3, rel=0.1)
        assert BW.w_bore.lf_alpha.value() == pytest.approx(0.39269908, rel=0.1)
        assert BW.w_bore.si_N.value() == 8

        # Check set values
        BW.w_bore.lf_Rarc.setValue(60e-3)
        BW.w_bore.lf_Rarc.editingFinished.emit()
        assert BW.w_bore.bore.Rarc == 60e-3

        BW.w_bore.si_N.setValue(9)
        BW.w_bore.si_N.editingFinished.emit()
        assert BW.w_bore.bore.N == 9

        assert BW.w_bore.c_alpha_unit.currentText() == "[rad]"
        BW.w_bore.lf_alpha.setValue(1)
        BW.w_bore.lf_alpha.editingFinished.emit()
        assert BW.w_bore.bore.alpha == 1
        BW.w_bore.c_alpha_unit.setCurrentIndex(1)

        assert BW.w_bore.c_alpha_unit.currentText() == "[deg]"
        BW.w_bore.lf_alpha.setValue(45)
        BW.w_bore.lf_alpha.editingFinished.emit()
        assert BW.w_bore.bore.alpha == pytest.approx(0.39269908 * 2, rel=0.1)

        # Checking plot/preview function
        BW.b_plot.clicked.emit()

        # Clicking on OK button
        BW.b_ok.clicked.emit()
        assert isinstance(self.widget.w_step.obj.bore, BoreFlower)
        self.widget.nav_step.setCurrentRow(5)
        self.widget.nav_step.setCurrentRow(7)

        assert isinstance(self.widget.w_step, SLamShape)
        assert self.widget.w_step.g_bore.isChecked()
        assert self.widget.w_step.b_bore.isEnabled()

        # Open again the GUI to check that parameters are correctly set
        self.widget.w_step.b_bore.clicked.emit()
        assert isinstance(self.widget.w_step.bore_win, DBore)
        assert self.widget.w_step.bore_win.w_bore.lf_Rarc.value() == 60e-3
        assert self.widget.w_step.bore_win.w_bore.lf_alpha.value() == 0.39269908 * 2
        assert self.widget.w_step.bore_win.w_bore.si_N.value() == 9
        assert (
            self.widget.w_step.bore_win.w_bore.w_out.out_Rmin.text()
            == "Min Radius: 0.07858 [m]"
        )
        assert (
            self.widget.w_step.bore_win.w_bore.w_out.out_surface.text()
            == "Rotor surface: 0.007946 [m²]"
        )
        self.widget.w_step.bore_win.b_cancel.clicked.emit()

        # Remove the bore shape
        self.widget.w_step.g_bore.setChecked(False)
        assert self.widget.w_step.obj.bore is None

    def test_boresin_addition(self):
        """Checking that the UI allow the definition and the addition to a machine"""

        assert self.widget.machine.name == "Toyota_Prius"
        Rbo = self.widget.machine.rotor.Rext

        # Step 1 : Checking bore groupBox and recovering dialog
        self.widget.nav_step.setCurrentRow(5)  # Stator Shape step
        assert isinstance(self.widget.w_step, SLamShape)
        assert self.widget.w_step.g_bore.isHidden()

        self.widget.nav_step.setCurrentRow(7)  # Rotor Shape step
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_bore.isHidden()
        assert not self.widget.w_step.g_bore.isChecked()
        assert self.widget.w_step.obj.bore is None

        self.widget.w_step.g_bore.setChecked(True)

        assert self.widget.w_step.b_bore.isEnabled()
        self.widget.w_step.b_bore.clicked.emit()

        assert isinstance(self.widget.w_step.bore_win, DBore)

        # Check initial state
        BW = self.widget.w_step.bore_win
        assert BW.c_bore_type.currentText() == "Bore Flower"
        assert isinstance(BW.w_bore, PBoreFlower)
        # select Bore Sin
        BW.c_bore_type.setCurrentIndex(1)
        assert BW.c_bore_type.currentText() == "Bore Sine Pole"
        assert isinstance(BW.w_bore, PBoreSinePole)

        assert BW.w_bore.si_N.value() == 8
        assert BW.w_bore.lf_W0.value() is None
        assert BW.w_bore.lf_k.value() == 1
        assert BW.w_bore.lf_delta_d.value() is None
        assert BW.w_bore.lf_delta_q.value() is None
        assert BW.w_bore.lf_alpha.value() == 0

        # Check set values
        BW.w_bore.si_N.setValue(9)
        BW.w_bore.si_N.editingFinished.emit()
        assert BW.w_bore.bore.N == 9

        BW.w_bore.lf_W0.setValue(30e-3)
        BW.w_bore.lf_W0.editingFinished.emit()
        assert BW.w_bore.bore.W0 == 30e-3

        BW.w_bore.lf_k.setValue(0.5)
        BW.w_bore.lf_k.editingFinished.emit()
        assert BW.w_bore.bore.k == 0.5

        BW.w_bore.lf_delta_d.setValue(5e-3)
        BW.w_bore.lf_delta_d.editingFinished.emit()
        assert BW.w_bore.bore.delta_d == 5e-3

        BW.w_bore.lf_delta_q.setValue(20e-3)
        BW.w_bore.lf_delta_q.editingFinished.emit()
        assert BW.w_bore.bore.delta_q == 20e-3

        assert BW.w_bore.c_alpha_unit.currentText() == "[rad]"
        BW.w_bore.lf_alpha.setValue(1)
        BW.w_bore.lf_alpha.editingFinished.emit()
        assert BW.w_bore.bore.alpha == 1
        BW.w_bore.c_alpha_unit.setCurrentIndex(1)

        assert BW.w_bore.c_alpha_unit.currentText() == "[deg]"
        BW.w_bore.lf_alpha.setValue(45)
        BW.w_bore.lf_alpha.editingFinished.emit()
        assert BW.w_bore.bore.alpha == pytest.approx(0.39269908 * 2, rel=0.1)

        # Checking plot/preview function
        BW.b_plot.clicked.emit()

        # Clicking on OK button
        BW.b_ok.clicked.emit()
        assert isinstance(self.widget.w_step.obj.bore, BoreSinePole)
        self.widget.nav_step.setCurrentRow(5)
        self.widget.nav_step.setCurrentRow(7)

        assert isinstance(self.widget.w_step, SLamShape)
        assert self.widget.w_step.g_bore.isChecked()
        assert self.widget.w_step.b_bore.isEnabled()

        # Open again the GUI to check that parameters are correctly set
        self.widget.w_step.b_bore.clicked.emit()
        BW = self.widget.w_step.bore_win
        assert isinstance(self.widget.w_step.bore_win, DBore)
        assert BW.w_bore.si_N.value() == 9
        assert BW.w_bore.lf_W0.value() == 30e-3
        assert BW.w_bore.lf_k.value() == 0.5
        assert BW.w_bore.lf_delta_d.value() == 5e-3
        assert BW.w_bore.lf_delta_q.value() == 20e-3
        assert BW.w_bore.lf_alpha.value() == pytest.approx(0.39269908 * 2, rel=0.1)
        assert (
            self.widget.w_step.bore_win.w_bore.w_out.out_Rmin.text()
            == "Min Radius: 0.0652 [m]"
        )
        assert (
            self.widget.w_step.bore_win.w_bore.w_out.out_surface.text()
            == "Rotor surface: 0.005424 [m²]"
        )
        self.widget.w_step.bore_win.b_cancel.clicked.emit()

        # Remove the bore shape
        self.widget.w_step.g_bore.setChecked(False)
        assert self.widget.w_step.obj.bore is None


if __name__ == "__main__":
    a = TestBoreAddition()
    a.setup_class()
    a.setup_method()
    a.test_boresin_addition()
    a.teardown_class()
    print("Done")
