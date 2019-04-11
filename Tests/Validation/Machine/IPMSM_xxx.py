# -*- coding: utf-8 -*-
from numpy import pi
from pyleecan.Classes.MachineIPMSM import MachineIPMSM

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.CondType12 import CondType12

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.Frame import Frame

from pyleecan.Classes.Shaft import Shaft

from pyleecan.Tests.Validation.Material.M400_50A import M400_50A
from pyleecan.Tests.Validation.Material.Magnet3 import Magnet3
from pyleecan.Tests.Validation.Material.Copper1 import Copper1


mm = 1e-3  # Millimeter

# Stator setup
stator = LamSlotWind(
    Rint=160.4 * mm / 2,
    Rext=221.0 * mm / 2,
    Nrvd=0,
    L1=70 * mm,
    Kf1=1,
    is_internal=False,
    is_stator=True,
)
stator.slot = SlotW21(
    Zs=48, H0=1.0 * mm, H1=0.5 * mm, H2=14.5 * mm, W0=2.0 * mm, W1=5 * mm, W2=7 * mm
)
stator.winding = WindingDW1L(
    qs=3,  # number of phases
    Lewout=10 * mm,  # staight length of conductor outside lamination before EW-bend
    p=4,  # number of pole pairs
    Ntcoil=2,  # number of turns per coil
    Npcpp=1,  # number of parallel circuits per phase
    Nslot_shift_wind=0,  #
)
stator.winding.conductor = CondType12(
    Wwire=1.0 * mm,  # single wire without isolation
    Wins_wire=0.1 * mm,  # single wire isolation thickness
    Wins_cond=1.3 * mm,  # winding coil isolation
    Nwppc=1,  # number of strands in parallel per coil
    Kwoh=1,
)

# Rotor setup
rotor = LamHole(
    Rint=59 * mm / 2, Rext=158 * mm / 2, is_internal=True, is_stator=False, L1=stator.L1
)
rotor.hole = list()
rotor.hole.append(
    HoleM50(
        Zh=8,
        W0=43.4 * mm,
        W1=3.0 * mm,
        W2=1.0 * mm,
        W3=10.0 * mm,
        W4=22.0 * mm,
        H0=20.0 * mm,
        H1=2.0 * mm,
        H2=2.5 * mm,
        H3=6.0 * mm,
        H4=0.8 * mm,
    )
)
"""
rotor.axial_vent = list()                  
rotor.axial_vent.append(VentilationCirc(
    Zh=8, 
    Alpha0=0, 
    D0=5e-3, 
    H0=40e-3
))
rotor.axial_vent.append(VentilationCirc(
    Zh=8, 
    Alpha0=pi / 8, 
    D0=7e-3, 
    H0=40e-3
))
"""
shaft = Shaft(Drsh=rotor.Rint * 2, Lshaft=1.2)

frame = Frame(Rint=stator.Rext, Rext=stator.Rext + 10 * mm, Lfra=1)

# Set Materials
stator.mat_type = M400_50A
rotor.mat_type = M400_50A
stator.winding.conductor.cond_mat = Copper1
rotor.hole[0].magnet_0.mat_type = Magnet3
rotor.hole[0].magnet_1.mat_type = Magnet3

IPMSM_xxx = MachineIPMSM(
    name="IPMSM", stator=stator, rotor=rotor, shaft=shaft, frame=frame
)
