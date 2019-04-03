# -*- coding: utf-8 -*-
"""@package assign_FEMM_Machine_part
@date Created on août 09 14:12 2018
@author franco_i
"""
import femm
from numpy import angle, pi


def assign_FEMM_surface(surf, prop, mesh_dict, rotor, stator):
    """Assign the property given in parameter to surface having the label given

    Parameters
    ----------
    surf : Surface
        the surface to assign
    prop : str
        The property to assign in FEMM
    mesh_dict : dict
        Dictionnary containing the mesh parameters corresponding to the surface
    rotor : Lamination
        The rotor of the machine
    stator : Lamination
        The stator of the machine

    Returns
    -------
    None

    """
    label = surf.label
    Clabel = 0  # By default no circuit
    Ntcoil = 0  # By default no circuit
    mag = 0  # By default no magnetization

    # point_ref is None => don't assign the surface
    if surf.point_ref is not None:
        # Select the surface
        point_ref = surf.point_ref
        femm.mi_addblocklabel(point_ref.real, point_ref.imag)
        femm.mi_selectlabel(point_ref.real, point_ref.imag)

        # Get circuit or magnetization properties if needed
        if "Wind" in label:  # If the surface is a winding
            if "Rotor" in label:  # Winding on the rotor
                Clabel = "Circr" + prop[2]
                Ntcoil = rotor.winding.Ntcoil
            else:  # winding on the stator
                Clabel = "Circs" + prop[2]
                Ntcoil = stator.winding.Ntcoil
            if prop[-1] == "-":  # Adapt Ntcoil sign if needed
                Ntcoil *= -1
        elif "Magnet" in label:  # Magnet
            if "Radial" in label and label[-10] == "N":  # Radial magnetization
                mag = "theta"  # North pole magnet
            elif "Radial" in label:
                mag = "theta + 180"  # South pole magnet
            elif "Parallel" in label and label[-10] == "N":
                mag = angle(point_ref) * 180 / pi  # North pole magnet
            elif "Parallel" in label:
                mag = angle(point_ref) * 180 / pi + 180  # South pole magnet

        # Set the surface property
        femm.mi_setblockprop(
            prop,
            mesh_dict["automesh"],
            mesh_dict["meshsize"],
            Clabel,
            mag,
            mesh_dict["group"],
            Ntcoil,
        )
        femm.mi_clearselected()
