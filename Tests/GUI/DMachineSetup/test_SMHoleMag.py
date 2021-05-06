# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM58 import HoleM58
from pyleecan.Classes.HoleUD import HoleUD
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
from pyleecan.Classes.Material import Material


import pytest


class TestSMHoleMag(object):
    """Test that the widget SMHoleMag behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineIPMSM(type_machine=8)
        test_obj.stator = LamSlotWind()
        test_obj.stator.winding.p = 4
        test_obj.rotor = LamHole(Rint=0.1, Rext=0.2)
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(HoleM50(Zh=8))
        test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet3"

        test_obj2 = MachineSyRM(type_machine=5)
        test_obj2.stator = LamSlotWind()
        test_obj2.stator.winding.p = 4
        test_obj2.rotor = LamHole(Rint=0.1, Rext=0.2)
        test_obj2.rotor.hole = list()
        test_obj2.rotor.hole.append(HoleM54(Zh=16))

        matlib = MatLib()
        matlib.list_mat = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]
        matlib.index_first_mat_mach = 3

        widget = SMHoleMag(machine=test_obj, matlib=matlib, is_stator=False)
        widget2 = SMHoleMag(machine=test_obj2, matlib=matlib, is_stator=False)

        yield {
            "widget": widget,
            "widget2": widget2,
            "test_obj": test_obj,
            "test_obj2": test_obj2,
            "matlib": matlib,
        }

        self.app.quit()

    def test_init(self, setup):
        """Check that the Widget initialize to the correct hole"""

        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 45 °"
        assert setup["widget"].tab_hole.count() == 1
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 0
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 50"
        )
        assert setup["widget"].tab_hole.widget(0).c_hole_type.count() == 7

        setup["test_obj2"] = MachineSyRM(type_machine=5)
        setup["test_obj2"].stator = LamSlotWind()
        setup["test_obj2"].stator.winding.p = 4
        setup["test_obj2"].rotor = LamHole(Rint=0.1, Rext=0.2)
        setup["test_obj2"].rotor.hole = list()
        setup["widget2"] = SMHoleMag(
            machine=setup["test_obj2"], matlib=setup["matlib"], is_stator=False
        )

        assert setup["widget2"].machine.rotor.hole[0].magnet_0 == None
        assert setup["widget2"].machine.rotor.hole[0].magnet_1 == None

        setup["test_obj"] = MachineIPMSM(type_machine=8)
        setup["test_obj"].stator = LamSlotWind()
        setup["test_obj"].stator.winding.p = 4
        setup["test_obj"].rotor = LamHole(Rint=0.1, Rext=0.2)
        setup["test_obj"].rotor.hole = list()
        setup["test_obj"].rotor.hole.append(HoleM50(Zh=0))
        setup["test_obj"].rotor.hole[0].magnet_0.mat_type.name = "Magnet3"
        setup["widget"] = SMHoleMag(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
        )

        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = ?"

    def test_init_SyRM(self, setup):
        """Check that the Widget initialize to the correct hole"""

        assert (
            setup["widget2"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 22.5 °"
        )
        assert setup["widget2"].tab_hole.count() == 1
        assert setup["widget2"].tab_hole.widget(0).c_hole_type.currentIndex() == 4
        assert (
            setup["widget2"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 54"
        )
        assert setup["widget2"].tab_hole.widget(0).c_hole_type.count() == 8

    def test_init_SyRM_51(self, setup):
        """Check that the Widget initialize to the correct hole"""

        setup["test_obj2"].rotor.hole = list()
        setup["test_obj2"].rotor.hole.append(
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
        setup["test_obj2"].rotor.hole[0].remove_magnet()
        setup["widget2"] = SMHoleMag(
            machine=setup["test_obj2"], matlib=setup["matlib"], is_stator=False
        )
        assert (
            setup["widget2"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 22.5 °"
        )
        assert setup["widget2"].tab_hole.count() == 1
        assert setup["widget2"].tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            setup["widget2"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 51"
        )
        assert setup["widget2"].tab_hole.widget(0).c_hole_type.count() == 8

        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W0.text() == "0.11"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W1.text() == "0.12"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W2.text() == "0"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W3.text() == "0"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W4.text() == "0"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W5.text() == "0"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W6.text() == "0"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_W7.text() == "0"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_H0.text() == "0.19"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_H1.text() == "0.2"
        assert setup["widget2"].tab_hole.widget(0).w_hole.lf_H2.text() == "0.21"

    def test_init_51(self, setup):
        """Check that you can edit a hole 51"""
        setup["test_obj"].rotor.hole[0] = HoleM51(Zh=18)
        setup["test_obj"].rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        setup["widget"] = SMHoleMag(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
        )
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 20 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 51"
        )

    def test_init_52(self, setup):
        """Check that you can edit a hole 52"""
        setup["test_obj"].rotor.hole[0] = HoleM52(Zh=18)
        setup["test_obj"].rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        setup["widget"] = SMHoleMag(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
        )
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 20 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 2
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 52"
        )

    def test_init_53(self, setup):
        """Check that you can edit a hole 53"""
        setup["test_obj"].rotor.hole[0] = HoleM53(Zh=11)
        setup["test_obj"].rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        setup["widget"] = SMHoleMag(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
        )
        assert (
            setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 32.73 °"
        )
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 3
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 53"
        )

    def test_init_57(self, setup):
        """Check that you can edit a hole 57"""
        setup["test_obj"].rotor.hole[0] = HoleM57(Zh=18)
        setup["test_obj"].rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        setup["widget"] = SMHoleMag(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
        )
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 20 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 4
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 57"
        )

    def test_init_58(self, setup):
        """Check that you can edit a hole 58"""
        setup["test_obj"].rotor.hole[0] = HoleM58(Zh=18)
        setup["test_obj"].rotor.hole[0].magnet_0.mat_type.name = "Magnet1"
        setup["widget"] = SMHoleMag(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
        )
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 20 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 5
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 58"
        )

    # def test_init_UD(self, setup):
    #     """Check that you can edit a hole UD"""
    #     setup["test_obj"].rotor.hole[0] = HoleUD(Zh=20)
    #     setup["test_obj"].rotor.hole[0].magnet_dict["magnet_0"] = Magnet()
    #     setup["test_obj"].rotor.hole[0].magnet_dict[
    #         "magnet_0"
    #     ].mat_type.name = "Magnet1"
    #     setup["widget"] = SMHoleMag(
    #         machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
    #     )
    #     assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 18 °"
    #     assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 6
    #     assert (
    #         setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
    #         == "Import from DXF"
    #     )

    def test_set_type_51(self, setup):
        """ """
        setup["widget"].tab_hole.widget(0).c_hole_type.setCurrentIndex(1)

        assert type(setup["test_obj"].rotor.hole[0]) == HoleM51
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 45 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 51"
        )

    def test_set_type_52(self, setup):
        """ """
        setup["widget"].tab_hole.widget(0).c_hole_type.setCurrentIndex(2)

        assert type(setup["test_obj"].rotor.hole[0]) == HoleM52
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 45 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 2
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 52"
        )

    def test_set_type_53(self, setup):
        """ """
        setup["widget"].tab_hole.widget(0).c_hole_type.setCurrentIndex(3)

        assert type(setup["test_obj"].rotor.hole[0]) == HoleM53
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 45 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 3
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 53"
        )

    def test_set_type_57(self, setup):
        """ """
        setup["widget"].tab_hole.widget(0).c_hole_type.setCurrentIndex(4)

        assert type(setup["test_obj"].rotor.hole[0]) == HoleM57
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 45 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 4
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 57"
        )

    def test_set_type_58(self, setup):
        """ """
        setup["widget"].tab_hole.widget(0).c_hole_type.setCurrentIndex(5)

        assert type(setup["test_obj"].rotor.hole[0]) == HoleM58
        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 45 °"
        assert setup["widget"].tab_hole.widget(0).c_hole_type.currentIndex() == 5
        assert (
            setup["widget"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 58"
        )

    def test_SyRM_set_type_54_51_54(self, setup):
        """Set a type 54 for a SyRM then set a 51 to check how the magnets are handled"""
        # Init a HoleM54
        assert setup["widget2"].tab_hole.widget(0).c_hole_type.currentIndex() == 4
        assert (
            setup["widget2"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 54"
        )
        assert setup["test_obj2"].rotor.hole[0].Zh == 16

        # Set type 51
        setup["widget2"].tab_hole.widget(0).c_hole_type.setCurrentIndex(1)
        assert setup["widget2"].tab_hole.widget(0).c_hole_type.currentIndex() == 1
        assert (
            setup["widget2"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 51"
        )
        assert type(setup["test_obj2"].rotor.hole[0]) == HoleM51
        assert setup["test_obj2"].rotor.hole[0].magnet_0 == None
        assert setup["test_obj2"].rotor.hole[0].Zh == 16

        # Set type 54
        setup["widget2"].tab_hole.widget(0).c_hole_type.setCurrentIndex(4)
        assert setup["widget2"].tab_hole.widget(0).c_hole_type.currentIndex() == 4
        assert (
            setup["widget2"].tab_hole.widget(0).c_hole_type.currentText()
            == "Hole Type 54"
        )
        assert type(setup["test_obj2"].rotor.hole[0]) == HoleM54
        assert setup["test_obj2"].rotor.hole[0].Zh == 16

    def test_add_remove_hole(self, setup):
        assert len(setup["test_obj"].rotor.hole) == 1
        assert setup["widget"].tab_hole.count() == 1

        setup["widget"].b_add.clicked.emit()

        assert len(setup["test_obj"].rotor.hole) == 2
        assert type(setup["test_obj"].rotor.hole[1]) == HoleM50
        assert setup["test_obj"].rotor.hole[1].Zh == 8
        assert setup["widget"].tab_hole.count() == 2

        setup["widget"].b_add.clicked.emit()

        assert len(setup["test_obj"].rotor.hole) == 3
        assert type(setup["test_obj"].rotor.hole[2]) == HoleM50
        assert setup["test_obj"].rotor.hole[2].Zh == 8
        assert setup["widget"].tab_hole.count() == 3
        assert setup["widget"].tab_hole.tabText(0) == "Hole 1"
        assert setup["widget"].tab_hole.tabText(1) == "Hole 2"
        assert setup["widget"].tab_hole.tabText(2) == "Hole 3"

        setup["widget"].b_remove.clicked.emit()
        assert len(setup["test_obj"].rotor.hole) == 2
        assert type(setup["test_obj"].rotor.hole[1]) == HoleM50
        assert setup["widget"].tab_hole.count() == 2

        setup["widget"].b_remove.clicked.emit()
        assert len(setup["test_obj"].rotor.hole) == 1
        assert setup["widget"].tab_hole.count() == 1

        # There is always at least 1 hole
        setup["widget"].b_remove.clicked.emit()
        assert len(setup["test_obj"].rotor.hole) == 1
        assert setup["widget"].tab_hole.count() == 1

    def test_add_remove_hole_SyRM(self, setup):
        assert len(setup["test_obj2"].rotor.hole) == 1
        assert setup["widget2"].tab_hole.count() == 1

        setup["widget2"].b_add.clicked.emit()

        assert len(setup["test_obj2"].rotor.hole) == 2
        assert type(setup["test_obj2"].rotor.hole[1]) == HoleM50
        assert setup["test_obj2"].rotor.hole[1].Zh == 16
        assert setup["test_obj2"].rotor.hole[1].magnet_0 == None
        assert setup["widget2"].tab_hole.count() == 2

        setup["widget2"].b_remove.clicked.emit()
        assert len(setup["test_obj2"].rotor.hole) == 1
        assert setup["widget2"].tab_hole.count() == 1

        # There is always at least 1 hole
        setup["widget2"].b_remove.clicked.emit()
        assert len(setup["test_obj2"].rotor.hole) == 1
        assert setup["widget2"].tab_hole.count() == 1

    @pytest.mark.skip
    def test_s_plot(self, setup):
        setup["test_obj"] = MachineIPMSM(type_machine=8)
        setup["test_obj"].stator = LamSlotWind(slot=None)
        setup["test_obj"].stator.winding.p = 4
        setup["test_obj"].rotor = LamHole(Rint=0.1, Rext=0.2)
        setup["test_obj"].rotor.hole = list()
        setup["test_obj"].rotor.hole.append(
            HoleM50(Zh=1, W1=0.055, W0=0.150, W3=0.0015, H2=0.005, H3=0.006)
        )
        setup["test_obj"].rotor.hole[0].magnet_0.mat_type.name = "Magnet3"
        setup["widget"] = SMHoleMag(
            machine=setup["test_obj"], matlib=setup["matlib"], is_stator=False
        )
        setup["widget"].s_plot(is_show_fig=False)

        assert setup["widget"].machine.rotor.hole[0].Zh == 8

        setup["widget"].machine.rotor.hole[0].W1 = 0.300
        setup["widget"].s_plot(is_show_fig=False)

        assert setup["widget"].out_hole_pitch.text() == "Slot pitch = 360 / 2p = 45 °"
