# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationCirc.comp_radius
Compute the radius of the two circle that contains all the ventilation ducts
@date Created on Wed Dec 09 17:17:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_radius(self):
    """Compute the radius of the two circle that contains all the ventilation
    ducts

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    (Rmin, Rmax): tuple
        Tuple of circle radius [m]

    """

    self.check()

    Rmin = self.H0 - self.D0 / 2.0
    Rmax = self.H0 + self.D0 / 2.0

    return (Rmin, Rmax)
