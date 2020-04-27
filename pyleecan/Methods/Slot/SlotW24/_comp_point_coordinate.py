from numpy import exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    point_list: list
        A list of 4 PointS

    """
    Rbo = self.get_Rbo()

    (alpha_0, alpha_2) = self.comp_alphas()

    # comp point coordinate (in complex)
    Z1 = Rbo * exp(1j * alpha_0 / 2.0)

    if self.is_outwards():
        Z2 = (Rbo + self.H2) * exp(1j * alpha_2 / 2.0)
    else:  # inward slot
        Z2 = (Rbo - self.H2) * exp(1j * alpha_2 / 2.0)

    # symetry
    Z3 = Z2.conjugate()
    Z4 = Z1.conjugate()
    return [Z4, Z3, Z2, Z1]
