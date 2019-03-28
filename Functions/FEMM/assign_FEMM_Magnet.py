# -*- coding: utf-8 -*-
"""@package assign_FEMM_Magnet
@date Created on août 01 17:19 2018
@author franco_i
"""
import femm
from numpy import angle, pi

from pyleecan.Functions.FEMM import GROUP_RW, GROUP_SW


def assign_FEMM_Magnet(surf, prop, mesh_dict):
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
    theta = angle(point_ref)  # For parallele magnetization

    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    if "Radial" in label and label[-10] == "N":  # Radial magnetization
        mag = "theta"  # North pole magnet
    elif "Radial" in label:
        mag = "theta + 180"  # South pole magnet
    elif "Parallel" in label and label[-10] == "N":
        mag = theta * 180 / pi  # North pole magnet
    elif "Parallel" in label:
        mag = theta * 180 / pi + 180  # South pole magnet

    # Set property
    femm.mi_setblockprop(
        prop,
        mesh_dict["automesh"],
        mesh_dict["meshsize"],
        0,
        mag,
        mesh_dict["group"],
        0,
    )
    femm.mi_clearselected()
