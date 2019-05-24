# -*- coding: utf-8 -*-
"""Validation machine: polar SIPMSM with surface magnet

From publication
Lubin, S. Mezani, and A. Rezzoug,
“2-D Exact Analytical Model for Surface-Mounted Permanent-Magnet Motors with Semi-Closed Slots,”
IEEE Trans. Magn., vol. 47, no. 2, pp. 479–492, 2011.
"""
from numpy import pi
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.CondType11 import CondType11

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.MagnetType11 import MagnetType11

from pyleecan.Classes.Shaft import Shaft

from pyleecan.Tests.Validation.Material.M400_50A import M400_50A
from pyleecan.Tests.Validation.Material.Magnet3 import Magnet3
from pyleecan.Tests.Validation.Material.Copper1 import Copper1

# Stator setup
stator = LamSlotWind(
    Rint=0.116, Rext=0.2, Nrvd=0, L1=0.4, Kf1=1, is_internal=False, is_stator=True
)

stator.slot = SlotW22(
    Zs=12, H0=4e-3, H2=25e-3, W0=0.6 * 12 * pi / 180, W2=12 * pi / 180
)
stator.winding = WindingDW1L(
    qs=3, Lewout=15e-3, p=1, Ntcoil=12, Npcpp=1, Nslot_shift_wind=0
)

stator.winding.conductor = CondType11(
    Nwppc_tan=1,
    Nwppc_rad=1,
    Wwire=2e-3,
    Hwire=2e-3,
    Wins_wire=1e-6,
    type_winding_shape=0,
)
# Rotor setup
rotor = LamSlotMag(
    Rext=0.1, Rint=0.0225, L1=0.4, Kf1=0.95, is_internal=True, is_stator=False, Nrvd=0
)
rotor.slot = SlotMPolar(Zs=2, W3=0, W0=2.82743338823, H0=0)
rotor.slot.magnet = [MagnetType11(Wmag=2.82743338823, Hmag=0.012)]

shaft = Shaft(Lshaft=0.442, Drsh=45e-3)
frame = None

# Set Materials
stator.mat_type = M400_50A
rotor.mat_type = M400_50A
stator.winding.conductor.cond_mat = Copper1
rotor.slot.magnet[0].mat_type = Magnet3

SPMSM_003 = MachineSIPMSM(
    name="SPMSM_003",
    desc="polar SIPMSM with surface magnet from Lubin, S. Mezani, and A. Rezzoug publication",
    stator=stator,
    rotor=rotor,
    shaft=shaft,
    frame=frame,
)
