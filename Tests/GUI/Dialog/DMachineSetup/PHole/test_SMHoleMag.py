# -*- coding: utf-8 -*-

import sys
import mock
import matplotlib.pyplot as plt

from qtpy import QtWidgets
from qtpy.QtWidgets import QTabBar

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM52R import HoleM52R
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM58 import HoleM58
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.HoleM61 import HoleM61
from pyleecan.Classes.HoleM62 import HoleM62
from pyleecan.Classes.HoleM63 import HoleM63
from pyleecan.Classes.HoleUD import HoleUD
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
from pyleecan.Classes.Material import Material

from Tests.GUI import gui_option  # Set unit as [m]


import pytest


class TestSMHoleMag(object):
    """Test that the widget SMHoleMag behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test SMHoleMag")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        self.test_obj = MachineIPMSM(type_machine=8)
        self.test_obj.stator = LamSlotWind()
        self.test_obj.stator.winding.p = 4
        self.test_obj.rotor = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=8))
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet3"

        self.test_obj2 = MachineSyRM(type_machine=5)
        self.test_obj2.stator = LamSlotWind()
        self.test_obj2.stator.winding.p = 4
        self.test_obj2.rotor = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj2.rotor.hole = list()
        self.test_obj2.rotor.hole.append(HoleM54(Zh=16))

        self.material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        self.material_dict[LIB_KEY] = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]

        self.widget = SMHoleMag(
            machine=self.test_obj, material_dict=self.material_dict, is_stator=False
        )
        self.widget2 = SMHoleMag(
            machine=self.test_obj2, material_dict=self.material_dict, is_stator=False
        )
        self.widget.is_test = True
        self.widget2.is_test = True

    def test_init(self):
        """Check that the Widget initialize to the correct hole"""

        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.count() == 1
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 0
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 50"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.count() == 12

        self.test_obj2 = MachineSyRM(type_machine=5)
        self.test_obj2.stator = LamSlotWind()
        self.test_obj2.stator.winding.p = 4
        self.test_obj2.rotor = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj2.rotor.hole = list()
        self.widget2 = SMHoleMag(
            machine=self.test_obj2,
            material_dict=self.material_dict,
            is_stator=False,
        )

        assert len(self.widget2.machine.rotor.hole) == 1  # HoleM50 automatically added
        assert isinstance(self.widget2.machine.rotor.hole[0], HoleM50)

        self.test_obj = MachineIPMSM(type_machine=8)
        self.test_obj.stator = LamSlotWind()
        self.test_obj.stator.winding.p = 4
        self.test_obj.rotor = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=0))
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet3"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )

        assert self.widget.out_hole_pitch.text() == "Slot pitch: 360 / 2p = ?"

    def test_init_SyRM(self):
        """Check that the Widget initialize to the correct hole"""

        assert (
            self.widget2.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 22.5 [°] = 0.3927 [rad]"
        )
        assert self.widget2.tab_hole.count() == 1
        assert self.widget2.tab_hole.widget(0).c_hole_type.currentIndex() == 5
        assert (
            self.widget2.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 54"
        )
        assert self.widget2.tab_hole.widget(0).c_hole_type.count() == 13

    def test_init_SyRM_51(self):
        """Check that the Widget initialize to the correct hole"""

        self.test_obj2.rotor.hole = list()
        self.test_obj2.rotor.hole.append(
            HoleM51(
                Zh=16,
                W0=0.11,
                W1=0.12,
                W2=0.13,
                W3=0.14,
                W4=0.15,
                W5=0.16,
                W6=0.17,
                W7=0.18,
                H0=0.19,
                H1=0.2,
                H2=0.21,
            )
        )
        self.test_obj2.rotor.hole[0].remove_magnet()
        self.widget2 = SMHoleMag(
            machine=self.test_obj2,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget2.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 22.5 [°] = 0.3927 [rad]"
        )
        assert self.widget2.tab_hole.count() == 1
        assert self.widget2.tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            self.widget2.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 51"
        )
        assert self.widget2.tab_hole.widget(0).c_hole_type.count() == 13

        assert self.widget2.tab_hole.widget(0).w_hole.lf_W0.text() == "0.11"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_W1.text() == "0.12"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_W2.text() == "0"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_W3.text() == "0"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_W4.text() == "0"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_W5.text() == "0"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_W6.text() == "0"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_W7.text() == "0"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_H0.text() == "0.19"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_H1.text() == "0.2"
        assert self.widget2.tab_hole.widget(0).w_hole.lf_H2.text() == "0.21"

    def test_init_51(self):
        """Check that you can edit a hole 51"""
        self.test_obj.rotor.hole[0] = HoleM51(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 51"
        )

    def test_init_52(self):
        """Check that you can edit a hole 52"""
        self.test_obj.rotor.hole[0] = HoleM52(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 2
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 52"
        )

    def test_init_52R(self):
        """Check that you can edit a hole 52R"""
        self.test_obj.rotor.hole[0] = HoleM52R(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 3
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 52R"
        )

    def test_init_53(self):
        """Check that you can edit a hole 53"""
        self.test_obj.rotor.hole[0] = HoleM53(Zh=11)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 32.73 [°] = 0.5712 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 4
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 53"
        )

    def test_init_57(self):
        """Check that you can edit a hole 57"""
        self.test_obj.rotor.hole[0] = HoleM57(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 5
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 57"
        )

    def test_init_58(self):
        """Check that you can edit a hole 58"""
        self.test_obj.rotor.hole[0] = HoleM58(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 6
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 58"
        )

    def test_init_60(self):
        """Check that you can edit a hole 60"""
        self.test_obj.rotor.hole[0] = HoleM60(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 7
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 60"
        )

    def test_init_61(self):
        """Check that you can edit a hole 61"""
        self.test_obj.rotor.hole[0] = HoleM61(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 8
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 61"
        )

    def test_init_62(self):
        """Check that you can edit a hole 62"""
        self.test_obj.rotor.hole[0] = HoleM62(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 9
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 62"
        )

    def test_init_63(self):
        """Check that you can edit a hole 63"""
        self.test_obj.rotor.hole[0] = HoleM63(Zh=18)
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 20 [°] = 0.3491 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 10
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 63"
        )

    def test_init_UD(self):
        """Check that you can edit a hole UD"""
        self.test_obj.rotor.hole[0] = HoleUD(Zh=20)
        self.test_obj.rotor.hole[0].magnet_dict["magnet_0"] = Magnet()
        self.test_obj.rotor.hole[0].magnet_dict["magnet_0"].mat_type.name = "Magnet1"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 18 [°] = 0.3142 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 11
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText()
            == "Import from DXF"
        )

    def test_set_type_51(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(1)

        assert type(self.test_obj.rotor.hole[0]) == HoleM51
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 51"
        )

    def test_set_type_52(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(2)

        assert type(self.test_obj.rotor.hole[0]) == HoleM52
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 2
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 52"
        )

    def test_set_type_52R(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(3)

        assert type(self.test_obj.rotor.hole[0]) == HoleM52R
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 3
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 52R"
        )

    def test_set_type_53(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(4)

        assert type(self.test_obj.rotor.hole[0]) == HoleM53
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 4
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 53"
        )

    def test_set_type_57(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(5)

        assert type(self.test_obj.rotor.hole[0]) == HoleM57
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 5
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 57"
        )

    def test_set_type_58(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(6)

        assert type(self.test_obj.rotor.hole[0]) == HoleM58
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 6
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 58"
        )

    def test_set_type_60(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(7)

        assert type(self.test_obj.rotor.hole[0]) == HoleM60
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 7
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 60"
        )

    def test_set_type_61(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(8)

        assert type(self.test_obj.rotor.hole[0]) == HoleM61
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 8
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 61"
        )

    def test_set_type_62(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(9)

        assert type(self.test_obj.rotor.hole[0]) == HoleM62
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 9
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 62"
        )

    def test_set_type_63(self):
        """ """
        self.widget.tab_hole.widget(0).c_hole_type.setCurrentIndex(10)

        assert type(self.test_obj.rotor.hole[0]) == HoleM63
        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )
        assert self.widget.tab_hole.widget(0).c_hole_type.currentIndex() == 10
        assert (
            self.widget.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 63"
        )

    def test_SyRM_set_type_54_51_54(self):
        """Set a type 54 for a SyRM then set a 51 to check how the magnets are handled"""
        # Init a HoleM54
        assert self.widget2.tab_hole.widget(0).c_hole_type.currentIndex() == 5
        assert (
            self.widget2.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 54"
        )
        assert self.test_obj2.rotor.hole[0].Zh == 16

        # Set type 51
        self.widget2.tab_hole.widget(0).c_hole_type.setCurrentIndex(1)
        assert self.widget2.tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            self.widget2.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 51"
        )
        assert type(self.test_obj2.rotor.hole[0]) == HoleM51
        assert self.test_obj2.rotor.hole[0].magnet_0 == None
        assert self.test_obj2.rotor.hole[0].Zh == 16

        # Set type 54
        self.widget2.tab_hole.widget(0).c_hole_type.setCurrentIndex(5)
        assert self.widget2.tab_hole.widget(0).c_hole_type.currentIndex() == 5
        assert (
            self.widget2.tab_hole.widget(0).c_hole_type.currentText() == "Hole Type 54"
        )
        assert type(self.test_obj2.rotor.hole[0]) == HoleM54
        assert self.test_obj2.rotor.hole[0].Zh == 16

    def test_add_remove_hole(self):
        assert len(self.test_obj.rotor.hole) == 1
        assert self.widget.tab_hole.count() == 1

        self.widget.b_add.clicked.emit()

        assert len(self.test_obj.rotor.hole) == 2
        assert type(self.test_obj.rotor.hole[1]) == HoleM50
        assert self.test_obj.rotor.hole[1].Zh == 8
        assert self.widget.tab_hole.count() == 2

        self.widget.b_add.clicked.emit()

        assert len(self.test_obj.rotor.hole) == 3
        assert type(self.test_obj.rotor.hole[2]) == HoleM50
        assert self.test_obj.rotor.hole[2].Zh == 8
        assert self.widget.tab_hole.count() == 3
        assert self.widget.tab_hole.tabText(0) == "Hole Set 1"
        assert self.widget.tab_hole.tabText(1) == "Hole Set 2"
        assert self.widget.tab_hole.tabText(2) == "Hole Set 3"

        b_remove = self.widget.tab_hole.tabBar().tabButton(
            self.widget.tab_hole.count() - 1, QTabBar.RightSide
        )
        b_remove.clicked.emit()
        assert len(self.test_obj.rotor.hole) == 2
        assert type(self.test_obj.rotor.hole[1]) == HoleM50
        assert self.widget.tab_hole.count() == 2

        b_remove = self.widget.tab_hole.tabBar().tabButton(
            self.widget.tab_hole.count() - 1, QTabBar.RightSide
        )
        b_remove.clicked.emit()
        assert len(self.test_obj.rotor.hole) == 1
        assert self.widget.tab_hole.count() == 1

        # There is always at least 1 hole
        b_remove = self.widget.tab_hole.tabBar().tabButton(
            self.widget.tab_hole.count() - 1, QTabBar.RightSide
        )
        with mock.patch(
            "qtpy.QtWidgets.QMessageBox.warning",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            b_remove.clicked.emit()
        assert len(self.test_obj.rotor.hole) == 1
        assert self.widget.tab_hole.count() == 1

    def test_add_remove_hole_SyRM(self):
        assert len(self.test_obj2.rotor.hole) == 1
        assert self.widget2.tab_hole.count() == 1

        self.widget2.b_add.clicked.emit()

        assert len(self.test_obj2.rotor.hole) == 2
        assert type(self.test_obj2.rotor.hole[1]) == HoleM50
        assert self.test_obj2.rotor.hole[1].Zh == 16
        assert self.widget2.tab_hole.count() == 2

        b_remove = self.widget2.tab_hole.tabBar().tabButton(
            self.widget.tab_hole.count() - 1, QTabBar.RightSide
        )
        b_remove.clicked.emit()

        # self.widget2.b_remove.clicked.emit()
        assert len(self.test_obj2.rotor.hole) == 1
        assert self.widget2.tab_hole.count() == 1

        # There is always at least 1 hole
        b_remove = self.widget2.tab_hole.tabBar().tabButton(
            self.widget.tab_hole.count() - 1, QTabBar.RightSide
        )
        with mock.patch(
            "qtpy.QtWidgets.QMessageBox.warning",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            b_remove.clicked.emit()
        assert len(self.test_obj2.rotor.hole) == 1
        assert self.widget2.tab_hole.count() == 1

    def test_s_plot(self):
        self.test_obj = MachineIPMSM(type_machine=8)
        self.test_obj.stator = LamSlotWind(slot=None)
        self.test_obj.stator.winding.p = 4
        self.test_obj.rotor = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(
            HoleM50(Zh=1, W1=0.055, W0=0.150, W3=0.0015, H2=0.005, H3=0.006)
        )
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet3"
        self.widget = SMHoleMag(
            machine=self.test_obj,
            material_dict=self.material_dict,
            is_stator=False,
        )
        self.widget.is_test = True
        self.widget.b_plot.clicked.emit()

        assert self.widget.machine.rotor.hole[0].Zh == 8

        self.widget.machine.rotor.hole[0].W1 = 0.300
        with mock.patch(
            "qtpy.QtWidgets.QMessageBox.critical",
            return_value=QtWidgets.QMessageBox.Ok,
        ):
            self.widget.b_plot.clicked.emit()

        assert (
            self.widget.out_hole_pitch.text()
            == "Slot pitch: 360 / 2p = 45 [°] = 0.7854 [rad]"
        )


if __name__ == "__main__":
    a = TestSMHoleMag()
    a.setup_class()
    a.setup_method()
    a.test_add_remove_hole_SyRM()
    a.teardown_class()
    print("Done")
