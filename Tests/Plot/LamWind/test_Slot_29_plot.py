# -*- coding: utf-8 -*-
"""
@date Created on Tue Jan 12 13:54:56 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.MatLamination import MatLamination
from pyleecan.Classes.SlotW29 import SlotW29

from pyleecan.Tests import save_plot_path as save_path
from pyleecan.Tests.Plot.LamWind import wind_mat


class test_Lam_Wind_29_plot(TestCase):
    """unittest for Lamination with winding plot"""

    def test_Lam_Wind_29_wind_22(self):
        """Test machine plot with Slot 29 and winding rad=2, tan=2
        """
        print("\nTest plot Slot 29")
        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotWind(
            Rint=0.1, Rext=0.5, is_internal=True, is_stator=False, L1=0.9, Nrvd=2
        )
        test_obj.rotor.axial_vent = [
            VentilationCirc(Zh=6, Alpha0=pi / 6, D0=60e-3, H0=0.35)
        ]
        test_obj.rotor.slot = SlotW29(
            Zs=6, W0=0.05, H0=0.05, H1=0.1, W1=0.1, H2=0.2, W2=0.15
        )
        test_obj.rotor.winding = WindingUD(
            user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3
        )
        test_obj.rotor.mat_type.mag = MatLamination(Wlam=0.5e-3)
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
        test_obj.stator.winding = WindingUD(
            user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3
        )
        test_obj.stator.mat_type.mag = MatLamination(Wlam=0.5e-3)
        test_obj.frame = Frame(Rint=0.8, Rext=0.9, Lfra=1)

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_1-Machine.png"))
        # rotor+stator+ 2 for frame + 1 for Shaft
        self.assertEqual(len(fig.axes[0].patches), 61)

        test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_2-Rotor.png"))
        # 2 for lam, 4*Zs for wind + 6 vent
        self.assertEqual(len(fig.axes[0].patches), 32)

        test_obj.stator.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s29_3-Stator.png"))
        # 2 for lam, 4*Zs for wind
        self.assertEqual(len(fig.axes[0].patches), 26)
