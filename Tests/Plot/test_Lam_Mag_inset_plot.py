# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 13 17:33:49 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""
from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.MagnetType14 import MagnetType14
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.MatLamination import MatLamination
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Tests import save_plot_path as save_path


class test_Lam_Mag_inset_plot(TestCase):
    """unittest for Lamination with inset magnet plot"""

    def test_Lam_Mag_10_inset(self):
        """Test machine plot with Magnet 10 inset"""

        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotMag(
            Rint=40e-3,
            Rext=100e-3,
            is_internal=True,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        magnet = [MagnetType10(Lmag=0.5, Hmag=0.02, Wmag=0.04)]
        test_obj.rotor.slot = SlotMFlat(Zs=4, W0=0.04, H0=0.02, magnet=magnet)
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.55)
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=4, Alpha0=0, D0=2.5e-3, H0=50e-3)
        )
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=60e-3)
        )
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=12, Alpha0=0, D0=10e-3, H0=70e-3)
        )

        test_obj.stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )

        magnet2 = [MagnetType10(Lmag=0.5, Hmag=0.02, Wmag=0.04)]
        test_obj.stator.slot = SlotMFlat(
            Zs=8, W0=0.04, W3=2 * pi / 64, H0=0.02, magnet=magnet2
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=200e-3, Rext=250e-3, Lfra=0.5)
        test_obj.stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=10e-3, W2=20e-3, D0=0.02, H0=0.140)
        )
        test_obj.stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=20e-3, W2=40e-3, D0=0.02, H0=0.170)
        )

        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 55)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_1-Machine.png"))

        test_obj.rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 30)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_2-Rotor.png"))

        test_obj.stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 22)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_3-Stator.png"))

    def test_Lam_Mag_10_inset_2_mag(self):
        """Test machine plot with Magnet 10 inset with two magnet in the slot"""
        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotMag(
            Rint=40e-3,
            Rext=100e-3,
            is_internal=True,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.rotor.slot = SlotMFlat(
            Zs=4,
            W0=0.03,
            H0=0.02,
            W3=2 * pi / 60,
            magnet=[
                MagnetType10(Lmag=0.5, Hmag=0.015, Wmag=0.03),
                MagnetType10(Lmag=0.5, Hmag=0.015, Wmag=0.03),
            ],
        )
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.55)
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=4, Alpha0=0, D0=2.5e-3, H0=50e-3)
        )
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=60e-3)
        )
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=12, Alpha0=0, D0=10e-3, H0=70e-3)
        )
        test_obj.stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )

        test_obj.stator.slot = SlotMFlat(
            Zs=8,
            W0=0.03,
            W3=2 * pi / 64,
            H0=0.02,
            magnet=[
                MagnetType10(Lmag=0.5, Hmag=0.025, Wmag=0.03),
                MagnetType10(Lmag=0.5, Hmag=0.025, Wmag=0.03),
            ],
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=200e-3, Rext=250e-3, Lfra=0.5)
        test_obj.stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=10e-3, W2=20e-3, D0=0.02, H0=0.140)
        )
        test_obj.stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=20e-3, W2=40e-3, D0=0.02, H0=0.170)
        )
        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 67)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_1_Mag_2-Machine.png"))

        test_obj.rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 34)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_2_Mag_2-Rotor.png"))

        test_obj.stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 30)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_3_Mag_2-Stator.png"))

    def test_Lam_Mag_11_inset(self):
        """Test machine plot with Magnet 11 inset"""

        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
        magnet = [MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 8)]
        test_obj.rotor.slot = SlotMPolar(
            Zs=8, W0=pi / 8, H0=0.01, W3=2 * pi / 64, magnet=magnet
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.55)

        test_obj.stator = LamSlotMag(
            Rint=115e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        magnet2 = [MagnetType11(Lmag=0.35, Hmag=0.03, Wmag=pi / 4)]
        test_obj.stator.slot = SlotMPolar(
            Zs=4, W0=pi / 4, H0=0.02, W3=2 * pi / 64, magnet=magnet2
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=200e-3, Rext=230e-3, Lfra=0.3)

        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 19)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_1-Machine.png"))

        test_obj.rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_2-Rotor.png"))

        test_obj.stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_3-Stator.png"))

    def test_Lam_Mag_11_inset_2_mag(self):
        """Test machine plot with Magnet 11 inset with two magnet in the slot"""
        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.rotor.slot = SlotMPolar(
            Zs=8,
            W0=pi / 12,
            H0=0.01,
            W3=pi / 18,
            magnet=[
                MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 12),
                MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 12),
            ],
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.55)

        test_obj.stator = LamSlotMag(
            Rint=115e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.stator.slot = SlotMPolar(
            Zs=4,
            W0=pi / 10,
            H0=0.02,
            W3=2 * pi / 50,
            magnet=[
                MagnetType11(Lmag=0.35, Hmag=0.03, Wmag=pi / 10),
                MagnetType11(Lmag=0.35, Hmag=0.03, Wmag=pi / 10),
            ],
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=200e-3, Rext=230e-3, Lfra=0.3)

        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 31)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_1_Mag_2-Machine.png"))

        test_obj.rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 18)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_2_Mag_2-Rotor.png"))

        test_obj.stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_3_Mag_2-Stator.png"))

    def test_Lam_Mag_12_inset(self):
        """Test machine plot with Magnet 12 inset"""

        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.35,
            Nrvd=3,
            Wrvd=0.05,
        )
        magnet = [MagnetType12(Lmag=0.5, Hmag=0.02, Wmag=0.04)]
        test_obj.rotor.slot = SlotMFlat(
            Zs=8, W0=0.04, H0=0.02, W3=2 * pi / 64, magnet=magnet
        )
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.55)

        test_obj.stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.35,
            Nrvd=3,
            Wrvd=0.05,
        )
        magnet2 = [MagnetType12(Lmag=0.5, Hmag=0.03, Wmag=0.04)]
        test_obj.stator.slot = SlotMFlat(
            Zs=4, W0=0.04, H0=0.02, W3=2 * pi / 64, magnet=magnet2
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=200e-3, Rext=250e-3, Lfra=0.5)

        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 19)
        fig.savefig(join(save_path, "test_Lam_Mag_12i_1-Machine.png"))

        test_obj.rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_12i_2-Rotor.png"))

        test_obj.stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_12i_3-Stator.png"))

    def test_Lam_Mag_13_inset(self):
        """Test machine plot with Magnet 12 inset"""

        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.42,
            Nrvd=4,
            Wrvd=0.02,
        )
        magnet = [MagnetType13(Lmag=0.5, Hmag=0.02, Wmag=0.04, Rtop=0.04)]
        test_obj.rotor.slot = SlotMFlat(
            Zs=8, W0=0.04, H0=0.02, W3=2 * pi / 64, magnet=magnet
        )
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.55)

        test_obj.stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.42,
            Nrvd=4,
            Wrvd=0.02,
        )
        magnet2 = [MagnetType13(Lmag=0.5, Hmag=0.02, Wmag=0.04, Rtop=0.04)]
        test_obj.stator.slot = SlotMFlat(
            Zs=4, W0=0.04, H0=0.025, W3=2 * pi / 64, magnet=magnet2
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=200e-3, Rext=250e-3, Lfra=0.5)

        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 19)
        fig.savefig(join(save_path, "test_Lam_Mag_13i_1-Machine.png"))

        test_obj.rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_13i_2-Rotor.png"))

        test_obj.stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_13i_3-Stator.png"))

    def test_Lam_Mag_14_inset(self):
        """Test machine plot with Magnet 14 inset"""

        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.4,
            Nrvd=5,
            Wrvd=0.02,
        )
        magnet = [MagnetType14(Lmag=0.5, Hmag=0.02, Wmag=0.628, Rtop=0.04)]
        test_obj.rotor.slot = SlotMPolar(Zs=4, W0=0.628, H0=0.02, magnet=magnet)
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.55)

        test_obj.stator = Lamination(
            Rint=130e-3,
            Rext=0.2,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=5,
            Wrvd=0.02,
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=200e-3, Rext=250e-3, Lfra=0.5)

        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 11)
        fig.savefig(join(save_path, "test_Lam_Mag_14i_1-Machine.png"))

        test_obj.rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_14i_2-Rotor.png"))

        test_obj.stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 2)
        fig.savefig(join(save_path, "test_Lam_Mag_14i_3-Stator.png"))
