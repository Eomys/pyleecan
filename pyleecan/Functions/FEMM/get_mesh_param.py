# -*- coding: utf-8 -*-
from ..labels import (
    AIRGAP_LAB,
    BAR_LAB,
    LAM_LAB,
    MAG_LAB,
    STATOR_LAB,
    ROTOR_LAB,
    BORE_LAB,
    NO_MESH_LAB,
    SLID_LAB,
    VENT_LAB,
    KEY_LAB,
    HOLEM_LAB,
    HOLEV_LAB,
    WIND_LAB,
    NOTCH_LAB,
    SOP_LAB,
    WEDGE_LAB,
)


def get_mesh_param(label_dict, FEMM_dict):
    """Returns main mesh parameters corresponding to a surface label
    Parameters
    ----------
    label_dict : str
        Decoded label of the surface to assign
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    Returns
    -------
    mesh_dict : dict
        dictionary containing the main mesh parameters of the surface
    """

    mesh_dict = dict()

    # Default automesh except airgap
    mesh_dict["automesh"] = FEMM_dict["mesh"]["automesh"]
    # Get the mesh sizes related to the lamination label
    if label_dict["lam_label"] != "None":
        lam_mesh_dict = FEMM_dict["mesh"][label_dict["lam_label"]]
    else:
        lam_mesh_dict = None
    maxelementsize = FEMM_dict["mesh"]["maxelementsize"]
    meshsize_air = FEMM_dict["mesh"]["meshsize_air"]

    # Lamination
    if LAM_LAB in label_dict["surf_type"]:
        if BORE_LAB in label_dict["surf_type"]:
            mesh_dict["element_size"] = FEMM_dict["mesh"]["elementsize_airgap"]
            mesh_dict["meshsize"] = FEMM_dict["mesh"]["meshsize_airgap"]
        else:  # Yoke or other lines
            mesh_dict["element_size"] = lam_mesh_dict["elementsize_yoke"]
            mesh_dict["meshsize"] = lam_mesh_dict["meshsize_yoke"]
        if STATOR_LAB in label_dict["lam_type"]:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
        elif ROTOR_LAB in label_dict["lam_type"]:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RC"]
    # Ventilation
    elif VENT_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = maxelementsize
        mesh_dict["meshsize"] = meshsize_air
        if STATOR_LAB in label_dict["lam_type"]:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SV"]
        else:  # if the Ventilation is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RV"]
    # Hole Air zone
    elif HOLEV_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = maxelementsize
        mesh_dict["meshsize"] = meshsize_air
        if STATOR_LAB in label_dict["lam_type"]:  # if the Hole is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SH"]
        else:  # if the Hole is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RH"]
    # Magnet or HoleMagnet
    elif HOLEM_LAB in label_dict["surf_type"] or MAG_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = lam_mesh_dict["elementsize_magnet"]
        mesh_dict["meshsize"] = lam_mesh_dict["meshsize_magnet"]
        if STATOR_LAB in label_dict["lam_type"]:  # if the Magnet is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SM"]
        else:  # if the Magnet is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RM"]
    # Winding or Bar
    elif WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = lam_mesh_dict["elementsize_slot"]
        mesh_dict["meshsize"] = lam_mesh_dict["meshsize_slot"]
        if STATOR_LAB in label_dict["lam_type"]:  # if the winding is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SW"]
        else:  # if the winding is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RW"]
    # Slot opening
    elif SOP_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = lam_mesh_dict["elementsize_slot"]
        mesh_dict["meshsize"] = lam_mesh_dict["meshsize_slot"]
        if STATOR_LAB in label_dict["lam_type"]:  # if the opening is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SSI"]
        else:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RSI"]
    # Slot Notches
    elif NOTCH_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = lam_mesh_dict["elementsize_slot"]
        mesh_dict["meshsize"] = lam_mesh_dict["meshsize_slot"]
        if STATOR_LAB in label_dict["lam_type"]:  # if the notch is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SN"]
        else:  # if the notch is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RN"]
    # Slot Wedges
    elif WEDGE_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = lam_mesh_dict["elementsize_slot"]
        mesh_dict["meshsize"] = lam_mesh_dict["meshsize_slot"]
        if STATOR_LAB in label_dict["lam_type"]:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SWE"]
        else:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RWE"]
    # Notches Keys
    elif KEY_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = lam_mesh_dict["elementsize_key"]
        mesh_dict["meshsize"] = lam_mesh_dict["meshsize_key"]
        if STATOR_LAB in label_dict["lam_type"]:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SK"]
        else:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RK"]
    # Sliding Band / Airgap
    elif SLID_LAB in label_dict["surf_type"] or AIRGAP_LAB in label_dict["surf_type"]:
        mesh_dict["automesh"] = FEMM_dict["mesh"]["automesh_airgap"]
        mesh_dict["element_size"] = FEMM_dict["mesh"]["elementsize_airgap"]
        mesh_dict["meshsize"] = FEMM_dict["mesh"]["meshsize_airgap"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    elif NO_MESH_LAB in label_dict["surf_type"]:
        mesh_dict["automesh"] = 0
        mesh_dict["element_size"] = 0
        mesh_dict["meshsize"] = 0
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    elif STATOR_LAB in label_dict["lam_type"]:
        # if label don't belong to any of the other groups
        mesh_dict["element_size"] = maxelementsize
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
    elif ROTOR_LAB in label_dict["lam_type"]:
        # if label don't belong to any of the other groups
        mesh_dict["element_size"] = maxelementsize
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RC"]
    else:
        raise Exception(
            "Error while assigning surfaces in FEMM: Unknown label "
            + label_dict["full"]
        )
    return mesh_dict
