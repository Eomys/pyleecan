from PySide2 import QtWidgets
from os.path import join, isfile
from os import remove
import mock
import sys
from numpy import pi
from numpy.testing import assert_almost_equal

from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.DNotchTab.DNotchTab import DNotchTab
from pyleecan.GUI.Dialog.DMachineSetup.DNotchTab.WNotch.WNotch import WNotch
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.WSlotCirc.WSlotCirc import WSlotCirc
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape
from Tests import save_gui_path as save_path

matlib_path = join(DATA_DIR, "Material")
machine_name = "Toyota_Prius"


class TestNotcheAddition(object):
    """Test that the widget DMachineSetup behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestDMachineSetup")
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

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_notch_addition(self):
        """Checking that the UI allow the definition and the addition to a machine"""

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

        assert self.widget.machine.name == "Toyota_Prius"

        # Checking notch and recovering dialog
        self.widget.nav_step.setCurrentRow(5)
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Adding first notch (rectangular)
        assert self.widget.w_step.notches_win.tab_notch.count() == 1

        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        assert notche_wid.c_notch_type.currentIndex() == 0

        Zs = 48 // 4
        notche_wid.si_Zs.setValue(Zs)
        notche_wid.si_Zs.editingFinished.emit()
        assert notche_wid.si_Zs.value() == Zs

        H0 = 2e-3
        W0 = 4e-3
        assert isinstance(notche_wid.w_notch, PMSlot10)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == H0
        notche_wid.w_notch.lf_H0.editingFinished.emit()
        assert notche_wid.w_notch.lf_W0.value() == W0
        notche_wid.w_notch.lf_W0.editingFinished.emit()
        # Checking plot/preview function
        notche_wid.b_plot.clicked.emit()
        self.widget.w_step.notches_win.b_plot.clicked.emit()

        # Adding second notch (circular)
        self.widget.w_step.notches_win.b_add.clicked.emit()
        assert self.widget.w_step.notches_win.tab_notch.count() == 2

        self.widget.w_step.notches_win.tab_notch.setCurrentIndex(1)
        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        notche_wid.c_notch_type.setCurrentIndex(2)
        assert notche_wid.c_notch_type.currentIndex() == 2

        Zs = 48 // 4
        notche_wid.si_Zs.setValue(Zs)
        notche_wid.si_Zs.editingFinished.emit()
        assert notche_wid.si_Zs.value() == Zs

        alpha = 15
        notche_wid.c_alpha_unit.setCurrentIndex(1)
        notche_wid.lf_alpha.setValue(alpha)
        notche_wid.lf_alpha.editingFinished.emit()
        assert notche_wid.c_alpha_unit.currentIndex() == 1
        assert notche_wid.lf_alpha.value() == alpha

        H0 = 2e-3
        W0 = 4e-3
        assert isinstance(notche_wid.w_notch, WSlotCirc)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == H0
        notche_wid.w_notch.lf_H0.editingFinished.emit()
        assert notche_wid.w_notch.lf_W0.value() == W0
        notche_wid.w_notch.lf_W0.editingFinished.emit()

        # Checking plot/preview function
        notche_wid.b_plot.clicked.emit()
        self.widget.w_step.notches_win.b_plot.clicked.emit()

        self.widget.w_step.notches_win.b_ok.clicked.emit()

        # Clicking on OK then selecting rotor lamination tab
        self.widget.nav_step.setCurrentRow(7)

        # Enabling notch on rotor
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Adding first notch polar
        assert self.widget.w_step.notches_win.tab_notch.count() == 1

        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        assert notche_wid.c_notch_type.currentIndex() == 0
        notche_wid.c_notch_type.setCurrentIndex(1)

        Zs = 8
        notche_wid.si_Zs.setValue(Zs)
        notche_wid.si_Zs.editingFinished.emit()
        assert notche_wid.si_Zs.value() == Zs

        H0 = 2e-3
        W0 = pi / 24
        assert isinstance(notche_wid.w_notch, PMSlot11)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == H0
        notche_wid.w_notch.lf_H0.editingFinished.emit()
        assert_almost_equal(notche_wid.w_notch.lf_W0.value(), W0)
        notche_wid.w_notch.lf_W0.editingFinished.emit()
        # Checking plot/preview function
        notche_wid.b_plot.clicked.emit()
        self.widget.w_step.notches_win.b_plot.clicked.emit()

        # Clicking on OK then saving the machine
        self.widget.w_step.notches_win.b_ok.clicked.emit()

        # Making sure that the machine was updated
        file_path = join(save_path, machine_name + ".json")

        # Check that the file didn't already exist
        if isfile(file_path):
            remove(file_path)
        assert not isfile(file_path)

        return_value = (file_path, "Json (*.json)")
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.b_save.clicked.emit()

        # Check that the file now exist => delete for next test
        assert isfile(file_path)
        remove(file_path)
        assert not isfile(file_path)
        # Check that the GUI have been updated
        self.widget.nav_step.setCurrentRow(0)
        assert type(self.widget.w_step) == SMachineType
        assert self.widget.w_step.le_name.text() == machine_name


if __name__ == "__main__":
    a = TestNotcheAddition()
    a.setup_class()
    a.setup_method()
    a.test_notch_addition()
    print("Done")
