# -*- coding: utf-8 -*-

from os.path import join, isfile
from os import remove
import sys
from unittest import TestCase
from ddt import ddt, data

import mock  # for unittest of raw_input
from PyQt5 import QtWidgets

from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.MachineSRM import MachineSRM
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.Tests import save_gui_path as save_path

from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.SMagnet import SMagnet
from pyleecan.GUI.Dialog.DMachineSetup.SWindParam.SWindParam import SWindParam
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMachineSetup.SBar.SBar import SBar
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.SWSlot import SWSlot
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
import matplotlib.pyplot as plt
from pyleecan.Tests import DATA_DIR

load_test = list()
load_test.append(  # 1
    {"type": "SCIM", "index": 0, "name": "SCIM_001", "p": 1, "count": 10}
)
load_test.append(  # 2
    {"type": "DFIM", "index": 1, "name": "DFIM_001", "p": 2, "count": 12}
)
load_test.append(  # 3
    {"type": "SyRM", "index": 2, "name": "SynRM_001", "p": 2, "count": 9}
)
load_test.append(  # 4
    {"type": "SPMSM", "index": 3, "name": "SPMSM_001", "p": 4, "count": 9}
)
load_test.append(  # 5
    {"type": "SIPMSM", "index": 4, "name": "SIPMSM_008", "p": 4, "count": 9}
)
load_test.append(  # 6
    {"type": "IPMSM", "index": 5, "name": "machine_IPMSM_A", "p": 5, "count": 9}
)
load_test.append(  # 7
    {"type": "WRSM", "index": 6, "name": "WRSM_001", "p": 6, "count": 12}
)
load_test.append(  # 8
    {"type": "SRM", "index": 7, "name": "SRM_test_load", "p": 10, "count": 9}
)
from PyQt5.QtCore import Qt

ENABLE_ITEM = Qt.ItemIsSelectable | Qt.ItemIsEnabled


@ddt
class test_DMachineSetup(TestCase):
    """Test that the widget DMachineSetup behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.widget = DMachineSetup(matlib_path="./MaterialData")

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test DMachineSetup")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    @data(*load_test)
    def test_load(self, test_dict):
        """Check that you can load a machine
        """

        return_value = (
            join(join(DATA_DIR, "Load_GUI"), test_dict["name"] + ".json"),
            "Json (*.json)",
        )
        with mock.patch(
            "PyQt5.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            self.widget.b_load.clicked.emit(True)
        # To remember to update when adding a new machine type
        self.assertEqual(self.widget.w_step.c_type.count(), 8)
        # Check load MachineType
        self.assertEqual(type(self.widget.w_step), SMachineType)
        self.assertEqual(self.widget.w_step.c_type.currentIndex(), test_dict["index"])
        self.assertEqual(self.widget.w_step.c_type.currentText(), test_dict["type"])
        self.assertEqual(self.widget.w_step.si_p.value(), test_dict["p"])
        self.assertEqual(self.widget.w_step.le_name.text(), test_dict["name"])
        # Check that the nav_step is correct
        self.assertEqual(self.widget.nav_step.count(), test_dict["count"])

    def test_set_save_machine_type(self):
        """Check that the Widget allow to change the machine type and save
        """
        # Check that all the machine type are available
        self.assertEqual(self.widget.w_step.c_type.count(), 8)
        # DFIM
        self.widget.w_step.c_type.setCurrentIndex(1)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "DFIM")
        self.assertEqual(type(self.widget.machine), MachineDFIM)
        save_function(self, self.widget, "test_dfim_save")
        # SyRM
        self.widget.w_step.c_type.setCurrentIndex(2)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "SyRM")
        self.assertEqual(type(self.widget.machine), MachineSyRM)
        save_function(self, self.widget, "test_syrm_save")
        # SPMSM
        self.widget.w_step.c_type.setCurrentIndex(3)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "SPMSM")
        self.assertEqual(type(self.widget.machine), MachineSIPMSM)
        save_function(self, self.widget, "test_spmsm_save")
        # SIPMSM
        self.widget.w_step.c_type.setCurrentIndex(4)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "SIPMSM")
        self.assertEqual(type(self.widget.machine), MachineSIPMSM)
        save_function(self, self.widget, "test_sipmsm_save")
        # IPMSM
        self.widget.w_step.c_type.setCurrentIndex(5)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "IPMSM")
        self.assertEqual(type(self.widget.machine), MachineIPMSM)
        save_function(self, self.widget, "test_ipmsm_save")
        # WRSM
        self.widget.w_step.c_type.setCurrentIndex(6)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "WRSM")
        self.assertEqual(type(self.widget.machine), MachineWRSM)
        save_function(self, self.widget, "test_wrsm_save")
        # SRM
        self.widget.w_step.c_type.setCurrentIndex(7)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "SRM")
        self.assertEqual(type(self.widget.machine), MachineSRM)
        save_function(self, self.widget, "test_srm_save")
        # SCIM
        self.widget.w_step.c_type.setCurrentIndex(0)
        self.assertEqual(self.widget.w_step.c_type.currentText(), "SCIM")
        self.assertEqual(type(self.widget.machine), MachineSCIM)


def save_function(self, widget, file_name):
    """Function to save a machine from the GUI
    """
    file_path = join(save_path, file_name + ".json")

    # Check that the file didn't already exist
    if isfile(file_path):
        remove(file_path)
    self.assertFalse(isfile(file_path))

    return_value = (file_path, "Json (*.json)")
    with mock.patch(
        "PyQt5.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
    ):
        # To trigger the slot
        widget.b_save.clicked.emit(True)

    # Check that the file now exist => delete for next test
    self.assertTrue(isfile(file_path))
    remove(file_path)
    # Check that the GUI have been updated
    self.assertEqual(type(widget.w_step), SMachineType)
    self.assertEqual(widget.w_step.le_name.text(), file_name)
