# -*- coding: utf-8 -*-
"""@package assign_FEMM_Winding
@date Created on août 01 17:14 2018
@author franco_i
"""
import femm

from pyleecan.Functions.FEMM import GROUP_RW, GROUP_SW


def assign_FEMM_Winding(surf, prop, FEMM_dict, rotor, stator):
    """Assign properties to the winding in FEMM

    Parameters
    ----------
    surf : Surface
        The surface to assign
    prop :
        the property to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM
    rotor :
        the rotor object of the machine
    stator :
        the stator object of the machine

    Returns
    -------
    None
    
    """
    point_ref = surf.point_ref
    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    if "Rotor" in surf.label:  # Winding on the rotor
        Clabel = "Circr"
        Ntcoil = rotor.winding.Ntcoil
        if prop[-1] == "+":
            femm.mi_setblockprop(
                prop,
                FEMM_dict["automesh"],
                FEMM_dict["meshsize_slotR"],
                Clabel + prop[2],
                0,
                GROUP_RW,
                Ntcoil,
            )
        else:
            femm.mi_setblockprop(
                prop,
                FEMM_dict["automesh"],
                FEMM_dict["meshsize_slotR"],
                Clabel + prop[2],
                0,
                GROUP_RW,
                -Ntcoil,
            )
    else:  # Winding on the stator
        Clabel = "Circs"
        Ntcoil = stator.winding.Ntcoil
        if prop[-1] == "+":
            femm.mi_setblockprop(
                prop,
                FEMM_dict["automesh"],
                FEMM_dict["meshsize_slotS"],
                Clabel + prop[2],
                0,
                GROUP_SW,
                Ntcoil,
            )
        else:
            femm.mi_setblockprop(
                prop,
                FEMM_dict["automesh"],
                FEMM_dict["meshsize_slotS"],
                Clabel + prop[2],
                0,
                GROUP_SW,
                -Ntcoil,
            )
        femm.mi_clearselected()
