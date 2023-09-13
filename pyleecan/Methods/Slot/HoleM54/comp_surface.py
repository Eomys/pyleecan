# -*- coding: utf-8 -*-
from numpy import pi


def comp_surface(self):
    """Compute the complete surface of the Hole

    Parameters
    ----------
    self : HoleM54
        A HoleM54 object

    Returns
    -------
    S: float
        Surface of the Hole [m**2]

    """

    Sint = pi * self.R1**2
    Sext = pi * (self.R1 + self.H1) ** 2
    Sarc = (Sext - Sint) * (self.W0 / (2 * pi))

    return Sarc + pi * (self.H1 / 2) ** 2
