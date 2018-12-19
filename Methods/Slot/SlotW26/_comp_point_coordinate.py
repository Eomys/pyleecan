"""Created on June 18th 2018

@author: franco_i
"""
from numpy import arcsin, exp, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    point_list: list
        A list of 11 Points and rot_sign

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))
    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        ZC1 = Z2.real + sqrt(self.R1 ** 2 - (self.W0 / 2.0) ** 2)
        Z3 = ZC1 + self.R1 * 1j
        Z4 = Z3 + self.H1
        Ztan2 = Z4 + self.R1 * (1 - 1j)
        rot_sign = -1  # Rotation direction for Arc1
    else:  # inward slot
        Z2 = Z1 - self.H0
        ZC1 = Z2.real - sqrt(self.R1 ** 2 - (self.W0 / 2.0) ** 2)
        Z3 = ZC1 + self.R1 * 1j
        Z4 = Z3 - self.H1
        Ztan2 = Z4 - self.R1 * (1 + 1j)
        rot_sign = 1  # Rotation direction for Arc1

    # symmetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Ztan1 = (Z2 + Z7) / 2.0
    Zmid = (Ztan1 + Ztan2) / 2.0
    Zrad1 = Zmid - 1j * self.R1
    Zrad2 = Zmid + 1j * self.R1

    return [Z2, Z3, Z4, Z5, Z6, Z7, Ztan1, Ztan2, Zmid, Zrad1, Zrad2, rot_sign]
