# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.Lamination import Lamination


def comp_masses(self):
    """Compute the Lamination masses

    Parameters
    ----------
    self : LamH
        A LamH object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionary (Mtot, Mlam, Mmag) [kg]

    """

    M_dict = Lamination.comp_masses(self)

    Mmag = 0
    for hole in self.get_hole_list():
        if hole.has_magnet():
            Mmag += hole.Zh * hole.comp_mass_magnets()

    M_dict["Mmag"] = Mmag
    M_dict["Mtot"] += Mmag

    return M_dict
