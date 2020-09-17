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
from pyleecan.Methods.Slot.SlotMFlat2.comp_angle_opening_slot import (
    comp_angle_opening_slot,
)
from pyleecan.Methods.Slot.SlotMFlat2.comp_height import comp_height
from pyleecan.Methods.Slot.SlotMFlat2.comp_surface import comp_surface
from pyleecan.Methods.Slot.SlotMFlat2.comp_W0m import comp_W0m
from pyleecan.Methods.Slot.SlotMFlat2.get_point_bottom import get_point_bottom
mm=1e-3

# For AlmostEqual
DELTA = 1e-6

slotW10_test = list()

# Internal Slot
lam = LamSlotMag(slot=-1, L1=25*mm, Rext=16.6*mm, Rint=5*mm, is_internal=True, is_stator=False)
lam.slot = SlotMFlat2(
    H1=1*mm, W1=2*mm, W0=4*mm, W0_is_rad=False, H0=10*mm, W3=0, Zs=8,
    magnet=list()
)
lam.slot.magnet.append(MagnetType10(Wmag=4*mm,Hmag=10*mm))
lam.plot()
# Outward Slot
# lam = LamSlotMag(slot=-1, L1=0.28, Rint=0.166, Rext=0.3, is_internal=False,)
# H1 is rad

# %%

# %%
