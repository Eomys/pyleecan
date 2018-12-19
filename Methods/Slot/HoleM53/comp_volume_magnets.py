# -*- coding: utf-8 -*-
"""@package Functions.comp_volume_magnets
Computation the HoleM53 magnet volume method
@date Created on Fri Mar 16 17:15:15 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_volume_magnets(self):
    """Compute the volume of the magnets (if any)

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    Vmag: float
        Volume of the Magnets [m**3]

    """

    V = 0
    if self.magnet_0:
        V += self.H2 * self.W3 * self.magnet_0.Lmag
    if self.magnet_1:
        V += self.H2 * self.W3 * self.magnet_1.Lmag
    return V
