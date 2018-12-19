# -*- coding: utf-8 -*-
"""@package Methods.Slot.HoleM51.comp_width
Compute the width of the Hole method
@date Created on Thu Dec 06 17:28:22 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import sin


def comp_width(self):
    """Compute the width of the Hole (cf schematics)

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    Whole: float
        Width of the Hole (cf schematics) [m]

    """

    Rbo = self.get_Rbo()
    return 2 * sin(self.W1 / 2) * (Rbo - self.H1)
