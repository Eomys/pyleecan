# -*- coding: utf-8 -*-
"""@package assign_FEMM_Lamination
@date Created on août 01 17:06 2018
@author franco_i
"""
import femm
from pyleecan.Functions.FEMM import GROUP_RC, GROUP_SC


def assign_FEMM_Lamination(surf, prop, FEMM_dict):
    """Assign the property of Lamination

    Parameters
    ----------
    surf : Surface
        The surface to assign
    prop : str
        the property to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM

    Returns
    -------
    None
    
    """
    point_ref = surf.point_ref

    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    if "Rotor" in surf.label:  # Lamination is Rotor
        femm.mi_setblockprop(
            prop, FEMM_dict["automesh"], FEMM_dict["meshsize_yokeR"], 0, 0, GROUP_RC, 0
        )
    else:  # Lamination is Stator
        femm.mi_setblockprop(
            prop, FEMM_dict["automesh"], FEMM_dict["meshsize_yokeS"], 0, 0, GROUP_SC, 0
        )
    femm.mi_clearselected()
