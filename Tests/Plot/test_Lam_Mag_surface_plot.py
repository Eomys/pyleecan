# -*- coding: utf-8 -*-

from os.path import join
import pytest

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
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
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.SlotMPolar import SlotMPolar
from Tests import save_plot_path as save_path


@pytest.mark.PLOT
class Test_Lam_Mag_surface_plot(object):
    """pytest for Lamination with surface magnet plot"""

    def test_Lam_Mag_10_surface(self):
        """Test machine plot with Magnet 10 surface"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=200e-3,
            is_internal=True,
            is_stator=False,
            L1=0.5,
            Nrvd=0,
            Wrvd=0.05,
        )
        magnet = [MagnetType10(Lmag=0.5, Hmag=0.02, Wmag=0.08)]
        rotor.slot = SlotMFlat(
            Zs=8, H0=0, W0=2 * pi / 10, W0_is_rad=True, magnet=magnet
        )
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_10s_2-Rotor.png"))

        magnet2 = [MagnetType10(Lmag=0.5, Hmag=0.02, Wmag=0.04)]
        rotor.slot = SlotMFlat(Zs=8, W0=0.04, W0_is_rad=False, magnet=magnet2)
        rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Mag_10s_5-Rotor 2.png"))

    def test_Lam_Mag_11_surface(self):
        """Test machine plot with Magnet 11 surface"""

        plt.close("all")
        rotor = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=True,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        magnet = [MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 8)]
        rotor.slot = SlotMPolar(Zs=8, W0=pi / 8, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator = LamSlotMag(
            Rint=115e-3,
            Rext=200e-3,
            is_internal=False,
            is_stator=True,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        magnet2 = [MagnetType11(Lmag=0.5, Hmag=0.01, Wmag=pi / 4)]
        stator.slot = SlotMPolar(Zs=4, W0=pi / 4, magnet=magnet2)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_11s_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        patches = fig.axes[0].patches
        assert len(patches) == 6
        assert isinstance(patches[0], Circle)
        assert patches[0].get_radius() == 200e-3
        assert patches[0].get_facecolor() == (0.0, 0.0, 1.0, 1.0)
        for i in range(1, 6):
            assert isinstance(patches[i], Polygon)
            if i == 1:
                assert patches[i].get_facecolor() == (1.0, 1.0, 1.0, 1.0)  # White
            else:  # Magnet
                assert patches[i].get_facecolor() == (0.75, 0.75, 0.75, 1.0)  # Gray
        fig.savefig(join(save_path, "test_Lam_Mag_11s_3-Stator.png"))

    def test_Lam_Mag_12_surface(self):
        """Test machine plot with Magnet 12 surface"""
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
        magnet = [MagnetType12(Lmag=0.5, Hmag=0.02, Wmag=0.06)]
        rotor.slot = SlotMFlat(Zs=8, W0=0.06, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator = Lamination(
            Rint=130e-3,
            Rext=0.2,
            is_internal=False,
            is_stator=True,
            L1=0.4,
            Nrvd=2,
            Wrvd=0.05,
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_12s_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_12s_3-Stator.png"))

    def test_Lam_Mag_13_surface(self):
        """Test machine plot with Magnet 13 surface"""

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
        magnet = [MagnetType13(Lmag=0.5, Hmag=0.02, Wmag=0.08, Rtop=0.0601)]
        rotor.slot = SlotMFlat(Zs=4, W0=0.08, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator = Lamination(
            Rint=130e-3,
            Rext=0.2,
            is_internal=False,
            is_stator=True,
            L1=0.35,
            Nrvd=3,
            Wrvd=0.05,
        )
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 6
        fig.savefig(join(save_path, "test_Lam_Mag_13s_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 2
        fig.savefig(join(save_path, "test_Lam_Mag_13s_3-Stator.png"))

    def test_Lam_Mag_14_surface(self):
        """Test machine plot with Magnet 14 surface"""

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
        magnet = [MagnetType14(Lmag=0.5, Hmag=0.02, Wmag=0.628, Rtop=0.05)]
        rotor.slot = SlotMPolar(Zs=8, W0=0.628, magnet=magnet)
        rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        stator = LamSlotMag(
            Rint=150e-3,
            Rext=0.2,
            is_internal=False,
            is_stator=True,
            L1=0.42,
            Nrvd=4,
            Wrvd=0.02,
        )
        magnet = [MagnetType14(Lmag=0.5, Hmag=0.02, Wmag=0.628, Rtop=0.05)]
        stator.slot = SlotMPolar(Zs=8, W0=0.628, magnet=magnet)
        stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        rotor.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_14s_2-Rotor.png"))

        stator.plot()
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 10
        fig.savefig(join(save_path, "test_Lam_Mag_14s_3-Stator.png"))
