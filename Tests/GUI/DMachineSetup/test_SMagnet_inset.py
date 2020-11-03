# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.MagnetType14 import MagnetType14
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.SMagnet import SMagnet
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet10.PMagnet10 import PMagnet10
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet11.PMagnet11 import PMagnet11
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet12.PMagnet12 import PMagnet12
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet13.PMagnet13 import PMagnet13
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet14.PMagnet14 import PMagnet14


import pytest


@pytest.mark.GUI
class TestSMagnet_inset(object):
    """Test that the widget SMagnet behave like it should (for SPMSM)"""

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
        test_obj.rotor.slot = SlotMPolar(Zs=8, W0=pi / 24, H0=5e-3)
        test_obj.rotor.slot.magnet = [MagnetType11(Wmag=pi / 24, Hmag=3e-3)]
        test_obj.rotor.slot.magnet[0].mat_type.name = "test3"

        matlib = MatLib()
        matlib.dict_mat["RefMatLib"] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        matlib.dict_mat["RefMatLib"][0].elec.rho = 0.31
        matlib.dict_mat["RefMatLib"][1].elec.rho = 0.32
        matlib.dict_mat["RefMatLib"][2].elec.rho = 0.33

        widget = SMagnet(
            machine=test_obj, matlib=matlib, is_stator=False
        )

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    def test_init(self, setup):
        """Check that the GUI initialize correctly"""
        assert setup["widget"].c_type.currentIndex() == 1

        assert setup["widget"].w_mag.unit_Wmag.text() == "rad"
        assert setup["widget"].w_mag.lf_Wmag.text() == "0.13089969"
        assert setup["widget"].w_mag.lf_Hmag.text() == "0.003"
        assert setup["widget"].w_mag.lf_H0.text() == "0.005"
        assert setup["widget"].w_mat.in_mat_type.text() == "mat_mag:"
        assert setup["widget"].w_mat.c_mat_type.currentIndex() == 2
        assert setup["widget"].w_mag.w_out.out_Smag.text() == "Magnet surface: 0.0003521 m²"
        assert setup["widget"].w_mag.w_out.out_gap.text() == "gap: 0.05 m"

    def test_set_material(self, setup):
        """Check that you can change the material"""
        setup["widget"].w_mat.c_mat_type.setCurrentIndex(0)
        assert setup["test_obj"].rotor.slot.magnet[0].mat_type.name == "test1"
        assert setup["test_obj"].rotor.slot.magnet[0].mat_type.elec.rho == 0.31
        assert type(setup["widget"].w_mag) == PMagnet11

    def test_Magnet_Type_10_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 10"""

        setup["widget"].c_type.setCurrentIndex(0)  # Index 0 is 10
        assert type(setup["widget"].w_mag) == PMagnet10
        assert setup["widget"].c_type.currentText() == "Rectangular"  # Index 0 is 10

        assert type(setup["test_obj"].rotor.slot.magnet[0]) == MagnetType10
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Wmag, "0.41")
        setup["widget"].w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Wmag == 0.41
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Hmag, "0.42")
        setup["widget"].w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Hmag == 0.42
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0.415")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.415
        # type_magnetization set test
        setup["widget"].c_type_magnetization.setCurrentIndex(2)
        assert setup["test_obj"].rotor.slot.magnet[0].type_magnetization == 2
        # Test change machine type
        assert setup["test_obj"].type_machine == 7
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0
        assert setup["test_obj"].type_machine == 6

    def test_Magnet_Type_11_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 11"""

        setup["widget"].c_type.setCurrentIndex(1)  # Index 1 is 11
        assert type(setup["widget"].w_mag) == PMagnet11
        assert setup["widget"].c_type.currentText() == "Polar"  # Index 2 is 11

        assert type(setup["test_obj"].rotor.slot.magnet[0]) == MagnetType11
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Wmag, "0.123")
        setup["widget"].w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Wmag == 0.123
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Hmag, "0.44")
        setup["widget"].w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Hmag == 0.44
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0.425")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.425
        # type_magnetization set test
        setup["widget"].c_type_magnetization.setCurrentIndex(1)
        assert setup["test_obj"].rotor.slot.magnet[0].type_magnetization == 1
        # Test change machine type
        assert setup["test_obj"].type_machine == 7
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0
        assert setup["test_obj"].type_machine == 6

    def test_Magnet_Type_12_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 12"""

        setup["widget"].c_type.setCurrentIndex(2)  # Index 2 is 12
        assert type(setup["widget"].w_mag) == PMagnet12
        assert (
            setup["widget"].c_type.currentText() == "Flat bottom, polar top"
        )  # Index 2 is 12

        assert type(setup["test_obj"].rotor.slot.magnet[0]) == MagnetType12
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Wmag, "0.45")
        setup["widget"].w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Wmag == 0.45
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Hmag, "0.46")
        setup["widget"].w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Hmag == 0.46
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0.435")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.435
        # type_magnetization set test
        setup["widget"].c_type_magnetization.setCurrentIndex(1)
        # 0 is the default index
        setup["widget"].c_type_magnetization.setCurrentIndex(0)
        assert setup["test_obj"].rotor.slot.magnet[0].type_magnetization == 0
        # Test change machine type
        assert setup["test_obj"].type_machine == 7
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0
        assert setup["test_obj"].type_machine == 6

    def test_Magnet_Type_13_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 13"""

        setup["widget"].c_type.setCurrentIndex(3)  # Index 3 is 13
        assert type(setup["widget"].w_mag) == PMagnet13
        assert setup["widget"].c_type.currentText() == "Flat bottom, curved top"

        assert type(setup["test_obj"].rotor.slot.magnet[0]) == MagnetType13
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Wmag, "0.47")
        setup["widget"].w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Wmag == 0.47

        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Hmag, "0.48")
        setup["widget"].w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Hmag == 0.48

        # Rtopm set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Rtopm.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Rtopm, "0.481")
        setup["widget"].w_mag.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Rtop == 0.481

        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0.445")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.445
        # Test change machine type
        assert setup["test_obj"].type_machine == 7
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0
        assert setup["test_obj"].type_machine == 6

    def test_Magnet_Type_14_inset(self, setup):
        """Check that the Widget is able to set inset Magnet type 14"""

        setup["widget"].c_type.setCurrentIndex(4)  # Index 4 is 14
        assert type(setup["widget"].w_mag) == PMagnet14
        assert (
            setup["widget"].c_type.currentText() == "Polar bottom, curved top"
        )  # Index 4 is 14

        assert type(setup["test_obj"].rotor.slot.magnet[0]) == MagnetType14
        # Wmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Wmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Wmag, "0.0491")
        setup["widget"].w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Wmag == 0.0491
        # Hmag set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Hmag.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Hmag, "0.492")
        setup["widget"].w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Hmag == 0.492
        # Rtopm set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_Rtopm.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_Rtopm, "0.493")
        setup["widget"].w_mag.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.magnet[0].Rtop == 0.493
        # H0 set test
        # Clear the field before writing the new value
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0.455")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0.455
        # Test change machine type
        assert setup["test_obj"].type_machine == 7
        setup["widget"].w_mag.lf_H0.clear()
        QTest.keyClicks(setup["widget"].w_mag.lf_H0, "0")
        setup["widget"].w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert setup["test_obj"].rotor.slot.H0 == 0
        assert setup["test_obj"].type_machine == 6
