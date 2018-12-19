# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Jan 08 11:26:43 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import cos


def comp_W5(self):
    """Compute the W5 width of the slot (cf schematics)

    Parameters
    ----------
    self : HoleM50
        a HoleM50 object

    Returns
    -------
    W5: float
        Cf schematics [m]

    """

    alpha = self.comp_alpha()

    # Distance fromZ8 to Z9
    L89 = (self.W0 / 2 - self.W1 / 2) / cos(alpha)

    return L89 - self.W4 - self.W2
