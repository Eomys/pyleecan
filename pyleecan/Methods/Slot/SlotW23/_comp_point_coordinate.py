from numpy import arcsin, exp, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """

    if self.is_cstt_tooth:
        # Compute W1 and W2 to match W3 tooth constraint
        self._comp_W()

    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(-1j * alpha)

    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(-1j * alpha)
        Z3 = Z2.real + self.get_H1() - 1j * self.W1 / 2

        H2 = sqrt(self.H2**2 - ((self.W2 - self.W1) / 2.0) ** 2)
        Z4 = Z3.real + H2 - 1j * self.W2 / 2
    else:  # inward slot
        Z2 = (Rbo - self.H0) * exp(-1j * alpha)
        Z3 = Z2.real - self.get_H1() - 1j * self.W1 / 2

        H2 = sqrt(self.H2**2 - ((self.W2 - self.W1) / 2.0) ** 2)
        Z4 = Z3.real - H2 - 1j * self.W2 / 2

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z4.conjugate()
    point_dict["Z6"] = Z3.conjugate()
    point_dict["Z7"] = Z2.conjugate()
    point_dict["Z8"] = Z1.conjugate()
    return point_dict
