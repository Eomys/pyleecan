# -*- coding: utf-8 -*-
from numpy import pi
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Tests.Validation.Material.Copper1 import Copper1
from pyleecan.Tests.Validation.Material.M400_50A import M400_50A

# Stator setup
stator = LamSlotWind(
    Rint=0.1325, Rext=0.2, Nrvd=0, L1=0.35, Kf1=0.95, is_internal=False, is_stator=True
)

stator.slot = SlotW10(Zs=36, H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3)
stator.winding = WindingDW2L(qs=3, Lewout=15e-3, p=3, coil_pitch=5, Ntcoil=7, Npcpp=2)

stator.winding.conductor = CondType11(
    Nwppc_tan=1, Nwppc_rad=1, Wwire=10e-3, Hwire=2e-3, Wins_wire=0, type_winding_shape=0
)
# Rotor setup
rotor = LamSquirrelCage(
    Rext=0.131,
    Rint=45e-3,
    L1=0.35,
    Kf1=0.95,
    is_internal=True,
    is_stator=False,
    Hscr=20e-3,
    Lscr=15e-3,
    Nrvd=0,
)
rotor.axial_vent = [VentilationCirc(Zh=8, D0=20e-3, H0=70e-3, Alpha0=0)]

rotor.slot = SlotW21(Zs=28, H0=3e-3, W0=3e-3, H1=0, H2=20e-3, W1=13e-3, W2=10e-3)
rotor.winding = WindingSC(Ntcoil=1, qs=28, Lewout=17e-3, Npcpp=1)
rotor.winding.conductor = CondType21(Hbar=0.02, Wbar=0.01, Wins=0)

shaft = Shaft(Drsh=90e-3)

frame = None

# Set materials
stator.mat_type = M400_50A
stator.winding.conductor.cond_mat = Copper1
rotor.mat_type = M400_50A
rotor.ring_mat = Copper1
rotor.winding.conductor.cond_mat = Copper1

SCIM_001 = MachineSCIM(stator=stator, rotor=rotor, shaft=shaft, frame=frame)
