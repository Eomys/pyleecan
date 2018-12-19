# -*- coding: utf-8 -*-
"""@package Methods.Machine.MagnetType10.comp_mass
Compute the Magnet mass method
@date Created on Wed Dec 17 14:56:19 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_mass(self):
    """Compute the Magnet mass (by analytical computation)

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    M: float
        Magnet mass [kg]

    """

    return self.comp_volume() * self.mat_type.mechanics.rho
