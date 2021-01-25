from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = 2*R2
    alpha = float(arcsin(self.R2 / Rbo))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(-1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Z3 = Z2 + self.R1 * 2
        Z4 = Z3 + self.H1
        Zc1 = Z2 + self.R1
        Zi2 = Z4.real + self.R2
    else:  # inward slot
        Z2 = Z1 - self.H0
        Z3 = Z2 - self.R1 * 2
        Z4 = Z3 - self.H1
        Zc1 = Z2 - self.R1
        Zi2 = Z4.real - self.R2
    Zc2 = Z4.real

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Zc1"] = Zc1
    point_dict["Zc2"] = Zc2
    point_dict["Z5"] = Z4.conjugate()
    point_dict["Z6"] = Z3.conjugate()
    point_dict["Z7"] = Z2.conjugate()
    point_dict["Z8"] = Z1.conjugate()
    point_dict["Zc3"] = Zc1.conjugate()
    point_dict["Zi1"] = Zc1 - 1j * self.R1
    point_dict["Zi2"] = Zi2
    point_dict["Zi3"] = point_dict["Zc3"] + 1j * self.R1

    return point_dict
