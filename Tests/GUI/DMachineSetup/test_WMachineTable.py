import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from pyleecan.GUI.Dialog.DMachineSetup.SPreview.WMachineTable.WMachineTable import (
    WMachineTable,
)
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.WindingDW2L import WindingDW2L

import pytest


@pytest.mark.GUI
class TestWMachine_Table(object):
    """Test that the widget WMachine_Table behave like it should"""

    @pytest.fixture
    def setup(self):
        obj = WMachineTable()

        machine = MachineSCIM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        machine.stator.winding = WindingDW2L()
        machine.stator.winding.qs = 6
        machine.stator.winding.coil_pitch = 8
        machine.stator.winding.Nslot_shift_wind = 10
        machine.stator.winding.is_reverse_wind = True

        obj.machine = machine

        return obj

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot27")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_plot_mmf(self, setup):
        """Checking that the plot_mmf can be trigger and works correctly"""
        QTest.mouseClick(setup.b_mmf, Qt.LeftButton)
        assert setup.machine.stator.plot_mmf_unit is not None
