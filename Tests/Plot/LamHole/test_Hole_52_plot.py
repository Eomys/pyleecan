# -*- coding: utf-8 -*-

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
from pyleecan.Classes.HoleM52 import HoleM52
from Tests import save_plot_path as save_path


"""pytest for Lamination with Hole 52 plot"""


class Test_Hole_52_plot(object):
    @pytest.fixture
    def machine(self):
        """Run at the begining of every test to setup the machine"""
        plt.close("all")
        test_obj = MachineIPMSM()
        test_obj.rotor = LamHole(
            Rint=45e-3 / 2, Rext=81.5e-3, is_stator=False, is_internal=True, L1=0.9
        )
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(
            HoleM52(Zh=8, W0=27e-3, W3=16.2e-3, H0=1e-3, H1=5e-3, H2=1e-3)
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1.2)

        test_obj.stator = LamSlotWind(
            Rint=0.09, Rext=0.12, is_internal=False, is_stator=True, L1=0.9, slot=None
        )
        test_obj.stator.slot = None
        test_obj.stator.winding = None

        test_obj.frame = Frame(Rint=0.12, Rext=0.12, Lfra=0.7)
        return test_obj

    def test_Lam_Hole_52(self, machine):
        """Test machine plot hole 52 with magnet"""
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s52_2-Rotor.png"))
        # 2 for lam + 3*8 for holes
        assert len(fig.axes[0].patches) == 26

    def test_Lam_Hole_52_no_mag(self, machine):
        """Test machine plot hole 52 without magnet"""
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        # 2 for lam + 1*8 for holes
        assert len(fig.axes[0].patches) == 10
        fig.savefig(
            join(save_path, "test_Lam_Hole_s52_3-Rotor hole without " "magnet.png")
        )
