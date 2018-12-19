# -*- coding: utf-8 -*-
"""@package Functions.comp_mass_magnets
Computation the HoleM50 magnet mass methode
@date Created on Thu Jan 07 17:15:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_mass_magnets(self):
    """Compute the mass of the hole magnets

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    Mmag: float
        mass of the 2 Magnets [kg]

    """

    M = 0
    # magnet_0 and magnet_1 can have different materials
    if self.magnet_0:
        M += (
            self.H3
            * self.W4
            * self.magnet_0.Lmag
            * self.magnet_0.mat_type.mechanics.rho
        )
    if self.magnet_1:
        M += (
            self.H3
            * self.W4
            * self.magnet_1.Lmag
            * self.magnet_1.mat_type.mechanics.rho
        )
    return M
