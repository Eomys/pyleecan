# -*- coding: utf-8 -*-
from os.path import join

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
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.SlotW28 import SlotW28

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat

import pytest

"""pytest for Lamination with winding plot"""


class Test_Slot_28_plot(object):
    def test_Lam_Wind_28_wind_rad_tan(self):
        """Test machine plot with Slot 28 and winding rad=1, tan=2 and rad=2 and tan=1"""
        print("\nTest plot Slot 28")
        plt.close("all")
        test_obj = MachineDFIM()
        test_obj.rotor = LamSlotWind(
            Rint=35e-3,
            Rext=84e-3,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.rotor.axial_vent = [
            VentilationCirc(Zh=6, Alpha0=pi / 6, D0=15e-3, H0=0.045)
        ]
        test_obj.rotor.slot = SlotW28(
            Zs=42, W0=3.5e-3, H0=0.45e-3, R1=3.5e-3, H3=14e-3, W3=5e-3
        )
        test_obj.rotor.winding = WindingUD(qs=3, p=3)
        test_obj.rotor.winding.init_as_CW2LT()
        test_obj.rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1)

        test_obj.stator = LamSlotWind(
            Rint=85e-3,
            Rext=0.2,
            is_internal=False,
            is_stator=True,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.stator.slot = SlotW28(
            Zs=18, W0=7e-3, R1=10e-3, H0=5e-3, H3=30e-3, W3=5e-3
        )
        test_obj.stator.winding = Winding(qs=3, p=3, Nlayer=2, coil_pitch=2)
        test_obj.stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=0.2, Rext=0.25, Lfra=1)

        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_2-Rotor.png"))
        # 2 for lam + 42*2 for wind + 6 vent
        assert len(fig.axes[0].patches) == 92

        test_obj.stator.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_3-Stator.png"))
        # 2 for lam, 2*18 for wind
        assert len(fig.axes[0].patches) == 38

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_1-Machine.png"))
        # Rotor + stator + 2 for frame + 1 for Shaft
        assert len(fig.axes[0].patches) == 133

    def test_Lam_Wind_28_wind_22(self):
        """Test machine plot with Slot 28 and winding rad=2, tan=2"""
        plt.close("all")
        test_obj = MachineDFIM()
        test_obj.rotor = LamSlotWind(
            Rint=0.01,
            Rext=0.129,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.rotor.slot = SlotW28(
            Zs=6, W0=20e-3, R1=25e-3, H0=10e-3, H3=50e-3, W3=15e-3
        )
        test_obj.rotor.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1)

        test_obj.stator = LamSlotWind(
            Rint=0.13,
            Rext=0.4,
            is_internal=False,
            is_stator=True,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.stator.axial_vent = [
            VentilationCirc(Zh=6, Alpha0=pi / 6, D0=60e-3, H0=0.25)
        ]
        test_obj.stator.slot = SlotW28(
            Zs=6, W0=40e-3, R1=50e-3, H0=10e-3, H3=70e-3, W3=85e-3
        )
        test_obj.stator.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_4-Machine.png"))
        # Rotor + stator + 0 for frame + 1 for shaft
        assert len(fig.axes[0].patches) == 59

        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_5-Rotor.png"))
        # 2 for lam + 6*4 for wind
        assert len(fig.axes[0].patches) == 26

        test_obj.stator.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_6-Stator.png"))
        # 2 for lam, 4*6 for wind + 6 vents
        assert len(fig.axes[0].patches) == 32

        tooth = test_obj.rotor.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_Tooth_in.png"))

        tooth = test_obj.stator.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s28_Tooth_out.png"))


if __name__ == "__main__":
    a = Test_Slot_28_plot()
    a.test_Lam_Wind_28_wind_rad_tan()
    a.test_Lam_Wind_28_wind_22()
    print("Done")
