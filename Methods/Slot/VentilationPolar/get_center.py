# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationPolar.get_center
Get the coordinate of the ventilation center methods
@date Created on Tue Mar 15 16:30:17 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import exp, pi


def get_center(self):
    """Return a list of the center of the ventilations

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object

    Returns
    -------
    Zc_list: list
        List of list of center complex coordinates

    """

    Zc_list = list()

    for ii in range(self.Zh):
        Zc = self.H0 + (self.D0 / 2.0) * exp(1j * self.Alpha0) * exp(
            1j * 2 * pi / self.Zh
        )
        Zc_list.append(Zc)

    return Zc_list
