# -*- coding: utf-8 -*-
"""@package get_element_size_from_label
@date Created on août 09 14:00 2018
@author franco_i
"""
from pyleecan.Functions.FEMM import (
    GROUP_RC,
    GROUP_RV,
    GROUP_RW,
    GROUP_SC,
    GROUP_SV,
    GROUP_SW,
    GROUP_AG,
)


def get_element_size(label, FEMM_dict):
    """Returns element parameter FEMM of each part of the machine

    Parameters
    ----------
    label : str
        label of the surface to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM

    Returns
    -------
    E_dict : dict
        dictionnary containing element size and group
    
    """

    E_dict = dict()
    if "Lamination_Stator" in label:  # Stator
        if "bore" in label:
            E_dict["element_size"] = FEMM_dict["elementsize_slotS"]
        else:
            E_dict["element_size"] = FEMM_dict["elementsize_yokeS"]
        E_dict["group"] = GROUP_SC
    elif "Lamination_Rotor" in label:  # Rotor
        if "bore" in label:
            E_dict["element_size"] = FEMM_dict["elementsize_slotR"]
        else:
            E_dict["element_size"] = FEMM_dict["elementsize_yokeR"]
        E_dict["group"] = GROUP_RC
    elif "Ventilation" in label:  # Ventilation
        E_dict["element_size"] = FEMM_dict["maxelementsize"]
        if label[12] == "S":  # if the Ventilation is on the Stator
            E_dict["group"] = GROUP_SV
        else:  # if the Ventilation is on the Rotor
            E_dict["group"] = GROUP_RV
    elif "Wind" in label:  # Winding on the Lamination
        if label[4] == "S":  # if the winding is on the Stator
            E_dict["element_size"] = FEMM_dict["elementsize_slotS"]
            E_dict["group"] = GROUP_SW
        else:  # if the winding is on the Rotor
            E_dict["element_size"] = FEMM_dict["elementsize_slotR"]
            E_dict["group"] = GROUP_RW
    elif "Magnet" in label:  # Magnet
        if label[6] == "S":  # if the Magnet is on the Stator
            E_dict["element_size"] = FEMM_dict["elementsize_magnetS"]
            E_dict["group"] = GROUP_SW
        else:  # if the Magnet is on the Rotor
            E_dict["element_size"] = FEMM_dict["elementsize_magnetR"]
            E_dict["group"] = GROUP_RW
    elif "Airgap" in label:
        E_dict["element_size"] = FEMM_dict["elementsize_airgap"]
        E_dict["group"] = GROUP_AG
    elif "No_mesh" in label:
        E_dict["element_size"] = 0
        E_dict["group"] = GROUP_AG
    return E_dict
