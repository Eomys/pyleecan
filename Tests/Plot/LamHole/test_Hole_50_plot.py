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
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.BoreFlower import BoreFlower
from Tests import save_plot_path as save_path

from pyleecan.Methods import ParentMissingError


"""unittest for Machine with Hole 50 plot"""


class Test_Hole_50_plot(object):
    @pytest.fixture
    def machine(self):
        """Run at the begining of every test to setup the machine"""
        plt.close("all")
        test_obj = MachineIPMSM()
        test_obj.rotor = LamHole(
            is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7
        )
        test_obj.rotor.bore = BoreFlower(N=8, Rarc=0.05, alpha=pi / 8)
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=2e-3,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=3e-3,
                H2=0.5e-3,
                H3=6.8e-3,
                H4=0,
            )
        )
        test_obj.rotor.axial_vent = list()
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=40e-3)
        )
        test_obj.rotor.axial_vent.append(
            VentilationCirc(Zh=8, Alpha0=pi / 8, D0=7e-3, H0=40e-3)
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1.2)

        test_obj.stator = LamSlotWind(
            Rint=0.078, Rext=0.104, is_internal=False, is_stator=True, L1=0.8
        )
        test_obj.stator.slot = None
        test_obj.stator.winding = None
        test_obj.stator.axial_vent.append(
            VentilationPolar(Zh=8, H0=0.08, D0=0.01, W1=pi / 8, Alpha0=pi / 8)
        )
        test_obj.stator.axial_vent.append(
            VentilationPolar(Zh=8, H0=0.092, D0=0.01, W1=pi / 8, Alpha0=0)
        )
        test_obj.frame = Frame(Rint=0.104, Rext=0.114, Lfra=1)

        return test_obj

    def test_Lam_Hole_50_W01(self, machine):
        """Test machine plot hole 50 with W1 > 0 and both magnets"""

        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_Rotor_W01.png"))
        # 2 for lam + (3*2)*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 66

        machine.rotor.axial_vent[0].plot(is_show_fig=False, is_all_hole=True)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_CircVent.png"))
        assert len(fig.axes[0].patches) == 8

    def test_Lam_Hole_50_N01(self, machine):
        """Test machine plot hole 50 with W1 = 0 and both magnets"""
        machine.rotor.hole[0].W1 = 0
        machine.rotor.hole[0].magnet_0 = Magnet()
        machine.rotor.hole[0].magnet_1 = Magnet()
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_RotorN01.png"))
        # 2 for lam + 5*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 58

    def test_Lam_Hole_50_WN1(self, machine):
        """Test machine plot hole 50 with W1 > 0 and only magnet_1"""
        machine.rotor.hole[0].W1 = 2e-3
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = Magnet()
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_RotorWN1.png"))
        # 2 for lam + (1+3)*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 50

    def test_Lam_Hole_50_NN1(self, machine):
        """Test machine plot hole 50 with W1 = 0 and no magnet_0"""
        machine.rotor.hole[0].W1 = 0
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = Magnet()
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_RotorNN1.png"))
        # 2 for lam + 3*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 42

    def test_Lam_Hole_50_W0N(self, machine):
        """Test machine plot hole 50 with W1 > 0 and no magnet_1"""
        machine.rotor.hole[0].W1 = 2e-3
        machine.rotor.hole[0].magnet_0 = Magnet()
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_RotorW0N.png"))
        # 2 for lam + 4*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 50

    def test_Lam_Hole_50_N0N(self, machine):
        """Test machine plot hole 50 with W1 =0 and no magnet_1"""
        machine.rotor.hole[0].W1 = 0
        machine.rotor.hole[0].magnet_0 = Magnet()
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_RotorN0N.png"))
        # 2 for lam + (1+2)*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 42

    def test_Lam_Hole_50_WNN(self, machine):
        """Test machine plot hole 50 with W1 > 0 and no magnets"""
        machine.rotor.hole[0].W1 = 2e-3
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_RotorWNN.png"))
        # 2 for lam + (1+1)*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 34

    def test_Lam_Hole_50_NNN(self, machine):
        """Test machine plot hole 50 with W1 = 0 and no magnets"""
        machine.rotor.hole[0].W1 = 0
        machine.rotor.hole[0].magnet_0 = None
        machine.rotor.hole[0].magnet_1 = None
        machine.rotor.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_RotorNNN.png"))
        # 2 for lam + 1*8 for holes + 16 vents
        assert len(fig.axes[0].patches) == 26

    def test_get_bore_line(self):
        """Test get_bore_line can return an error if the parent is missing"""
        bf = BoreFlower(N=8, Rarc=0.05, alpha=pi / 8)
        with pytest.raises(ParentMissingError) as context:
            bf.get_bore_line()

    def test_plot_stator_true(self, machine):
        """Test if the plot is right with a stator LamHole"""
        machine.rotor = LamHole(
            is_internal=True, Rint=0.021, Rext=0.075, is_stator=True, L1=0.7
        )
        machine.plot(is_show_fig=False)

        # The rotor will be blue

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s50_stator_true.png"))


if __name__ == "__main__":
    a = Test_Hole_50_plot()
    a.test_Lam_Hole_50_W01(a.machine())
    print("Done")
