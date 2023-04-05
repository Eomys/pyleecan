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
from pyleecan.Classes.HoleMLSRPM import HoleMLSRPM
from Tests import save_plot_path as save_path
from pyleecan.Classes.SlotWLSRPM import SlotWLSRPM


"""unittest for Lamination with Hole LSRPM plot"""


@pytest.fixture
def machine():
    """Run at the begining of every test to setup the machine"""
    plt.close("all")
    test_obj = MachineIPMSM()
    test_obj.rotor = LamHole(
        Rint=14e-3, Rext=50e-3, is_stator=False, is_internal=True, L1=0.95
    )
    test_obj.rotor.hole = list()
    test_obj.rotor.hole.append(
        HoleMLSRPM(
            Zh=8,
            W0=3.88e-3,
            W1=12.6 / 180 * pi,
            W2=0.0007,
            H1=0.0023515058436089,
            R1=0.0003,
            R2=0.019327,
            R3=0.0165,
        )
    )
    test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=0.95)
    test_obj.stator = LamSlotWind(
        Rint=50.7e-3,
        Rext=72.5e-3,
        is_internal=False,
        is_stator=True,
        L1=0.95,
        slot=None,
    )
    test_obj.frame = Frame(Rint=0.12, Rext=0.12, Lfra=0.95)
    return test_obj


def test_Lam_Hole_LSRPM(machine):
    """Test machine plot hole LSRPM with magnet"""

    machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_sLSRPM_1-Machine.png"))
    assert len(fig.axes[0].patches) == 31

    machine.rotor.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Hole_sLSRPM_2-Rotor.png"))

    assert len(fig.axes[0].patches) == 26


def test_Lam_Hole_LSRPM_no_mag(machine):
    """Test machine plot hole LSRPM without magnet"""
    machine.rotor.hole[0].magnet_0 = None
    machine.rotor.plot(is_show_fig=False)
    fig = plt.gcf()

    assert len(fig.axes[0].patches) == 10
    fig.savefig(
        join(save_path, "test_Lam_Hole_sLSRPM_3-Rotor hole without " "magnet.png")
    )


def test_Lam_Hole_LSRPM_mag_mass(machine):
    """Test calculate the magnet mass"""
    machine.rotor.hole[0].comp_mass_magnet()


def test_Lam_Hole_LSRPM_mag_surface(machine):
    """Test calculate the magnet mass"""
    machine.rotor.hole[0].comp_surface_magnet()


def test_Lam_Hole_LSRPM_mag_volume(machine):
    """Test calculate the magnet mass"""
    machine.rotor.hole[0].comp_volume_magnet()
