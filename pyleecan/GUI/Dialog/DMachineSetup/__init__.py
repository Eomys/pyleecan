# -*- coding: utf-8 -*-

from ....GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from ....GUI.Dialog.DMachineSetup.SMachineDimension.SMachineDimension import (
    SMachineDimension,
)
from ....GUI.Dialog.DMachineSetup.SLamParam.SLamParam import SLamParam
from ....GUI.Dialog.DMachineSetup.SWindPat.SWindPat import SWindPat
from ....GUI.Dialog.DMachineSetup.SWindParam.SWindParam import SWindParam
from ....GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from ....GUI.Dialog.DMachineSetup.SWSlot.SWSlot import SWSlot
from ....GUI.Dialog.DMachineSetup.SWPole.SWPole import SWPole
from ....GUI.Dialog.DMachineSetup.SBar.SBar import SBar
from ....GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
from ....GUI.Dialog.DMachineSetup.SMSlot.SMSlot import SMSlot

from ....Classes.Magnet import Magnet
from ....Classes.LamHole import LamHole
from ....Classes.LamSlot import LamSlot
from ....Classes.LamSlotMag import LamSlotMag
from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.LamSquirrelCage import LamSquirrelCage
from ....Classes.MachineIPMSM import MachineIPMSM
from ....Classes.MachineSyRM import MachineSyRM
from ....Classes.MachineDFIM import MachineDFIM
from ....Classes.MachineSCIM import MachineSCIM
from ....Classes.MachineSIPMSM import MachineSIPMSM
from ....Classes.MachineWRSM import MachineWRSM
from ....Classes.MachineSRM import MachineSRM
from ....Classes.SlotM10 import SlotM10
from ....Classes.HoleM50 import HoleM50
from ....Classes.WindingDW2L import WindingDW2L
from ....Classes.WindingCW2LT import WindingCW2LT
from ....Classes.WindingSC import WindingSC
from ....GUI.Resources import pixmap_dict

# Steps needed to setup a LamSlotWind
LSW_step = [SLamParam, SWSlot, SWindPat, SWindParam, SWindCond]
# Steps needed to setup a LamSlotWind for the rotor of a WRSM
LP_step = [SLamParam, SWPole, SWindPat, SWindParam, SWindCond]
# Steps needed to setup a LamSquirrelCage
LSC_step = [SLamParam, SWSlot, SBar]
# Steps needed to setup a LamHole
LH_step = [SLamParam, SMHoleMag]
# Steps needed to setup a LamSlot
LS_step = [SLamParam, SWSlot]
# Steps needed to setup a LamSlotMag
LSM_step = [SLamParam, SMSlot]
# Steps to start the design of a machine with 2 laminations
S_step = [SMachineType, SMachineDimension]

# Defaut machine for initialization
machine1 = MachineSCIM()
machine1.stator = LamSlotWind()
machine1.stator.winding = WindingDW2L()
machine1.rotor = LamSquirrelCage()
machine1.rotor.winding = WindingSC()
machine1._set_None()  # Empty machine
machine1.type_machine = 1
machine1.stator.is_stator = True
machine1.rotor.is_stator = False

machine4 = MachineDFIM()
machine4.stator = LamSlotWind()
machine4.stator.winding = WindingDW2L()
machine4.rotor = LamSlotWind()
machine4.rotor.winding = WindingDW2L()
machine4._set_None()  # Empty machine
machine4.type_machine = 4
machine4.stator.is_stator = True
machine4.rotor.is_stator = False

machine5 = MachineSyRM()
machine5.stator = LamSlotWind()
machine5.stator.winding = WindingDW2L()
machine5.rotor = LamHole()
machine5.rotor.hole = list()
machine5.rotor.hole.append(HoleM50())
machine5.rotor.hole[0].remove_magnet()
machine5._set_None()  # Empty machine
machine5.type_machine = 5
machine5.stator.is_stator = True
machine5.rotor.is_stator = False

machine7 = MachineSIPMSM()
machine7.stator = LamSlotWind()
machine7.stator.winding = WindingDW2L()
machine7.rotor = LamSlotMag()
machine7.rotor.slot = SlotM10()
machine7._set_None()  # Empty machine
machine7.type_machine = 7
machine7.stator.is_stator = True
machine7.rotor.is_stator = False

