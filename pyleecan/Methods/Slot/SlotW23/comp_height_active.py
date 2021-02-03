# -*- coding: utf-8 -*-


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    point_dict = self._comp_point_coordinate()
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z6 = point_dict["Z6"]

    if self.is_outwards():
        return abs(Z4) - abs((Z3 + Z6) / 2)
    else:
        return abs(Z3) - abs(Z4)
