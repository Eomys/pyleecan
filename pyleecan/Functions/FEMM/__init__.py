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
FEMM_GROUPS["GROUP_SV"] = {"name": "stator ventilation duct", "ID": 14}
FEMM_GROUPS["GROUP_SSI"] = {"name": "stator slot isthmus", "ID": 15}  # Opening
FEMM_GROUPS["GROUP_SH"] = {"name": "stator holes", "ID": 16}
FEMM_GROUPS["GROUP_SWE"] = {"name": "stator wedges", "ID": 17}
FEMM_GROUPS["GROUP_SK"] = {"name": "stator Keys", "ID": 18}
# rotor GROUPs
FEMM_GROUPS["GROUP_RC"] = {"name": "rotor core", "ID": 20}
FEMM_GROUPS["GROUP_RW"] = {"name": "rotor winding", "ID": 21}
FEMM_GROUPS["GROUP_RM"] = {"name": "rotor magnets", "ID": 22}
FEMM_GROUPS["GROUP_RN"] = {"name": "rotor notches", "ID": 23}
FEMM_GROUPS["GROUP_RV"] = {"name": "rotor ventilation duct", "ID": 24}
FEMM_GROUPS["GROUP_RSI"] = {"name": "rotor slot isthmus", "ID": 25}  # Opening
FEMM_GROUPS["GROUP_RH"] = {"name": "rotor holes", "ID": 26}
FEMM_GROUPS["GROUP_RWE"] = {"name": "rotor wedges", "ID": 27}
FEMM_GROUPS["GROUP_RK"] = {"name": "rotor keys", "ID": 28}
# other GROUPs
FEMM_GROUPS["GROUP_IN"] = {"name": "inner shaft", "ID": 30}
FEMM_GROUPS["GROUP_FM"] = {"name": "fictitious magnets", "ID": 31}
FEMM_GROUPS["GROUP_FR"] = {"name": "frame", "ID": 32}
# List of group needed to select a lamination
FEMM_GROUPS["lam_group_list"] = {
    "Stator-0": [10, 11, 12, 13, 14, 15, 16, 17, 18],
    "Rotor-0": [20, 21, 22, 23, 24, 25, 26, 27, 28],
}

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


LAM_MAT_NAME = "Iron"
AIRGAP_MAT_NAME = "Airgap"
