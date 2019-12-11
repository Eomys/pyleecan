# -*- coding: utf-8 -*-
"""
@date Created on Fri Jan 22 13:17:02 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from numpy import pi

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.MagnetType14 import MagnetType14
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.SMagnet import SMagnet
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet10.PMagnet10 import PMagnet10
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet11.PMagnet11 import PMagnet11
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet12.PMagnet12 import PMagnet12
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet13.PMagnet13 import PMagnet13
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet14.PMagnet14 import PMagnet14


class test_SMagnet_inset(TestCase):
    """Test that the widget SMagnet behave like it should (for SPMSM)"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = Machine(type_machine=7)  # IPMSM
        # For comp_output compatibility
        self.test_obj.stator = LamSlotWind(Rint=0.95, Rext=0.99)
        self.test_obj.rotor = LamSlotMag(Rint=0.1, Rext=0.9)
        self.test_obj.rotor.slot = SlotMPolar(Zs=8, W0=pi / 24, H0=5e-3)
        self.test_obj.rotor.slot.magnet = [MagnetType11(Wmag=pi / 24, Hmag=3e-3)]
        self.test_obj.rotor.slot.magnet[0].mat_type.name = "test3"

        self.matlib = list()
        self.matlib.append(Material(name="test1"))
        self.matlib[-1].elec.rho = 0.31
        self.matlib.append(Material(name="test2"))
        self.matlib[-1].elec.rho = 0.32
        self.matlib.append(Material(name="test3"))
        self.matlib[-1].elec.rho = 0.33

        self.widget = SMagnet(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test SMagnet_inset")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the GUI initialize correctly"""
        self.assertEqual(self.widget.c_type.currentIndex(), 1)

        self.assertEqual(self.widget.w_mag.unit_Wmag.text(), "rad")
        self.assertEqual(self.widget.w_mag.lf_Wmag.text(), "0.13089969")
        self.assertEqual(self.widget.w_mag.lf_Hmag.text(), "0.003")
        self.assertEqual(self.widget.w_mag.lf_H0.text(), "0.005")
        self.assertEqual(self.widget.w_mat.in_mat_type.text(), "mat_mag:")
        self.assertEqual(self.widget.w_mat.c_mat_type.currentIndex(), 2)
        self.assertEqual(
            self.widget.w_mag.w_out.out_Smag.text(), "Magnet surface: 0.0003521 m²"
        )
        self.assertEqual(self.widget.w_mag.w_out.out_gap.text(), "gap: 0.05 m")

    def test_set_material(self):
        """Check that you can change the material
        """
        self.widget.w_mat.c_mat_type.setCurrentIndex(0)
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].mat_type.name, "test1")
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].mat_type.elec.rho, 0.31)
        self.assertEqual(type(self.widget.w_mag), PMagnet11)

    def test_Magnet_Type_10_inset(self):
        """Check that the Widget is able to set inset Magnet type 10"""

        self.widget.c_type.setCurrentIndex(0)  # Index 0 is 10
        self.assertEqual(type(self.widget.w_mag), PMagnet10)
        self.assertEqual(
            self.widget.c_type.currentText(), "Rectangular"
        )  # Index 0 is 10

        self.assertEqual(type(self.test_obj.rotor.slot.magnet[0]), MagnetType10)
        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.41")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Wmag, 0.41)
        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.42")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Hmag, 0.42)
        # H0 set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.415")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0.415)
        # type_magnetization set test
        self.widget.c_type_magnetization.setCurrentIndex(2)
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].type_magnetization, 2)
        # Test change machine type
        self.assertEqual(self.test_obj.type_machine, 7)
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0)
        self.assertEqual(self.test_obj.type_machine, 6)

    def test_Magnet_Type_11_inset(self):
        """Check that the Widget is able to set inset Magnet type 11"""

        self.widget.c_type.setCurrentIndex(1)  # Index 1 is 11
        self.assertEqual(type(self.widget.w_mag), PMagnet11)
        self.assertEqual(self.widget.c_type.currentText(), "Polar")  # Index 2 is 11

        self.assertEqual(type(self.test_obj.rotor.slot.magnet[0]), MagnetType11)
        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.123")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Wmag, 0.123)
        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.44")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Hmag, 0.44)
        # H0 set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.425")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0.425)
        # type_magnetization set test
        self.widget.c_type_magnetization.setCurrentIndex(1)
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].type_magnetization, 1)
        # Test change machine type
        self.assertEqual(self.test_obj.type_machine, 7)
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0)
        self.assertEqual(self.test_obj.type_machine, 6)

    def test_Magnet_Type_12_inset(self):
        """Check that the Widget is able to set inset Magnet type 12"""

        self.widget.c_type.setCurrentIndex(2)  # Index 2 is 12
        self.assertEqual(type(self.widget.w_mag), PMagnet12)
        self.assertEqual(
            self.widget.c_type.currentText(), "Flat bottom, polar top"
        )  # Index 2 is 12

        self.assertEqual(type(self.test_obj.rotor.slot.magnet[0]), MagnetType12)
        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.45")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Wmag, 0.45)
        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.46")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Hmag, 0.46)
        # H0 set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.435")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0.435)
        # type_magnetization set test
        self.widget.c_type_magnetization.setCurrentIndex(1)
        # 0 is the default index
        self.widget.c_type_magnetization.setCurrentIndex(0)
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].type_magnetization, 0)
        # Test change machine type
        self.assertEqual(self.test_obj.type_machine, 7)
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0)
        self.assertEqual(self.test_obj.type_machine, 6)

    def test_Magnet_Type_13_inset(self):
        """Check that the Widget is able to set inset Magnet type 13"""

        self.widget.c_type.setCurrentIndex(3)  # Index 3 is 13
        self.assertEqual(type(self.widget.w_mag), PMagnet13)
        self.assertEqual(self.widget.c_type.currentText(), "Flat bottom, curved top")

        self.assertEqual(type(self.test_obj.rotor.slot.magnet[0]), MagnetType13)
        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.47")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Wmag, 0.47)

        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.48")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Hmag, 0.48)

        # Rtopm set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Rtopm.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Rtopm, "0.481")
        self.widget.w_mag.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Rtop, 0.481)

        # H0 set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.445")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0.445)
        # Test change machine type
        self.assertEqual(self.test_obj.type_machine, 7)
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0)
        self.assertEqual(self.test_obj.type_machine, 6)

    def test_Magnet_Type_14_inset(self):
        """Check that the Widget is able to set inset Magnet type 14"""

        self.widget.c_type.setCurrentIndex(4)  # Index 4 is 14
        self.assertEqual(type(self.widget.w_mag), PMagnet14)
        self.assertEqual(
            self.widget.c_type.currentText(), "Polar bottom, curved top"
        )  # Index 4 is 14

        self.assertEqual(type(self.test_obj.rotor.slot.magnet[0]), MagnetType14)
        # Wmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Wmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Wmag, "0.0491")
        self.widget.w_mag.lf_Wmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Wmag, 0.0491)
        # Hmag set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Hmag.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Hmag, "0.492")
        self.widget.w_mag.lf_Hmag.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Hmag, 0.492)
        # Rtopm set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_Rtopm.clear()
        QTest.keyClicks(self.widget.w_mag.lf_Rtopm, "0.493")
        self.widget.w_mag.lf_Rtopm.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.magnet[0].Rtop, 0.493)
        # H0 set test
        # Clear the field before writing the new value
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0.455")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0.455)
        # Test change machine type
        self.assertEqual(self.test_obj.type_machine, 7)
        self.widget.w_mag.lf_H0.clear()
        QTest.keyClicks(self.widget.w_mag.lf_H0, "0")
        self.widget.w_mag.lf_H0.editingFinished.emit()  # To trigger the slot
        self.assertEqual(self.test_obj.rotor.slot.H0, 0)
        self.assertEqual(self.test_obj.type_machine, 6)
