# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWindParam.SWindParam import SWindParam


import pytest


class TestSWindParam(object):
    """Test that the widget SWindParam behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM()
        test_obj.stator = LamSlotWind(is_stator=True)
        test_obj.stator.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.stator.winding = Winding(Npcp=10, Ntcoil=11)

        test_obj.rotor = LamSlotWind(is_stator=False)
        test_obj.rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        test_obj.rotor.winding = Winding(Npcp=20, Ntcoil=21)

        widget = SWindParam(machine=test_obj, matlib=[], is_stator=True)
        widget2 = SWindParam(machine=test_obj, matlib=[], is_stator=False)

        yield {"widget": widget, "widget2": widget2, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].si_Npcp.value() == 10
        assert setup["widget"].si_Ntcoil.value() == 11
        assert setup["widget"].in_Npcp.text() == "Npcp"
        assert setup["widget"].in_Ntcoil.text() == "Ntcoil"
        assert setup["widget"].in_Zs.text() == "Zs: 36"
        assert setup["widget"].in_qs.text() == "qs: 3"
        assert setup["widget"].out_Ncspc.text() == "Ncspc: ?"
        assert setup["widget"].out_Ntspc.text() == "Ntspc: ?"

        assert setup["widget2"].si_Npcp.value() == 20
        assert setup["widget2"].si_Ntcoil.value() == 21
        assert setup["widget2"].in_Npcp.text() == "Npcp"
        assert setup["widget2"].in_Ntcoil.text() == "Ntcoil"
        assert setup["widget2"].in_Zs.text() == "Zs: 36"
        assert setup["widget2"].in_qs.text() == "qs: 3"
        assert setup["widget2"].out_Ncspc.text() == "Ncspc: ?"
        assert setup["widget2"].out_Ntspc.text() == "Ntspc: ?"
        setup["test_obj"] = MachineSCIM()
        setup["test_obj"].rotor = LamSlotWind(is_stator=False)
        setup["test_obj"].rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        setup["test_obj"].rotor.winding = Winding(Npcp=20, Ntcoil=None)

        setup["test_obj"].type_machine = 9

        setup["widget2"] = SWindParam(
            machine=setup["test_obj"], matlib=[], is_stator=False
        )

        assert setup["widget2"].in_Zs.isHidden()
        assert setup["widget2"].in_Nlay.isHidden()

    def test_set_Npcp1(self, setup):
        """Check that the Widget allow to update Npcp1"""
        # Clear the field before writing the new value
        setup["widget"].si_Npcp.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(setup["widget"].si_Npcp, str(value))
        setup["widget"].si_Npcp.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.Npcp == value

    def test_set_Npcp2(self, setup):
        """Check that the Widget allow to update Npcp2"""
        # Clear the field before writing the new value
        setup["widget2"].si_Npcp.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(setup["widget2"].si_Npcp, str(value))
        setup["widget2"].si_Npcp.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.Npcp == value

    def test_set_Ntcoil1(self, setup):
        """Check that the Widget allow to update Ntcoil1"""
        # Clear the field before writing the new value
        setup["widget"].si_Ntcoil.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(setup["widget"].si_Ntcoil, str(value))
        setup["widget"].si_Ntcoil.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.Ntcoil == value

    def test_set_Ntcoil2(self, setup):
        """Check that the Widget allow to update Ntcoil2"""
        # Clear the field before writing the new value
        setup["widget2"].si_Ntcoil.clear()
        value = int(uniform(5, 100))
        QTest.keyClicks(setup["widget2"].si_Ntcoil, str(value))
        setup["widget2"].si_Ntcoil.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].rotor.winding.Ntcoil == value

    def test_check(self, setup):
        """Check that the check method return errors"""
        rotor = LamSlotWind(is_stator=False)
        rotor.winding = None
        assert rotor.comp_fill_factor() == 0

        rotor.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)
        rotor.winding = Winding(Npcp=20, Ntcoil=None)

        assert setup["widget"].check(rotor) == "You must set Ntcoil !"
