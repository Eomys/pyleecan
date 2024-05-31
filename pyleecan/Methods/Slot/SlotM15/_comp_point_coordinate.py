from numpy import arcsin, exp, cos


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM15
        A SlotM15 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    Z1 = Rbo * exp(-1j * self.W0 / 2)

    alpha_lim = 2 * arcsin(self.W1 * 0.5 / self.Rtopm)  # Angle of the top arc
    H_top_arc = self.Rtopm * (1 - cos(alpha_lim / 2))  # Heiht of the top arc
    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(-1j * self.W0 / 2)
    else:  # inward slot
        Z2 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)

    alpha_M = float(arcsin(self.W1 / (2 * abs(Z2))))
    ZM1 = abs(Z2) * exp(-1j * alpha_M)
    if self.is_outwards():
        ZM0 = abs(Z2) - self.H1
        Zc = ZM0 + self.Rtopm
    else:  # inward slot
        ZM0 = abs(Z2) + self.H1
        Zc = ZM0 - self.Rtopm

    sign = -1 if self.is_outwards() else 1
    x = abs(Z2) - sign * (
        -self.H1 + self.Rtopm - (self.Rtopm**2 - self.W1**2 / 4) ** 0.5
    )
    ZM2 = x - 1j * self.W1 / 2

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["ZM1"] = ZM1
    point_dict["ZM2"] = ZM2
    point_dict["ZM0"] = ZM0
    point_dict["Zc"] = Zc
    # symetry
    point_dict["Z3"] = Z2.conjugate()
    point_dict["Z4"] = Z1.conjugate()
    point_dict["ZM3"] = ZM2.conjugate()
    point_dict["ZM4"] = ZM1.conjugate()

    return point_dict
