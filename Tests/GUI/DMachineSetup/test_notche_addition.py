from PySide2 import QtWidgets
from os.path import join, isfile
from os import remove
import mock
import sys
import logging
from numpy import pi
from numpy.testing import assert_almost_equal

from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotCirc import SlotCirc
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

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)


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

    def test_notch_addition(self):
        """Checking that the UI allow the definition and the addition to a machine"""

        assert self.widget.machine.name == "Toyota_Prius"

        # Step 1 : Checking notch groupBox and recovering dialog
        self.widget.nav_step.setCurrentRow(5)
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Step 1-1 : Adding first notch (rectangular)
        assert self.widget.w_step.notches_win.tab_notch.count() == 1

        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        assert notche_wid.c_notch_type.currentIndex() == 0

        Zn = 48 // 4
        notche_wid.si_Zn.setValue(Zn)
        notche_wid.si_Zn.editingFinished.emit()
        assert notche_wid.si_Zn.value() == Zn

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

        # Checking that we set alpha to None, then the value is set back to 0
        notche_wid.lf_alpha.setValue(None)
        notche_wid.lf_alpha.editingFinished.emit()
        assert notche_wid.lf_alpha.value() == 0

        # Step 1-2 : Adding second notch (circular)
        self.widget.w_step.notches_win.b_add.clicked.emit()
        assert self.widget.w_step.notches_win.tab_notch.count() == 2

        self.widget.w_step.notches_win.tab_notch.setCurrentIndex(1)
        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        notche_wid.c_notch_type.setCurrentIndex(2)
        assert notche_wid.c_notch_type.currentIndex() == 2

        Zn = 48 // 4
        notche_wid.si_Zn.setValue(Zn)
        notche_wid.si_Zn.editingFinished.emit()
        assert notche_wid.si_Zn.value() == Zn

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
        assert notche_wid.err_msg == None
        self.widget.w_step.notches_win.b_plot.clicked.emit()
        assert self.widget.w_step.notches_win.err_msg == None

        # Step 1-3 : Adding third notch with dimensions equal to 0
        self.widget.w_step.notches_win.b_add.clicked.emit()
        assert self.widget.w_step.notches_win.tab_notch.count() == 3

        self.widget.w_step.notches_win.tab_notch.setCurrentIndex(2)
        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        notche_wid.c_notch_type.setCurrentIndex(2)
        assert notche_wid.c_notch_type.currentIndex() == 2

        Zn = 48 // 4
        notche_wid.si_Zn.setValue(Zn)
        notche_wid.si_Zn.editingFinished.emit()
        assert notche_wid.si_Zn.value() == Zn

        alpha = 15
        notche_wid.c_alpha_unit.setCurrentIndex(1)
        notche_wid.lf_alpha.setValue(alpha)
        notche_wid.lf_alpha.editingFinished.emit()
        assert notche_wid.c_alpha_unit.currentIndex() == 1
        assert notche_wid.lf_alpha.value() == alpha

        H0 = 0
        W0 = 0
        assert isinstance(notche_wid.w_notch, WSlotCirc)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == H0
        notche_wid.w_notch.lf_H0.editingFinished.emit()
        assert notche_wid.w_notch.lf_W0.value() == W0
        notche_wid.w_notch.lf_W0.editingFinished.emit()

        # Checking that we detect that the dimensions are null
        assert notche_wid.check() == "W0 must be higher than 0"

        W0 = 2e-3
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_W0.value() == W0
        notche_wid.w_notch.lf_W0.editingFinished.emit()

        assert notche_wid.check() == "H0 must be higher than 0"

        # Removing the notches with null dimensions
        self.widget.w_step.notches_win.b_remove.clicked.emit()
        assert self.widget.w_step.notches_win.tab_notch.count() == 2

        # Clicking on OK button
        self.widget.w_step.notches_win.b_ok.clicked.emit()

        # Step 1-3 : Making sure that the groupBox and the widget are updated according to the new stator (with notches)
        self.widget.nav_step.setCurrentRow(7)
        self.widget.nav_step.setCurrentRow(5)

        assert isinstance(self.widget.w_step, SLamShape)
        assert self.widget.w_step.g_notches.isChecked()
        assert self.widget.w_step.b_notch.isEnabled()

        assert self.widget.w_step.out_notch.text() == "2 set (24 notches)"

        self.widget.w_step.b_notch.clicked.emit()
        assert isinstance(self.widget.w_step.notches_win, DNotchTab)
        assert self.widget.w_step.notches_win.tab_notch.count() == 2
        self.widget.w_step.notches_win.b_cancel.clicked.emit()

        # Step 2 : Adding notches on the rotor (polar)
        self.widget.nav_step.setCurrentRow(7)

        # Enabling notch on rotor
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Step 2-1 : Adding polar notches on the rotor
        assert self.widget.w_step.notches_win.tab_notch.count() == 1

        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        assert notche_wid.c_notch_type.currentIndex() == 0
        notche_wid.c_notch_type.setCurrentIndex(1)

        Zn = 8
        notche_wid.si_Zn.setValue(Zn)
        notche_wid.si_Zn.editingFinished.emit()
        assert notche_wid.si_Zn.value() == Zn

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
        assert notche_wid.err_msg == None
        self.widget.w_step.notches_win.b_plot.clicked.emit()
        assert self.widget.w_step.notches_win.err_msg == None

        # Clicking on OK button
        self.widget.w_step.notches_win.b_ok.clicked.emit()

        # Step 2-2 : Making sure that the groupBox and the widget are updated according to the new stator (with notches)
        self.widget.nav_step.setCurrentRow(5)
        self.widget.nav_step.setCurrentRow(7)

        assert isinstance(self.widget.w_step, SLamShape)
        assert self.widget.w_step.g_notches.isChecked()
        assert self.widget.w_step.b_notch.isEnabled()

        assert self.widget.w_step.out_notch.text() == "1 set (8 notches)"

        self.widget.w_step.b_notch.clicked.emit()
        assert isinstance(self.widget.w_step.notches_win, DNotchTab)
        assert self.widget.w_step.notches_win.tab_notch.count() == 1
        self.widget.w_step.notches_win.b_cancel.clicked.emit()

        # Step 3 : Making sure that the notches are added on the machine
        assert len(self.widget.machine.stator.notch) == 2
        assert isinstance(self.widget.machine.stator.notch[0].notch_shape, SlotM10)
        assert isinstance(self.widget.machine.stator.notch[1].notch_shape, SlotCirc)

        assert len(self.widget.machine.rotor.notch) == 1
        assert isinstance(self.widget.machine.rotor.notch[0].notch_shape, SlotM11)

        # Step 4 : Saving the machine with notches
        # Making sure that the updated machine was saved
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

        self.widget.close()

        # Check that the file now exist => delete for next test
        assert isfile(file_path)
        remove(file_path)
        assert not isfile(file_path)

    def test_cancel_button(self):
        """Checking that when clicking on cancel button, the machine is not update (no new notches added)"""

        assert self.widget.machine.name == "Toyota_Prius"
        assert self.widget.machine.stator.notch in [list(), None]

        # Step 1 : Checking notch groupBox and recovering dialog
        self.widget.nav_step.setCurrentRow(5)
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Step 2: Adding notch (rectangular)
        assert self.widget.w_step.notches_win.tab_notch.count() == 1

        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        assert notche_wid.c_notch_type.currentIndex() == 0

        Zn = 48 // 4
        notche_wid.si_Zn.setValue(Zn)
        notche_wid.si_Zn.editingFinished.emit()
        assert notche_wid.si_Zn.value() == Zn

        H0 = 2e-3
        W0 = 4e-3
        assert isinstance(notche_wid.w_notch, PMSlot10)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == H0
        notche_wid.w_notch.lf_H0.editingFinished.emit()
        assert notche_wid.w_notch.lf_W0.value() == W0
        notche_wid.w_notch.lf_W0.editingFinished.emit()

        # Step 3 : Clicking on cancel button
        self.widget.w_step.notches_win.b_cancel.clicked.emit()

        assert self.widget.machine.stator.notch in [list(), None]

        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.question",
            return_value=QtWidgets.QMessageBox.No,
        ):
            self.widget.close()

    def test_notch_addition_without_input(self):
        """Checking that if the UI is not completely defined, then we can not add a notch and a error message is shown"""
        assert self.widget.machine.name == "Toyota_Prius"

        # Step 1 : Checking notch groupBox and recovering dialog
        self.widget.nav_step.setCurrentRow(5)
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Step 1-1 : Adding first notch (rectangular)
        assert self.widget.w_step.notches_win.tab_notch.count() == 1

        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        assert notche_wid.c_notch_type.currentIndex() == 0

        assert notche_wid.si_Zn.value() == 48
        assert notche_wid.w_notch.lf_H0.value() == None
        assert notche_wid.w_notch.lf_W0.value() == None

        # Detecting that an error is raised after clicking on preview of DNotchTab
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.w_step.notches_win.b_plot.clicked.emit()

        assert (
            self.widget.w_step.notches_win.err_msg
            == "Error in Notch definition:\nNotch 1: You must set W0 !"
        )

        # Detecting that an error is raised after clicking on preview of WNotch
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            notche_wid.b_plot.clicked.emit()

        assert notche_wid.err_msg == "Unable to generate a preview:\nYou must set W0 !"

        # Detecting that an error is raised after clicking on ok button of DNotchTab
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.w_step.notches_win.b_ok.clicked.emit()

        assert (
            self.widget.w_step.notches_win.err_msg
            == "Error in Notch definition:\nNotch 1: You must set W0 !"
        )

        self.widget.w_step.notches_win.b_cancel.clicked.emit()

        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.question",
            return_value=QtWidgets.QMessageBox.No,
        ):
            self.widget.close()

    def test_notch_addition_wrong_input(self):
        """Checking that if the UI is wrongly defined, then we can not add a notch and a error message is shown"""
        assert self.widget.machine.name == "Toyota_Prius"

        # Step 1 : Checking notch groupBox and recovering dialog
        self.widget.nav_step.setCurrentRow(5)
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Step 1-1 : Adding first notch (rectangular)
        assert self.widget.w_step.notches_win.tab_notch.count() == 1

        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        assert notche_wid.c_notch_type.currentIndex() == 0

        assert notche_wid.si_Zn.value() == 48
        H0 = 5e-3
        W0 = 10e-3
        assert isinstance(notche_wid.w_notch, PMSlot10)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == H0
        notche_wid.w_notch.lf_H0.editingFinished.emit()
        assert notche_wid.w_notch.lf_W0.value() == W0
        notche_wid.w_notch.lf_W0.editingFinished.emit()

        # Detecting that an error is raised after clicking on preview of DNotchTab
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.w_step.notches_win.b_plot.clicked.emit()

        assert (
            self.widget.w_step.notches_win.err_msg
            == "Error while plotting Lamination in Notch definition:\nNotches and/or Slots are colliding"
        )

        # Detecting that an error is raised after clicking on ok button of DNotchTab
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.w_step.notches_win.b_ok.clicked.emit()

        assert (
            self.widget.w_step.notches_win.err_msg
            == "Error in Notch definition:\nNotches and/or Slots are colliding"
        )

        self.widget.w_step.notches_win.b_cancel.clicked.emit()

        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.question",
            return_value=QtWidgets.QMessageBox.No,
        ):
            self.widget.close()

    def test_set_empty_floatedit(self):
        """Test that if we set "" in one of the floatEdit then the value returned is None"""
        assert self.widget.machine.name == "Toyota_Prius"

        # Step 1 : Checking notch groupBox and recovering dialog
        self.widget.nav_step.setCurrentRow(5)
        assert isinstance(self.widget.w_step, SLamShape)
        assert not self.widget.w_step.g_notches.isChecked()

        self.widget.w_step.g_notches.setChecked(True)

        assert self.widget.w_step.b_notch.isEnabled()
        self.widget.w_step.b_notch.clicked.emit()

        assert isinstance(self.widget.w_step.notches_win, DNotchTab)

        # Adding  notch (rectangular)
        assert self.widget.w_step.notches_win.tab_notch.count() == 1
        notche_wid = self.widget.w_step.notches_win.tab_notch.currentWidget()
        assert isinstance(notche_wid, WNotch)

        H0 = ""
        W0 = ""
        assert notche_wid.c_notch_type.currentIndex() == 0
        assert isinstance(notche_wid.w_notch, PMSlot10)
        notche_wid.w_notch.lf_H0.setValue(H0)
        notche_wid.w_notch.lf_W0.setValue(W0)
        assert notche_wid.w_notch.lf_H0.value() == None
        notche_wid.w_notch.lf_H0.editingFinished.emit()
        assert notche_wid.w_notch.lf_W0.value() == None
        notche_wid.w_notch.lf_W0.editingFinished.emit()

        self.widget.w_step.notches_win.b_cancel.clicked.emit()
        with mock.patch(
            "PySide2.QtWidgets.QMessageBox.question",
            return_value=QtWidgets.QMessageBox.No,
        ):
            self.widget.close()


if __name__ == "__main__":
    a = TestNotcheAddition()
    a.setup_class()
    a.setup_method()
    a.test_notch_addition()
    # a.test_cancel_button()
    # a.test_notch_addition_without_input()
    # a.test_notch_addition_wrong_input()
    # a.test_set_empty_floatedit()
    a.teardown_class()
    print("Done")
