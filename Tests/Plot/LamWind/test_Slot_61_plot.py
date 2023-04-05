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
from pyleecan.Classes.SlotW61 import SlotW61

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat

import pytest

"""pytest for Lamination with winding plot"""


class Test_Slot_61_plot(object):
    def test_Lam_Wind_61(self):
        """Test machine plot with Slot 61"""
        print("\nTest plot Slot 61")
        plt.close("all")
        test_obj = MachineDFIM()
        test_obj.rotor = LamSlotWind(
            Rint=0, Rext=0.1325, is_internal=True, is_stator=False, L1=0.9
        )
        test_obj.rotor.slot = SlotW61(
            Zs=12,
            W0=15e-3,
            W1=35e-3,
            W2=12.5e-3,
            H0=15e-3,
            H1=20e-3,
            H2=25e-3,
            H3=1e-3,
            H4=2e-3,
            W3=3e-3,
        )
        test_obj.rotor.winding = WindingUD(qs=3, p=3, Lewout=60e-3)
        test_obj.rotor.winding.init_as_CW2LT()
        plt.close("all")

        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s61_1-Rotor.png"))
        # 1 for Lam, Zs*2 for wind
        assert len(fig.axes[0].patches) == 26

        test_obj.rotor.slot.W3 = 0
        test_obj.rotor.slot.H3 = 0
        test_obj.rotor.slot.H4 = 0
        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s61_2-Rotor Wind.png"))
        # 1 for Lam, Zs*2 for wind
        assert len(fig.axes[0].patches) == 26

        tooth = test_obj.rotor.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s61_Tooth_in.png"))
