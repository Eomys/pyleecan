# -*- coding: utf-8 -*-

from numpy import exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the hole

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    (Rmin, Rmax): tuple
        Radius of the circle that contains the hole [m]

    """

    Rext = self.get_Rext()

    Rmax = Rext - self.H1
    Rmin = Rext - self.H0 - self.H2

    return (Rmin, Rmax)
