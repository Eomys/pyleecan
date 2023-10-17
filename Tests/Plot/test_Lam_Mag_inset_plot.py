# -*- coding: utf-8 -*-
from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.SlotM13 import SlotM13
from pyleecan.Classes.SlotM14 import SlotM14
from pyleecan.Classes.SlotM15 import SlotM15
from pyleecan.Classes.SlotM16 import SlotM16
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.MatMagnetics import MatMagnetics
from Tests import save_plot_path as save_path


class Test_Lam_Mag_inset_plot(object):
    """pytest for Lamination with inset magnet plot"""

    def test_Lam_Mag_10_inset(self):
        """Test machine plot with SlotM10 inset"""

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
        rotor.magnet.Lmag = 0.5
        rotor.slot = SlotM10(Zs=4, W0=0.04, H0=0.02, H1=0.02, W1=0.04)
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
        stator.magnet.Lmag = 0.5
        stator.slot = SlotM10(Zs=8, W0=0.04, H1=0.02, W1=0.04, H0=0.02)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=10e-3, W2=20e-3, D0=0.02, H0=0.140)
        )
        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=20e-3, W2=40e-3, D0=0.02, H0=0.170)
        )

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 30
        fig.savefig(join(save_path, "test_Lam_Mag_10i_1-Rotor.png"))

        stator.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 22
        fig.savefig(join(save_path, "test_Lam_Mag_10i_2-Stator.png"))

        rotor.slot.H1 = rotor.slot.H1 * 1.2
        rotor.slot.W1 = rotor.slot.W1 * 0.5
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 30
        fig.savefig(join(save_path, "test_Lam_Mag_10i_3-Rotor_missmatch.png"))

        rotor.magnet = None
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 26
        fig.savefig(join(save_path, "test_Lam_Mag_10i_4-Rotor_no_mag.png"))

    @pytest.mark.skip(reason="No multi magnet for now")
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
                SlotM10(Lmag=0.5, H1=0.015, W1=0.03),
                SlotM10(Lmag=0.5, H1=0.015, W1=0.03),
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
                SlotM10(Lmag=0.5, H1=0.025, W1=0.03),
                SlotM10(Lmag=0.5, H1=0.025, W1=0.03),
            ],
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=10e-3, W2=20e-3, D0=0.02, H0=0.140)
        )
        stator.axial_vent.append(
            VentilationTrap(Zh=6, Alpha0=pi / 6, W1=20e-3, W2=40e-3, D0=0.02, H0=0.170)
        )

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 34
        fig.savefig(join(save_path, "test_Lam_Mag_10i_2_Mag_2-Rotor.png"))

        stator.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 30
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
        rotor.magnet.Lmag = 0.5
        rotor.slot = SlotM11(Zs=8, W0=pi / 8, H0=0.01, H1=0.01, W1=pi / 8)

        stator = LamSlotMag(
            Rint=115e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        stator.magnet.Lmag = 0.35
        stator.slot = SlotM11(
            Zs=4,
            W0=pi / 4,
            H1=0.03,
            W1=pi / 4,
            H0=0.02,
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_11i_1-Rotor.png"))

        stator.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_11i_2-Stator.png"))

        rotor.slot.H1 = rotor.slot.H1 * 1.2
        rotor.slot.W1 = rotor.slot.W1 * 0.5
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_11i_3-Rotor_missmatch.png"))

        rotor.magnet = None
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_11i_4-Rotor_no_mag.png"))

    @pytest.mark.skip(reason="Only one magnet for now")
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
                SlotM11(Lmag=0.5, H1=0.01, W1=pi / 12),
                SlotM11(Lmag=0.5, H1=0.01, W1=pi / 12),
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
                SlotM11(Lmag=0.35, H1=0.03, W1=pi / 10),
                SlotM11(Lmag=0.35, H1=0.03, W1=pi / 10),
            ],
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 18
        fig.savefig(join(save_path, "test_Lam_Mag_11i_2_Mag_2-Rotor.png"))

        stator.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
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
        rotor.magnet.Lmag = 0.5
        rotor.slot = SlotM12(Zs=8, W0=0.04, H0=0.02, H1=0.02, W1=0.04)
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
        stator.magnet.Lmag = 0.5
        stator.slot = SlotM12(Zs=4, W0=0.04, H0=0.02, H1=0.03, W1=0.04)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_12i_1-Rotor.png"))

        stator.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_12i_2-Stator.png"))

        rotor.slot.H1 = rotor.slot.H1 * 1.2
        rotor.slot.W1 = rotor.slot.W1 * 0.5
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_12i_3-Rotor_missmatch.png"))

        rotor.magnet = None
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_12i_4-Rotor_no_mag.png"))

    def test_Lam_Mag_13_inset(self):
        """Test machine plot with Magnet 13 inset"""

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
        rotor.magnet.Lmag = 0.5
        rotor.slot = SlotM13(Zs=8, W0=0.04, H0=0.02, H1=0.02, W1=0.04, Rtopm=0.04)
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
        stator.magnet.Lmag = 0.5
        stator.slot = SlotM13(Zs=4, W0=0.04, H0=0.025, H1=0.02, W1=0.04, Rtopm=0.04)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_13i_1-Rotor.png"))

        stator.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_13i_2-Stator.png"))

        rotor.slot.W1 = rotor.slot.W1 * 0.5
        rotor.slot.H1 = rotor.slot.H1 * 1.4
        rotor.slot.Rtopm = rotor.slot.Rtopm * 0.5
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_13i_3-Rotor_missmatch.png"))

        rotor.magnet = None
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_13i_4-Rotor_No_mag.png"))

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
        rotor.magnet.Lmag = 0.5
        rotor.slot = SlotM14(Zs=4, W0=0.628, H0=0.02, H1=0.02, W1=0.628, Rtopm=0.04)
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

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_14i_1-Rotor.png"))

        rotor.slot.W1 = rotor.slot.W1 * 0.5
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_14i_2-Rotor_missmatch.png"))

        rotor.magnet = None
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_14i_3-Rotor_no_mag.png"))

    def test_Lam_Mag_15_inset(self):
        """Test machine plot with Magnet 15 inset"""

        plt.close("all")
        mm = 1e-3
        rotor = LamSlotMag(Rint=40 * mm, Rext=110 * mm, is_internal=True)
        rotor.slot = SlotM15(
            Zs=4,
            W0=80 * pi / 180,
            H0=10 * mm,
            H1=20 * mm,
            W1=100 * mm,
            Rtopm=100 * mm,
        )

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_15i_1-Rotor.png"))

        rotor.slot.W1 = rotor.slot.W1 * 0.5
        rotor.slot.Rtopm = rotor.slot.Rtopm * 0.5
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_15i_2-Rotor_missmatch.png"))

        rotor.magnet = None
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_15i_3-Rotor_No_mag.png"))

    def test_Lam_Mag_16_inset(self):
        """Test machine plot with SlotM10 inset"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=80e-3,
            Rext=200e-3,
            is_internal=True,
            is_stator=False,
        )
        rotor.slot = SlotM16(Zs=4, W0=0.02, H0=0.02, H1=0.08, W1=0.04)

        stator = LamSlotMag(
            Rint=220e-3,
            Rext=400e-3,
            is_internal=False,
            is_stator=True,
        )
        stator.slot = SlotM16(Zs=8, W0=0.02, H0=0.02, H1=0.08, W1=0.04)

        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_16i_1-Rotor.png"))

        stator.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_16i_2-Stator.png"))

        rotor.magnet = None
        rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_16i_3-Rotor_no_mag.png"))
