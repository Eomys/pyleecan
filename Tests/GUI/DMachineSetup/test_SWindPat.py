# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest

from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.WindingCW2LR import WindingCW2LR
from pyleecan.Classes.WindingSC import WindingSC

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWindPat.SWindPat import SWindPat

import pytest


@pytest.mark.GUI
class TestSWindPat(object):
    """Test that the widget SWindPat behave like it should"""

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
        test_obj.stator.winding = WindingDW2L()
        test_obj.stator.winding.qs = 6
        test_obj.stator.winding.coil_pitch = 8
        test_obj.stator.winding.Nslot_shift_wind = 10
        test_obj.stator.winding.is_reverse_wind = True

        widget = SWindPat(machine=test_obj, matlib=[], is_stator=True)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].si_qs.value() == 6
        assert setup["widget"].si_coil_pitch.value() == 8
        assert setup["widget"].si_Nslot.value() == 10
        assert setup["widget"].c_wind_type.currentIndex() == 2
        assert setup["widget"].is_reverse.checkState() == Qt.Checked
        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [2, 1, 36, 6]"

        setup["test_obj"] = MachineSCIM()
        setup["test_obj"].stator = LamSlotWind()
        setup["test_obj"].stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].stator.winding = None
        setup["widget"] = SWindPat(machine=setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].c_wind_type.currentIndex() == 0
        assert type(setup["test_obj"].stator.winding) == WindingCW2LT

        setup["test_obj"] = MachineSCIM()
        setup["test_obj"].stator = LamSlotWind()
        setup["test_obj"].stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].stator.winding = WindingDW2L()
        setup["test_obj"].stator.winding.qs = None
        setup["test_obj"].stator.winding.coil_pitch = None
        setup["test_obj"].stator.winding.Nslot_shift_wind = None
        setup["test_obj"].stator.winding.Ntcoil = None
        setup["test_obj"].stator.winding.is_reverse_wind = None

        setup["widget"] = SWindPat(machine=setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].si_qs.value() == 3
        assert setup["widget"].si_coil_pitch.value() == 0
        assert setup["widget"].si_Nslot.value() == 0
        assert setup["widget"].machine.stator.winding.Ntcoil == 1
        assert not setup["widget"].machine.stator.winding.is_reverse_wind

        setup["test_obj"] = MachineSCIM()
        setup["test_obj"].stator = LamSlotWind()
        setup["test_obj"].stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding = Winding(p=8, qs=None)

        setup["widget"] = SWindPat(machine=setup["test_obj"], matlib=[], is_stator=True)

        assert setup["widget"].c_wind_type.currentIndex() == 0
        assert type(setup["test_obj"].stator.winding) == WindingCW2LT

    def test_init_WRSM(self, setup):
        """Check that the GUI is correctly initialize with a WRSM machine"""
        setup["test_obj"] = MachineWRSM(type_machine=9)

        setup["test_obj"].stator = LamSlotWind()
        setup["test_obj"].stator.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].stator.winding = WindingDW2L(p=8, qs=4)

        setup["test_obj"].rotor = LamSlotWind()
        setup["test_obj"].rotor.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding = Winding(p=8, qs=4)

        setup["widget"] = SWindPat(machine=setup["test_obj"], matlib=[], is_stator=True)
        setup["widget2"] = SWindPat(machine=setup["test_obj"], matlib=[], is_stator=False)

        # Check result stator
        assert type(setup["test_obj"].stator.winding) == WindingDW2L
        assert setup["test_obj"].stator.winding.p == 8
        assert setup["test_obj"].stator.winding.qs == 4
        assert setup["widget"].si_qs.isEnabled() == True
        assert setup["widget"].si_coil_pitch.isHidden() == False
        assert setup["widget"].si_Nslot.value() == 0
        assert setup["widget"].c_wind_type.currentIndex() == 2
        assert setup["widget"].c_wind_type.currentText() == "Double Layer Distributed"
        assert setup["widget"].is_reverse.checkState() == Qt.Unchecked
        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [2, 1, 36, 4]"
        # check result rotor
        assert type(setup["test_obj"].rotor.winding) == WindingCW2LT
        assert setup["test_obj"].rotor.winding.p == 8
        assert setup["test_obj"].rotor.winding.qs == 1
        assert setup["widget2"].si_qs.value() == 1
        assert setup["widget2"].si_qs.isEnabled() == False
        assert setup["widget2"].si_coil_pitch.isHidden() == True
        assert setup["widget2"].si_Nslot.value() == 0
        assert setup["widget2"].c_wind_type.currentIndex() == 0
        assert (
            setup["widget2"].c_wind_type.currentText()
            == "DC wound winding for salient pole"
        )
        assert setup["widget2"].is_reverse.checkState() == Qt.Unchecked
        assert setup["widget2"].out_shape.text() == "Winding Matrix shape: [1, 2, 36, 1]"

    def test_set_wind_type(self, setup):
        """Check that the Widget allow to update type_winding"""
        setup["widget"].c_wind_type.setCurrentIndex(0)
        assert type(setup["test_obj"].stator.winding) == WindingCW2LT
        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [1, 2, 36, 6]"

        setup["widget"].c_wind_type.setCurrentIndex(1)
        assert type(setup["test_obj"].stator.winding) == WindingCW1L
        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [1, 1, 36, 6]"

        setup["widget"].c_wind_type.setCurrentIndex(2)
        assert type(setup["test_obj"].stator.winding) == WindingDW2L
        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [2, 1, 36, 6]"

        setup["widget"].c_wind_type.setCurrentIndex(3)
        assert type(setup["test_obj"].stator.winding) == WindingDW1L
        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [1, 1, 36, 6]"

        setup["widget"].c_wind_type.setCurrentIndex(4)
        assert type(setup["test_obj"].stator.winding) == WindingCW2LR
        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [2, 1, 36, 6]"

    def test_set_qs(self, setup):
        """Check that the Widget allow to update qs"""
        setup["widget"].si_qs.clear()  # Clear the field before writing
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_qs, str(value))
        setup["widget"].si_qs.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.qs == value
        assert (
            setup["widget"].out_shape.text()
            == "Winding Matrix shape: [2, 1, 36, " + str(value) + "]"
        )

    def test_set_is_reverse(self, setup):
        """Check that the Widget allow to update is_reverse_wind"""
        setup["widget"].is_reverse.setCheckState(Qt.Unchecked)
        assert not setup["test_obj"].stator.winding.is_reverse_wind
        setup["widget"].is_reverse.setCheckState(Qt.Checked)
        assert setup["test_obj"].stator.winding.is_reverse_wind

    def test_set_coil_pitch(self, setup):
        """Check that the Widget allow to update coil_pitch"""
        setup["widget"].si_coil_pitch.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(setup["widget"].si_coil_pitch, str(value))
        setup["widget"].si_coil_pitch.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.coil_pitch == value

    def test_set_Nslot(self, setup):
        """Check that the Widget allow to update Nslot"""
        setup["widget"].si_Nslot.clear()  # Clear the field before writing
        value = int(uniform(0, 100))
        QTest.keyClicks(setup["widget"].si_Nslot, str(value))
        setup["widget"].si_Nslot.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.Nslot_shift_wind == value

    def test_set_output(self, setup):
        """Check that the set_output works correctly"""
        setup["test_obj"].rotor = LamSlotWind()
        setup["test_obj"].rotor.slot = SlotW22(Zs=None, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding = Winding(p=8, qs=None)
        setup["widget"] = SWindPat(machine=setup["test_obj"], matlib=[], is_stator=False)

        assert setup["widget"].out_shape.text() == "Winding Matrix shape: [1, 2, ?, 3]"
        assert setup["widget"].out_ms.text() == "ms = Zs / (2*p*qs) = ?"

    def test_check(self, setup):
        """Check that the check works correctly"""
        rotor = LamSlotWind()
        rotor.slot = SlotW22(Zs=36, H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(p=8, qs=None)

        assert setup["widget"].check(rotor) == "You must set qs !"
