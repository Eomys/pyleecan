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
from pyleecan.Classes.SlotW16 import SlotW16

from pyleecan.Tests.Plot import save_path
from pyleecan.Tests.Plot.LamWind import wind_mat, wind_mat2


class test_Lam_Wind_16_plot(TestCase):
    """unittest for Lamination with winding plot"""

    def setUp(self):
        """Run at the begining of every test to setup the machine"""
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

        self.test_obj = test_obj

    def test_Lam_Wind_16_wind_22(self):
        """Test machine plot with Slot 16 and winding rad=2, tan=2
        """
        print("\nTest plot Slot 16")
        self.test_obj.winding = WindingUD(
            user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3
        )
        self.test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s16_1-4-wind.png"))
        # 2 for lam + Zs*4 for wind
        self.assertEqual(len(fig.axes[0].patches), 26)

    def test_Lam_Wind_16_wind_tan(self):
        """Test machine plot with Slot 16 and winding rad=1, tan=2
        """
        self.test_obj.winding = WindingCW2LT(qs=3, p=3, Lewout=60e-3)
        self.test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s16_2-tan-wind.png"))
        # 2 for lam + Zs*2 for wind
        self.assertEqual(len(fig.axes[0].patches), 14)

    def test_Lam_Wind_16_wind_rad(self):
        """Test machine plot with Slot 16 and winding rad=2, tan=1
        """
        self.test_obj.winding = WindingUD(
            user_wind_mat=wind_mat2, qs=3, p=3, Lewout=60e-3
        )
        self.test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s16_3-rad-wind.png"))
        # 2 for lam + Zs*2 for wind
        self.assertEqual(len(fig.axes[0].patches), 14)
