from numpy import exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    point_list: list
        A list of Points

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha0 = self.comp_angle_opening() / 2
    alpha1 = self.comp_angle_bottom() / 2

    # comp point coordinate (in complex)
    Z_ = Rbo * exp(1j * 0)
    Z0 = Z_ * exp(1j * alpha0)

    if self.is_outwards():
        Z1 = (Rbo + self.H0) * exp(1j * alpha1)
    else:  # inward slot
        Z1 = (Rbo - self.H0) * exp(1j * alpha1)

    # symetry
    Z2 = Z1.conjugate()
    Z3 = Z0.conjugate()

    return [Z3, Z2, Z1, Z0]
