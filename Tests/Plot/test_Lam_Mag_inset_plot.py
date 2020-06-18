# -*- coding: utf-8 -*-
from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.MagnetType14 import MagnetType14
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.SlotMPolar import SlotMPolar
from Tests import save_plot_path as save_path


class test_Lam_Mag_inset_plot(TestCase):
    """unittest for Lamination with inset magnet plot"""

    def test_Lam_Mag_10_inset(self):
        """Test machine plot with Magnet 10 inset"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=100e-3,
            is_internal=True,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        magnet = [MagnetType10(Lmag=0.5, Hmag=0.02, Wmag=0.04)]
        rotor.slot = SlotMFlat(Zs=4, W0=0.04, H0=0.02, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.axial_vent.append(VentilationCirc(Zh=4, Alpha0=0, D0=2.5e-3, H0=50e-3))
        rotor.axial_vent.append(VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=60e-3))
        rotor.axial_vent.append(VentilationCirc(Zh=12, Alpha0=0, D0=10e-3, H0=70e-3))

        stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )

        magnet2 = [MagnetType10(Lmag=0.5, Hmag=0.02, Wmag=0.04)]
        stator.slot = SlotMFlat(Zs=8, W0=0.04, W3=2 * pi / 64, H0=0.02, magnet=magnet2)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=10e-3, W2=20e-3, D0=0.02, H0=0.140)
        )
        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=20e-3, W2=40e-3, D0=0.02, H0=0.170)
        )

        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 30)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 22)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_3-Stator.png"))

        rotor.slot.magnet = []
        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 26)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_4-Rotor_no_mag.png"))

    def test_Lam_Mag_10_inset_2_mag(self):
        """Test machine plot with Magnet 10 inset with two magnet in the slot"""
        plt.close("all")

        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=100e-3,
            is_internal=True,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        rotor.slot = SlotMFlat(
            Zs=4,
            W0=0.03,
            H0=0.02,
            W3=2 * pi / 60,
            magnet=[
                MagnetType10(Lmag=0.5, Hmag=0.015, Wmag=0.03),
                MagnetType10(Lmag=0.5, Hmag=0.015, Wmag=0.03),
            ],
        )
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.axial_vent.append(VentilationCirc(Zh=4, Alpha0=0, D0=2.5e-3, H0=50e-3))
        rotor.axial_vent.append(VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=60e-3))
        rotor.axial_vent.append(VentilationCirc(Zh=12, Alpha0=0, D0=10e-3, H0=70e-3))
        stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )

        stator.slot = SlotMFlat(
            Zs=8,
            W0=0.03,
            W3=2 * pi / 64,
            H0=0.02,
            magnet=[
                MagnetType10(Lmag=0.5, Hmag=0.025, Wmag=0.03),
                MagnetType10(Lmag=0.5, Hmag=0.025, Wmag=0.03),
            ],
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=10e-3, W2=20e-3, D0=0.02, H0=0.140)
        )
        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=20e-3, W2=40e-3, D0=0.02, H0=0.170)
        )

        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 34)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_2_Mag_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 30)
        fig.savefig(join(save_path, "test_Lam_Mag_10i_3_Mag_2-Stator.png"))

    def test_Lam_Mag_11_inset(self):
        """Test machine plot with Magnet 11 inset"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        magnet = [MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 8)]
        rotor.slot = SlotMPolar(Zs=8, W0=pi / 8, H0=0.01, W3=2 * pi / 64, magnet=magnet)

        stator = LamSlotMag(
            Rint=115e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        magnet2 = [MagnetType11(Lmag=0.35, Hmag=0.03, Wmag=pi / 4)]
        stator.slot = SlotMPolar(
            Zs=4, W0=pi / 4, H0=0.02, W3=2 * pi / 64, magnet=magnet2
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_3-Stator.png"))

        rotor.slot.magnet = []
        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 2)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_4-Rotor_no_mag.png"))

    def test_Lam_Mag_11_inset_2_mag(self):
        """Test machine plot with Magnet 11 inset with two magnet in the slot"""
        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        rotor.slot = SlotMPolar(
            Zs=8,
            W0=pi / 12,
            H0=0.01,
            W3=pi / 18,
            magnet=[
                MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 12),
                MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 12),
            ],
        )

        stator = LamSlotMag(
            Rint=115e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        stator.slot = SlotMPolar(
            Zs=4,
            W0=pi / 10,
            H0=0.02,
            W3=2 * pi / 50,
            magnet=[
                MagnetType11(Lmag=0.35, Hmag=0.03, Wmag=pi / 10),
                MagnetType11(Lmag=0.35, Hmag=0.03, Wmag=pi / 10),
            ],
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 18)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_2_Mag_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_11i_3_Mag_2-Stator.png"))

    def test_Lam_Mag_12_inset(self):
        """Test machine plot with Magnet 12 inset"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.35,
            Nrvd=3,
            Wrvd=0.05,
        )
        magnet = [MagnetType12(Lmag=0.5, Hmag=0.02, Wmag=0.04)]
        rotor.slot = SlotMFlat(Zs=8, W0=0.04, H0=0.02, W3=2 * pi / 64, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.35,
            Nrvd=3,
            Wrvd=0.05,
        )
        magnet2 = [MagnetType12(Lmag=0.5, Hmag=0.03, Wmag=0.04)]
        stator.slot = SlotMFlat(Zs=4, W0=0.04, H0=0.02, W3=2 * pi / 64, magnet=magnet2)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_12i_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_12i_3-Stator.png"))

    def test_Lam_Mag_13_inset(self):
        """Test machine plot with Magnet 12 inset"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.42,
            Nrvd=4,
            Wrvd=0.02,
        )
        magnet = [MagnetType13(Lmag=0.5, Hmag=0.02, Wmag=0.04, Rtop=0.04)]
        rotor.slot = SlotMFlat(Zs=8, W0=0.04, H0=0.02, W3=2 * pi / 64, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator = LamSlotMag(
            Rint=110e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.42,
            Nrvd=4,
            Wrvd=0.02,
        )
        magnet2 = [MagnetType13(Lmag=0.5, Hmag=0.02, Wmag=0.04, Rtop=0.04)]
        stator.slot = SlotMFlat(Zs=4, W0=0.04, H0=0.025, W3=2 * pi / 64, magnet=magnet2)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(join(save_path, "test_Lam_Mag_13i_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_13i_3-Stator.png"))

    def test_Lam_Mag_14_inset(self):
        """Test machine plot with Magnet 14 inset"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.4,
            Nrvd=5,
            Wrvd=0.02,
        )
        magnet = [MagnetType14(Lmag=0.5, Hmag=0.02, Wmag=0.628, Rtop=0.04)]
        rotor.slot = SlotMPolar(Zs=4, W0=0.628, H0=0.02, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator = Lamination(
            Rint=130e-3,
            Rext=0.2,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=5,
            Wrvd=0.02,
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 6)
        fig.savefig(join(save_path, "test_Lam_Mag_14i_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 2)
        fig.savefig(join(save_path, "test_Lam_Mag_14i_3-Stator.png"))
