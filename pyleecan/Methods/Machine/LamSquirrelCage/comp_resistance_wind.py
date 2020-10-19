# -*- coding: utf-8 -*-

from numpy import pi
from math import sin


def comp_resistance_wind(self):
    """Computation of the rotor resistance

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    Rrot: float
         resistance of the rotor[Ohm]

    """
    # calculate resistance ring
    Sring = self.comp_surface_ring()
    lring = self.comp_length_ring()
    rho = self.ring_mat.struct.rho
    Zs = self.get_Zs(self)
    P = self.get_pole_pair_number(self)

    Rring = rho * lring / (2 * Sring * sin(pi * P / Zs) ** 2)

    # calculate resistance rod
    Srod = self.slot.comp_surface_wind()
    lrod = self.comp_length()
    Rrod = rho * lrod / Srod

    Rtot = Rring + Rrod

    return Rtot
