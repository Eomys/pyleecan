# -*- coding: utf-8 -*-
from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.SlotWLSRPM import SlotWLSRPM

from Tests import save_plot_path as save_path

# from Tests.Plot.LamWind import wind_mat, wind_mat2


"""unittest for Lamination with winding plot"""


@pytest.fixture
def machine():
    """Run at the begining of every test to setup the machine"""
    plt.close("all")
    test_obj = LamSlotWind(
        Rint=50.7e-3,
        Rext=72.5e-3,
        is_internal=False,
        is_stator=True,
        L1=0.95,
        Nrvd=0,
        Wrvd=0,
    )
    test_obj.slot = SlotWLSRPM(
        Zs=12, W1=8e-3, W3=11.6e-3, H2=14.8e-3, R1=0.75e-3, H3=2e-3
    )

    return test_obj


# wind_mat = zeros((2, 2, 6, 4))  # Nrad, Ntan, Zs, qs
# wind_mat[0, 0, :, :] = array(
#     [[1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, -1, -1, 0], [0, -1, 0, 0, 0, 1]]
# ).T

# wind_mat[1, 0, :, :] = array(
#     [[0, 0, 0, 0, 0, 0], [-1, 0, -1, 0, 0, -1], [0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0]]
# ).T

# wind_mat[0, 1, :, :] = array(
#     [[-1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, -1, 0, 0, -1]]
# ).T

# wind_mat[1, 1, :, :] = array(
#     [[0, 0, 0, -1, -1, 0], [1, 0, 0, 0, 0, 1], [0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# ).T
###
wind_mat_LSRPM = zeros((2, 2, 12, 6))  # Nrad, Ntan, Zs, qs
wind_mat_LSRPM[0, 0, :, :] = array(
    [
        [-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0],
        [0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0],
        [0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
).T

wind_mat_LSRPM[1, 0, :, :] = array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0],
        [0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0],
        [0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1],
    ]
).T

wind_mat_LSRPM[0, 1, :, :] = array(
    [
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
).T

wind_mat_LSRPM[1, 1, :, :] = array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    ]
).T


def test_Lam_Wind_LSRPM_wind_tan(machine):
    """Test machine plot with Slot LSRPM and winding rad=1, tan=2"""
    machine.winding = WindingUD(wind_mat=wind_mat_LSRPM, qs=6, p=4, Lewout=0)
    machine.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_sLSRPM_2-tan-wind.png"))
    # 2 for lam + Zs*2 for wind
    # assert len(fig.axes[0].patches) == 26


def test_stator_slot_angle_opening(machine):
    """Test calculate the angle opening"""
    machine.slot.comp_angle_opening()


def test_stator_slot_height_damper(machine):
    """Test calculate the damper height"""
    machine.slot.comp_height_damper()


def test_stator_slot_height_wind(machine):
    """Test calculate the winding height"""
    machine.slot.comp_height_wind()


def test_stator_slot_height(machine):
    """Test calculate the total height"""
    machine.slot.comp_height()
