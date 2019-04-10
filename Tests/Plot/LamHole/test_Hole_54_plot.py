# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 13 17:45:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Tests import save_plot_path as save_path


class test_Hole_54_plot(TestCase):
    """unittest for Lamination with Hole plot"""

    def test_Lam_Hole_54_plot(self):
        """Test machine plot hole 54"""

        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamHole(
            is_internal=True, Rint=0.1, Rext=0.2, is_stator=False, L1=0.7
        )
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(
            HoleM54(Zh=8, W0=pi / 4, H0=50e-3, H1=10e-3, R1=100e-3)
        )
        test_obj.rotor.hole.append(
            HoleM54(Zh=8, W0=pi / 6, H0=25e-3, H1=10e-3, R1=100e-3)
        )

        test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s54-Rotor.png"))
        self.assertEqual(len(fig.axes[0].patches), 18)

        test_obj.rotor.hole[0].plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s54-Rotor hole.png"))
        self.assertEqual(len(fig.axes[0].patches), 1)
