# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamHole.comp_masses
Lamination with Buried Magnets computation of all masses method
@date Created on Mon Jan 12 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi
from pyleecan.Classes.Lamination import Lamination


def comp_masses(self):
    """Compute the Lamination masses

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionnary (Mtot, Mlam, Mmag) [kg]

    """

    M_dict = Lamination.comp_masses(self)

    Mmag = 0
    for hole in self.hole:
        if hole.has_magnet():
            Mmag += hole.Zh * hole.comp_mass_magnets()

    M_dict["Mmag"] = Mmag
    M_dict["Mtot"] += Mmag

    return M_dict
