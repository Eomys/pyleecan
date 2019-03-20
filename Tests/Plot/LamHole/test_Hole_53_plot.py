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
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Tests.Plot import save_path


class test_Hole_53_plot(TestCase):
    """unittest for Machine with Hole 53 plot"""

    def setUp(self):
        """Run at the begining of every test to setup the machine"""
        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamHole(
            is_internal=True, Rint=0.1, Rext=0.2, is_stator=False, L1=0.7
        )
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(
            HoleM53(
                Zh=8,
                W1=15e-3,
                W2=10e-3,
                W3=40e-3,
                W4=pi / 4,
                H0=75e-3,
                H1=5e-3,
                H2=20e-3,
                H3=5e-3,
            )
        )

        self.test_obj = test_obj

    def test_Lam_Hole_53_W01(self):
        """Test machine plot hole 53 with W1 > 0 and both magnets
        """
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_Rotor_W01.png"))
        # 2 for lam + 3*2*8 for the holes
        self.assertEqual(len(fig.axes[0].patches), 50)

    def test_Lam_Hole_53_N01(self):
        """Test machine plot hole 53 with W1 = 0 and both magnets
        """
        self.test_obj.rotor.hole[0].W1 = 0
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_RotorN01.png"))
        # 2 lam + 5*8 for the holes
        self.assertEqual(len(fig.axes[0].patches), 42)

    def test_Lam_Hole_53_WN1(self):
        """Test machine plot hole 53 with W1 > 0 and only magnet_1
        """
        self.test_obj.rotor.hole[0].W1 = 2e-3
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_RotorWN1.png"))
        # 2 for lam + (1+3)*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 34)

    def test_Lam_Hole_53_NN1(self):
        """Test machine plot hole 53 with W1 = 0 and no magnet_0
        """
        self.test_obj.rotor.hole[0].W1 = 0
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_RotorNN1.png"))
        # 2 for lam + 3*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 26)

    def test_Lam_Hole_53_W0N(self):
        """Test machine plot hole 53 with W1 > 0 and no magnet_1
        """
        self.test_obj.rotor.hole[0].W1 = 2e-3
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_RotorW0N.png"))
        # 2 for lam + (3+1)*8
        self.assertEqual(len(fig.axes[0].patches), 34)

    def test_Lam_Hole_53_N0N(self):
        """Test machine plot hole 53 with W1 =0 and no magnet_1
        """
        self.test_obj.rotor.hole[0].W1 = 0
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_RotorN0N.png"))
        # 2 for lam + 3*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 26)

    def test_Lam_Hole_53_WNN(self):
        """Test machine plot hole 53 with W1 > 0 and no magnets
        """
        self.test_obj.rotor.hole[0].W1 = 2e-3
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_RotorWNN.png"))
        # 2 for lam + 2*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 18)

    def test_Lam_Hole_53_NNN(self):
        """Test machine plot hole 53 with W1 = 0 and no magnets
        """
        self.test_obj.rotor.hole[0].W1 = 0
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.hole[0].magnet_1 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_53_s53_RotorNNN.png"))
        # 2 for lam + 8 for holes
        self.assertEqual(len(fig.axes[0].patches), 10)
