from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    H1 = self.get_H1()

    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(-1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Z3 = Z2.real + H1 - 1j * self.W1 / 2.0
        Z4 = Z2.real + H1 - 1j * self.W0 / 2.0
        Z5 = Z2.real + H1 + self.H2 - 1j * self.W2 / 2.0
    else:  # inward slot
        Z2 = Z1 - self.H0
        Z3 = Z2.real - H1 - 1j * self.W1 / 2.0
        Z4 = Z2.real - H1 - 1j * self.W0 / 2.0
        Z5 = Z2.real - H1 - self.H2 - 1j * self.W2 / 2.0

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z5.conjugate()
    point_dict["Z7"] = Z4.conjugate()
    point_dict["Z8"] = Z3.conjugate()
    point_dict["Z9"] = Z2.conjugate()
    point_dict["Z10"] = Z1.conjugate()
    return point_dict
