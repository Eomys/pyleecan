# -*- coding: utf-8 -*-
import pytest

from os.path import join

import matplotlib.pyplot as plt
from numpy import pi, linspace

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from Tests import save_plot_path as save_path


class Test_Winding_plot(object):
    """unittest for Winding connection matrix plot"""

    def test_type_wind_CW2LT(self):
        """Test Winding matrix plot for type_winding CW2LT"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW22(Zs=6, H0=20e-3, H2=0.2, W0=pi / 10, W2=pi / 6)
        test_obj.winding = WindingCW2LT(p=2, qs=3)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_wind.png"))

        test_obj.slot = SlotW22(Zs=12, H0=20e-3, H2=0.2, W0=pi / 12, W2=pi / 8)
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam_ms=0,25.png"))

        test_obj.winding.p = 4
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam_p=4.png"))

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False, is_stator=False)
        test_obj.slot = SlotW22(Zs=6, H0=20e-3, H2=0.2, W0=pi / 10, W2=pi / 6)
        test_obj.winding = WindingCW2LT(p=2, qs=3)
        test_obj.plot_winding(all_slot=True, is_show_fig=False)

    def test_type_wind_CW1L(self):
        """Test Winding matrix plot for type_winding CW1L"""

        plt.close("all")
        # Artificial winding for test purpose
        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=36, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingCW1L(p=3, qs=3)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW1L_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW1L_wind.png"))

        test_obj.slot.Zs = 20
        test_obj.winding.qs = 5

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW1L_lam2.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW1L_wind2.png"))

    def test_type_wind_DW2L(self):
        """Test Winding matrix plot for type_winding DW2L"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=36, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingDW2L(p=3, qs=3, coil_pitch=5)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_wind.png"))

        test_obj.slot.Zs = 24
        test_obj.winding = WindingDW2L(p=1, qs=3, coil_pitch=10)
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_lam2.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_wind2.png"))

    def test_type_wind_DW1L(self):
        """Test Winding matrix plot for type_winding DW1L"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=24, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingDW1L(p=1, qs=3)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_wind.png"))

        test_obj.slot.Zs = 36
        test_obj.winding = WindingDW1L(p=2, qs=3)
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_lam2.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_wind2.png"))

    def test_type_wind_CW2LR(self):
        """Test Winding matrix plot for type_winding CW2LR"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=12, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingCW2LR(p=5, qs=3)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_wind.png"))

        test_obj.slot.Zs = 36
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_lam2.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_wind2.png"))

    def test_plot_mmf_unit(self):
        """Test plot unit mmf"""
        stator = LamSlotWind(
            Rint=0.1325,
            Rext=0.2,
            Nrvd=0,
            L1=0.35,
            Kf1=0.95,
            is_internal=False,
            is_stator=True,
        )
        stator.slot = SlotW10(
            Zs=36, H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
        )
        stator.winding = WindingDW2L(
            qs=3, Lewout=15e-3, p=3, coil_pitch=5, Ntcoil=7, Npcp=2
        )
        stator.plot_mmf_unit(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_unit_mmf.png"))
