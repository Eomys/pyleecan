# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot.comp_surface
Slot Computation of surface (Numerical) method
@date Created on Thu Dec 06 10:22:33 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the Hole total surface (by numerical computation).

    Parameters
    ----------
    self : Hole
        A Hole object

    Returns
    -------
    S : float
        Slot total surface [m**2]

    """

    surf_list = self.build_geometry()
    S = 0
    for surf in surf_list:
        S += surf.comp_surface()

    return S
