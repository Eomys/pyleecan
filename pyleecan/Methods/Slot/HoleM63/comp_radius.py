# -*- coding: utf-8 -*-

from numpy import abs


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM63
        A HoleM63 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """
    point_dict = self._comp_point_coordinate()
    Rbo = self.get_Rbo()

    if self.top_flat:
        Rmax = abs(point_dict["Z2"])
        Rmin = abs((point_dict["Z1"] + point_dict["Z4"]) / 2)

    else:
        Rmax = Rbo - self.H1
        Rmin = abs((point_dict["Z1"] + point_dict["Z4"]) / 2)
    return (Rmin, Rmax)
