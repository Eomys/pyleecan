from numpy import pi, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM18
        A SlotM18 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    sp = 2 * pi / self.Zs
    Z1 = Rbo * exp(-1j * sp / 2)
    ZM1 = Rbo * exp(-1j * sp / 2)

    if self.is_outwards():
        ZM2 = (Rbo - self.H0) * exp(-1j * sp / 2)
    else:  # inward slot
        ZM2 = (Rbo + self.H0) * exp(-1j * sp / 2)

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["ZM1"] = ZM1
    point_dict["ZM2"] = ZM2
    # symetry
    point_dict["Z2"] = Z1.conjugate()
    point_dict["ZM3"] = ZM2.conjugate()
    point_dict["ZM4"] = ZM1.conjugate()

    return point_dict