machine8 = MachineIPMSM()
machine8.stator = LamSlotWind()
machine8.stator.winding = WindingDW2L()
machine8.rotor = LamHole()
machine8.rotor.hole = list()
machine8.rotor.hole.append(HoleM50())
machine8._set_None()  # Empty machine
machine8.type_machine = 8
machine8.stator.is_stator = True
machine8.rotor.is_stator = False

machine9 = MachineWRSM()
machine9.stator = LamSlotWind()
machine9.stator.winding = WindingDW2L()
machine9.rotor = LamSlotWind()
machine9.rotor.winding = WindingCW2LT()
machine9._set_None()  # Empty machine
machine9.type_machine = 9
machine9.stator.is_stator = True
machine9.rotor.is_stator = False

machine10 = MachineSRM()
machine10.stator = LamSlotWind()
machine10.stator.winding = WindingDW2L()
machine10.rotor = LamSlot()
machine10._set_None()  # Empty machine
machine10.type_machine = 10
machine10.stator.is_stator = True
machine10.rotor.is_stator = False

# Dictionnary with all the information to set a SCIM
SCIM_dict = {
    "machine_type": MachineSCIM,
    "init_machine": machine1,
    "start_step": S_step,
    "stator_step": LSW_step,
    "rotor_step": LSC_step,
    "name": "SCIM",
    "img": pixmap_dict["SCIM"],
    "txt": "SCIM (Squirrel Cage Induction Machine)",
}
# Dictionnary with all the information to set a DFIM
DFIM_dict = {
    "machine_type": MachineDFIM,
    "init_machine": machine4,
    "start_step": S_step,
    "stator_step": LSW_step,
    "rotor_step": LSW_step,
    "name": "DFIM",
    "img": pixmap_dict["DFIM"],
    "txt": "DFIM (Doubly Fed Induction Machine)",
}
# Dictionnary with all the information to set a SynRM
SynRM_dict = {
    "machine_type": MachineSyRM,
    "init_machine": machine5,
    "start_step": S_step,
    "stator_step": LSW_step,
    "rotor_step": LH_step,
    "name": "SynRM",
    "img": pixmap_dict["SynRM"],
    "txt": "SynRM (Synchronous Reluctance Machine)",
}
# Dictionnary with all the information to set a SIPMSM
SIPMSM_dict = {
    "machine_type": MachineSIPMSM,
    "init_machine": machine7,
    "start_step": S_step,
    "stator_step": LSW_step,
    "rotor_step": LSM_step,
    "name": "SPMSM",
    "img": pixmap_dict["SPMSM"],
    "txt": "SPMSM (Surface Permanent Magnet Synchronous Machine)",
}
# Dictionnary with all the information to set a IPMSM
IPMSM_dict = {
    "machine_type": MachineIPMSM,
    "init_machine": machine8,
    "start_step": S_step,
    "stator_step": LSW_step,
    "rotor_step": LH_step,
    "name": "IPMSM",
    "img": pixmap_dict["IPMSM"],
    "txt": "IPMSM (Interior Permanent Magnet Synchronous Machine)",
}
# Dictionnary with all the information to set a WRSM
WRSM_dict = {
    "machine_type": MachineWRSM,
    "init_machine": machine9,
    "start_step": S_step,
    "stator_step": LSW_step,
    "rotor_step": LP_step,
    "name": "WRSM",
    "img": pixmap_dict["WRSM"],
    "txt": "WRSM (Wound Rotor Synchronous Machine)",
}
# Dictionnary with all the information to set a SCIM
SRM_dict = {
    "machine_type": MachineSRM,
    "init_machine": machine10,
    "start_step": S_step,
    "stator_step": LSW_step,
    "rotor_step": LS_step,
    "name": "SRM",
    "img": pixmap_dict["SCIM"],
    "txt": "SRM (Switched Reluctance Machine)",
}
# List of machine types available in the GUI
mach_list = [
    SCIM_dict,
    DFIM_dict,
    SynRM_dict,
    SIPMSM_dict,
    IPMSM_dict,
    WRSM_dict,
    SRM_dict,
]
# To find the correct index according to the machine
mach_index = [mach_dict["machine_type"] for mach_dict in mach_list]
