# -*- coding: utf-8 -*-

from numpy import abs

from pyleecan.Classes.Arc1 import Arc1


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM62
        A HoleM62 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """

    Rbo = self.get_Rbo()

    Rmax = Rbo - self.H1

    if not self.W0_is_rad:
        point_dict = self._comp_point_coordinate()
        Rmin = abs(point_dict["Z1"])
    else:
        Rmin = Rbo - self.H1 - self.H0

    return (Rmin, Rmax)
