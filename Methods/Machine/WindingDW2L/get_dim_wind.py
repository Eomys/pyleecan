# -*- coding: utf-8 -*-
"""@package Methods.Machine.Winding.get_dim_wind
Compute the Winding Matrix Dimension Method
@date Created on Fri Jan 15 11:03:49 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from pyleecan.Methods import NotImplementedYetError


def get_dim_wind(self):
    """Get the two first dimension of the winding matrix

    Parameters
    ----------
    self : Winding
        A Winding object

    Returns
    -------
    (Nrad, Ntan): tuple
        Number of layer in radial and tangential direction

    """

    return (2, 1)
