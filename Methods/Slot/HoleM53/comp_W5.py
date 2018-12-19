# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Jan 08 11:26:43 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import exp, sin

from pyleecan.Functions.Geometry.inter_line_circle import inter_line_circle
from pyleecan.Methods.Slot.HoleM53 import Slot53InterError


def comp_W5(self):
    """Compute the W5 width of the hole (cf schematics)

    Parameters
    ----------
    self : HoleM53
        a HoleM53 object

    Returns
    -------
    W5: float
        Cf schematics [m]
    Raises
    --------
    Slot53InterError
        ERROR: Slot 53, Can't find Z11 coordinates

    """

    Rbo = self.get_Rbo()

    Z7 = Rbo - self.H0 - 1j * self.W1 / 2
    Z8 = Z7 + (self.H2 - self.H3) * sin(self.W4)
    Z10 = (self.W2 + self.W3) * exp(-1j * self.W4) + Z8

    # Z1 and Z11 are defined as intersection between line and circle
    Zlist = inter_line_circle(Z8, Z10, Rbo - self.H1)
    if len(Zlist) == 2 and Zlist[0].imag < 0 and Zlist[0].real > 0:
        Z11 = Zlist[0]
    elif len(Zlist) == 2 and Zlist[1].imag < 0 and Zlist[1].real > 0:
        Z11 = Zlist[1]
    else:
        raise Slot53InterError("ERROR: Slot 53, Can't find Z11 coordinates")

    return abs(Z11 - Z8) - self.W2 - self.W3
