# -*- coding: utf-8 -*-
"""@package Methods.Machine.MagnetType12.comp_height
Compute the height of the magnet method
@date Created on Thu Feb 05 17:29:11 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_height(self):
    """Compute the height of the magnet

    Parameters
    ----------
    self : MagnetType12
        A MagnetType12 object

    Returns
    -------
    Hmag: float
        The magnet's height [m]

    """

    return self.Hmag
