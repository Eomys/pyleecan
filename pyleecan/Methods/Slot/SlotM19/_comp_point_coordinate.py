from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM19
        A SlotM19 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z4|| = W1
    alpha = float(arcsin(self.W1 / (2 * Rbo)))

    Z1 = Rbo * exp(-1j * alpha)

    if self.is_outwards():
        Zmid = Rbo + self.H0

    else:  # inward slot
        Zmid = Rbo - self.H0

    Z2 = Zmid - 1j * (self.W0 / 2)

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Zmid"] = Zmid
    # symetry
    point_dict["Z3"] = Z2.conjugate()
    point_dict["Z4"] = Z1.conjugate()

    return point_dict
