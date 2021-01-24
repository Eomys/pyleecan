# -*- coding: utf-8 -*-


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotM16
        A SlotM16 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    point_dict = self._comp_point_coordinate()
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]

    if self.is_outwards():
        R1 = abs((Z3 + Z6) / 2)
        R2 = abs(Z4)
    else:
        R1 = abs((Z4 + Z5) / 2)
        R2 = abs(Z3)
    return R2 - R1
