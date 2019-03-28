# -*- coding: utf-8 -*-
"""@package assign_FEMM_Winding
@date Created on août 01 17:14 2018
@author franco_i
"""
import femm

from pyleecan.Functions.FEMM import GROUP_RW, GROUP_SW


def assign_FEMM_Winding(surf, prop, mesh_dict, rotor, stator):
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

    if "Rotor" in surf.label:  # Winding on the rotor
        Clabel = "Circr" + prop[2]
        Ntcoil = rotor.winding.Ntcoil
    else:  # winding on the stator
        Clabel = "Circs" + prop[2]
        Ntcoil = stator.winding.Ntcoil
    if prop[-1] == "-":  # Adapt Ntcoil sign if needed
        Ntcoil *= -1

    # Select the surface
    point_ref = surf.point_ref
    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)

    # Apply property
    femm.mi_setblockprop(
        prop,
        mesh_dict["automesh"],
        mesh_dict["meshsize"],
        Clabel,
        0,
        mesh_dict["group"],
        Ntcoil,
    )
    femm.mi_clearselected()
