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
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.DBore.DBore import DBore
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

    def test_bore_addition(self):
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
        assert BW.w_bore.lf_Rarc.value() == pytest.approx(68.17 *1e-3, rel=0.1)
        assert BW.w_bore.lf_alpha.value() == pytest.approx(0.39269908, rel=0.1)

        # Check set values
        BW.w_bore.lf_Rarc.setValue(60e-3)
        BW.w_bore.lf_Rarc.editingFinished.emit()
        assert BW.w_bore.bore.Rarc == 60e-3

        assert BW.w_bore.c_alpha_unit.currentText() == "[rad]"
        BW.w_bore.lf_alpha.setValue(1)
        BW.w_bore.lf_alpha.editingFinished.emit()
        assert BW.w_bore.bore.alpha == 1
        BW.w_bore.c_alpha_unit.setCurrentIndex(1)

        assert BW.w_bore.c_alpha_unit.currentText() == "[deg]"
        BW.w_bore.lf_alpha.setValue(45)
        BW.w_bore.lf_alpha.editingFinished.emit()
        assert BW.w_bore.bore.alpha == pytest.approx(0.39269908*2, rel=0.1)

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
        assert self.widget.w_step.bore_win.w_bore.lf_alpha.value() == 0.39269908*2
        assert self.widget.w_step.bore_win.w_bore.w_out.out_Rmin.text() == "Min Radius: 0.07816 [m]"
        assert self.widget.w_step.bore_win.w_bore.w_out.out_surface.text() == "Rotor surface: 0.007876 [m²]"
        self.widget.w_step.bore_win.b_cancel.clicked.emit()

        # Remove the bore shape
        self.widget.w_step.g_bore.setChecked(False)
        assert self.widget.w_step.obj.bore is None


if __name__ == "__main__":
    a = TestBoreAddition()
    a.setup_class()
    a.setup_method()
    a.test_bore_addition()
    a.teardown_class()
    print("Done")
