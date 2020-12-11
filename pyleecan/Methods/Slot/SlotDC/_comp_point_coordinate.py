from numpy import arcsin, exp, pi, sqrt

from ....Functions.Geometry.inter_line_circle import inter_line_circle


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotDC
        A SlotDC object

    Returns
    -------
    point_list: list
        A list of 15 Point

    """

    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z12|| = W1
    # alpha = self.comp_angle_opening()
    alpha = 2 * float(arcsin(self.W1 / (2 * Rbo)))

    # Compute all points coordinates
    Z0 = Rbo * exp(1j * 0)
    Z1 = Rbo * exp(-1j * alpha / 2)
    if self.is_outwards():
        sign = +1
    else:
        sign = -1

    Zc1 = Z1.real + sign * self.H1
    Zc2 = Zc1 + sign * self.H2
    Zc3 = Zc2 + sign * self.H3

    Z2 = Zc1 - sign * sqrt((self.D1 / 2) ** 2 - (self.W1 / 2) ** 2) - 1j * (self.W1 / 2)
    Z3 = Zc1 + sign * sqrt((self.D1 / 2) ** 2 - (self.W2 / 2) ** 2) - 1j * (self.W2 / 2)
    Z4 = Zc2 - sign * sqrt((self.D2 / 2) ** 2 - (self.W2 / 2) ** 2) - 1j * (self.W2 / 2)

    Z5 = Zc2.real - 1j * self.D2 / 2
    Z6 = Zc3.real - 1j * self.R3

    # Symmetries
    Z7 = Z6.conjugate()
    Z8 = Z5.conjugate()
    Z9 = Z4.conjugate()
    Z10 = Z3.conjugate()
    Z11 = Z2.conjugate()
    Z12 = Z1.conjugate()

    return [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Zc1, Zc2, Zc3]
