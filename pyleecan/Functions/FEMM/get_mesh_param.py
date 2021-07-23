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
    HOLEM_LAB,
    HOLEV_LAB,
    WIND_LAB,
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
    mesh_dict["automesh"] = FEMM_dict["automesh"]

    if LAM_LAB in label_dict["surf_type"] and STATOR_LAB in label_dict["lam_type"]:
        # Stator Lamination
        if BORE_LAB in label_dict["surf_type"]:
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotS"]
        else:  # Yoke or other lines
            mesh_dict["element_size"] = FEMM_dict["elementsize_yokeS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_yokeS"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
    elif LAM_LAB in label_dict["surf_type"] and ROTOR_LAB in label_dict["lam_type"]:
        # Rotor Lamination
        if BORE_LAB in label_dict["surf_type"]:
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotR"]
        else:  # Yoke or other lines
            mesh_dict["element_size"] = FEMM_dict["elementsize_yokeR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_yokeR"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
    elif VENT_LAB in label_dict["surf_type"]:  # Ventilation
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["meshsize"] = FEMM_dict["meshsize_air"]
        if STATOR_LAB in label_dict["lam_type"]:
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SV"]
        else:  # if the Ventilation is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RV"]
    elif HOLEV_LAB in label_dict["surf_type"]:
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["meshsize"] = FEMM_dict["meshsize_air"]
        if STATOR_LAB in label_dict["lam_type"]:  # if the Hole is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SH"]
        else:  # if the Hole is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RH"]
    elif HOLEM_LAB in label_dict["surf_type"] or MAG_LAB in label_dict["surf_type"]:
        # Magnet or HoleMagnet
        if STATOR_LAB in label_dict["lam_type"]:  # if the Magnet is on the Stator
            mesh_dict["element_size"] = FEMM_dict["elementsize_magnetS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_magnetS"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SM"]
        else:  # if the Magnet is on the Rotor
            mesh_dict["element_size"] = FEMM_dict["elementsize_magnetR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_magnetR"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RM"]
    elif WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
        # Winding
        if STATOR_LAB in label_dict["lam_type"]:  # if the winding is on the Stator
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotS"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotS"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SW"]
        else:  # if the winding is on the Rotor
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotR"]
            mesh_dict["meshsize"] = FEMM_dict["meshsize_slotR"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RW"]
    elif SLID_LAB in label_dict["surf_type"] or AIRGAP_LAB in label_dict["surf_type"]:
        mesh_dict["automesh"] = FEMM_dict["automesh_airgap"]
        mesh_dict["element_size"] = FEMM_dict["elementsize_airgap"]
        mesh_dict["meshsize"] = FEMM_dict["meshsize_airgap"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    elif NO_MESH_LAB in label_dict["surf_type"]:
        mesh_dict["automesh"] = 0
        mesh_dict["element_size"] = 0
        mesh_dict["meshsize"] = 0
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    elif STATOR_LAB in label_dict["lam_type"]:
        # if label don't belong to any of the other groups
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
    elif ROTOR_LAB in label_dict["lam_type"]:
        # if label don't belong to any of the other groups
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RC"]
    else:
        raise Exception(
            "Error while assigning surfaces in FEMM: Unknown label "
            + label_dict["full"]
        )
    return mesh_dict
