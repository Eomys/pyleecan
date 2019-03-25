# -*- coding: utf-8 -*-
"""@package assign_FEMM_Ventilation
@date Created on août 01 17:10 2018
@author franco_i
"""
import femm

from pyleecan.Functions.FEMM import GROUP_RV, GROUP_SV


def assign_FEMM_Ventilation(surf, prop, FEMM_dict):
    """Assign property of Ventilation in FEMM

    Parameters
    ----------
    surf : Surface
        Surface to assign
    label : str 
        the label of the surface to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM

    Returns
    -------
    None
    
    """
    point_ref = surf.point_ref

    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    if "Rotor" in surf.label:  # Ventilation on the rotor
        femm.mi_setblockprop(
            prop, FEMM_dict["automesh"], FEMM_dict["meshsize_air"], 0, 0, GROUP_RV, 0
        )
    else:  # Ventilation on the stator
        femm.mi_setblockprop(
            prop, FEMM_dict["automesh"], FEMM_dict["meshsize_air"], 0, 0, GROUP_SV, 0
        )
    femm.mi_clearselected()
