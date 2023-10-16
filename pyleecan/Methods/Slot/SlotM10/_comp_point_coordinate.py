from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    point_dict = dict()
    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    Z1 = Rbo * exp(-1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
    else:  # inward slot
        Z2 = Z1 - self.H0
    ZM1 = Z2.real - 1j * self.W1 / 2
    if self.is_outwards():
        ZM2 = ZM1 - self.H1
    else:  # inward slot
        ZM2 = ZM1 + self.H1

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
