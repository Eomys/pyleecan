# -*- coding: utf-8 -*-

# regions ID
GROUP_AG = 0  # airgap GROUP for segments added between the rotor and
# stator structures (except middle airgap)
GROUP_SC = 1  # stator core GROUP
GROUP_RC = 2  # rotor core GROUP
GROUP_SW = 3  # stator winding GROUP
GROUP_RW = 4  # rotor winding / magnet GROUP
GROUP_AGM = 5  # airgap middle for torque calculations
GROUP_IN = 6  # inner shaft GROUP
GROUP_FM = 7  # fictitious magnets
GROUP_SV = 8  # stator cooling duct
GROUP_RV = 8  # rotor ventilation duct
GROUP_SSI = 9  # stator slot isthmus
GROUP_RSI = 10  # rotor slot isthmus
GROUP_SN = 11  # stator notches
GROUP_RN = 12  # rotor notches
GROUP_SH = 13  # stator hole
GROUP_RH = 14  # rotor hole


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

# dictionary matching boundary condition with line in FEMM
boundary_prop = dict()
boundary_prop["airgap_line_1"] = "bc_ag1"
boundary_prop["sliding_line"] = "bc_ag2"
boundary_prop["airgap_line_2"] = "bc_ag3"
boundary_prop["Rotor_Yoke_Radius"] = "bc_A0"
boundary_prop["Stator_Yoke_Radius"] = "bc_A0"
boundary_prop["Rotor_Yoke_Side"] = "bc_r1"
boundary_prop["Stator_Yoke_Side"] = "bc_s1"
