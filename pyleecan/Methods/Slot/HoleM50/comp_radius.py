# -*- coding: utf-8 -*-

from numpy import angle, arcsin, arctan, array, cos, exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """

    Rmax = self.get_Rext() - self.H1

    point_dict = self._comp_point_coordinate()
    Rmin = min(abs(point_dict["Z5"]), abs(point_dict["Z7"]))

    return (Rmin, Rmax)
