# -*- coding: utf-8 -*-
"""@package Functions.get_height_magnet
Getter for magnet height of the HoleM54
@date Created on Fri Apr 12 12:05:00 2019
@author sebastian_g
@todo unittest it
"""


def get_height_magnet(self):
    """get the height of the hole for convenience

    Parameters
    ----------
    self : HoleM54
        A HoleM54 object

    Returns
    -------
    Hmag: float
        height of the hole [m]

    """

    Hmag = self.H1

    return Hmag
