"""Created on June 18th 2018

@author: franco_i
"""
from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

    Returns
    -------
    point_list: list
        A list of  Points

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z12|| = W0
    alpha = arcsin(self.W0 / (2 * Rbo))

    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Z3 = Z2 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 + self.H1
        Z5 = Z4 + (self.W2 - self.W1) * 1j / 2.0
        Z6 = Z5 + self.H2
    else:
        Z2 = Z1 - self.H0
        Z3 = Z2 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 - self.H1
        Z5 = Z4 + (self.W2 - self.W1) * 1j / 2.0
        Z6 = Z5 - self.H2

    # symetry
    Z7 = Z6.conjugate()
    Z8 = Z5.conjugate()
    Z9 = Z4.conjugate()
    Z10 = Z3.conjugate()
    Z11 = Z2.conjugate()
    Z12 = Z1.conjugate()

    return [Z12, Z11, Z10, Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]
