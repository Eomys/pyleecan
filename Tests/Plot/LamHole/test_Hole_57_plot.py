# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 13 17:45:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.HoleM57 import HoleM57
from Tests import save_plot_path as save_path


class Test_Hole_57_plot(object):

    """pytest for Machine with Hole 57 plot"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the machine"""
        plt.close("all")
        test_obj = MachineIPMSM()
        test_obj.rotor = LamHole(
            is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7
        )
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(
            HoleM57(
                Zh=8,
                W0=pi * 0.8,
                W1=10e-3,
                W2=0e-3,
                W3=5e-3,
                W4=10e-3,
                H1=3e-3,
                H2=5e-3,
            )
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1.2)

        test_obj.stator = LamSlotWind(
            Rint=0.078, Rext=0.104, is_internal=False, is_stator=True, L1=0.8
        )
        test_obj.stator.slot = None
        test_obj.stator.winding = None
        test_obj.frame = Frame(Rint=0.104, Rext=0.114, Lfra=1)
        self.test_obj = test_obj

    def test_Lam_Hole_57_W01(self):
        """Test machine plot hole 57 with W1 > 0 and both magnets"""
        self.test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_57_s57_Machine.png"))
        assert len(fig.axes[0].patches) == 57

        self.test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_57_s57_Rotor_W01.png"))
        # 2 for lam + (3*2)*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 50

    def test_Lam_Hole_57_N01(self):
        """Test machine plot hole 57 with W1 = 0 and both magnets"""
        self.test_obj.rotor.hole[0].W1 = 0
        self.test_obj.rotor.hole[0].magnet_0 = Magnet()
        self.test_obj.rotor.hole[0].magnet_1 = Magnet()
        self.test_obj.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_57_s57_RotorN01.png"))
        # 2 for lam + (3*2)*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 42
