# -*- coding: utf-8 -*-
"""@package assign_FEMM_Ventilation
@date Created on août 01 17:10 2018
@author franco_i
"""
import femm

from pyleecan.Functions.FEMM import GROUP_RV, GROUP_SV


def assign_FEMM_Ventilation(point_ref, label, prop, draw_FEMM_param):
    """Assign property of Ventilation in FEMM

    Parameters
    ----------
    point_ref :
        the reference point of the surface
    prop :
        the property to assign
    label :
        the label of the surface to assign
    draw_FEMM_param :
        Dictionnary containing parameter needed
        to draw in FEMM

    Returns
    -------
    None
    
    """
    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    if "Rotor" in label:  # Ventilation on the rotor
        femm.mi_setblockprop(
            prop,
            draw_FEMM_param["automesh"],
            draw_FEMM_param["meshsize_air"],
            0,
            0,
            GROUP_RV,
            0,
        )
    else:  # Ventilation on the stator
        femm.mi_setblockprop(
            prop,
            draw_FEMM_param["automesh"],
            draw_FEMM_param["meshsize_air"],
            0,
            0,
            GROUP_SV,
            0,
        )
    femm.mi_clearselected()
