# -*- coding: utf-8 -*-
from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.SlotW16 import SlotW16

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat, wind_mat2


"""pytest for Lamination with winding plot"""


class Test_Slot_16_plot(object):
    @pytest.fixture
    def lamination(self):
        """Run at the begining of every test to setup the lamination"""
        plt.close("all")
        test_obj = LamSlotWind(
            Rint=92.5e-3,
            Rext=0.2,
            is_internal=True,
            is_stator=True,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.slot = SlotW16(
            Zs=6, W0=2 * pi / 60, W3=30e-3, H0=10e-3, H2=70e-3, R1=15e-3
        )

        return test_obj

    def test_Lam_Wind_16_wind_22(self, lamination):
        """Test lamination plot with Slot 16 and winding rad=2, tan=2"""
        print("\nTest plot Slot 16")
        lamination.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
        lamination.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s16_1-4-wind.png"))
        # 2 for lam + Zs*4 for wind
        assert len(fig.axes[0].patches) == 28

    def test_Lam_Wind_16_wind_tan(self, lamination):
        """Test lamination plot with Slot 16 and winding rad=1, tan=2"""
        lamination.winding = WindingUD(qs=3, p=3)
        lamination.winding.init_as_CW2LT()
        lamination.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s16_2-tan-wind.png"))
        # 2 for lam + Zs*2 for wind
        assert len(fig.axes[0].patches) == 16

    def test_Lam_Wind_16_wind_rad(self, lamination):
        """Test lamination plot with Slot 16 and winding rad=2, tan=1"""
        lamination.winding = WindingUD(wind_mat=wind_mat2, qs=3, p=3, Lewout=60e-3)
        lamination.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s16_3-rad-wind.png"))
        # 2 for lam + Zs*2 for wind
        assert len(fig.axes[0].patches) == 16

    def test_Lam_Wind_16_tooth(self, lamination):
        """Test the Slot 16 tooth plot"""
        tooth = lamination.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s16_Tooth_in.png"))
