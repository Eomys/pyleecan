# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.LamH import LamH


def comp_surfaces(self):
    """Compute the Lamination surfaces

    Parameters
    ----------
    self : LamHoleNS
        A LamHoleNS object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionary (Slam, Svent, Smag, Shole) [m**2]

    """

    S_dict = LamH.comp_surfaces(self)

    # Magnets are counted twice (Zh = 2*p for both north and south)
    S_dict["Smag"] = S_dict["Smag"] / 2
    S_dict["Shole"] = S_dict["Shole"] / 2
    S_dict["Slam"] += S_dict["Shole"]
    S_dict["Steeth"] += S_dict["Shole"]

    return S_dict
