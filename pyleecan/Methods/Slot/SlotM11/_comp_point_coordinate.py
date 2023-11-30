from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    Z1 = Rbo * exp(-1j * self.W0 / 2)

    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(-1j * self.W0 / 2)
        ZM1 = (Rbo + self.H0) * exp(-1j * self.W1 / 2)
        ZM2 = (Rbo + self.H0 - self.H1) * exp(-1j * self.W1 / 2)
    else:  # inward slot
        Z2 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)
        ZM1 = (Rbo - self.H0) * exp(-1j * self.W1 / 2)
        ZM2 = (Rbo - self.H0 + self.H1) * exp(-1j * self.W1 / 2)

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["ZM1"] = ZM1
    point_dict["ZM2"] = ZM2
    # symetry

    point_dict["Z3"] = Z2.conjugate()
    point_dict["Z4"] = Z1.conjugate()
    point_dict["ZM3"] = ZM2.conjugate()
    point_dict["ZM4"] = ZM1.conjugate()

    return point_dict
