# -*- coding: utf-8 -*-


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW62
        A SlotW62 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    point_dict = self._comp_point_coordinate()
    Zw1 = point_dict["Zw1"]
    Zw2 = point_dict["Zw2"]

    return abs(Zw1 - Zw2)
