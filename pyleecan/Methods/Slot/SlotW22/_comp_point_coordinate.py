from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    # comp point coordinate (in complex)
    Z1 = Rbo * exp(-1j * self.W0 / 2)
    if self.is_outwards():
        R1 = Rbo + self.H0
        R2 = Rbo + self.H0 + self.H2
    else:  # inward slot
        R1 = Rbo - self.H0
        R2 = Rbo - self.H0 - self.H2
    Z2 = R1 * exp(-1j * self.W0 / 2.0)
    Z3 = R1 * exp(-1j * self.W2 / 2.0)
    Z4 = R2 * exp(-1j * self.W2 / 2.0)

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
