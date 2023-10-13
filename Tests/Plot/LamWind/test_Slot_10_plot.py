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
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Methods import ParentMissingError, NotImplementedYetError

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat

import pytest


"""pytest for Lamination with winding plot"""


class Test_Slot_10_plot(object):
    def test_Lam_Wind_10_wind_22(self):
        """Test machine plot with Slot 10 and winding rad=2, tan=2"""
        print("\nTest plot Slot 10")
        plt.close("all")
        test_obj = MachineDFIM()
        test_obj.rotor = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.rotor.slot = SlotW10(
            Zs=6,
            W0=50e-3,
            W1=90e-3,
            W2=100e-3,
            H0=20e-3,
            H1=35e-3,
            H2=130e-3,
            H1_is_rad=False,
        )
        test_obj.rotor.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1)

        test_obj.stator = LamSlotWind(
            Rint=0.51,
            Rext=0.8,
            is_internal=False,
            is_stator=True,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.stator.slot = SlotW10(
            Zs=6,
            W0=50e-3,
            W1=80e-3,
            W2=50e-3,
            H0=15e-3,
            H1=25e-3,
            H2=140e-3,
            H1_is_rad=False,
        )
        test_obj.stator.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)

        test_obj.frame = Frame(Rint=0.8, Rext=0.9, Lfra=1)
        test_obj.frame.mat_type.name = "M330_35A"

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_1-Machine.png"))
        # Rotor + Stator + 2 for frame + 1 for Shaft
        assert len(fig.axes[0].patches) == 55

        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        assert len(fig.axes[0].patches) == 26
        fig.savefig(join(save_path, "test_Lam_Wind_s10_2-Rotor.png"))
        # 2 for lam + 6*4 for wind
        assert len(fig.axes[0].patches) == 26
        # Don't display the plot
        assert len(test_obj.rotor.plot(is_display=False, is_show_fig=False)) == 26

        test_obj.stator.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_3-Stator.png"))
        # 2 for lam + 6*4 for wind
        assert len(fig.axes[0].patches) == 26

        lines = test_obj.stator.slot.build_geometry_half_tooth(is_top=False)
        surf = SurfLine(line_list=lines)
        surf.plot_lines(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_Tooth_bottom_out.png"))

        lines = test_obj.stator.slot.build_geometry_half_tooth(is_top=True)
        surf = SurfLine(line_list=lines)
        surf.plot_lines(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_Tooth_top_out.png"))

        lines = test_obj.rotor.slot.build_geometry_half_tooth(is_top=False)
        surf = SurfLine(line_list=lines)
        surf.plot_lines(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_Tooth_bottom_in.png"))

        lines = test_obj.rotor.slot.build_geometry_half_tooth(is_top=True)
        surf = SurfLine(line_list=lines)
        surf.plot_lines(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_Tooth_top_in.png"))

        tooth = test_obj.rotor.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_Tooth_in.png"))

        tooth = test_obj.stator.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        mesh_dict = tooth.comp_mesh_dict(5e-3)
        for ii, line in enumerate(tooth.get_lines()):
            mid = line.get_middle()
            plt.text(mid.real, mid.imag, str(mesh_dict[str(ii)]))
        fig.savefig(join(save_path, "test_Lam_Wind_s10_Tooth_out.png"))

        slot = SlotW10(
            Zs=6,
            W0=50e-3,
            W1=80e-3,
            W2=50e-3,
            H0=15e-3,
            H1=25e-3,
            H2=140e-3,
            H1_is_rad=False,
        )

        with pytest.raises(ParentMissingError) as context:
            slot.get_surface_tooth()

        test_obj.rotor.comp_wind_function(alpha_mmf0=1)

        test_obj.stator.slot = SlotW10(
            Zs=6,
            W0=50e-1,
            W1=80e-1,
            W2=50e-1,
            H0=15e-1,
            H1=25e-1,
            H2=140e-1,
            H1_is_rad=False,
        )

        lines = test_obj.stator.slot.build_geometry_half_tooth(is_top=False)
        assert len(lines) == 7

        # Testing comp_angle_d_axis
        test_obj.stator.winding = None
        assert test_obj.stator.comp_angle_d_axis() == 0

    def test_plot_stator_true(self):
        """Test if the plot is right with a stator LamSlotWind"""
        plt.close("all")
        test_obj = MachineDFIM()

        test_obj.stator = LamSlotWind(
            Rint=0.51,
            Rext=0.8,
            is_internal=False,
            is_stator=True,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.stator.slot = SlotW10(
            Zs=6,
            W0=50e-3,
            W1=80e-3,
            W2=50e-3,
            H0=15e-3,
            H1=25e-3,
            H2=140e-3,
            H1_is_rad=False,
        )
        test_obj.stator.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)

        test_obj.frame = Frame(Rint=0.8, Rext=0.9, Lfra=1)
        test_obj.frame.mat_type.name = "M330_35A"

        test_obj.stator.plot(is_show_fig=False)

        # The rotor will be blue

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s10_Stator.png"))

        result = test_obj.stator.plot(is_display=False)
        # 2 lam + 4*6 wind
        assert len(result) == 26


if __name__ == "__main__":
    a = Test_Slot_10_plot()
    a.test_Lam_Wind_10_wind_22()
    a.test_plot_stator_true()
    print("Done")
