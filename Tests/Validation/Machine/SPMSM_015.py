# -*- coding: utf-8 -*-
from numpy import pi
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.CondType12 import CondType12

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.MagnetType11 import MagnetType11

from pyleecan.Tests.Validation.Material.M400_50A import M400_50A
from pyleecan.Tests.Validation.Material.Magnet5 import Magnet5
from pyleecan.Tests.Validation.Material.Copper1 import Copper1

# Stator setup
stator = LamSlotWind(
    Rint=0.05, Rext=0.078, Nrvd=0, L1=0.035, Kf1=0.95, is_internal=True, is_stator=True
)

stator.slot = SlotW23(
    Zs=27,
    H0=0.0015,
    H1=0.002,
    H2=0.015,
    W0=0.006,
    W3=0.005,
    H1_is_rad=False,
    is_cstt_tooth=True,
)
stator.winding = WindingCW2LT(
    qs=3, Lewout=15e-3, p=9, Ntcoil=57, Npcpp=3, Nslot_shift_wind=0
)

stator.winding.conductor = CondType12(Nwppc=1, Wwire=0.0007, Wins_wire=1e-6, Kwoh=0.5)
# Rotor setup
rotor = LamSlotMag(
    Rext=0.085,
    Rint=0.082,
    L1=0.035,
    Kf1=0.95,
    is_internal=False,
    is_stator=False,
    Nrvd=0,
)
rotor.slot = SlotMPolar(Zs=18, W3=0, W0=0.23529412, H0=0)
rotor.slot.magnet = [MagnetType11(Wmag=0.23529412, Hmag=0.002)]

shaft = None
frame = None

# Set Materials
stator.mat_type = M400_50A
rotor.mat_type = M400_50A
stator.winding.conductor.cond_mat = Copper1
rotor.slot.magnet[0].mat_type = Magnet5

SPMSM_015 = MachineSIPMSM(
    name="SPMSM_015", stator=stator, rotor=rotor, shaft=shaft, frame=frame
)
