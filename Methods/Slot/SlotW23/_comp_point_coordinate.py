"""
Created on June 18th 2018

@author: franco_i
"""

from numpy import arcsin, exp, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    point_list: list
        A list of Points

    """
    Rbo = self.get_Rbo()
    if self.is_cstt_tooth:
        # Compute W1 and W2 to match W3 tooth constraint
        self._comp_W()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)

    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(1j * alpha)
        Z3 = Z2.real + self.H1 + 1j * self.W1 / 2

        H2 = sqrt(self.H2 ** 2 - ((self.W2 - self.W1) / 2.0) ** 2)
        Z4 = Z3.real + H2 + 1j * self.W2 / 2
    else:  # inward slot
        Z2 = (Rbo - self.H0) * exp(1j * alpha)
        Z3 = Z2.real - self.H1 + 1j * self.W1 / 2

        H2 = sqrt(self.H2 ** 2 - ((self.W2 - self.W1) / 2.0) ** 2)
        Z4 = Z3.real - H2 + 1j * self.W2 / 2

    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()
    return [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]
