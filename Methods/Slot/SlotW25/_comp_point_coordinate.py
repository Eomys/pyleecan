from numpy import arcsin, exp, pi


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    point_list: list
        A list of PointS

    """
    Rbo = self.get_Rbo()

    # We compute the point on the tooth, then rotation to get the slot

    # alpha_0 is the angle to rotate Z0 so ||Z1,Z8|| = W4
    alpha_0 = float(arcsin(self.W4 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha_0)

    if self.is_outwards():
        Z2 = Z1 + self.H1
        # alpha_1 is the angle of Z3 so ||Z3,Z6|| = W3
        alpha_1 = float(arcsin(self.W3 / (2 * abs(Z2))))
        Z3 = abs(Z2) * exp(1j * alpha_1)
        Z4 = Z3 + self.H2
    else:  # inward slot
        Z2 = Z1 - self.H1
        # alpha_1 is the angle of Z3 so ||Z3,Z6|| = W3
        alpha_1 = float(arcsin(self.W3 / (2 * abs(Z2))))
        Z3 = abs(Z2) * exp(1j * alpha_1)
        Z4 = Z3 - self.H2

    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()

    # Creation of points
    # Rotation to get the slot
    hssp = pi / self.Zs
    # Left part
    Z1 = Z1 * exp(-1j * hssp)
    Z2 = Z2 * exp(-1j * hssp)
    Z3 = Z3 * exp(-1j * hssp)
    Z4 = Z4 * exp(-1j * hssp)
    # Right part
    Z5 = Z5 * exp(1j * hssp)
    Z6 = Z6 * exp(1j * hssp)
    Z7 = Z7 * exp(1j * hssp)
    Z8 = Z8 * exp(1j * hssp)

    return [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]
