# -*- coding: utf-8 -*-
"""@package Functions.comp_surface_magnets
Computation the HoleM57 magnet surface methode
@date Created on Thu Jan 07 17:15:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_surface_magnets(self):
    """Compute the surface of the hole magnets

    Parameters
    ----------
    self : HoleM57
        A HoleM57 object

    Returns
    -------
    Smag: float
        Surface of the 2 Magnets [m**2]

    """

    S = 0
    if self.magnet_0:
        S += self.H2 * self.W4
    if self.magnet_1:
        S += self.H2 * self.W4
    return S
