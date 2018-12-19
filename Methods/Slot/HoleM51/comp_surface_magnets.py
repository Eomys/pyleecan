# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Dec 06 11:26:13 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_surface_magnets(self):
    """Compute the surface of the hole magnets (some of them may be missing)

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    Smag: float
        Surface of the magnets [m**2]

    """

    S = 0
    if self.magnet_0:
        S += self.W7 * self.H2
    if self.magnet_1:
        S += self.W3 * self.H2
    if self.magnet_2:
        S += self.W5 * self.H2
    return S
