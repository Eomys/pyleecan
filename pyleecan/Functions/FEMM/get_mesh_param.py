# -*- coding: utf-8 -*-


def get_mesh_param(label, FEMM_dict):
    """Returns main mesh parameters corresponding to a surface label
    Parameters
    ----------
    label : str
        label of the surface to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM
    Returns
    -------
    mesh_dict : dict
        dictionnary containing the main mesh parameters of the surface
    """

    mesh_dict = dict()

    # Default automesh except airgap
    mesh_dict["automesh"] = FEMM_dict["automesh"]

    if "Lamination_Stator" in label:  # Stator
        if "Bore" in label:
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotS"]
        else:
            mesh_dict["element_size"] = FEMM_dict["elementsize_yokeS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_yokeS"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
    elif "Lamination_Rotor" in label:  # Rotor
        if "Bore" in label:
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotR"]
        else:
            mesh_dict["element_size"] = FEMM_dict["elementsize_yokeR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_yokeR"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RC"]
    elif "Ventilation" in label:  # Ventilation
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["meshsize"] = FEMM_dict["meshsize_air"]
        if "Stator" in label:  # if the Ventilation is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SV"]
        else:  # if the Ventilation is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RV"]
    elif "Hole_" in label:
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["meshsize"] = FEMM_dict["meshsize_air"]
        if "Stator" in label:  # if the Hole is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SH"]
        else:  # if the Hole is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RH"]
    elif "Wind" in label or "Bar" in label:  # Winding on the Lamination
        if "Stator" in label:  # if the winding is on the Stator
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotS"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SW"]
        else:  # if the winding is on the Rotor
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotR"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RW"]
    elif "Magnet" in label:  # Magnet
        if "Stator" in label:  # if the Magnet is on the Stator
            mesh_dict["element_size"] = FEMM_dict["elementsize_magnetS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_magnetS"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SM"]
        else:  # if the Magnet is on the Rotor
            mesh_dict["element_size"] = FEMM_dict["elementsize_magnetR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_magnetR"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RM"]
    elif "airgap" in label.lower() or "sliding" in label:
        mesh_dict["automesh"] = FEMM_dict["automesh_airgap"]
        mesh_dict["element_size"] = FEMM_dict["elementsize_airgap"]
        mesh_dict["meshsize"] = FEMM_dict["meshsize_airgap"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    elif "No_mesh" in label:
        mesh_dict["automesh"] = 0
        mesh_dict["element_size"] = 0
        mesh_dict["meshsize"] = 0
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    elif "Stator" in label:  # if label don't belong to any of the other groups
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
    elif "Rotor" in label:  # if label don't belong to any of the other groups
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RC"]
    return mesh_dict
