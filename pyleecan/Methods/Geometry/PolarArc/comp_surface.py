# -*- coding: utf-8 -*-
from numpy import pi


def comp_surface(self):
    """Compute the PolarArc surface

    Parameters
    ----------
    self : PolarArc
        A PolarArc object

    Returns
    -------
    surf: float
        The PolarArc surface [m**2]

    """

    Rint = abs(self.point_ref) - self.height / 2
    Rext = Rint + self.height

    return (pi * Rext**2 - pi * Rint**2) * (self.angle / (2 * pi))
