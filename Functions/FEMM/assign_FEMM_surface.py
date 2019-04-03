# -*- coding: utf-8 -*-
"""@package assign_FEMM_Machine_part
@date Created on août 09 14:12 2018
@author franco_i
"""
from pyleecan.Functions.FEMM.assign_FEMM_Lamination import assign_FEMM_Lamination
from pyleecan.Functions.FEMM.assign_FEMM_Magnet import assign_FEMM_Magnet
from pyleecan.Functions.FEMM.assign_FEMM_Ventilation import assign_FEMM_Ventilation
from pyleecan.Functions.FEMM.assign_FEMM_Hole import assign_FEMM_Hole
from pyleecan.Functions.FEMM.assign_FEMM_Winding import assign_FEMM_Winding
from pyleecan.Functions.FEMM.assign_FEMM_airgap import assign_FEMM_airgap
from pyleecan.Functions.FEMM.assign_FEMM_no_mesh import assign_FEMM_no_mesh


def assign_FEMM_surface(surf, prop, FEMM_dict, rotor, stator):
    """Assign the property given in parameter to surface having the label given

    Parameters
    ----------
    surf : Surface
        the surface to assign
    prop : str
        The property to assign in FEMM
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM
    rotor : Lamination
        The rotor of the machine
    stator : Lamination
        The stator of the machine

    Returns
    -------
    None
    
    """
    label = surf.label

    # point_ref is None => don't assign the surface
    if surf.point_ref is not None:
        if "Lamination_Stator" in label:  # Stator
            assign_FEMM_Lamination(surf, prop, FEMM_dict)
        elif "Lamination_Rotor" in label:  # Rotor
            assign_FEMM_Lamination(surf, prop, FEMM_dict)
        elif "Ventilation" in label:  # Ventilation
            assign_FEMM_Ventilation(surf, prop, FEMM_dict)
        elif "Hole" in label:  # Ventilation
            assign_FEMM_Hole(surf, prop, FEMM_dict)
        elif "Wind" in label:  # Winding on the Lamination
            assign_FEMM_Winding(surf, prop, FEMM_dict, rotor, stator)
        elif "Magnet" in label:  # Magnet
            assign_FEMM_Magnet(surf, prop, FEMM_dict)
        elif "Airgap" in label:  # Airgap
            assign_FEMM_airgap(surf, prop, FEMM_dict)
        elif "No_mesh" in label:  # Sliding band
            assign_FEMM_no_mesh(surf)
