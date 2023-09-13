from numpy import arcsin, exp, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))
    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(-1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Zc1 = Z2.real + sqrt(self.R1**2 - (self.W0 / 2.0) ** 2)
        Z3 = Zc1 - self.R1 * 1j
        Zc2 = Zc1 + self.H1
        Z4 = Zc2 - 1j * self.R2
        Zbot = Zc2 + self.R2
    else:  # inward slot
        Z2 = Z1 - self.H0
        Zc1 = Z2.real - sqrt(self.R1**2 - (self.W0 / 2.0) ** 2)
        Z3 = Zc1 - self.R1 * 1j
        Zc2 = Zc1 - self.H1
        Z4 = Zc2 - 1j * self.R2
        Zbot = Zc2 - self.R2

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
    point_dict["Zc1"] = Zc1
    point_dict["Zc2"] = Zc2
    point_dict["Zbot"] = Zbot
    return point_dict
