from numpy import arcsin, exp, cos


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM13
        A SlotM13 object

    Returns
    -------
    point_list: list
        A list of the slot coordinates

    """

    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    Z1 = Rbo * exp(-1j * alpha)

    alpha_lim = 2 * arcsin(self.Wmag * 0.5 / self.Rtopm)  # Angle of the top arc
    H_top_arc = self.Rtopm * (1 - cos(alpha_lim / 2))  # Heiht of the top arc
    if self.is_outwards():
        Z2 = Z1 + self.H0
    else:  # inward slot
        Z2 = Z1 - self.H0
    ZM1 = Z2.real - 1j * self.Wmag / 2
    if self.is_outwards():
        ZM0 = Z2.real - self.Hmag
        ZM2 = ZM1 - self.Hmag + H_top_arc
    else:  # inward slot
        ZM0 = Z2.real + self.Hmag
        ZM2 = ZM1 + self.Hmag - H_top_arc

    # symetry
    Z3 = Z2.conjugate()
    Z4 = Z1.conjugate()
    ZM3 = ZM2.conjugate()
    ZM4 = ZM1.conjugate()

    return [Z1, Z2, Z3, Z4, ZM1, ZM2, ZM3, ZM4, ZM0]
