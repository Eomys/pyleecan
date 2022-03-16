# -*- coding: utf-8 -*-

import sys
from random import uniform

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.Classes.HoleM50 import HoleM50


import pytest


class TestSMachineType(object):
    """Test that the widget SMachineType behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSCIM(name="test_machine", type_machine=1)
        test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        test_obj.stator.winding.p = 6
        test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )

        widget = SMachineType(machine=test_obj, material_dict=dict(), is_stator=False)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert setup["widget"].le_name.text() == "test_machine"
        assert setup["widget"].si_p.value() == 6
        assert setup["widget"].c_type.currentIndex() == 0
        assert setup["widget"].c_type.currentText() == "SCIM"
        assert setup["widget"].c_topology.currentText() == "Internal Rotor"

        # DFIM
        setup["test_obj"] = MachineDFIM(name="test_machine_dfim", type_machine=4)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].stator.winding.p = 7
        setup["test_obj"].rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        assert setup["widget"].le_name.text() == "test_machine_dfim"
        assert setup["widget"].si_p.value() == 7
        assert setup["widget"].c_type.currentIndex() == 1
        assert setup["widget"].c_type.currentText() == "DFIM"
        assert setup["widget"].c_topology.currentText() == "External Rotor"

        # SynRM
        setup["test_obj"] = MachineSyRM(name="test_machine_synrm", type_machine=5)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].stator.winding.p = 21
        setup["test_obj"].rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        assert setup["widget"].le_name.text() == "test_machine_synrm"
        assert setup["widget"].si_p.value() == 21
        assert setup["widget"].c_type.currentIndex() == 2
        assert setup["widget"].c_type.currentText() == "SynRM"
        assert setup["widget"].c_topology.currentText() == "External Rotor"

        # SPMSM
        setup["test_obj"] = MachineSIPMSM(name="test_machine_spmsm", type_machine=7)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].stator.winding.p = 9
        setup["test_obj"].rotor = LamSlotMag(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        assert setup["widget"].le_name.text() == "test_machine_spmsm"
        assert setup["widget"].si_p.value() == 9
        assert setup["widget"].c_type.currentIndex() == 3
        assert setup["widget"].c_type.currentText() == "SIPMSM"
        assert setup["widget"].c_topology.currentText() == "Internal Rotor"

        # IPMSM
        setup["test_obj"] = MachineIPMSM(name="test_machine_ipmsm", type_machine=8)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].stator.winding.p = 10
        setup["test_obj"].rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        assert setup["widget"].le_name.text() == "test_machine_ipmsm"
        assert setup["widget"].si_p.value() == 10
        assert setup["widget"].c_type.currentIndex() == 4
        assert setup["widget"].c_type.currentText() == "IPMSM"
        assert setup["widget"].c_topology.currentText() == "External Rotor"

        # WRSM
        setup["test_obj"] = MachineWRSM(name="test_machine_wrsm", type_machine=9)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].stator.winding.p = 5
        setup["test_obj"].rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        assert setup["widget"].le_name.text() == "test_machine_wrsm"
        assert setup["widget"].si_p.value() == 5
        assert setup["widget"].c_type.currentIndex() == 5
        assert setup["widget"].c_type.currentText() == "WRSM"
        assert setup["widget"].c_topology.currentText() == "External Rotor"

    def test_set_name(self, setup):
        """Check that the Widget allow to update name"""
        # Clear the field before writing the new value
        setup["widget"].le_name.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(setup["widget"].le_name, "test_" + str(value))
        setup["widget"].le_name.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].name == "test_" + str(value)

    def test_set_is_inner_rotor(self, setup):
        """Check that the Widget allow to update is_inner_rotor"""
        setup["widget"].c_topology.setCurrentIndex(0)
        assert setup["test_obj"].rotor.is_internal
        setup["widget"].c_topology.setCurrentIndex(1)
        assert not setup["test_obj"].rotor.is_internal

    def test_set_p_scim(self, setup):
        """Check that the Widget allow to update p"""
        # Clear the field before writing the new value
        setup["widget"].si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_p, str(value))
        setup["widget"].si_p.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.p == value
        assert setup["test_obj"].rotor.winding.p == value

    def test_set_p_dfim(self, setup):
        """Check that the Widget allow to update p"""
        setup["test_obj"] = MachineDFIM(name="test_machine_dfim", type_machine=4)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        setup["widget"].si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_p, str(value))
        setup["widget"].si_p.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.p == value
        assert setup["test_obj"].rotor.winding.p == value

    def test_set_p_sipmsm(self, setup):
        """Check that the Widget allow to update p"""
        setup["test_obj"] = MachineSIPMSM(name="test_machine_ipmsm", type_machine=7)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].rotor = LamSlotMag(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        setup["widget"].si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_p, str(value))
        setup["widget"].si_p.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.p == value
        assert setup["test_obj"].rotor.slot.Zs == 2 * value

    def test_set_p_ipmsm(self, setup):
        """Check that the Widget allow to update p"""
        setup["test_obj"] = MachineIPMSM(name="test_machine_ipmsm", type_machine=8)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["test_obj"].rotor.hole = list()
        setup["test_obj"].rotor.hole.append(HoleM50(Zh=0))
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        setup["widget"].si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_p, str(value))
        setup["widget"].si_p.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].stator.winding.p == value
        assert setup["test_obj"].rotor.hole[0].Zh == 2 * value

    def test_set_p_syrm(self, setup):
        """Check that the Widget allow to update p"""
        setup["test_obj"] = MachineSyRM(name="test_machine_ipmsm", type_machine=5)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["test_obj"].rotor.hole = list()
        setup["test_obj"].rotor.hole.append(HoleM50(Zh=0))
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        setup["widget"].si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_p, str(value))
        setup["widget"].si_p.editingFinished.emit()  # To trigger the slot

        assert setup["test_obj"].stator.winding.p == value
        assert setup["test_obj"].rotor.hole[0].Zh == 2 * value

    def test_set_p(self, setup):
        """Check that the Widget allow to update p when Winding is None"""
        setup["test_obj"] = MachineSyRM(name="test_machine_ipmsm", type_machine=5)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22, Ksfill=0.545
        )
        setup["test_obj"].stator.winding = None
        setup["test_obj"].rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        setup["test_obj"].rotor.hole = list()
        setup["test_obj"].rotor.hole.append(HoleM50(Zh=0))
        setup["widget"] = SMachineType(
            machine=setup["test_obj"], material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        setup["widget"].si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_p, str(value))
        setup["widget"].si_p.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].machine.stator.winding.p == value
        assert setup["widget"].machine.stator.winding.is_reverse_wind == None
        assert setup["widget"].machine.stator.winding.Nslot_shift_wind == None
        assert setup["widget"].machine.stator.winding.qs == None
        assert setup["widget"].machine.stator.winding.Ntcoil == None
        assert setup["widget"].machine.stator.winding.Npcp == None
        assert setup["widget"].machine.stator.winding.type_connection == None
        assert setup["widget"].machine.stator.winding.Lewout == None

    @pytest.mark.skip(reason="Need to have DMachineSetup as parent")
    def test_set_type_ipmsm(self, setup):
        """Check that you can define an IPMSM machine"""
        setup["widget"].c_type.setCurrentText("IPMSM")
        # Clear the field before writing the new value
        setup["widget"].si_p.clear()
        value = int(uniform(3, 100))
        QTest.keyClicks(setup["widget"].si_p, str(value))
        setup["widget"].si_p.editingFinished.emit()  # To trigger the slot

        assert setup["widget"].machine.stator.winding.p == value
        assert type(setup["widget"].machine) is MachineIPMSM
        assert setup["widget"].machine.rotor.hole == list()

    # def test_set_c_type(self, setup):
    #     """Check that the Widget allow to update c_type when changing value in the combobox"""
    #     # SIPMSM
    #     setup["test_obj"] = MachineSIPMSM(name="test_machine_sipmsm", type_machine=7)
    #     setup["test_obj"].stator = LamSlotWind(
    #         is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
    #     )
    #     setup["test_obj"].stator.winding.p = 9
    #     setup["test_obj"].rotor = LamSlotMag(
    #         is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
    #     )
    #     setup["widget"] = SMachineType(machine=setup["test_obj"], material_dict=dict(), is_stator=False)

    #     assert setup["widget"].le_name.text() == "test_machine_sipmsm"
    #     assert setup["widget"].si_p.value() == 9
    #     assert setup["widget"].c_type.currentIndex() == 4
    #     assert setup["widget"].c_type.currentText() == "SIPMSM"
    #     assert setup["widget"].is_inner_rotor.checkState() == Qt.Checked

    #     QTest.keyClicks(setup["widget"].c_type, "WRSM")

    #     assert setup["widget"].c_type.currentIndex() == 3
    #     assert setup["widget"].c_type.currentText() == "WRSM"   TODO

    def test_check(self, setup):
        setup["test_obj"] = MachineSyRM(name="test_machine_ipmsm", type_machine=5)
        setup["test_obj"].stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        setup["test_obj"].stator.winding = None

        assert setup["widget"].check(setup["test_obj"]) == "Missing stator winding"
