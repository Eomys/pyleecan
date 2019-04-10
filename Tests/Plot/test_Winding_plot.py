# -*- coding: utf-8 -*-
"""
@date Created on Tue Dec 16 16:45:07 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.WindingCW2LR import WindingCW2LR
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Tests import save_plot_path as save_path


class test_Winding_plot(TestCase):
    """unittest for Winding connection matrix plot"""

    def test_type_wind_CW2LT(self):
        """Test Winding matrix plot for type_winding CW2LT"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW22(Zs=6, H0=20e-3, H2=0.2, W0=pi / 10, W2=pi / 6)
        test_obj.winding = WindingCW2LT(p=2, qs=3)

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam.png"))

        test_obj.plot_winding()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_wind.png"))

        test_obj.slot = SlotW22(Zs=12, H0=20e-3, H2=0.2, W0=pi / 12, W2=pi / 8)
        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam_ms=0,25.png"))

        test_obj.winding.p = 4
        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam_p=4.png"))

    def test_type_wind_CW1L(self):
        """Test Winding matrix plot for type_winding CW1L"""

        plt.close("all")
        # Artificial winding for test purpose
        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=36, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingCW1L(p=3, qs=3)

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW1L_lam.png"))

        test_obj.plot_winding()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW1L_wind.png"))

        test_obj.slot.Zs = 20
        test_obj.winding.qs = 5

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW1L_lam2.png"))

        test_obj.plot_winding()
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

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_lam.png"))

        test_obj.plot_winding()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_wind.png"))

        test_obj.slot.Zs = 24
        test_obj.winding = WindingDW2L(p=1, qs=3, coil_pitch=10)
        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_lam2.png"))

        test_obj.plot_winding()
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

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_lam.png"))

        test_obj.plot_winding()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_wind.png"))

        test_obj.slot.Zs = 36
        test_obj.winding = WindingDW1L(p=2, qs=3)
        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_lam2.png"))

        test_obj.plot_winding()
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

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_lam.png"))

        test_obj.plot_winding()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_wind.png"))

        test_obj.slot.Zs = 36
        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_lam2.png"))

        test_obj.plot_winding()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_wind2.png"))
