# -*- coding: utf-8 -*-
"""@package Functions.get_height_magnet
Getter for magnet height of the HoleM52
@date Created on Fri Apr 12 12:05:00 2019
@author sebastian_g
@todo unittest it
"""


def get_height_magnet(self):
    """get the height of the hole magnet

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    Hmag: float
        height of the Magnet [m]

    """

    Hmag = self.H1

    return Hmag
