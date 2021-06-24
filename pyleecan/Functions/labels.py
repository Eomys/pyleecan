STATOR_LAB = "Stator"
ROTOR_LAB = "Rotor"
LAM_LAB = "Lamination"
BORE_LAB = "Bore"
YOKE_LAB = "Yoke"
SLID_LAB = "SlidingBand"
WIND_LAB = "Winding"
BAR_LAB = "Bar"
HOLEV_LAB = "HoleVoid"
HOLEM_LAB = "HoleMag"
MAG_LAB = "Magnet"
AIRGAP_LAB = "Airgap"
NO_MESH_LAB = "NoMesh"
VENT_LAB = "Ventilation"
NO_LAM_LAB = "None"  # To replace "Stator-X" when no lamination
TOOTH_LAB = "Tooth"

# Line Property dict
BOUNDARY_PROP_LAB = "Boundary"
YS_LAB = "YokeSide"
SLID_LINE1_LAB = "airgap_line_1"
SLID_LINE2_LAB = "airgap_line_2"
SLID_LINE_LAB = "airgap_line"

RADIUS_PROP_LAB = "LamRadius"
MAGNET_PROP_LAB = "MagnetLines"


def decode_label(label):
    """Spit the label to return a dict with the main information"""
    label_dict = {"full": label}
    label_split = label.split("_")

    # Decode Lamination label
    if len(label_split) > 0:
        # Label like "Stator-X"
        label_dict["lam_label"] = label_split[0]
        if "-" in label_split[0]:
            label_dict["lam_type"] = label_split[0].split("-")[0]
            label_dict["lam_id"] = label_split[0].split("-")[1]
        else:
            label_dict["lam_type"] = label_split[0]
            label_dict["lam_id"] = 0
    # Decode surf type
    if len(label_split) > 1:
        label_dict["surf_type"] = label_split[1]
    # Decode surf index
    if len(label_split) > 2:
        label_dict["index"] = label_split[2]
        id_list = label_dict["index"].split("-")
        label_dict["R_id"] = int(id_list[0][1:])
        label_dict["T_id"] = int(id_list[1][1:])
        label_dict["S_id"] = int(id_list[2][1:])
    # Decode line label
    if len(label_split) > 3:
        label_dict["line_label"] = label_split[3]

    return label_dict


def get_obj_from_label(machine, label=None, label_dict=None):
    """Return the object from the machine corresponding to the label"""
    if label_dict is None:
        label_dict = decode_label(label)
    if label_dict["lam_label"] is NO_LAM_LAB:
        raise NotImplementedError(label_dict["full"] + " is not available yet")

    lam_obj = machine.get_lam_by_label(label_dict["lam_label"])
    if LAM_LAB in label_dict["surf_type"]:
        return lam_obj
    elif WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
        return lam_obj
    elif VENT_LAB in label_dict["surf_type"]:
        return lam_obj.axial_vent[label_dict["R_id"]]
    elif HOLEV_LAB in label_dict["surf_type"]:
        return lam_obj.hole[label_dict["R_id"]]
    elif HOLEM_LAB in label_dict["surf_type"]:
        hole = lam_obj.hole[label_dict["R_id"]]
        return hole.get_magnet_dict()["magnet_" + str(label_dict["T_id"])]
    elif MAG_LAB in label_dict["surf_type"]:
        return lam_obj.magnet
    raise NotImplementedError(label_dict["full"] + " is not available yet")
