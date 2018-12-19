# -*- coding: utf-8 -*-
"""@package

@date Created on Tue Feb 02 09:26:13 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_surface_magnets(self):
    """Compute the surface of the magnet (if any)

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    Smag: float
        Surface of the magnet [m**2]

    """
    if self.magnet_0:
        return self.W0 * self.H1
    else:
        return 0
