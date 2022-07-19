# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.Lamination import Lamination


def comp_surfaces(self):
    """Compute the Lamination surfaces

    Parameters
    ----------
    self : LamH
        A LamH object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionary (Slam, Svent, Smag, Shole) [m**2]

    """

    S_dict = Lamination.comp_surfaces(self)

    # hole surface
    Shole = 0
    Smag = 0
    for hole in self.get_hole_list():
        Shole += hole.Zh * hole.comp_surface()
        if hole.has_magnet():
            Smag += hole.Zh * hole.comp_surface_magnets()

    Ryoke = self.get_Ryoke()
    Hyoke = self.comp_height_yoke()
    if self.is_internal:
        S_dict["Syoke"] = pi * ((Ryoke + Hyoke) ** 2 - Ryoke ** 2) - S_dict["Svent"]
    else:
        S_dict["Syoke"] = pi * (Ryoke ** 2 - (Ryoke - Hyoke) ** 2) - S_dict["Svent"]

    S_dict["Smag"] = Smag
    S_dict["Shole"] = Shole
    S_dict["Slam"] -= Shole  # the magnet surface in included in the hole one
    S_dict["Steeth"] = S_dict["Slam"] - S_dict["Syoke"]

    return S_dict
