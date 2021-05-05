# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest

from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.GUI.Dialog.DMachineSetup.SWinding.SWinding import SWinding
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.SlotW22 import SlotW22

import pytest


class TestSWinding(object):
    """Test that the widget SWinding behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind()
        test_obj.stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.stator.winding = Winding(p=3)
        test_obj.stator.winding.qs = 6
        test_obj.stator.winding.coil_pitch = 8
        test_obj.stator.winding.Nlayer = 9
        test_obj.stator.winding.Nslot_shift_wind = 10
        test_obj.stator.winding.Npcp = 22
        test_obj.stator.winding.is_reverse_wind = True

        widget = SWinding(machine=test_obj, matlib=[], is_stator=True)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""
        assert setup["widget"].in_Zs.text() == "Slot number=36"
        assert setup["widget"].in_p.text() == "Pole pair number=3"
        assert setup["widget"].si_qs.value() == 6
        assert setup["widget"].si_Nlayer.value() == 9
        assert setup["widget"].si_coil_pitch.value() == 8
        assert setup["widget"].si_Nslot.value() == 10
        assert setup["widget"].si_Npcp.value() == 22
        assert setup["widget"].c_wind_type.currentIndex() == 0
        assert setup["widget"].c_wind_type.currentText() == "Star of Slot"
        assert setup["widget"].is_reverse.checkState() == Qt.Checked
        assert setup["widget"].out_shape.text() == "Matrix shape [9, 1, 36, 6]"

        setup["test_obj"] = MachineSCIM()
        setup["test_obj"].stator = LamSlotWind()
        setup["test_obj"].stator.slot = SlotW22(
            Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2
        )
        setup["test_obj"].stator.winding = None
        setup["widget"] = SWinding(machine=setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].c_wind_type.currentIndex() == 0
        assert type(setup["test_obj"].stator.winding) == Winding

        setup["test_obj"] = MachineSCIM()
        setup["test_obj"].stator = LamSlotWind()
        setup["test_obj"].stator.slot = SlotW22(
            Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2
        )
        setup["test_obj"].stator.winding = Winding()
        setup["test_obj"].stator.winding.qs = None
        setup["test_obj"].stator.winding.coil_pitch = None
        setup["test_obj"].stator.winding.Nslot_shift_wind = None
        setup["test_obj"].stator.winding.Ntcoil = None
        setup["test_obj"].stator.winding.is_reverse_wind = None

        setup["widget"] = SWinding(machine=setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_qs.value() == 3
        assert setup["widget"].si_coil_pitch.value() == 0
        assert setup["widget"].si_Nslot.value() == 0
        assert setup["widget"].si_Nlayer.value() == 1
        assert setup["widget"].machine.stator.winding.Ntcoil == 1
        assert not setup["widget"].machine.stator.winding.is_reverse_wind

    def test_set_wind_type(self, setup):
        """Check that the Widget allow to update type_winding"""

        setup["widget"].c_wind_type.setCurrentIndex(1)
        assert type(setup["test_obj"].stator.winding) == WindingUD

        setup["widget"].c_wind_type.setCurrentIndex(0)
        assert type(setup["test_obj"].stator.winding) == Winding

    def test_generate(self, setup):
        """Check that the Widget allow to update qs"""
        setup["widget"].si_qs.setValue(3)
        setup["widget"].si_Nlayer.setValue(2)
        setup["widget"].si_coil_pitch.setValue(5)
        setup["widget"].si_Ntcoil.setValue(9)
        setup["widget"].si_Npcp.setValue(2)

        setup["widget"].b_generate.clicked.emit()
        assert setup["widget"].obj.winding.wind_mat.shape == (2, 1, 36, 3)
        assert setup["widget"].out_shape.text() == "Matrix shape [2, 1, 36, 3]"
        assert setup["widget"].out_ms.text() == "ms = Zs / (2*p*qs) = 2.0"
        assert setup["widget"].out_Nperw.text() == "Nperw: 6"
        assert setup["widget"].out_Ncspc.text() == "Ncspc: 12"
        assert setup["widget"].out_Ntspc.text() == "Ntspc: 108"

    def test_set_is_reverse(self, setup):
        """Check that the Widget allow to update is_reverse_wind"""
        setup["widget"].is_reverse.setCheckState(Qt.Unchecked)
        assert not setup["test_obj"].stator.winding.is_reverse_wind
        setup["widget"].is_reverse.setCheckState(Qt.Checked)
        assert setup["test_obj"].stator.winding.is_reverse_wind

    def test_set_Nslot(self, setup):
        """Check that the Widget allow to update Nslot"""
        setup["widget"].si_Nslot.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(setup["widget"].si_Nslot, str(value))
        setup["widget"].si_Nslot.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.Nslot_shift_wind == value

    def test_set_Npcp(self, setup):
        """Check that the Widget allow to update Npcp"""
        setup["widget"].si_Npcp.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(setup["widget"].si_Npcp, str(value))
        setup["widget"].si_Npcp.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.Npcp == value

    def test_check(self, setup):
        """Check that the check works correctly"""
        rotor = LamSlotWind()
        rotor.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(p=8, qs=None)

        assert "Error in winding matrix gen" in setup["widget"].check(rotor)
