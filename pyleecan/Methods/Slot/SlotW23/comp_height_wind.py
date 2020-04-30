# -*- coding: utf-8 -*-


def comp_height_wind(self):
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

    Rbo = self.get_Rbo()
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()

    if self.is_outwards():
        return abs(Z4) - abs((Z3 + Z6) / 2)
    else:
        return abs(Z3) - abs(Z4)
