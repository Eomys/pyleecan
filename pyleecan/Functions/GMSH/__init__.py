class InputError(Exception):
    """ """

    pass

#
# boundary_list = [
#     "MASTER_ROTOR_BOUNDARY",
#     "SLAVE_ROTOR_BOUNDARY",
#     "SB_ROTOR_BOUNDARY",
#     "MASTER_STATOR_BOUNDARY",
#     "SLAVE_STATOR_BOUNDARY",
#     "SB_STATOR_BOUNDARY",
#     "AIRGAP_ARC_BOUNDARY",
#     "VP0_BOUNDARY",
# ]
#
# # dictionary to match FEA boundary conditions (dict values)
# # with line labels (dict keys) that are set in the build_geometry methods
# boundary_prop = dict()
# boundary_prop["int_airgap_line_1"] = "MASTER_ROTOR_BOUNDARY"
# boundary_prop["int_airgap_line_2"] = "SLAVE_ROTOR_BOUNDARY"
# boundary_prop["int_sb_line_1"] = "MASTER_ROTOR_BOUNDARY"
# boundary_prop["int_sb_line_2"] = "SLAVE_ROTOR_BOUNDARY"
# boundary_prop["Lamination_Rotor_Yoke_Side_Right"] = "MASTER_ROTOR_BOUNDARY"
# boundary_prop["Lamination_Rotor_Yoke_Side_Left"] = "SLAVE_ROTOR_BOUNDARY"
# boundary_prop["Shaft_Side_Right"] = "MASTER_ROTOR_BOUNDARY"
# boundary_prop["Shaft_Side_Left"] = "SLAVE_ROTOR_BOUNDARY"
# boundary_prop["int_sb_arc"] = "SB_ROTOR_BOUNDARY"
# boundary_prop["ext_airgap_line_1"] = "MASTER_STATOR_BOUNDARY"
# boundary_prop["ext_airgap_line_2"] = "SLAVE_STATOR_BOUNDARY"
# boundary_prop["ext_sb_line_1"] = "MASTER_STATOR_BOUNDARY"
# boundary_prop["ext_sb_line_2"] = "SLAVE_STATOR_BOUNDARY"
# boundary_prop["airbox_line_1"] = "MASTER_STATOR_BOUNDARY"
# boundary_prop["airbox_line_2"] = "SLAVE_STATOR_BOUNDARY"
# boundary_prop["Lamination_Stator_Yoke_Side_Right"] = "MASTER_STATOR_BOUNDARY"
# boundary_prop["Lamination_Stator_Yoke_Side_Left"] = "SLAVE_STATOR_BOUNDARY"
# boundary_prop["ext_sb_arc"] = "SB_STATOR_BOUNDARY"
# boundary_prop["ext_airgap_arc_copy"] = "AIRGAP_ARC_BOUNDARY"
# boundary_prop["airbox_arc"] = "VP0_BOUNDARY"
#
# # dict for the translation of the actual surface labels into Elmer compatible labels,
# # i.e. max. 30 characters; key: actual label, value: Elmer label
# surface_label = dict()
# surface_label["Shaft"] = "SHAFT"
# surface_label["Lamination_Rotor"] = "ROTOR_LAM"
# surface_label["Lamination_Stator"] = "STATOR_LAM"
# surface_label["Lamination_Rotor_Bore_Radius_Ext"] = "ROTOR_LAM"
# surface_label["Lamination_Stator_Bore_Radius_Int"] = "STATOR_LAM"
# surface_label["Airgap_int"] = "AG_INT"
# surface_label["SlidingBand_int"] = "SB_INT"
# surface_label["SlidingBand_ext"] = "SB_EXT"
# surface_label["Airgap_ext"] = "AG_EXT"
# surface_label["Airbox"] = "AIRBOX"
#
# # TODO: use actual surface labels
# for rr in range(0, 3):
#     for tt in range(0, 3):
#         for ss in range(0, 60):
#             # Windings
#             old_label = "Wind_Stator_R" + str(rr) + "_T" + str(tt) + "_S" + str(ss)
#             new_label = "W_STA_R" + str(rr) + "_T" + str(tt) + "_S" + str(ss)
#             surface_label[old_label] = new_label
#
#
# for rr in range(0, 5):
#     for tt in range(0, 5):
#         for ss in range(0, 20):
#             # Rotor Holes
#             old_label = "Hole_Rotor_R" + str(rr) + "_T" + str(tt) + "_S" + str(ss)
#             new_label = "H_ROTOR_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             # Interior Magnets
#             old_label = (
#                 "HoleMagnet_Rotor_Parallel_N_R"
#                 + str(rr)
#                 + "_T"
#                 + str(tt)
#                 + "_S"
#                 + str(ss)
#             )
#             new_label = "H_MAGNET_ROT_PAR_N_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             old_label = (
#                 "HoleMagnet_Rotor_Parallel_S_R"
#                 + str(rr)
#                 + "_T"
#                 + str(tt)
#                 + "_S"
#                 + str(ss)
#             )
#             new_label = "H_MAGNET_ROT_PAR_S_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             old_label = (
#                 "HoleMagnet_Rotor_Radial_N_R"
#                 + str(rr)
#                 + "_T"
#                 + str(tt)
#                 + "_S"
#                 + str(ss)
#             )
#             new_label = "H_MAGNET_ROT_RAD_N_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             old_label = (
#                 "HoleMagnet_Rotor_Radial_S_R"
#                 + str(rr)
#                 + "_T"
#                 + str(tt)
#                 + "_S"
#                 + str(ss)
#             )
#             new_label = "H_MAGNET_ROT_RAD_S_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             # Surface Magnets
#             old_label = (
#                     "MagnetRotorParallel_N_R"
#                     + str(rr)
#                     + "_T"
#                     + str(tt)
#                     + "_S"
#                     + str(ss)
#             )
#             new_label = "MAGNET_ROT_PAR_N_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             old_label = (
#                     "MagnetRotorParallel_S_R"
#                     + str(rr)
#                     + "_T"
#                     + str(tt)
#                     + "_S"
#                     + str(ss)
#             )
#             new_label = "MAGNET_ROT_PAR_S_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             old_label = (
#                     "MagnetRotorRadial_N_R"
#                     + str(rr)
#                     + "_T"
#                     + str(tt)
#                     + "_S"
#                     + str(ss)
#             )
#             new_label = "MAGNET_ROT_RAD_N_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#             old_label = (
#                     "MagnetRotorRadial_S_R"
#                     + str(rr)
#                     + "_T"
#                     + str(tt)
#                     + "_S"
#                     + str(ss)
#             )
#             new_label = "MAGNET_ROT_RAD_S_R" + str(rr) + "T" + str(tt) + "S" + str(ss)
#             surface_label[old_label] = new_label
#
#
