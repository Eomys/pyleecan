from numpy import arcsin, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening()

    Z1 = Rbo * exp(-1j * alpha / 2)
    Z2 = Rbo * exp(1j * alpha / 2)
    if self.is_outwards():
        ZM = (Z1 + Z2) / 2 + self.H0
    else:
        ZM = (Z1 + Z2) / 2 - self.H0

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["ZM"] = ZM
    return point_dict
