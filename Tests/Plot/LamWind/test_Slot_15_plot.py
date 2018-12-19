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
from pyleecan.Classes.BHCurveMat import BHCurveMat
from pyleecan.Classes.BHCurveParam import BHCurveParam
from pyleecan.Classes.MatLamination import MatLamination
from pyleecan.Classes.SlotW15 import SlotW15

from pyleecan.Tests.Plot import save_path
from pyleecan.Tests.Plot.LamWind import wind_mat


class test_Lam_Wind_15_plot(TestCase):
    """unittest for Lamination with winding plot"""

    def test_Lam_Wind_15_wind_22(self):
        """Test machine plot with Slot 15 and winding rad=2, tan=2
        """
        print("\nTest plot Slot 15")
        plt.close("all")
        test_obj = LamSlotWind(
            Rint=92.5e-3,
            Rext=0.2,
            is_internal=False,
            is_stator=True,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.slot = SlotW15(
            Zs=6, W0=10e-3, W3=30e-3, H0=5e-3, H1=20e-3, H2=50e-3, R1=15e-3, R2=10e-3
        )
        test_obj.winding = WindingUD(user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
        test_obj.mat_type.name = "Param"
        test_obj.mat_type.magnetics = MatLamination(Wlam=0.5e-3)
        BH = BHCurveParam(Bmax=1.5, mur_0=8585, mur_1=21.79, a=0.25575)
        test_obj.mat_type.magnetics.BH_curve = BH

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s15.png"))
        # 2 for lam + Zs*4 for wind
        self.assertEqual(len(fig.axes[0].patches), 26)
