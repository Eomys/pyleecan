from numpy import arcsin, exp
from ....Functions.Geometry.circle_from_3_points import circle_from_3_points


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

    if self.is_H0_bore is None:
        self.is_H0_bore = True  # Set default value
    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening()

    Z1 = Rbo * exp(-1j * alpha / 2)
    Z2 = Rbo * exp(1j * alpha / 2)
    if self.is_H0_bore:
        if self.is_outwards():
            ZM = Rbo + self.H0
        else:
            ZM = Rbo - self.H0
        R0, _ = circle_from_3_points(Z1, Z2, ZM)
        ZH = Rbo
    else:
        if self.is_outwards():
            ZM = (Z1 + Z2) / 2 + self.H0
        else:
            ZM = (Z1 + Z2) / 2 - self.H0
        ZH = (Z1 + Z2) / 2
        R0 = None

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["ZM"] = ZM
    point_dict["ZH"] = ZH  # For H0 schematics
    # Store R0 for _comp_R0
    if R0 is not None:
        point_dict["R0"] = R0
    return point_dict
