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
from pyleecan.Classes.HoleM51 import HoleM51
from Tests import save_plot_path as save_path


"""pytest for Lamination with Hole 51 plot"""


class Test_Hole_51_plot(object):
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

        test_obj.stator = LamSlotWind(
            Rint=0.09, Rext=0.12, is_internal=False, is_stator=True, L1=0.9, slot=None
        )
        test_obj.stator.slot = None
        test_obj.stator.winding = None
        test_obj.frame = Frame(Rint=0.12, Rext=0.12, Lfra=0.7)
        return test_obj

    def test_Lam_Hole_51_012(self, machine):
        """Test machine plot hole 51 with all magnets"""
        machine.rotor.hole[0].magnet_0 = Magnet()
        machine.rotor.hole[0].magnet_1 = Magnet()
        machine.rotor.hole[0].magnet_2 = Magnet()

        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_1-Rotor_012.png"))
        # 2 for lam + 7*8 for holes
        assert len(fig.axes[0].patches) == 58

    def test_Lam_Hole_51_N12(self, machine):
        """Test machine plot hole 51 with no magnet_0"""
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = Magnet()
        machine.rotor.hole[0].magnet_2 = Magnet()
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_2-Rotor_N12.png"))
        # 2 for lam + 5*8 for holes
        assert len(fig.axes[0].patches) == 42

    def test_Lam_Hole_51_0N2(self, machine):
        """Test machine plot hole 51 with no magnet_1"""
        machine.rotor.hole[0].magnet_0 = Magnet()
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.hole[0].magnet_2 = Magnet()
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_3-Rotor_0N2.png"))
        # 2 for lam + 5*8 for holes
        assert len(fig.axes[0].patches) == 42

    def test_Lam_Hole_51_NN2(self, machine):
        """Test machine plot hole 51 with no magnet_0 and no magnet_1"""
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.hole[0].magnet_2 = Magnet()
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_4-Rotor_NN2.png"))
        # 2 for lam + 3*8 for holes
        assert len(fig.axes[0].patches) == 26

    def test_Lam_Hole_51_01N(self, machine):
        """Test machine plot hole 51 with no magnet_2"""
        machine.rotor.hole[0].magnet_0 = Magnet()
        machine.rotor.hole[0].magnet_1 = Magnet()
        machine.rotor.hole[0].magnet_2 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_5-Rotor_01N.png"))
        # 2 for lam + 5*8 for holes
        assert len(fig.axes[0].patches) == 42

    def test_Lam_Hole_51_N1N(self, machine):
        """Test machine plot hole 51 with no magnet_0 and no magnet_2"""
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = Magnet()
        machine.rotor.hole[0].magnet_2 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_6-Rotor_N1N.png"))
        # 2 for lam + 3*8 for holes
        assert len(fig.axes[0].patches) == 26

    def test_Lam_Hole_51_0NN(self, machine):
        """Test machine plot hole 51 with no magnet_1 and no magnet_2"""
        machine.rotor.hole[0].magnet_0 = Magnet()
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.hole[0].magnet_2 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_7-Rotor_0NN.png"))
        # 2 for lam + 3*8 for holes
        assert len(fig.axes[0].patches) == 26

    def test_Lam_Hole_51_NNN(self, machine):
        """Test machine plot hole 51 with no magnet"""
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.hole[0].magnet_2 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s51_8-Rotor_NNN.png"))
        # 2 for lam + 1*8 for holes
        assert len(fig.axes[0].patches) == 10
