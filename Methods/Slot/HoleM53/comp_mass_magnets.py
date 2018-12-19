# -*- coding: utf-8 -*-
"""@package Functions.comp_mass_magnets
Computation the HoleM53 magnet mass method
@date Created on Fri Mar 16 17:15:15 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_mass_magnets(self):
    """Compute the mass of the magnets (if any)

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    Mmag: float
        mass of the Magnets [kg]

    """

    V = 0
    if self.magnet_0:
        V += (
            self.H2
            * self.W3
            * self.magnet_0.Lmag
            * self.magnet_0.mat_type.mechanics.rho
        )
    if self.magnet_1:
        V += (
            self.H2
            * self.W3
            * self.magnet_1.Lmag
            * self.magnet_1.mat_type.mechanics.rho
        )
    return V
