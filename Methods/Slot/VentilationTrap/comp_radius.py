# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationTrap.comp_radius
Compute the radius of the two circle that contains all the ventilation ducts
@date Created on Wed Dec 09 17:43:57 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import sqrt


def comp_radius(self):
    """Compute the radius of the two circle that contains all the ventilation
    ducts

    Parameters
    ----------
    self : VentilationTrap
        A VentilationTrap object

    Returns
    -------
    (Rmin, Rmax): tuple
        Tuple of circle radius [m]

    """

    self.check()

    Rmin = sqrt(self.W1 ** 2 + self.H0 ** 2)
    Rmax = sqrt(self.W2 ** 2 + (self.H0 + self.D0) ** 2)

    return (Rmin, Rmax)
