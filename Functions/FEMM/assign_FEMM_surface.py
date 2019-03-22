# -*- coding: utf-8 -*-
"""@package assign_FEMM_Machine_part
@date Created on août 09 14:12 2018
@author franco_i
"""
from pyleecan.Functions.FEMM.assign_FEMM_Lamination import assign_FEMM_Lamination
from pyleecan.Functions.FEMM.assign_FEMM_Magnet import assign_FEMM_Magnet
from pyleecan.Functions.FEMM.assign_FEMM_Ventilation import assign_FEMM_Ventilation
from pyleecan.Functions.FEMM.assign_FEMM_Winding import assign_FEMM_Winding
from pyleecan.Functions.FEMM.assign_FEMM_airgap import assign_FEMM_airgap
from pyleecan.Functions.FEMM.assign_FEMM_no_mesh import assign_FEMM_no_mesh


def assign_FEMM_surface(surf, prop, draw_FEMM_param, rotor, stator):
    """Assign the property given in parameter to surface having the label given

    Parameters
    ----------
    surf :
        the surface to assign
    prop :
        The property to assign in FEMM
    draw_FEMM_param :
        Dictionnary containing parameter needed to draw in FEMM
    rotor :
        rotor object of the machine
    stator :
        stator object of the machine

    Returns
    -------
    None
    
    """
    label = surf.label
    point_ref = surf.point_ref
    if point_ref is not None:
        if "Lamination_Stator" in label:  # Stator
            assign_FEMM_Lamination(surf, prop, draw_FEMM_param)
        elif "Lamination_Rotor" in label:  # Rotor
            assign_FEMM_Lamination(surf, prop, draw_FEMM_param)
        elif "Ventilation" in label:  # Ventilation
            assign_FEMM_Ventilation(point_ref, label, prop, draw_FEMM_param)
        elif "Wind" in label:  # Winding on the Lamination
            assign_FEMM_Winding(point_ref, label, prop, draw_FEMM_param, rotor, stator)
        elif "Magnet" in label:  # Magnet
            assign_FEMM_Magnet(surf, prop, draw_FEMM_param)
        elif "Airgap" in label:  # Airgap
            assign_FEMM_airgap(surf, prop, draw_FEMM_param)
        elif "No_mesh" in label:  # Sliding band
            assign_FEMM_no_mesh(surf)
