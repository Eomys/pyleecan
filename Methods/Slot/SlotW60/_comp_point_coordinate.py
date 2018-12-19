# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW60._comp_point_coordinate
SlotW60 _comp_point_coordinate method
@date Created on Tue Jul 31 12:05:43 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from numpy import pi, exp, cos, arcsin


def _comp_point_coordinate(self):
    """Compute the point coordinate needed to plot the Slot.

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    point_list: list
        A list of 11 complex

    """

    Rbo = self.get_Rbo()
    hsp = pi / self.Zs

    # Zxt => In the tooth ref (Ox as the sym axis of the tooth)
    Z1t = Rbo

    # Height of the arc (Z2t, Rbo-R1, Z2t.conjugate())
    alpha = arcsin(self.W1 / (2 * self.R1))
    Harc = float(self.R1 * (1 - cos(alpha)))

    Z2t = Rbo - Harc + 1j * self.W1 / 2
    Z3t = Z2t - self.H1
    Z4t = Z3t.real + 1j * self.W2 / 2
    Z5t = Z4t - self.H2
    Z6t = (Z5t.real / cos(hsp)) * exp(1j * hsp)

    # Go to the slot ref
    Z1 = Z1t * exp(-1j * hsp)
    Z2 = Z2t * exp(-1j * hsp)
    Z3 = Z3t * exp(-1j * hsp)
    Z4 = Z4t * exp(-1j * hsp)
    Z5 = Z5t * exp(-1j * hsp)
    Z6 = Z6t * exp(-1j * hsp)
    Z7 = Z5.conjugate()
    Z8 = Z4.conjugate()
    Z9 = Z3.conjugate()
    Z10 = Z2.conjugate()
    Z11 = Z1.conjugate()

    return [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11]
