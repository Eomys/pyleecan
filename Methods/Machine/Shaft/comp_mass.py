# -*- coding: utf-8 -*-
"""@package Methods.Machine.Shaft.comp_mass
Shaft computation of the mass method
@date Created on Thu Jan 22 11:41:47 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_mass(self):
    """Computation of the Shaft mass

    Parameters
    ----------
    self: Shaft
        A Shaft object
    Returns
    -------
    M_shaft: float
        Mass of the Shaft [kg]

    """

    return self.Lshaft * pi * ((self.Drsh / 2) ** 2) * self.mat_type.mechanics.rho
