# -*- coding: utf-8 -*-
"""@package Functions.comp_volume_magnets
Computation the HoleM57 magnet volume methode
@date Created on Thu Jan 07 17:15:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_volume_magnets(self):
    """Compute the volume of the hole magnets

    Parameters
    ----------
    self : HoleM57
        A HoleM57 object

    Returns
    -------
    Vmag: float
        Volume of the 2 Magnets [m**3]

    """

    V = 0
    if self.magnet_0:
        V += self.H2 * self.W4 * self.magnet_0.Lmag
    if self.magnet_1:
        V += self.H2 * self.W4 * self.magnet_1.Lmag
    return V
