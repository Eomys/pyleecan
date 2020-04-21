from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object

    Returns
    -------
    point_list: list
        A list of 7 Points

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z1 = Rbo * exp(1j * alpha)

    if self.is_outwards():
        Z3 = Z1 + self.H0 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 + self.H1 + (self.W2 - self.W1) / 2.0 * 1j
        Z5 = Z4 + self.H2 + (self.W3 - self.W2) / 2.0 * 1j
    else:  # inward slot
        Z3 = Z1 - self.H0 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 - self.H1 + (self.W2 - self.W1) / 2.0 * 1j
        Z5 = Z4 - self.H2 + (self.W3 - self.W2) / 2.0 * 1j

    # symmetry
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    return [Z1, Z3, Z4, Z5, Z6, Z7, Z8]
