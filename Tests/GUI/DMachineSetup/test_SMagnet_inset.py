# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.SlotM13 import SlotM13
from pyleecan.Classes.SlotM14 import SlotM14
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.SMSlot import SMSlot
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot10.PMSlot10 import PMSlot10
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot11.PMSlot11 import PMSlot11
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot12.PMSlot12 import PMSlot12
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot13.PMSlot13 import PMSlot13
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot14.PMSlot14 import PMSlot14


import pytest


@pytest.mark.GUI
class TestSMSlot_inset(object):
    """Test that the widget SMSlot behave like it should (for SIPMSM)"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = MachineSIPMSM(type_machine=7)  # IPMSM
        # For comp_output compatibility
        test_obj.stator = LamSlotWind(Rint=0.95, Rext=0.99)
        test_obj.rotor = LamSlotMag(Rint=0.1, Rext=0.9)
        test_obj.rotor.slot = SlotM11(
            Zs=8, W0=pi / 24, H0=5e-3, Wmag=pi / 24, Hmag=3e-3
        )
        test_obj.rotor.magnet.mat_type.name = "test3"

        matlib = MatLib()
        matlib.dict_mat["RefMatLib"] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        matlib.dict_mat["RefMatLib"][0].elec.rho = 0.31
        matlib.dict_mat["RefMatLib"][1].elec.rho = 0.32
        matlib.dict_mat["RefMatLib"][2].elec.rho = 0.33

        widget = SMSlot(machine=test_obj, matlib=matlib, is_stator=False)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the GUI initialize correctly"""
        assert setup["widget"].c_slot_type.currentIndex() == 1

        assert setup["widget"].w_slot.unit_Wmag.text() == "[rad]"
        assert setup["widget"].w_slot.lf_Wmag.text() == "0.13089969"
        assert setup["widget"].w_slot.lf_Hmag.text() == "0.003"
        assert setup["widget"].w_slot.lf_H0.text() == "0.005"
        assert setup["widget"].w_slot.lf_W0.text() == "0.13089969"
        assert setup["widget"].w_mat.in_mat_type.text() == "mat_mag:"
        assert setup["widget"].w_mat.c_mat_type.currentIndex() == 2
        assert (
            setup["widget"].w_slot.w_out.out_wind_surface.text()
            == "Active surface: 0.0003521 [m²]"
        )

    def test_set_material(self, setup):
        """Check that you can change the material"""
        setup["widget"].w_mat.c_mat_type.setCurrentIndex(0)
        assert setup["test_obj"].rotor.magnet.mat_type.name == "test1"
        assert setup["test_obj"].rotor.magnet.mat_type.elec.rho == 0.31
        assert type(setup["widget"].w_slot) == PMSlot11

    def test_Magnet_Type_10_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 10"""

        setup["widget"].c_slot_type.setCurrentIndex(0)  # Index 0 is 10
        assert type(setup["widget"].w_slot) == PMSlot10
        assert (
            setup["widget"].c_slot_type.currentText() == "Rectangular Magnet"
        )  # Index 0 is 10

        assert type(setup["test_obj"].rotor.slot) == SlotM10
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Wmag, "0.41")
        setup["widget"].w_slot.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Wmag == 0.41
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Hmag, "0.42")
        setup["widget"].w_slot.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Hmag == 0.42
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_H0, "0.415")
        setup["widget"].w_slot.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.415
        # W0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_W0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_W0, "0.415")
        setup["widget"].w_slot.lf_W0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.W0 == 0.415
        # type_magnetization set test
        setup["widget"].c_type_magnetization.setCurrentIndex(2)
        assert setup["test_obj"].rotor.magnet.type_magnetization == 2

    def test_Magnet_Type_11_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 11"""

        setup["widget"].c_slot_type.setCurrentIndex(1)  # Index 1 is 11
        assert type(setup["widget"].w_slot) == PMSlot11
        assert (
            setup["widget"].c_slot_type.currentText() == "Polar Magnet"
        )  # Index 2 is 11

        assert type(setup["test_obj"].rotor.slot) == SlotM11
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Wmag, "0.123")
        setup["widget"].w_slot.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Wmag == 0.123
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Hmag, "0.44")
        setup["widget"].w_slot.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Hmag == 0.44
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_H0, "0.425")
        setup["widget"].w_slot.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.425
        # W0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_W0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_W0, "0.4898")
        setup["widget"].w_slot.lf_W0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.W0 == 0.4898
        # type_magnetization set test
        setup["widget"].c_type_magnetization.setCurrentIndex(1)
        assert setup["test_obj"].rotor.magnet.type_magnetization == 1

    def test_Magnet_Type_12_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 12"""

        setup["widget"].c_slot_type.setCurrentIndex(2)  # Index 2 is 12
        assert type(setup["widget"].w_slot) == PMSlot12
        assert (
            setup["widget"].c_slot_type.currentText()
            == "Rectangular Magnet with polar top"
        )  # Index 2 is 12

        assert type(setup["test_obj"].rotor.slot) == SlotM12
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Wmag, "0.45")
        setup["widget"].w_slot.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Wmag == 0.45
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Hmag, "0.46")
        setup["widget"].w_slot.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Hmag == 0.46
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_H0, "0.435")
        setup["widget"].w_slot.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.435
        # W0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_W0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_W0, "0.4898")
        setup["widget"].w_slot.lf_W0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.W0 == 0.4898
        # type_magnetization set test
        setup["widget"].c_type_magnetization.setCurrentIndex(1)
        # 0 is the default index
        setup["widget"].c_type_magnetization.setCurrentIndex(0)
        assert setup["test_obj"].rotor.magnet.type_magnetization == 0

    def test_Magnet_Type_13_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 13"""

        setup["widget"].c_slot_type.setCurrentIndex(3)  # Index 3 is 13
        assert type(setup["widget"].w_slot) == PMSlot13
        assert (
            setup["widget"].c_slot_type.currentText()
            == "Rectangular Magnet with curved top"
        )

        assert type(setup["test_obj"].rotor.slot) == SlotM13
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Wmag, "0.47")
        setup["widget"].w_slot.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Wmag == 0.47

        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Hmag, "0.48")
        setup["widget"].w_slot.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Hmag == 0.48

        # Rtopm set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Rtopm.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Rtopm, "0.481")
        setup["widget"].w_slot.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Rtopm == 0.481

        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_H0, "0.445")
        setup["widget"].w_slot.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.445
        # W0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_W0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_W0, "0.4898")
        setup["widget"].w_slot.lf_W0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.W0 == 0.4898

    def test_Magnet_Type_14_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 14"""

        setup["widget"].c_slot_type.setCurrentIndex(4)  # Index 4 is 14
        assert type(setup["widget"].w_slot) == PMSlot14
        assert (
            setup["widget"].c_slot_type.currentText() == "Polar Magnet with curved top"
        )  # Index 4 is 14

        assert type(setup["test_obj"].rotor.slot) == SlotM14
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Wmag, "0.0491")
        setup["widget"].w_slot.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Wmag == 0.0491
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Hmag, "0.492")
        setup["widget"].w_slot.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Hmag == 0.492
        # Rtopm set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_Rtopm.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_Rtopm, "0.493")
        setup["widget"].w_slot.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.Rtopm == 0.493
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_H0, "0.455")
        setup["widget"].w_slot.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.455
        # W0 set test
        # Clear the field before writing the new value
        setup["widget"].w_slot.lf_W0.clear()
        QTest.keyClicks(setup["widget"].w_slot.lf_W0, "0.4898")
        setup["widget"].w_slot.lf_W0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.W0 == 0.4898
