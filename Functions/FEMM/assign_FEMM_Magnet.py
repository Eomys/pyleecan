# -*- coding: utf-8 -*-
"""@package assign_FEMM_Magnet
@date Created on août 01 17:19 2018
@author franco_i
"""
import femm
from numpy import angle, pi

from pyleecan.Functions.FEMM import GROUP_RW, GROUP_SW


def assign_FEMM_Magnet(surf, prop, FEMM_dict):
    """Assign the property of Magnet in FEMM

    Parameters
    ----------
    surf : Surface
        the surface of the magnet to assign
    prop : str
        the property to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM

    Returns
    -------
    None
    
    """
    label = surf.label
    point_ref = surf.point_ref
    Zbegin = surf.get_lines()[0].get_begin()
    theta = angle(Zbegin)

    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    if "Rotor" in label:  # magnet on the rotor
        if "Radial" in label:  # Radial magnetization
            if label[-10] == "N":  # North pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetR"],
                    0,
                    "theta",
                    GROUP_RW,
                    0,
                )
            else:  # South pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetR"],
                    0,
                    "theta+180",
                    GROUP_RW,
                    0,
                )
        else:  # Parallel magnetization
            if label[-10] == "N":  # North pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetR"],
                    0,
                    theta * 180 / pi,
                    GROUP_RW,
                    0,
                )
            else:  # South pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetR"],
                    0,
                    theta * 180 / pi + 180,
                    GROUP_RW,
                    0,
                )

    else:  # magnet on the stator
        if "Radial" in label:  # Radial Magnetization
            if label[-10] == "N":  # North pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetS"],
                    0,
                    "theta",
                    GROUP_SW,
                    0,
                )
            else:  # South pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetS"],
                    0,
                    "theta+180",
                    GROUP_SW,
                    0,
                )

        else:  # Parallel magnetization
            if label[-10] == "N":  # North pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetS"],
                    0,
                    theta * 180 / pi,
                    GROUP_SW,
                    0,
                )
            else:  # South pole magnet
                femm.mi_setblockprop(
                    prop,
                    FEMM_dict["automesh"],
                    FEMM_dict["meshsize_magnetS"],
                    0,
                    theta * 180 / pi + 180,
                    GROUP_SW,
                    0,
                )

    femm.mi_clearselected()
