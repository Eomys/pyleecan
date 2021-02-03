# -*- coding: utf-8 -*-


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    point_dict = self._comp_point_coordinate()
    Rbo = self.get_Rbo()
    return abs(Rbo - abs(point_dict["Z2"]))
