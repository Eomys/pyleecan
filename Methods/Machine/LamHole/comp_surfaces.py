# -*- coding: utf-8 -*-

from numpy import pi
from pyleecan.Classes.Lamination import Lamination


def comp_surfaces(self):
    """Compute the Lamination surfaces

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionnary (Slam, Svent, Smag, Shole) [m**2]

    """

    S_dict = Lamination.comp_surfaces(self)

    # hole surface
    Shole = 0
    Smag = 0
    for hole in self.hole:
        Shole += hole.Zh * hole.comp_surface()
        if hole.has_magnet():
            Smag += hole.Zh * hole.comp_surface_magnets()
    S_dict["Smag"] = Smag
    S_dict["Shole"] = Shole
    S_dict["Slam"] -= Shole  # the magnet surface in included in the hole one

    return S_dict
