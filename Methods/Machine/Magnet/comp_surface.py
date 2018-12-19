# -*- coding: utf-8 -*-
"""@package Methods.Machine.Magnet.comp_surface
Magnet Computation of surface (Numerical) method
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the Magnet total surface (by numerical computation).

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    S: float
        Magnet total surface [m**2]

    """

    surf_list = self.build_geometry()
    S = 0
    for surf in surf_list:
        S += surf.comp_surface()
    return S
