# -*- coding: utf-8 -*-
"""@package Methods.Machine.Magnet.comp_height
Magnet numerical Computation of height method
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import array


def comp_height(self):
    """Compute the height of the Magnet.
    Caution, the bottom of the Magnet is an Arc

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    Htot: float
        Height of the Magnet [m]

    """

    surf = self.build_geometry()

    # Numerical computation
    point_list = surf[0].discretize(200)
    point_list = array(point_list)
    abs_list = abs(point_list)

    return max(abs_list) - min(abs_list)
