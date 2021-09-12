from numpy import arcsin, exp, pi


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    # alpha_0 is the angle to have a W3 tooth width on the bore
    alpha_0 = float(arcsin(self.W3 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1t = Z0 * exp(1j * alpha_0)

    if self.is_outwards():
        Z2t = Z1t + self.H2
    else:  # inward slot
        Z2t = Z1t - self.H2
    hsp = pi / self.Zs

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1t * exp(-1j * hsp)
    point_dict["Z2"] = Z2t * exp(-1j * hsp)
    point_dict["Z3"] = point_dict["Z2"].conjugate()
    point_dict["Z4"] = point_dict["Z1"].conjugate()
    return point_dict
