# -*- coding: utf-8 -*-

from numpy import exp


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]
    """

    if self.is_H0_bore is None:
        self.is_H0_bore = True  # Set default value

    if self.is_H0_bore:
        return self.H0
    else:
        point_dict = self._comp_point_coordinate()
        ZM = point_dict["ZM"]
        Rbo = self.get_Rbo()
        return abs(Rbo - abs(ZM))
