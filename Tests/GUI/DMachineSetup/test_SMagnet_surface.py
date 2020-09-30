# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.MagnetType14 import MagnetType14
from pyleecan.Classes.SlotMFlat import SlotMFlat
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
class TestSMagnet_surface(object):
    """Test that the widget SMagnet behave like it should (for SPMSM)"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = MachineSIPMSM(type_machine=6)  # SPMSM
        # For comp_output compatibility
        self.test_obj.stator = LamSlotWind(Rint=0.95, Rext=0.99)
        self.test_obj.rotor = LamSlotMag(Rint=0.1, Rext=0.9)
        self.test_obj.rotor.slot = SlotMFlat(Zs=8, W0=10e-3, H0=0e-3)
        self.test_obj.rotor.slot.magnet = [
            MagnetType13(Wmag=10e-3, Hmag=3e-3, Rtop=12e-3)
        ]
        self.test_obj.rotor.slot.magnet[0].mat_type.name = "test2"

        self.matlib = MatLib()
        self.matlib.dict_mat["RefMatLib"] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        self.matlib.dict_mat["RefMatLib"][0].elec.rho = 0.31
        self.matlib.dict_mat["RefMatLib"][1].elec.rho = 0.32
        self.matlib.dict_mat["RefMatLib"][2].elec.rho = 0.33

        self.widget = SMagnet(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test SMagnet_surface")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the GUI initialize correctly"""
        assert self.widget.c_type.currentIndex() == 3
        assert type(self.widget.w_mag) == PMagnet13
        assert self.widget.w_mag.unit_Wmag.text() == "m"
        assert self.widget.w_mag.lf_Wmag.text() == "0.01"
        assert self.widget.w_mag.lf_Hmag.text() == "0.003"
        assert self.widget.w_mag.lf_H0.text() == "0"
        assert self.widget.w_mag.lf_Rtopm.text() == "0.012"
        assert self.widget.w_mat.c_mat_type.currentIndex() == 1
        assert self.widget.w_mag.w_out.out_Smag.text() == "Magnet surface: 3.734e-05 m²"
        assert self.widget.w_mag.w_out.out_gap.text() == "gap: 0.05 m"

    def test_set_material(self):
        """Check that you can change the material"""
        self.widget.w_mat.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.rotor.slot.magnet[0].mat_type.name == "test1"
        assert self.test_obj.rotor.slot.magnet[0].mat_type.elec.rho == 0.31

    def test_Magnet_Type_10_surface(self):
        """Check that the Widget is able to set surface Magnet type 10"""

        self.widget.c_type.setCurrentIndex(0)  # Index 0 is 10
        assert type(self.widget.w_mag) == PMagnet10
        assert self.widget.c_type.currentText() == "Rectangular"

        assert type(self.test_obj.rotor.slot.magnet[0]) == MagnetType10
        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.31")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Wmag == 0.31

        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.32")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Hmag == 0.32
        # type_magnetization set test
        self.widget.c_type_magnetization.setCurrentIndex(2)
        assert self.test_obj.rotor.slot.magnet[0].type_magnetization == 2
        # Test change machine type
        assert self.test_obj.type_machine == 6
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.123")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.H0 == 0.123
        assert self.test_obj.type_machine == 7

    def test_Magnet_Type_11_surface(self):
        """Check that the Widget is able to set surface Magnet type 11"""

        self.widget.c_type.setCurrentIndex(1)  # Index 1 is 11
        assert type(self.widget.w_mag) == PMagnet11
        assert self.widget.c_type.currentText() == "Polar"  # Index 2 is 11

        assert type(self.test_obj.rotor.slot.magnet[0]) == MagnetType11

        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.033")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Wmag == 0.033

        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.34")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Hmag == 0.34
        # type_magnetization set test
        self.widget.c_type_magnetization.setCurrentIndex(1)
        assert self.test_obj.rotor.slot.magnet[0].type_magnetization == 1
        # Test change machine type
        assert self.test_obj.type_machine == 6
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.123")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.H0 == 0.123
        assert self.test_obj.type_machine == 7

    def test_Magnet_Type_12_surface(self):
        """Check that the Widget is able to set surface Magnet type 12"""

        self.widget.c_type.setCurrentIndex(2)  # Index 2 is 12
        assert type(self.widget.w_mag) == PMagnet12
        assert self.widget.c_type.currentText() == "Flat bottom, polar top"

        assert type(self.test_obj.rotor.slot.magnet[0]) == MagnetType12

        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.35")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Wmag == 0.35

        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.36")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Hmag == 0.36
        # type_magnetization set test
        self.widget.c_type_magnetization.setCurrentIndex(1)
        # 0 is the default index
        self.widget.c_type_magnetization.setCurrentIndex(0)
        assert self.test_obj.rotor.slot.magnet[0].type_magnetization == 0
        # Test change machine type
        assert self.test_obj.type_machine == 6
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.123")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.H0 == 0.123
        assert self.test_obj.type_machine == 7

    def test_Magnet_Type_13_surface(self):
        """Check that the Widget is able to set surface Magnet type 13"""

        self.widget.c_type.setCurrentIndex(3)  # Index 3 is 13
        assert type(self.widget.w_mag) == PMagnet13
        assert (
            self.widget.c_type.currentText() == "Flat bottom, curved top"
        )  # Index 3 is 13

        assert type(self.test_obj.rotor.slot.magnet[0]) == MagnetType13

        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.37")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Wmag == 0.37

        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.38")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Hmag == 0.38

        # Rtopm set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Rtopm.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Rtopm, "0.381")
        self.widget.w_mag.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Rtop == 0.381
        # Test change machine type
        assert self.test_obj.type_machine == 6
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.123")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.H0 == 0.123
        assert self.test_obj.type_machine == 7

    def test_Magnet_Type_14_surface(self):
        """Check that the Widget is able to set surface Magnet type 14"""

        self.widget.c_type.setCurrentIndex(4)  # Index 4 is 14
        assert type(self.widget.w_mag) == PMagnet14
        assert self.widget.c_type.currentText() == "Polar bottom, curved top"

        assert type(self.test_obj.rotor.slot.magnet[0]) == MagnetType14

        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.0391")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Wmag == 0.0391

        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.392")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Hmag == 0.392

        # Rtopm set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Rtopm.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Rtopm, "0.393")
        self.widget.w_mag.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.magnet[0].Rtop == 0.393
        # Test change machine type
        assert self.test_obj.type_machine == 6
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.123")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        assert self.test_obj.rotor.slot.H0 == 0.123
        assert self.test_obj.type_machine == 7
