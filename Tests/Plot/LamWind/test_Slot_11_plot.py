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
from pyleecan.Classes.SlotW11 import SlotW11

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat

import pytest

"""pytest for Lamination with winding plot"""


class Test_Slot_11_plot(object):
    def test_Lam_Wind_11_wind_22(self):
        """Test machine plot with Slot 11 and winding rad=2, tan=2"""
        print("\nTest plot Slot 11")
        plt.close("all")
        test_obj = MachineDFIM()
        test_obj.rotor = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        test_obj.rotor.axial_vent = [
            VentilationCirc(Zh=6, Alpha0=pi / 6, D0=60e-3, H0=0.35)
        ]
        test_obj.rotor.slot = SlotW11(
            Zs=6,
            W0=50e-3,
            W1=60e-3,
            W2=70e-3,
            H0=20e-3,
            H1=35e-3,
            H2=130e-3,
            H1_is_rad=False,
            R1=10e-3,
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
        test_obj.stator.slot = SlotW11(
            Zs=18,
            W0=40e-3,
            W1=60e-3,
            W2=90e-3,
            H0=15e-3,
            H1=35e-3,
            H2=140e-3,
            H1_is_rad=False,
            R1=40e-3,
        )
        test_obj.stator.winding.Lewout = 60e-3
        test_obj.stator.winding = Winding(qs=3, p=3, Nlayer=2, coil_pitch=2)
        test_obj.stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=0.8, Rext=0.9, Lfra=1)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s11_1-Machine.png"))
        # Rotor + Stator + 2 for frame + 1 for Shaft
        assert len(fig.axes[0].patches) == 77

        test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s11_2-Rotor.png"))
        # 2 for lam + Zs*4 for wind + 6 vents
        assert len(fig.axes[0].patches) == 34

        test_obj.stator.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s11_3-Stator.png"))
        # 2 for lam + Zs*2 for wind
        assert len(fig.axes[0].patches) == 40

        tooth = test_obj.rotor.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s11_Tooth_in.png"))

        tooth = test_obj.stator.slot.get_surface_tooth()
        tooth.plot(color="r", is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s11_Tooth_out.png"))
