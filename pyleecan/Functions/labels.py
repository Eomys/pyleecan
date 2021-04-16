STATOR_LAB = "Stator"
ROTOR_LAB = "Rotor"
LAM_LAB = "Lamination"
BORE_LAB = "Bore"
YOKE_LAB = "Yoke"
SLID_LAB = "SlidingBand"
NO_MESH_LAB = "NoMesh"
NO_LAM_LAB = "None"  # To replace "Stator-X" when no lamination


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
    raise NotImplementedError(label_dict["full"] + " is not available yet")