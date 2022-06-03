from PySide2 import QtWidgets
from os.path import join, isfile
import mock
import sys
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMachineSetup.DNotchTab.DNotchTab import DNotchTab
from pyleecan.GUI.Dialog.DMachineSetup.DNotchTab.WNotch.WNotch import WNotch
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from pyleecan.Functions.load import load_matlib
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.SLamShape import SLamShape
from pyleecan.definitions import DATA_DIR
from Tests import TEST_DATA_DIR

matlib_path = join(TEST_DATA_DIR, "Material")


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
            material_dict=material_dict, machine_path=join(TEST_DATA_DIR, "Machine")
        )

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_adding_notch(self):
        """Checking that the UI allow the definition and the addition to a machine"""

        # Loading Prius machine
        return_value = (
            join(DATA_DIR, "Machine", "Toyota_Prius.json"),
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
        assert notche_wid.si_Zs.value() == Zs

        H0 = 20e-3
        W0 = 45e-3
        assert isinstance(notche_wid.w_notch, PMSlot10)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == H0
        assert notche_wid.w_notch.lf_W0.value() == W0

        # Checking plot/preview function
        self.widget.w_step.notches_win.b_plot.clicked.emit()

        # Adding second notch (circular)

        # Checking plot/preview function

        # Clicking on OK then selecting rotor lamination tab
        self.widget.nav_step.setCurrentRow(7)
        # Enabling notch on rotor

        # Adding first notch polar

        # checking preview/plot function

        # Clicking on OK then saving the machine

        # Making sure that the machine was updated


if __name__ == "__main__":
    a = TestNotcheAddition()
    a.setup_class()
    a.setup_method()
    a.test_adding_notch()
    print("Done")
