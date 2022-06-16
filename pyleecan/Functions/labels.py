## Lamination Label
STATOR_LAB = "Stator"
ROTOR_LAB = "Rotor"
NO_LAM_LAB = "None"  # To replace "Stator-X" when no lamination
# Short Lamination label alternative
STATOR_LAB_S = "STA"  # Short version
ROTOR_LAB_S = "ROT"  # Short version

## Surface label
LAM_LAB = "Lamination"
SHAFT_LAB = "Shaft"
BORE_LAB = "Bore"
YOKE_LAB = "Yoke"
SLID_LAB = "SlidingBand"
WIND_LAB = "Winding"
SOP_LAB = "SlotOpening"
WEDGE_LAB = "SlotWedge"
BAR_LAB = "Bar"
HOLEV_LAB = "HoleVoid"
HOLEM_LAB = "HoleMag"
MAG_LAB = "Magnet"
AIRGAP_LAB = "Airgap"
NO_MESH_LAB = "NoMesh"
VENT_LAB = "Ventilation"
TOOTH_LAB = "Tooth"
AIRBOX_LAB = "Airbox"
NOTCH_LAB = "Notch"
# Short Surface label alternative
LAM_LAB_S = "Lam"
HOLEV_LAB_S = "HV"
WIND_LAB_S = "Wind"
HOLEM_LAB_S = "HM"
VENT_LAB_S = "Vent"

## Line Property dict
DRAW_PROP_LAB = "IS_DRAW"
BOUNDARY_PROP_LAB = "Boundary"
RIGHT_LAB = "Right"  # Right is 0x line
LEFT_LAB = "Left"
BOT_LAB = "Bot"
TOP_LAB = "Top"
YS_LAB = "YokeSide"
YSN_LAB = YS_LAB + NOTCH_LAB
YSM_LAB = YS_LAB + MAG_LAB
YSR_LAB = YS_LAB + "-" + RIGHT_LAB
YSL_LAB = YS_LAB + "-" + LEFT_LAB
YSNR_LAB = YSN_LAB + "-" + RIGHT_LAB
YSNL_LAB = YSN_LAB + "-" + LEFT_LAB
YSMR_LAB = YSM_LAB + "-" + RIGHT_LAB
YSML_LAB = YSM_LAB + "-" + LEFT_LAB
# Shaft BC properties
SHAFTS_LAB = "ShaftSide"
SHAFTSR_LAB = SHAFTS_LAB + "-" + RIGHT_LAB
SHAFTSL_LAB = SHAFTS_LAB + "-" + LEFT_LAB
SHAFTR_LAB = "ShaftRadius"
# AirBox BC properties
AIRBOX_S_LAB = "ABSide"
AIRBOX_SR_LAB = AIRBOX_S_LAB + "-" + RIGHT_LAB
AIRBOX_SL_LAB = AIRBOX_S_LAB + "-" + LEFT_LAB
AIRBOX_R_LAB = "ABRadius"
# Sliding Band BC properties
SBS_TR_LAB = "sliding_sideline_" + TOP_LAB + "_" + RIGHT_LAB
SBS_TL_LAB = "sliding_sideline_" + TOP_LAB + "_" + LEFT_LAB
SBS_BR_LAB = "sliding_sideline_" + BOT_LAB + "_" + RIGHT_LAB
SBS_BL_LAB = "sliding_sideline_" + BOT_LAB + "_" + LEFT_LAB
SBR_B_LAB = "sliding_radius_" + BOT_LAB
SBR_T_LAB = "sliding_radius_" + TOP_LAB
# Airgap  BC properties
AS_TR_LAB = "airgap_sideline_" + TOP_LAB + "_" + RIGHT_LAB
AS_TL_LAB = "airgap_sideline_" + TOP_LAB + "_" + LEFT_LAB
AS_BR_LAB = "airgap_sideline_" + BOT_LAB + "_" + RIGHT_LAB
AS_BL_LAB = "airgap_sideline_" + BOT_LAB + "_" + LEFT_LAB
AR_B_LAB = "airgap_radius_" + BOT_LAB
AR_T_LAB = "airgap_radius_" + TOP_LAB

