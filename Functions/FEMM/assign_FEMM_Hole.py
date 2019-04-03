# -*- coding: utf-8 -*-
"""@package assign_FEMM_Hole
@date Created on April 03 08:27 2019
@author sebastian_g
"""
import femm

from pyleecan.Functions.FEMM import GROUP_RH, GROUP_SH


def assign_FEMM_Hole(surf, prop, FEMM_dict):
    """Assign property of Hole in FEMM

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
    if "HoleR" in surf.label:  # Hole on the rotor
        femm.mi_setblockprop(
            prop, FEMM_dict["automesh"], FEMM_dict["meshsize_air"], 0, 0, GROUP_RH, 0
        )
    else:  # Hole on the stator
        femm.mi_setblockprop(
            prop, FEMM_dict["automesh"], FEMM_dict["meshsize_air"], 0, 0, GROUP_SH, 0
        )
    femm.mi_clearselected()
