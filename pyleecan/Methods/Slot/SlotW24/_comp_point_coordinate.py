from numpy import exp


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

    (alpha_0, alpha_2) = self.comp_alphas()

    # comp point coordinate (in complex)
    Z1 = Rbo * exp(-1j * alpha_0 / 2.0)

    if self.is_outwards():
        Z2 = (Rbo + self.H2) * exp(-1j * alpha_2 / 2.0)
    else:  # inward slot
        Z2 = (Rbo - self.H2) * exp(-1j * alpha_2 / 2.0)

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z2.conjugate()
    point_dict["Z4"] = Z1.conjugate()
    return point_dict
