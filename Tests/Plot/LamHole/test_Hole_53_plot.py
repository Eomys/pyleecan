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
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Tests import save_plot_path as save_path


"""unittest for Machine with Hole 53 plot"""


@pytest.fixture
def machine():
    """Run at the begining of every test to setup the machine"""
    plt.close("all")
    test_obj = MachineIPMSM()
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

    return test_obj


def test_Lam_Hole_53_W01(machine):
    """Test machine plot hole 53 with W1 > 0 and both magnets
    """
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_Rotor_W01.png"))
    # 2 for lam + 3*2*8 for the holes
    assert len(fig.axes[0].patches) == 50


def test_Lam_Hole_53_N01(machine):
    """Test machine plot hole 53 with W1 = 0 and both magnets
    """
    machine.rotor.hole[0].W1 = 0
    machine.rotor.hole[0].magnet_0 = Magnet()
    machine.rotor.hole[0].magnet_1 = Magnet()
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_RotorN01.png"))
    # 2 lam + 5*8 for the holes
    assert len(fig.axes[0].patches) == 42


def test_Lam_Hole_53_WN1(machine):
    """Test machine plot hole 53 with W1 > 0 and only magnet_1
    """
    machine.rotor.hole[0].W1 = 2e-3
    machine.rotor.hole[0].magnet_0 = None
    machine.rotor.hole[0].magnet_1 = Magnet()
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_RotorWN1.png"))
    # 2 for lam + (1+3)*8 for holes
    assert len(fig.axes[0].patches) == 34


def test_Lam_Hole_53_NN1(machine):
    """Test machine plot hole 53 with W1 = 0 and no magnet_0
    """
    machine.rotor.hole[0].W1 = 0
    machine.rotor.hole[0].magnet_0 = None
    machine.rotor.hole[0].magnet_1 = Magnet()
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_RotorNN1.png"))
    # 2 for lam + 3*8 for holes
    assert len(fig.axes[0].patches) == 26


def test_Lam_Hole_53_W0N(machine):
    """Test machine plot hole 53 with W1 > 0 and no magnet_1
    """
    machine.rotor.hole[0].W1 = 2e-3
    machine.rotor.hole[0].magnet_0 = Magnet()
    machine.rotor.hole[0].magnet_1 = None
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_RotorW0N.png"))
    # 2 for lam + (3+1)*8
    assert len(fig.axes[0].patches) == 34


def test_Lam_Hole_53_N0N(machine):
    """Test machine plot hole 53 with W1 =0 and no magnet_1
    """
    machine.rotor.hole[0].W1 = 0
    machine.rotor.hole[0].magnet_0 = Magnet()
    machine.rotor.hole[0].magnet_1 = None
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_RotorN0N.png"))
    # 2 for lam + 3*8 for holes
    assert len(fig.axes[0].patches) == 26


def test_Lam_Hole_53_WNN(machine):
    """Test machine plot hole 53 with W1 > 0 and no magnets
    """
    machine.rotor.hole[0].W1 = 2e-3
    machine.rotor.hole[0].magnet_0 = None
    machine.rotor.hole[0].magnet_1 = None
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_RotorWNN.png"))
    # 2 for lam + 2*8 for holes
    assert len(fig.axes[0].patches) == 18


def test_Lam_Hole_53_NNN(machine):
    """Test machine plot hole 53 with W1 = 0 and no magnets
    """
    machine.rotor.hole[0].W1 = 0
    machine.rotor.hole[0].magnet_0 = None
    machine.rotor.hole[0].magnet_1 = None
    machine.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_s53_RotorNNN.png"))
    # 2 for lam + 8 for holes
    assert len(fig.axes[0].patches) == 10