RADIUS_PROP_LAB = "LamRadius"
MAGNET_PROP_LAB = "MagnetLines"
MESH_PROP_LAB = "Mesh"


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
    if len(label_split) > 2 and label_split[2].count("-") == 2:
        label_dict["index"] = label_split[2]
        id_list = label_dict["index"].split("-")
        label_dict["R_id"] = int(id_list[0][1:])
        label_dict["T_id"] = int(id_list[1][1:])
        label_dict["S_id"] = int(id_list[2][1:])

    return label_dict


def update_RTS_index(
    label=None, label_dict=None, R_id=None, T_id=None, S_id=None, surf_type_label=None
):
    """Update the index part of a label
    Stator_Winding_R0-T0-S0 => Stator_Winding_RX-TY-SZ

    Parameters
    ----------
    label : str
        Label to update
    label_dict : dict
        Split dict of the label (to avoid decoding twice)
    R_id : int
        Radial index to use
    T_id : int
        Tangantial index to use
    S_id : int
        Slot index to use
    surf_type_label : str
        To overwritte the surf_type part of the label
    """
    if label_dict is None:
        label_dict = decode_label(label)
    assert label_dict is not None
    if R_id is not None:
        label_dict["R_id"] = R_id
    if T_id is not None:
        label_dict["T_id"] = T_id
    if S_id is not None:
        label_dict["S_id"] = S_id
    if surf_type_label is not None:
        label_dict["surf_type"] = surf_type_label

    return (
        label_dict["lam_label"]
        + "_"
        + label_dict["surf_type"]
        + "_R"
        + str(label_dict["R_id"])
        + "-T"
        + str(label_dict["T_id"])
        + "-S"
        + str(label_dict["S_id"])
    )


def get_obj_from_label(machine, label=None, label_dict=None):
    """Return the object from the machine corresponding to the label"""
    if label_dict is None:
        label_dict = decode_label(label)
    if label_dict["lam_label"] is NO_LAM_LAB:
        raise NotImplementedError(label_dict["full"] + " is not available yet")

    lam_obj = machine.get_lam_by_label(label_dict["lam_label"])
    if LAM_LAB in label_dict["surf_type"]:
        return lam_obj
    elif (
        WIND_LAB in label_dict["surf_type"]
        or BAR_LAB in label_dict["surf_type"]
        or WIND_LAB_S in label_dict["surf_type"]
    ):
        return lam_obj
    elif VENT_LAB in label_dict["surf_type"]:
        return lam_obj.axial_vent[label_dict["R_id"]]
    elif HOLEV_LAB in label_dict["surf_type"] or HOLEV_LAB_S in label_dict["surf_type"]:
        return lam_obj.get_hole_list()[label_dict["R_id"]]
    elif HOLEM_LAB in label_dict["surf_type"] or HOLEM_LAB_S in label_dict["surf_type"]:
        hole = lam_obj.get_hole_list()[label_dict["R_id"]]
        return hole.get_magnet_dict()["magnet_" + str(label_dict["T_id"])]
    elif MAG_LAB in label_dict["surf_type"]:
        return lam_obj.magnet
    raise NotImplementedError(label_dict["full"] + " is not available yet")


def short_label(label):
    """Returns a short version of a label"""
    label_dict = decode_label(label)
    # Short Lamination name
    label_dict["lam_label"] = label_dict["lam_label"].replace(STATOR_LAB, STATOR_LAB_S)
    label_dict["lam_label"] = label_dict["lam_label"].replace(ROTOR_LAB, ROTOR_LAB_S)
    # Short Surface name
    label_dict["surf_type"] = label_dict["surf_type"].replace(LAM_LAB, LAM_LAB_S)
    label_dict["surf_type"] = label_dict["surf_type"].replace(WIND_LAB, WIND_LAB_S)
    label_dict["surf_type"] = label_dict["surf_type"].replace(HOLEV_LAB, HOLEV_LAB_S)
    label_dict["surf_type"] = label_dict["surf_type"].replace(HOLEM_LAB, HOLEM_LAB_S)
    label_dict["surf_type"] = label_dict["surf_type"].replace(VENT_LAB, VENT_LAB_S)

    # Build the new label
    label = label_dict["lam_label"] + "_" + label_dict["surf_type"]
    if "index" in label_dict:
        label += "_" + label_dict["index"]
    return label
