from numpy import arcsin, exp, pi


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    # We compute the point on the tooth, then rotation to get the slot
    # Zxt is the equivalent of point Zx in tooth ref

    # alpha_0 is the angle to rotate Z0 so ||Z1,Z8|| = W4
    alpha_0 = float(arcsin(self.W4 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1t = Z0 * exp(1j * alpha_0)

    if self.is_outwards():
        Z2t = Z1t + self.H1
        # alpha_1 is the angle of Z3t so ||Z3t,Z6t|| = W3
        alpha_1 = float(arcsin(self.W3 / (2 * abs(Z2t))))
        Z3t = abs(Z2t) * exp(1j * alpha_1)
        Z4t = Z3t + self.H2
    else:  # inward slot
        Z2t = Z1t - self.H1
        # alpha_1 is the angle of Z3t so ||Z3t,Z6t|| = W3
        alpha_1 = float(arcsin(self.W3 / (2 * abs(Z2t))))
        Z3t = abs(Z2t) * exp(1j * alpha_1)
        Z4t = Z3t - self.H2

    point_dict = dict()
    # Rotation to get the slot
    hssp = pi / self.Zs
    point_dict["Z1"] = Z1t * exp(-1j * hssp)
    point_dict["Z2"] = Z2t * exp(-1j * hssp)
    point_dict["Z3"] = Z3t * exp(-1j * hssp)
    point_dict["Z4"] = Z4t * exp(-1j * hssp)
    # symetry
    point_dict["Z5"] = point_dict["Z4"].conjugate()
    point_dict["Z6"] = point_dict["Z3"].conjugate()
    point_dict["Z7"] = point_dict["Z2"].conjugate()
    point_dict["Z8"] = point_dict["Z1"].conjugate()

    return point_dict
