from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object

    Returns
    -------
    point_list: list
        A list of the slot coordinates

    """

    Rbo = self.get_Rbo()

    Z1 = Rbo * exp(-1j * self.W0 / 2)

    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(-1j * self.W0 / 2)
        ZM1 = (Rbo + self.H0) * exp(-1j * self.Wmag / 2)
        ZM2 = (Rbo + self.H0 - self.Hmag) * exp(-1j * self.Wmag / 2)
    else:  # inward slot
        Z2 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)
        ZM1 = (Rbo - self.H0) * exp(1j * self.Wmag / 2)
        ZM2 = (Rbo - self.H0 + self.Hmag) * exp(-1j * self.Wmag / 2)

    # symetry
    Z3 = Z2.conjugate()
    Z4 = Z1.conjugate()
    ZM3 = ZM2.conjugate()
    ZM4 = ZM1.conjugate()

    return [Z1, Z2, Z3, Z4, ZM1, ZM2, ZM3, ZM4]
