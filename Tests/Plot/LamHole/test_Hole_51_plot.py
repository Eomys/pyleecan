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
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Tests.Plot import save_path


class test_Hole_51_plot(TestCase):
    """unittest for Lamination with Hole 51 plot"""

    def setUp(self):
        """Run at the begining of every test to setup the machine"""
        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamHole(
            Rint=45e-3 / 2, Rext=81.5e-3, is_stator=False, is_internal=True, L1=0.9
        )
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(
            HoleM51(
                Zh=8,
                W0=0.016,
                W1=pi / 6,
                W2=0.004,
                W3=0.01,
                W4=0.002,
                W5=0.01,
                W6=0.002,
                W7=0.01,
                H0=0.01096,
                H1=0.0015,
                H2=0.0055,
            )
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1.2)

        test_obj.stator = Lamination(
            Rint=0.09, Rext=0.12, is_internal=False, is_stator=True, L1=0.9
        )
        test_obj.frame = Frame(Rint=0.12, Rext=0.12, Lfra=0.7)
        self.test_obj = test_obj

    def test_Lam_Hole_51_012(self):
        """Test machine plot hole 51 with all magnets
        """
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.hole[0].magnet_2 = Magnet()

        self.test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_1-Machine_012.png"))
        # Rotor + 2 for stator + 0 for frame + 1 for shaft
        self.assertEqual(len(fig.axes[0].patches), 61)

        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_1-Rotor_012.png"))
        # 2 for lam + 7*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 58)

    def test_Lam_Hole_51_N12(self):
        """Test machine plot hole 51 with no magnet_0
        """
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.hole[0].magnet_2 = Magnet()
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_2-Rotor_N12.png"))
        # 2 for lam + 5*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 42)

    def test_Lam_Hole_51_0N2(self):
        """Test machine plot hole 51 with no magnet_1
        """
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.hole[0].magnet_2 = Magnet()
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_3-Rotor_0N2.png"))
        # 2 for lam + 5*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 42)

    def test_Lam_Hole_51_NN2(self):
        """Test machine plot hole 51 with no magnet_0 and no magnet_1
        """
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.hole[0].magnet_2 = Magnet()
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_4-Rotor_NN2.png"))
        # 2 for lam + 3*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 26)

    def test_Lam_Hole_51_01N(self):
        """Test machine plot hole 51 with no magnet_2
        """
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.hole[0].magnet_2 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_5-Rotor_01N.png"))
        # 2 for lam + 5*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 42)

    def test_Lam_Hole_51_N1N(self):
        """Test machine plot hole 51 with no magnet_0 and no magnet_2
        """
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.hole[0].magnet_2 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_6-Rotor_N1N.png"))
        # 2 for lam + 3*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 26)

    def test_Lam_Hole_51_0NN(self):
        """Test machine plot hole 51 with no magnet_1 and no magnet_2
        """
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.hole[0].magnet_2 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_7-Rotor_0NN.png"))
        # 2 for lam + 3*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 26)

    def test_Lam_Hole_51_NNN(self):
        """Test machine plot hole 51 with no magnet
        """
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.hole[0].magnet_2 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_51_s51_8-Rotor_NNN.png"))
        # 2 for lam + 1*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 10)
