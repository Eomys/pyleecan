# -*- coding: utf-8 -*-
from os.path import join

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.SlotW29 import SlotW29

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat

import pytest

"""pytest for Lamination with winding plot"""


class Test_Slot_29_plot(object):
    def test_Lam_Wind_29_wind_22(self):
        """Test machine plot with Slot 29 and winding rad=2, tan=2"""
        print("\nTest plot Slot 29")
        plt.close("all")
        test_obj = MachineDFIM()
        test_obj.rotor = LamSlotWind(
            Rint=0.1, Rext=0.5, is_internal=True, is_stator=False, L1=0.9, Nrvd=2
        )
        test_obj.rotor.axial_vent = [
            VentilationCirc(Zh=6, Alpha0=pi / 6, D0=60e-3, H0=0.35)
        ]
        test_obj.rotor.slot = SlotW29(
            Zs=6, W0=0.05, H0=0.05, H1=0.1, W1=0.1, H2=0.2, W2=0.15
        )
        test_obj.rotor.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
        test_obj.rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1)

        test_obj.stator = LamSlotWind(
            Rint=0.51,
            Rext=0.8,
            is_internal=False,
            is_stator=True,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.stator.slot = SlotW29(
            Zs=6, W0=0.05, H0=0.025, H1=0.04, W1=0.1, H2=0.15, W2=0.2
        )
        test_obj.stator.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
        test_obj.stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=0.8, Rext=0.9, Lfra=1)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_1-Machine.png"))
        # rotor+stator+ 2 for frame + 1 for Shaft
        assert len(fig.axes[0].patches) == 61

        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_2-Rotor.png"))
        # 2 for lam, 4*6 for wind + 6 vent
        assert len(fig.axes[0].patches) == 32

        test_obj.stator.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_3-Stator.png"))
        # 2 for lam, 4*6 for wind
        assert len(fig.axes[0].patches) == 26

        tooth = test_obj.rotor.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_Tooth_in.png"))

        tooth = test_obj.stator.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_Tooth_out.png"))


if __name__ == "__main__":
    a = Test_Slot_29_plot()
    a.test_Lam_Wind_29_wind_22()
    print("Done")
