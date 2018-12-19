# -*- coding: utf-8 -*-
"""@package Methods.Slot.HoleM54.comp_surface
Compute the HoleM54 surface methode
@date Created on Wed Dec 05 15:22:11 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""
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

    Sint = pi * self.R1 ** 2
    Sext = pi * (self.R1 + self.R1) ** 2
    Sarc = (Sext - Sint) * (self.W0 / (2 * pi))

    return Sarc + pi * self.H1 ** 2
