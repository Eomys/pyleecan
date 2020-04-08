# -*- coding: utf-8 -*-

from numpy import arcsin, exp


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    # alpha_0 is the angle to rotate P0 so ||P1,P8|| = W4
    alpha_0 = float(arcsin(self.W4 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha_0)

    if self.is_outwards():
        Z2 = Z1 + self.H1
        # alpha_1 is the angle of P3 so ||P3,P6|| = W3
        alpha_1 = float(arcsin(self.W3 / (2 * abs(Z2))))
        Z3 = abs(Z2) * exp(1j * alpha_1)
        Z4 = Z3 + self.H2
        return abs(Z4) - Rbo
    else:  # inward slot
        Z2 = Z1 - self.H1
        # alpha_1 is the angle of P3 so ||P3,P6|| = W3
        alpha_1 = float(arcsin(self.W3 / (2 * abs(Z2))))
        Z3 = abs(Z2) * exp(1j * alpha_1)
        Z4 = Z3 - self.H2
        return Rbo - abs(Z4)
