from ...Functions.labels import (
    SHAFTSR_LAB,
    SHAFTSL_LAB,
    YSR_LAB,
    YSL_LAB,
    ROTOR_LAB,
    STATOR_LAB,
)

R_LAB = ROTOR_LAB + "-0_"
S_LAB = STATOR_LAB + "-0_"
# dictionary to match MagElmer FEA boundary conditions (dict values)
# with pyleecan line boundary properties (dict keys)
# that are set in the build_geometry methods
MagElmer_BP_dict = dict()
MagElmer_BP_dict["int_airgap_line_1"] = "MASTER_ROTOR_BOUNDARY"
MagElmer_BP_dict["int_airgap_line_2"] = "SLAVE_ROTOR_BOUNDARY"
MagElmer_BP_dict["int_sb_line_1"] = "MASTER_ROTOR_BOUNDARY"
MagElmer_BP_dict["int_sb_line_2"] = "SLAVE_ROTOR_BOUNDARY"
MagElmer_BP_dict[R_LAB + YSR_LAB] = "MASTER_ROTOR_BOUNDARY"  # Rotor Yoke Side Right
MagElmer_BP_dict[R_LAB + YSL_LAB] = "SLAVE_ROTOR_BOUNDARY"  # Rotor Yoke Side Left
MagElmer_BP_dict[SHAFTSR_LAB] = "MASTER_ROTOR_BOUNDARY"  # Shfat Side Right
MagElmer_BP_dict[SHAFTSL_LAB] = "SLAVE_ROTOR_BOUNDARY"  # Shaft Side Left
MagElmer_BP_dict["int_sb_arc"] = "SB_ROTOR_BOUNDARY"
MagElmer_BP_dict["ext_airgap_line_1"] = "MASTER_STATOR_BOUNDARY"
MagElmer_BP_dict["ext_airgap_line_2"] = "SLAVE_STATOR_BOUNDARY"
MagElmer_BP_dict["ext_sb_line_1"] = "MASTER_STATOR_BOUNDARY"
MagElmer_BP_dict["ext_sb_line_2"] = "SLAVE_STATOR_BOUNDARY"
MagElmer_BP_dict["airbox_line_1"] = "MASTER_STATOR_BOUNDARY"
MagElmer_BP_dict["airbox_line_2"] = "SLAVE_STATOR_BOUNDARY"
MagElmer_BP_dict[S_LAB + YSR_LAB] = "MASTER_STATOR_BOUNDARY"  # Stator Yoke Side Right
MagElmer_BP_dict[S_LAB + YSL_LAB] = "SLAVE_STATOR_BOUNDARY"  # Stator Yoke Side Left
MagElmer_BP_dict["ext_sb_arc"] = "SB_STATOR_BOUNDARY"
MagElmer_BP_dict["ext_airgap_arc_copy"] = "AIRGAP_ARC_BOUNDARY"
MagElmer_BP_dict["airbox_arc"] = "VP0_BOUNDARY"
