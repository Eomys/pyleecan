class InputError(Exception):
    """ """

    pass


boundary_prop = dict()
boundary_list = ["MASTER_ROTOR_BOUNDARY",
                 "SLAVE_ROTOR_BOUNDARY",
                 "MASTER_SLAVE_ROTOR_BOUNDARY",
                 "SB_ROTOR_BOUNDARY",
                 "MASTER_STATOR_BOUNDARY",
                 "SLAVE_STATOR_BOUNDARY",
                 "MASTER_SLAVE_STATOR_BOUNDARY",
                 "SB_STATOR_BOUNDARY",
                 "AIRGAP_ARC_BOUNDARY",
                 "VP0_BOUNDARY"
                 ]

boundary_prop["int_airgap_line_1"] = "MASTER_ROTOR_BOUNDARY"
boundary_prop["int_airgap_line_2"] = "SLAVE_ROTOR_BOUNDARY"
boundary_prop["int_sb_line_1"] = "MASTER_ROTOR_BOUNDARY"
boundary_prop["int_sb_line_2"] = "SLAVE_ROTOR_BOUNDARY"
boundary_prop["Rotor_Yoke_Side"] = "MASTER_SLAVE_ROTOR_BOUNDARY"   # it needs to be found out later

boundary_prop["int_sb_arc"] = "SB_ROTOR_BOUNDARY"

boundary_prop["ext_airgap_line_1"] = "MASTER_STATOR_BOUNDARY"
boundary_prop["ext_airgap_line_2"] = "SLAVE_STATOR_BOUNDARY"
boundary_prop["ext_sb_line_1"] = "MASTER_STATOR_BOUNDARY"
boundary_prop["ext_sb_line_2"] = "SLAVE_STATOR_BOUNDARY"
boundary_prop["airbox_line_1"] = "MASTER_STATOR_BOUNDARY"
boundary_prop["airbox_line_2"] = "SLAVE_STATOR_BOUNDARY"
boundary_prop["Stator_Yoke_Side"] = "MASTER_SLAVE_STATOR_BOUNDARY"   # it needs to be found out later

boundary_prop["ext_sb_arc"] = "SB_STATOR_BOUNDARY"
boundary_prop["ext_airgap_arc_copy"] = "AIRGAP_ARC_BOUNDARY"

boundary_prop["airbox_arc"] = "VP0_BOUNDARY"

