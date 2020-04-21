# -*- coding: utf-8 -*-
"""Validation machine a polar SIPMSM with inset magnet

from publication
A. Rahideh and T. Korakianitis,
“Analytical Magnetic Field Calculation of Slotted Brushless Permanent-Magnet Machines With Surface Inset Magnets,”
vol. 48, no. 10, pp. 2633–2649, 2012.
"""
from numpy import pi
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.CondType12 import CondType12

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.MagnetType11 import MagnetType11

from pyleecan.Classes.Shaft import Shaft    

from Tests.Validation.Material.M400_50A import M400_50A
from Tests.Validation.Material.Magnet1 import Magnet1
from Tests.Validation.Material.Copper1 import Copper1

# Stator setup
stator = LamSlotWind(
    Rint=0.026, Rext=0.048, Nrvd=0, L1=0.09, Kf1=0.96, is_internal=False, is_stator=True
)

stator.slot = SlotW22(Zs=6, H0=0.002, H2=0.01, W0=0.44, W2=0.628)
stator.winding = WindingCW1L(qs=3, Lewout=0.015, p=2, Ntcoil=42, Npcpp=1)

stator.winding.conductor = CondType12(
    Nwppc=1, Wwire=0.0011283792, Wins_wire=1e-6, Kwoh=0.5
)
# Rotor setup
rotor = LamSlotMag(
    Rext=0.025, Rint=0.005, L1=0.09, Kf1=0.95, is_internal=True, is_stator=False, Nrvd=0
)
rotor.slot = SlotMPolar(Zs=4, W3=0, W0=1.3351769, H0=0.007)
rotor.slot.magnet = [MagnetType11(Wmag=1.3351769, Hmag=0.007)]

shaft = Shaft(Lshaft=0.442, Drsh=0.01)
frame = None

# Set Materials
stator.mat_type = M400_50A
rotor.mat_type = M400_50A
stator.winding.conductor.cond_mat = Copper1
rotor.slot.magnet[0].mat_type = Magnet1

SIPMSM_001 = MachineSIPMSM(
    name="SIPMSM_001",
    desc="polar SIPMSM with inset magnet from A. Rahideh and T. Korakianitis publication",
    stator=stator,
    rotor=rotor,
    shaft=shaft,
    frame=frame,
)
