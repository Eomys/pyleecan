# -*- coding: utf-8 -*-
from ..labels import (
    YSR_LAB,
    YSL_LAB,
    ROTOR_LAB,
    STATOR_LAB,
    YOKE_LAB,
    LAM_LAB,
    SBS_TR_LAB,
    SBS_TL_LAB,
    SBS_BR_LAB,
    SBS_BL_LAB,
    SBR_B_LAB,
    SBR_T_LAB,
)

# regions IDs and names (must be unique)

FEMM_GROUPS = dict()

# airgap GROUP for segments added between the rotor and stator (except middle airgap)
FEMM_GROUPS["GROUP_AG"] = {"name": "airgap", "ID": 0}
FEMM_GROUPS["GROUP_AGM"] = {"name": "airgap middle", "ID": 1}  # for torque calculations
# stator GROUPs
FEMM_GROUPS["GROUP_SC"] = {"name": "stator core", "ID": 10}
FEMM_GROUPS["GROUP_SW"] = {"name": "stator winding", "ID": 11}
FEMM_GROUPS["GROUP_SM"] = {"name": "stator magnets", "ID": 12}
FEMM_GROUPS["GROUP_SN"] = {"name": "stator notches", "ID": 13}
FEMM_GROUPS["GROUP_SV"] = {"name": "stator ventialtion duct", "ID": 14}
FEMM_GROUPS["GROUP_SSI"] = {"name": "stator slot isthmus", "ID": 15}
FEMM_GROUPS["GROUP_SH"] = {"name": "stator holes", "ID": 16}
# rotor GROUPs
FEMM_GROUPS["GROUP_RC"] = {"name": "rotor core", "ID": 20}
FEMM_GROUPS["GROUP_RW"] = {"name": "rotor winding", "ID": 21}
FEMM_GROUPS["GROUP_RM"] = {"name": "rotor magnets", "ID": 22}
FEMM_GROUPS["GROUP_RN"] = {"name": "rotor notches", "ID": 23}
FEMM_GROUPS["GROUP_RV"] = {"name": "rotor ventialtion duct", "ID": 24}
FEMM_GROUPS["GROUP_RSI"] = {"name": "rotor slot isthmus", "ID": 25}
FEMM_GROUPS["GROUP_RH"] = {"name": "rotor holes", "ID": 26}
# other GROUPs
FEMM_GROUPS["GROUP_IN"] = {"name": "inner shaft", "ID": 30}
FEMM_GROUPS["GROUP_FM"] = {"name": "fictitious magnets", "ID": 31}
FEMM_GROUPS["GROUP_FR"] = {"name": "frame", "ID": 32}

# global Values
pbtype = "planar"  # problem type
precision = 1e-8  # solver precision (default: 1e-8)
is_eddies = 0  # 1 to calculate eddy currents
hidebc = 0  # 1 to hide BC properties
type_yokeS = 0  # 0 for circular stator yoke, 1 for squared yoke
minangle = 15  # finite element mesh min angle
is_middleag = 0  # 1 to draw an arc in the middle of the airgap for torque calculations(
# not necessary)
acsolver = 0  # AC solver type 0 for successive approx, 1 for Newton


# dictionary to match MagFEMM FEA boundary conditions (dict values)
# with pyleecan line boundary properties (dict keys)
# that are set in the build_geometry methods
# actual FEMM boundary condition is set in Arc and Segment draw_FEMM methods
R_LAB = ROTOR_LAB + "-0_"
S_LAB = STATOR_LAB + "-0_"
MagFEMM_BP_dict = dict()
MagFEMM_BP_dict[SBS_BR_LAB] = "bc_ag1"  # Bottom Sliding Band Side Right
MagFEMM_BP_dict[SBS_BL_LAB] = "bc_ag1"  # Bottom Sliding Band Side Left
MagFEMM_BP_dict[SBR_B_LAB] = "bc_ag2"  # Bottom Sliding Band Radius
MagFEMM_BP_dict[SBR_T_LAB] = "bc_ag2"  # Top Sliding Band Radius
MagFEMM_BP_dict[SBS_TR_LAB] = "bc_ag3"  # Top Sliding Band Side Right
MagFEMM_BP_dict[SBS_TL_LAB] = "bc_ag3"  # Top Sliding Band Side Left
MagFEMM_BP_dict[R_LAB + LAM_LAB + YOKE_LAB] = "bc_A0"
MagFEMM_BP_dict[S_LAB + LAM_LAB + YOKE_LAB] = "bc_A0"
MagFEMM_BP_dict[R_LAB + YSR_LAB] = "bc_r1"  # Rotor Yoke Side Right
MagFEMM_BP_dict[R_LAB + YSL_LAB] = "bc_r1"  # Rotor Yoke Side Left
MagFEMM_BP_dict[S_LAB + YSR_LAB] = "bc_s1"  # STATOR Yoke Side Right
MagFEMM_BP_dict[S_LAB + YSL_LAB] = "bc_s1"  # STATOR Yoke Side Left

LAM_MAT_NAME = "Iron"
AIRGAP_MAT_NAME = "Airgap"
