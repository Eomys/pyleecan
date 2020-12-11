from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    point_list: list
        A list of 7 Points and rot_sign

    """
    Rbo = self.get_Rbo()

    H1 = self.get_H1()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Z3 = Z2 + H1 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 + (self.H2 - self.R1) + (self.W2 - self.W1) / 2.0 * 1j
        Z5 = Z4 + self.R1 - self.R1 * 1j
        rot_sign = 1  # Rotation direction for Arc1
    else:  # inward slot
        Z2 = Z1 - self.H0
        Z3 = Z2 - H1 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 - (self.H2 - self.R1) + (self.W2 - self.W1) / 2.0 * 1j
        Z5 = Z4 - self.R1 - self.R1 * 1j
        rot_sign = -1  # Rotation direction for Arc1

    # symetry
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    Z9 = Z2.conjugate()
    Z10 = Z1.conjugate()
    return [Z10, Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1, rot_sign]
