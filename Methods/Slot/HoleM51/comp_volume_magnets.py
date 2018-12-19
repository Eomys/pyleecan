# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Dec 06 11:26:13 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_volume_magnets(self):
    """Compute the volume of the hole magnets (some of them may be missing)

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    Vmag: float
        Volume of the magnets [m**3]

    """

    V = 0
    if self.magnet_0:
        V += self.W7 * self.H2 * self.magnet_0.Lmag
    if self.magnet_1:
        V += self.W3 * self.H2 * self.magnet_1.Lmag
    if self.magnet_2:
        V += self.W5 * self.H2 * self.magnet_2.Lmag
    return V
