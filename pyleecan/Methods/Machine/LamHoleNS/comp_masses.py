# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.LamH import LamH


def comp_masses(self):
    """Compute the Lamination masses

    Parameters
    ----------
    self : LamHoleNS
        A LamHoleNS object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionary (Mtot, Mlam, Mmag) [kg]

    """

    M_dict = LamH.comp_masses(self)

    # Magnets are counted twice (Zh = 2*p for both north and south)
    M_dict["Mmag"] = M_dict["Mmag"] / 2
    M_dict["Mtot"] -= M_dict["Mmag"]

    return M_dict
