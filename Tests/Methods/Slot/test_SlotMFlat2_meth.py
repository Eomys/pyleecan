# -*- coding: utf-8 -*-
#%%
import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMFlat2 import SlotMFlat2
from pyleecan.Classes.MagnetType10 import MagnetType10
from numpy import exp, arcsin, ndarray, pi
from pyleecan.Methods.Slot.SlotMFlat2.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotMFlat2.comp_angle_opening_magnet import (
    comp_angle_opening_magnet,
)
from pyleecan.Methods.Slot.SlotMFlat2.comp_angle_magnet import comp_angle_magnet
from pyleecan.Methods.Slot.SlotMFlat2.comp_height import comp_height
from pyleecan.Methods.Slot.SlotMFlat2.comp_surface import comp_surface
from pyleecan.Methods.Slot.SlotMFlat2.comp_W0m import comp_W0m
from pyleecan.Methods.Slot.SlotMFlat2.get_point_bottom import get_point_bottom

mm = 1e-3

# For AlmostEqual
DELTA = 1e-6


def test_SlotMFlat2_plot():
    # Internal Slot
    lam = LamSlotMag(
        slot=-1,
        L1=25 * mm,
        Rext=16.6 * mm,
        Rint=5 * mm,
        is_internal=True,
        is_stator=False,
    )
    lam.slot = SlotMFlat2(
        H1=1 * mm,
        W1=2 * mm,
        W0=4 * mm,
        W0_is_rad=False,
        H0=10 * mm,
        W3=0,
        Zs=8,
        magnet=list(),
    )
    lam.slot.magnet.append(MagnetType10(Wmag=4 * mm, Hmag=10 * mm))
    lam.plot()
    #%%
    # W0 is rad
    lam.slot.W0_is_rad = True
    lam.slot.W0 = arcsin(4 * mm / lam.slot.get_Rbo())
    lam.plot()
    # Wmag < W0
    lam.slot.magnet[0].Wmag = 2 * mm
    lam.plot()
    # Hmag < H0
    lam.slot.magnet[0].Hmag = 2 * mm
    lam.plot()
    #%%
    # Outward Slot
    lam = LamSlotMag(
        slot=-1,
        L1=25 * mm,
        Rext=30 * mm,
        Rint=16.6 * mm,
        is_internal=False,
        is_stator=False,
    )
    lam.slot = SlotMFlat2(
        H1=1 * mm,
        W1=2 * mm,
        W0=4 * mm,
        W0_is_rad=False,
        H0=10 * mm,
        W3=0,
        Zs=8,
        magnet=list(),
    )
    lam.slot.magnet.append(MagnetType10(Wmag=4 * mm, Hmag=10 * mm))
    lam.plot()
    # W0 is rad
    lam.slot.W0_is_rad = True
    lam.slot.W0 = arcsin(4 * mm / lam.slot.get_Rbo())
    lam.plot()
    # Wmag < W0
    lam.slot.magnet[0].Wmag = 2 * mm
    lam.plot()
    # Hmag < H0
    lam.slot.magnet[0].Hmag = 2 * mm
    lam.plot()
    # %%

    # %%

    lam.slot.magnet = list()
    assert lam.slot.comp_angle_opening() == 0
