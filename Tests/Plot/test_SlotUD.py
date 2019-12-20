# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 13 17:33:49 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""
from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.MachineSRM import MachineSRM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotUD import SlotUD
from pyleecan.Classes.VentilationTrap import VentilationTrap

from pyleecan.Tests import save_plot_path as save_path


class test_SlotUD(TestCase):
    """unittest for UserDefined slot + animation
    """

    def test_christmas(self):
        """Test User Defined slot "snowflake"
        """

        plt.close("all")
        Rrotor = abs(0.205917893677990 - 0.107339745962156j)
        test_obj = MachineSRM()
        # Stator definintion
        test_obj.stator = LamSlotWind(
            Rint=Rrotor + 5e-3, Rext=Rrotor + 120e-3, is_internal=False, is_stator=True
        )
        test_obj.stator.slot = SlotW21(
            Zs=36, W0=7e-3, H0=10e-3, H1=0, H2=70e-3, W1=30e-3, W2=0.1e-3
        )
        test_obj.stator.winding = WindingDW2L(qs=3, p=3, coil_pitch=5)

        # Rotor definition
        test_obj.rotor = LamSlot(
            Rint=0.02, Rext=Rrotor, is_internal=True, is_stator=False
        )
        test_obj.rotor.axial_vent = [
            VentilationTrap(Zh=6, Alpha0=0, D0=0.025, H0=0.025, W1=0.015, W2=0.04)
        ]
        # Complex coordinates of the snowflake slot
        point_list = [
            0.205917893677990 - 0.107339745962156j,
            0.187731360198517 - 0.0968397459621556j,
            0.203257639640145 - 0.0919474411167423j,
            0.199329436409870 - 0.0827512886940357j,
            0.174740979141750 - 0.0893397459621556j,
            0.143564064605510 - 0.0713397459621556j,
            0.176848674296337 - 0.0616891108675446j,
            0.172822394854708 - 0.0466628314259158j,
            0.146001886779019 - 0.0531173140978201j,
            0.155501886779019 - 0.0366628314259158j,
            0.145109581933606 - 0.0306628314259158j,
            0.127109581933606 - 0.0618397459621556j,
            0.0916025403784439 - 0.0413397459621556j,
            0.134949327895761 - 0.0282609076372691j,
            0.129324972242779 - 0.0100025773880714j,
            0.0690858798800485 - 0.0283397459621556j,
            0.0569615242270663 - 0.0213397459621556j,
        ]
        test_obj.rotor.slot = SlotUD(Zs=6, is_sym=True, point_list=point_list)

        # Plot, check and save
        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 83)
        fig.savefig(join(save_path, "test_Christmas.png"))
