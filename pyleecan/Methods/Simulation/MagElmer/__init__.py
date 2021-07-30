from ....Functions.labels import (
    AIRBOX_R_LAB,
    AIRBOX_SR_LAB,
    SHAFTSR_LAB,
    SHAFTSL_LAB,
    YSR_LAB,
    YSL_LAB,
    ROTOR_LAB,
    STATOR_LAB,
    SBS_TR_LAB,
    SBS_TL_LAB,
    SBS_BR_LAB,
    SBS_BL_LAB,
    SBR_B_LAB,
    SBR_T_LAB,
    AS_TR_LAB,
    AS_TL_LAB,
    AS_BR_LAB,
    AS_BL_LAB,
    AR_T_LAB,
    AIRBOX_SL_LAB,
    AIRBOX_SR_LAB,
    AIRBOX_R_LAB
)

R_LAB = ROTOR_LAB + "-0_"
S_LAB = STATOR_LAB + "-0_"
# dictionary to match MagElmer FEA boundary conditions (dict values)
# with pyleecan line boundary properties (dict keys)
# that are set in the build_geometry methods
MagElmer_BP_dict = dict()
MagElmer_BP_dict[AS_BR_LAB] = "MASTER_ROTOR_BOUNDARY"
MagElmer_BP_dict[AS_BL_LAB] = "SLAVE_ROTOR_BOUNDARY"

MagElmer_BP_dict[SBS_BR_LAB] = "MASTER_ROTOR_BOUNDARY"
MagElmer_BP_dict[SBS_BL_LAB] = "SLAVE_ROTOR_BOUNDARY"
MagElmer_BP_dict[SBR_B_LAB] = "SB_ROTOR_BOUNDARY"

MagElmer_BP_dict[R_LAB + YSR_LAB] = "MASTER_ROTOR_BOUNDARY"  # Rotor Yoke Side Right
MagElmer_BP_dict[R_LAB + YSL_LAB] = "SLAVE_ROTOR_BOUNDARY"  # Rotor Yoke Side Left
MagElmer_BP_dict[S_LAB + YSR_LAB] = "MASTER_STATOR_BOUNDARY"  # Stator Yoke Side Right
MagElmer_BP_dict[S_LAB + YSL_LAB] = "SLAVE_STATOR_BOUNDARY"  # Stator Yoke Side Left
MagElmer_BP_dict[SHAFTSR_LAB] = "MASTER_ROTOR_BOUNDARY"  # Shaft Side Right
MagElmer_BP_dict[SHAFTSL_LAB] = "SLAVE_ROTOR_BOUNDARY"  # Shaft Side Left

MagElmer_BP_dict[AS_TR_LAB] = "MASTER_STATOR_BOUNDARY"
MagElmer_BP_dict[AS_TL_LAB] = "SLAVE_STATOR_BOUNDARY"
MagElmer_BP_dict[AR_T_LAB] = "AIRGAP_ARC_BOUNDARY"

MagElmer_BP_dict[SBS_TR_LAB] = "MASTER_STATOR_BOUNDARY"
MagElmer_BP_dict[SBS_TL_LAB] = "SLAVE_STATOR_BOUNDARY"
MagElmer_BP_dict[SBR_T_LAB] = "SB_STATOR_BOUNDARY"

MagElmer_BP_dict[AIRBOX_SR_LAB] = "MASTER_STATOR_BOUNDARY"
MagElmer_BP_dict[AIRBOX_SL_LAB] = "SLAVE_STATOR_BOUNDARY"
MagElmer_BP_dict[AIRBOX_R_LAB] = "VP0_BOUNDARY"
