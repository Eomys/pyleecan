# -*- coding: utf-8 -*-
"""Validation machine of a polar SCIM
From publication:
K. Boughrara
Analytical Analysis of Cage Rotor Induction Motors in Healthy, Defective and Broken Bars Conditions
IEEE Trans on Mag, 2014
"""
from numpy import pi
from ....Classes.CondType12 import CondType12
from ....Classes.CondType21 import CondType21
from ....Classes.Frame import Frame
from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.MachineSCIM import MachineSCIM
from ....Classes.LamSquirrelCage import LamSquirrelCage
from ....Classes.Shaft import Shaft
from ....Classes.VentilationCirc import VentilationCirc
from ....Classes.WindingDW1L import WindingDW1L
from ....Classes.WindingSC import WindingSC
from ....Classes.SlotW22 import SlotW22
from ....Classes.SlotW21 import SlotW21
from ....Tests.Validation.Material.Copper1 import Copper1
from ....Tests.Validation.Material.M400_50A import M400_50A

# Stator setup
stator = LamSlotWind(
    Rint=0.061, Rext=0.1, Nrvd=0, L1=0.2, Kf1=1, is_internal=False, is_stator=True
)

stator.slot = SlotW22(Zs=36, H0=0.002, H2=0.022, W0=0.0523598775598, W2=0.0872664625997)
stator.winding = WindingDW1L(qs=3, Lewout=0, p=2, Ntcoil=15, Npcpp=1, coil_pitch=9)

stator.winding.conductor = CondType12(Nwppc=1, Wwire=0.0005, Wins_wire=1e-06, Kwoh=0)
# Rotor setup
rotor = LamSquirrelCage(
    Rext=0.06,
    Rint=0,
    L1=0.2,
    Kf1=1,
    is_internal=True,
    is_stator=False,
    Hscr=0.1,
    Lscr=0.1,
    Nrvd=0,
)

rotor.slot = SlotW22(Zs=28, H0=0.002, H2=0.02, W0=0.067369709127, W2=0.112224670903)
rotor.winding = WindingSC(Ntcoil=1, qs=28, Lewout=0, Npcpp=1)
rotor.winding.conductor = CondType21(Hbar=0.02, Wbar=0.01, Wins=0)

shaft = None

frame = None

# Set materials
stator.mat_type = M400_50A
stator.winding.conductor.cond_mat = Copper1
rotor.mat_type = M400_50A
rotor.ring_mat = Copper1
rotor.winding.conductor.cond_mat = Copper1

SCIM_006 = MachineSCIM(
    name="SCIM_006",
    desc="polar SCIM from K. Boughrara publication",
    stator=stator,
    rotor=rotor,
    shaft=shaft,
    frame=frame,
)
