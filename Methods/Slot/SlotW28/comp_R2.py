# -*- coding: utf-8 -*-
"""@package

@date Created on Wed Jul 13 11:22:53 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import arcsin, exp, pi, sqrt


def comp_R2(self):
    """Compute the radius to get a constant tooth

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    R2: float
        Top radius [m]

    """

    Rbo = self.get_Rbo()

    # alpha is the angle to rotate P0 so ||P1,P8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))
    slot_pitch = 2 * pi / self.Zs

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z8 = Z0 * exp(-1j * alpha)

    if self.is_outwards():
        Z7 = Z8 + self.H0
        # Rotation to get the tooth on X axis
        Z7 = Z7 * exp(1j * slot_pitch / 2)
        Z8 = Z8 * exp(1j * slot_pitch / 2)
        Z6 = (
            Z7.real
            + sqrt(-4 * ((Z7.imag - (self.W3 / 2.0 + self.R1)) ** 2 - self.R1 ** 2)) / 2
            + 1j * self.W3 / 2.0
        )
        Z5 = Z6 + self.H3
    else:  # inward slot
        Z7 = Z8 - self.H0
        # Rotation to get the tooth on X axis
        Z7 = Z7 * exp(1j * slot_pitch / 2)
        Z8 = Z8 * exp(1j * slot_pitch / 2)
        Z6 = (
            Z7.real
            - sqrt(-4 * ((Z7.imag - (self.W3 / 2.0 + self.R1)) ** 2 - self.R1 ** 2)) / 2
            + 1j * self.W3 / 2.0
        )
        Z5 = Z6 - self.H3
    Z5 = Z5 * exp(-1j * slot_pitch / 2)

    return -Z5.imag
