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
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    Z1 = Rbo * exp(-1j * self.W0 / 2)
    Z4 = Rbo * exp(+1j * self.W0 / 2)

    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(-1j * self.W0 / 2)
        Z3 = (Rbo + self.H0) * exp(+1j * self.W0 / 2)
        ZM1 = (Rbo + self.H0) * exp(-1j * self.W1 / 2)
        ZM4 = (Rbo + self.H0) * exp(+1j * self.W1 / 2)
        (alpha_lim, ZM3, ZM2) = comp_flower_arc(
            abs(angle(ZM1) - angle(ZM4)), self.Rtopm, abs(ZM1) - self.H1
        )
        ZM0 = Rbo + self.H0 - self.H1
        Zc = ZM0 + self.Rtopm
    else:
        Z2 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)
        Z3 = (Rbo - self.H0) * exp(+1j * self.W0 / 2)
        ZM1 = (Rbo - self.H0) * exp(-1j * self.W1 / 2)
        ZM4 = (Rbo - self.H0) * exp(+1j * self.W1 / 2)
        (alpha_lim, ZM3, ZM2) = comp_flower_arc(
            abs(angle(ZM1) - angle(ZM4)), self.Rtopm, abs(ZM1) + self.H1
        )
        ZM0 = Rbo - self.H0 + self.H1
        Zc = ZM0 - self.Rtopm

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["ZM1"] = ZM1
    point_dict["ZM2"] = ZM2
    point_dict["ZM0"] = ZM0
    point_dict["Zc"] = Zc
    # symetry
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["ZM3"] = ZM3
    point_dict["ZM4"] = ZM4

    return point_dict
