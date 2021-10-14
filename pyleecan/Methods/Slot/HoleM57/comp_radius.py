# -*- coding: utf-8 -*-

from numpy import pi, cos, sin, tan, arcsin, exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM57
        A HoleM57 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """
    Rext = self.get_Rext()

    Rmax = Rext - self.H1
    Rmin = abs(self._comp_point_coordinate()["Z5"])

    return (Rmin, Rmax)
