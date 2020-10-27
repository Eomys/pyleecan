# -*- coding: utf-8 -*-
"""Validation machine file IPMSM
TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
50 kW peak, 400 Nm peak at 1500 rpm from publication

Z. Yang, M. Krishnamurthy and I. P. Brown,
"Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
"""
from numpy import pi
from os.path import join
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import pytest


@pytest.fixture
def CEFC_Lam():
    # Stator setup
    stator = LamSlotWind(
        Rint=80.95e-3,
        Rext=134.62e-3,
        Nrvd=0,
        L1=0.08382,
        Kf1=0.95,
        is_internal=False,
        is_stator=True,
    )
    stator.slot = None
    stator.winding.qs = 0
    stator.winding.p = 0

    # Rotor setup
    rotor = LamHole(
        Rext=80.2e-3,
        Rint=55.32e-3,
        L1=0.08382,
        Kf1=0.95,
        is_internal=True,
        is_stator=False,
        Nrvd=0,
    )
    rotor.hole = [
        HoleM50(
            Zh=8,
            H0=0.01096,
            H1=0.0015,
            H2=0.001,
            H3=0.0065,
            H4=0,
            W0=0.042,
            W1=0,
            W2=0,
            W3=0.014,
            W4=0.0189,
        )
    ]
    rotor.hole[0].magnet_0.type_magnetization = 1
    rotor.hole[0].magnet_1.type_magnetization = 1
    shaft = Shaft(Lshaft=0.1, Drsh=0.11064)
    frame = None

    # Set Materials

    M400_50A = load(join(DATA_DIR, "Material", "M400-50A.json"))
    Magnet_prius = load(join(DATA_DIR, "Material", "MagnetPrius.json"))
    stator.mat_type = M400_50A
    rotor.mat_type = M400_50A
    rotor.hole[0].magnet_0.mat_type = Magnet_prius
    rotor.hole[0].magnet_1.mat_type = Magnet_prius

    CEFC_Lam = MachineIPMSM(
        name="CEFC_Lam",
        desc="Slotless machine from CEFC publication",
        stator=stator,
        rotor=rotor,
        shaft=shaft,
        frame=frame,
    )

    return CEFC_Lam
