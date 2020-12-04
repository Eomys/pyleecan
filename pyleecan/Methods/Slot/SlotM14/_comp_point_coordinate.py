from numpy import arcsin, exp, angle
from ....Functions.Geometry.comp_flower_arc import comp_flower_arc


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotM14
        A SlotM14 object

    Returns
    -------
    point_list: list
        A list of the slot coordinates

    """

    Rbo = self.get_Rbo()

    Z1 = Rbo * exp(-1j * self.W0 / 2)
    Z4 = Rbo * exp(+1j * self.W0 / 2)

    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(-1j * self.W0 / 2)
        Z3 = (Rbo + self.H0) * exp(+1j * self.W0 / 2)
        ZM1 = (Rbo + self.H0) * exp(-1j * self.Wmag / 2)
        ZM4 = (Rbo + self.H0) * exp(+1j * self.Wmag / 2)
        (alpha_lim, ZM3, ZM2) = comp_flower_arc(
            abs(angle(ZM1) - angle(ZM4)), self.Rtopm, abs(ZM1) - self.Hmag
        )
        ZM0 = Rbo + self.H0 - self.Hmag
    else:
        Z2 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)
        Z3 = (Rbo - self.H0) * exp(+1j * self.W0 / 2)
        ZM1 = (Rbo - self.H0) * exp(-1j * self.Wmag / 2)
        ZM4 = (Rbo - self.H0) * exp(+1j * self.Wmag / 2)
        (alpha_lim, ZM3, ZM2) = comp_flower_arc(
            abs(angle(ZM1) - angle(ZM4)), self.Rtopm, abs(ZM1) + self.Hmag
        )
        ZM0 = Rbo - self.H0 + self.Hmag

    return [Z1, Z2, Z3, Z4, ZM1, ZM2, ZM3, ZM4, ZM0]
