# -*- coding: utf-8 -*-

import sys
from random import uniform

import pytest
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest

from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType


class TestSMachineType(object):
    """Test that the widget SMachineType behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Create widget before each test"""
        self.test_obj = MachineSCIM(name="test_machine", type_machine=1)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 6
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )

        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    @pytest.mark.SCIM
    @pytest.mark.IPMSM
    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.le_name.text() == "test_machine"
        assert self.widget.si_p.value() == 6
        assert self.widget.c_type.currentIndex() == 0
        assert self.widget.c_type.currentText() == "SCIM"
        assert self.widget.c_topology.currentText() == "Internal Rotor"

        # DFIM
        self.test_obj = MachineDFIM(name="test_machine_dfim", type_machine=4)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 7
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        assert self.widget.le_name.text() == "test_machine_dfim"
        assert self.widget.si_p.value() == 7
        assert self.widget.c_type.currentIndex() == 1
        assert self.widget.c_type.currentText() == "DFIM"
        assert self.widget.c_topology.currentText() == "External Rotor"

        # SynRM
        self.test_obj = MachineSyRM(name="test_machine_synrm", type_machine=5)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 21
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        assert self.widget.le_name.text() == "test_machine_synrm"
        assert self.widget.si_p.value() == 21
        assert self.widget.c_type.currentIndex() == 2
        assert self.widget.c_type.currentText() == "SynRM"
        assert self.widget.c_topology.currentText() == "External Rotor"

        # SPMSM
        self.test_obj = MachineSIPMSM(name="test_machine_spmsm", type_machine=7)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 9
        self.test_obj.rotor = LamSlotMag(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        assert self.widget.le_name.text() == "test_machine_spmsm"
        assert self.widget.si_p.value() == 9
        assert self.widget.c_type.currentText() == "SPMSM"
        assert self.widget.c_topology.currentText() == "Internal Rotor"
        assert (
            self.widget.in_machine_desc.placeholderText()
            == "SPMSM (Surface Permanent Magnet Synchronous Machine)"
        )

        # IPMSM
        self.test_obj = MachineIPMSM(name="test_machine_ipmsm", type_machine=8)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 10
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        assert self.widget.le_name.text() == "test_machine_ipmsm"
        assert self.widget.si_p.value() == 10
        assert self.widget.c_type.currentText() == "IPMSM"
        assert self.widget.c_topology.currentText() == "External Rotor"
        assert (
            self.widget.in_machine_desc.placeholderText()
            == "IPMSM (Interior Permanent Magnet Synchronous Machine)"
        )

        # WRSM
        self.test_obj = MachineWRSM(name="test_machine_wrsm", type_machine=9)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 5
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        assert self.widget.le_name.text() == "test_machine_wrsm"
        assert self.widget.si_p.value() == 5
        assert self.widget.c_type.currentIndex() == 5
        assert self.widget.c_type.currentText() == "WRSM"
        assert self.widget.c_topology.currentText() == "External Rotor"

        # Test Initialization of the machine desc
        ###########################################

        self.test_obj = MachineSCIM(name="test_machine_scim_desc", type_machine=1)
        self.test_obj.desc = "SCIM Machine"
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 7
        self.test_obj.rotor = LamSquirrelCage(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        assert self.widget.le_name.text() == "test_machine_scim_desc"
        assert self.widget.si_p.value() == 7
        assert self.widget.c_type.currentText() == "SCIM"
        assert self.widget.c_topology.currentText() == "External Rotor"
        assert self.widget.in_machine_desc.toPlainText() == "SCIM Machine"

    @pytest.mark.SCIM
    def test_set_name(self):
        """Check that the Widget allow to update name"""
        # Clear the field before writing the new value
        self.widget.le_name.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.le_name, "test_" + str(value))
        self.widget.le_name.editingFinished.emit()  # To trigger the slot

        assert self.test_obj.name == "test_" + str(value)

    @pytest.mark.SCIM
    def test_set_desc(self):
        """Check if the machine description changes are updated into machine object"""
        self.widget.in_machine_desc.clear()
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.in_machine_desc, "My machine_" + str(value))
        self.widget.in_machine_desc.textChanged.emit()  # To trigger the slot

        assert self.test_obj.desc == "My machine_" + str(value)

    @pytest.mark.SCIM
    def test_set_is_inner_rotor(self):
        """Check that the Widget allow to update is_inner_rotor"""
        self.widget.c_topology.setCurrentIndex(0)
        assert self.test_obj.rotor.is_internal
        self.widget.c_topology.setCurrentIndex(1)
        assert not self.test_obj.rotor.is_internal

    @pytest.mark.SCIM
    def test_set_p_scim(self):
        """Check that the Widget allow to update p"""
        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        self.widget.si_p.setValue(value)

        assert self.test_obj.stator.winding.p == value
        assert self.test_obj.rotor.winding.p == value

    def test_set_p_dfim(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineDFIM(name="test_machine_dfim", type_machine=4)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamSlotWind(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        self.widget.si_p.setValue(value)

        assert self.test_obj.stator.winding.p == value
        assert self.test_obj.rotor.winding.p == value

    @pytest.mark.IPMSM
    def test_set_p_sipmsm(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineSIPMSM(name="test_machine_ipmsm", type_machine=7)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamSlotMag(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        self.widget.si_p.setValue(value)

        assert self.test_obj.stator.winding.p == value
        assert self.test_obj.rotor.slot.Zs == 2 * value

    @pytest.mark.IPMSM
    def test_set_p_ipmsm(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineIPMSM(name="test_machine_ipmsm", type_machine=8)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=0))
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        self.widget.si_p.setValue(value)
        assert self.test_obj.stator.winding.p == value
        assert self.test_obj.rotor.hole[0].Zh == 2 * value

    def test_set_p_syrm(self):
        """Check that the Widget allow to update p"""
        self.test_obj = MachineSyRM(name="test_machine_ipmsm", type_machine=5)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=0))
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        self.widget.si_p.setValue(value)

        assert self.test_obj.stator.winding.p == value
        assert self.test_obj.rotor.hole[0].Zh == 2 * value

    def test_set_p(self):
        """Check that the Widget allow to update p when Winding is None"""
        self.test_obj = MachineSyRM(name="test_machine_ipmsm", type_machine=5)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22, Ksfill=0.545
        )
        self.test_obj.stator.winding = None
        self.test_obj.rotor = LamHole(
            is_stator=False, is_internal=False, Rint=0.11, Rext=0.12
        )
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=0))
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        self.widget.si_p.setValue(value)

        assert self.widget.machine.stator.winding.p == value
        assert self.widget.machine.stator.winding.is_reverse_wind == None
        assert self.widget.machine.stator.winding.Nslot_shift_wind == None
        assert self.widget.machine.stator.winding.qs == None
        assert self.widget.machine.stator.winding.Ntcoil == None
        assert self.widget.machine.stator.winding.Npcp == None
        assert self.widget.machine.stator.winding.type_connection == None
        assert self.widget.machine.stator.winding.Lewout == None

    @pytest.mark.skip(reason="Need to have DMachineSetup as parent")
    def test_set_type_ipmsm(self):
        """Check that you can define an IPMSM machine"""
        self.widget.c_type.setCurrentText("IPMSM")
        # Clear the field before writing the new value
        self.widget.si_p.clear()
        value = int(uniform(3, 100))
        self.widget.si_p.setValue(value)

        assert self.widget.machine.stator.winding.p == value
        assert type(self.widget.machine) is MachineIPMSM
        assert self.widget.machine.rotor.hole == list()

    @pytest.mark.skip(reason="Test was commented")
    def test_set_c_type(self):
        """Check that the Widget allow to update c_type when changing value in the combobox"""
        # SIPMSM
        self.test_obj = MachineSIPMSM(name="test_machine_sipmsm", type_machine=7)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=False, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding.p = 9
        self.test_obj.rotor = LamSlotMag(
            is_stator=False, is_internal=True, Rint=0.11, Rext=0.12
        )
        self.widget = SMachineType(
            machine=self.test_obj, material_dict=dict(), is_stator=False
        )

        assert self.widget.le_name.text() == "test_machine_sipmsm"
        assert self.widget.si_p.value() == 9
        assert self.widget.c_type.currentIndex() == 4
        assert self.widget.c_type.currentText() == "SIPMSM"
        assert self.widget.is_inner_rotor.checkState() == Qt.Checked

        QTest.keyClicks(self.widget.c_type, "WRSM")

        assert self.widget.c_type.currentIndex() == 3
        assert self.widget.c_type.currentText() == "WRSM"  # TODO

    def test_check(self):
        self.test_obj = MachineSyRM(name="test_machine_ipmsm", type_machine=5)
        self.test_obj.stator = LamSlotWind(
            is_stator=True, is_internal=True, Rint=0.21, Rext=0.22
        )
        self.test_obj.stator.winding = None

        assert self.widget.check(self.test_obj) == "Missing stator winding"


if __name__ == "__main__":
    a = TestSMachineType()
    a.setup_class()
    a.setup_method()
    a.test_set_p_sipmsm()
    a.teardown_class()
    print("Done")
