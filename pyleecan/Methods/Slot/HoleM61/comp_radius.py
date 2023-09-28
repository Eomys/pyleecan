# -*- coding: utf-8 -*-

from numpy import abs

from pyleecan.Classes.Arc1 import Arc1


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM61
        A HoleM61 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """

    Rbo = self.get_Rbo()

    Rmax = Rbo - self.H2
    Rmin = abs((Rbo - self.H0) + 1j * self.W0 / 2)

    return (Rmin, Rmax)
