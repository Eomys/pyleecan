# -*- coding: utf-8 -*-
"""Validation of a SynRM machine from Syr-e r29 open source software
https://sourceforge.net/projects/syr-e/
"""
from numpy import pi
from pyleecan.Classes.MachineSyRM import MachineSyRM

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.CondType12 import CondType12

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM54 import HoleM54

from pyleecan.Classes.Shaft import Shaft

from pyleecan.Tests.Validation.Material.M530_65A import M530_65A
from pyleecan.Tests.Validation.Material.Copper1 import Copper1

# Stator setup
stator = LamSlotWind(
    Rint=0.0411,
    Rext=0.0675,
    Nrvd=0,
    L1=0.101,
    Kf1=0.96,
    is_internal=False,
    is_stator=True,
)

stator.slot = SlotW11(
    Zs=24,
    H0=0.00075,
    H1=0.4363323129985824,
    H1_is_rad=True,
    H2=0.015,
    W0=0.00268,
    W1=0.006828,
    W2=0.009,
)
stator.winding = WindingDW1L(qs=3, Lewout=15e-3, p=2, Ntcoil=30, Npcpp=1, coil_pitch=6)

stator.winding.conductor = CondType12(Nwppc=1, Wwire=0.001, Kwoh=0.5, Wins_wire=1e-6)
# Rotor setup
rotor = LamHole(
    Rext=0.0406, Rint=0, L1=0.101, Kf1=0.96, is_internal=True, is_stator=False, Nrvd=0
)
rotor.hole = list()
rotor.hole.append(HoleM54(Zh=4, H0=0.004, H1=0.0041, W0=0.78, R1=0.025))
rotor.hole.append(HoleM54(Zh=4, H0=0.011, H1=0.0041, W0=1.22, R1=0.03))
rotor.hole.append(HoleM54(Zh=4, H0=0.0185, H1=0.0041, W0=1.44, R1=0.035))

shaft = None
frame = None

# Set Materials
stator.mat_type = M530_65A
rotor.mat_type = M530_65A
stator.winding.conductor.cond_mat = Copper1

SynRM_001 = MachineSyRM(
    name="SynRM_001",
    desc="SynRM machine from Syr-e r29 open source software",
    stator=stator,
    rotor=rotor,
    shaft=shaft,
    frame=frame,
)
