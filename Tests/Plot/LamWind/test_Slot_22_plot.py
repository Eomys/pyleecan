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
from pyleecan.Classes.SlotW22 import SlotW22

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat

import pytest

"""pytest for Lamination with winding plot"""


class Test_Slot_22_plot(object):
    def test_Lam_Wind_22_wind_22(self):
        """Test machine plot with Slot 22 and winding rad=2, tan=2"""
        print("\nTest plot Slot 22")
        plt.close("all")
        test_obj = MachineDFIM()
        test_obj.rotor = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.8,
            Nrvd=4,
            Wrvd=0.05,
        )
        test_obj.rotor.slot = SlotW22(Zs=6, W0=pi / 20, W2=pi / 10, H0=20e-3, H2=150e-3)
        test_obj.rotor.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
        test_obj.rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1)

        test_obj.stator = LamSlotWind(
            Rint=0.51,
            Rext=0.8,
            is_internal=False,
            is_stator=True,
            L1=0.8,
            Nrvd=4,
            Wrvd=0.05,
        )
        test_obj.stator.slot = SlotW22(
            Zs=18, W0=pi / 20, W2=pi / 10, H0=20e-3, H2=150e-3
        )
        test_obj.stator.winding = Winding(qs=3, p=3, Nlayer=2, coil_pitch=2)
        test_obj.stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        test_obj.stator.winding.Lewout = 60e-3
        test_obj.frame = Frame(Rint=0.8, Rext=0.8, Lfra=1)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s22_1-Machine.png"))
        # Rotor + Stator + 0 for frame + 0 for shaft
        assert len(fig.axes[0].patches) == 63

        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s22_2-Rotor.png"))
        # 1 for lam + 4*6 for wind
        assert len(fig.axes[0].patches) == 25

        test_obj.stator.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s22_3-Stator.png"))
        # 2 for lam + 18*2 for wind
        assert len(fig.axes[0].patches) == 38

        tooth = test_obj.rotor.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s22_Tooth_in.png"))

        tooth = test_obj.stator.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s22_Tooth_out.png"))


if __name__ == "__main__":
    a = Test_Slot_22_plot()
    a.test_Lam_Wind_22_wind_22()
    print("Done")
