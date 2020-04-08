# -*- coding: utf-8 -*-
from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from ....Classes.Frame import Frame
from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.LamSquirrelCage import LamSquirrelCage
from ....Classes.MachineDFIM import MachineDFIM
from ....Classes.Shaft import Shaft
from ....Classes.VentilationCirc import VentilationCirc
from ....Classes.VentilationPolar import VentilationPolar
from ....Classes.VentilationTrap import VentilationTrap
from ....Classes.Winding import Winding
from ....Classes.WindingUD import WindingUD
from ....Classes.WindingCW2LT import WindingCW2LT
from ....Classes.WindingDW2L import WindingDW2L
from ....Classes.SlotW16 import SlotW16

from ....Tests import save_plot_path as save_path
from ....Tests.Plot.LamWind import wind_mat, wind_mat2


"""unittest for Lamination with winding plot"""


@pytest.fixture
def machine():
    """Run at the begining of every test to setup the machine"""
    plt.close("all")
    test_obj = LamSlotWind(
        Rint=92.5e-3,
        Rext=0.2,
        is_internal=True,
        is_stator=True,
        L1=0.95,
        Nrvd=1,
        Wrvd=0.05,
    )
    test_obj.slot = SlotW16(
        Zs=6, W0=2 * pi / 60, W3=30e-3, H0=10e-3, H2=70e-3, R1=15e-3
    )

    return test_obj


def test_Lam_Wind_16_wind_22(machine):
    """Test machine plot with Slot 16 and winding rad=2, tan=2
    """
    print("\nTest plot Slot 16")
    machine.winding = WindingUD(user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
    machine.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s16_1-4-wind.png"))
    # 2 for lam + Zs*4 for wind
    assert len(fig.axes[0].patches) == 26


def test_Lam_Wind_16_wind_tan(machine):
    """Test machine plot with Slot 16 and winding rad=1, tan=2
    """
    machine.winding = WindingCW2LT(qs=3, p=3, Lewout=60e-3)
    machine.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s16_2-tan-wind.png"))
    # 2 for lam + Zs*2 for wind
    assert len(fig.axes[0].patches) == 14


def test_Lam_Wind_16_wind_rad(machine):
    """Test machine plot with Slot 16 and winding rad=2, tan=1
    """
    machine.winding = WindingUD(user_wind_mat=wind_mat2, qs=3, p=3, Lewout=60e-3)
    machine.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s16_3-rad-wind.png"))
    # 2 for lam + Zs*2 for wind
    assert len(fig.axes[0].patches) == 14


def test_Lam_Wind_16_tooth(machine):
    """Test the Slot 16 tooth plot
    """
    tooth = machine.slot.get_surface_tooth()
    tooth.plot(color="r")
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s16_Tooth_in.png"))
