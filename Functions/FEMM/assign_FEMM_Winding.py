# -*- coding: utf-8 -*-
"""@package assign_FEMM_Winding
@date Created on août 01 17:14 2018
@author franco_i
"""
import femm

from pyleecan.Functions.FEMM import GROUP_RW, GROUP_SW


def assign_FEMM_Winding(point_ref, label, prop, draw_FEMM_param, rotor, stator):
    """Assign properties to the winding in FEMM

    Parameters
    ----------
    point_ref :
        the reference point of the surface
    label :
        the label of the surface to assign
    prop :
        the property to assign
    draw_FEMM_param :
        Dictionnary containing parameter needed to draw in
        FEMM
    rotor :
        the rotor object of the machine
    stator :
        the stator object of the machine

    Returns
    -------
    None
    
    """
    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    if "Rotor" in label:  # Winding on the rotor
        Clabel = "Circs"
        Ntcoil = rotor.winding.Ntcoil
        if prop[-1] == "+":
            femm.mi_setblockprop(
                prop,
                draw_FEMM_param["automesh"],
                draw_FEMM_param["meshsize_slotR"],
                Clabel + prop[2],
                0,
                GROUP_RW,
                Ntcoil,
            )
        else:
            femm.mi_setblockprop(
                prop,
                draw_FEMM_param["automesh"],
                draw_FEMM_param["meshsize_slotR"],
                Clabel + prop[2],
                0,
                GROUP_RW,
                -Ntcoil,
            )
    else:  # Winding on the stator
        Clabel = "Circr"
        Ntcoil = stator.winding.Ntcoil
        if prop[-1] == "+":
            femm.mi_setblockprop(
                prop,
                draw_FEMM_param["automesh"],
                draw_FEMM_param["meshsize_slotS"],
                Clabel + prop[2],
                0,
                GROUP_SW,
                Ntcoil,
            )
        else:
            femm.mi_setblockprop(
                prop,
                draw_FEMM_param["automesh"],
                draw_FEMM_param["meshsize_slotS"],
                Clabel + prop[2],
                0,
                GROUP_SW,
                -Ntcoil,
            )
        femm.mi_clearselected()
