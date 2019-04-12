# -*- coding: utf-8 -*-
"""@package Functions.get_height_magnet
Getter for magnet height of the HoleM53
@date Created on Fri Apr 12 12:05:00 2019
@author sebastian_g
@todo unittest it
"""


def get_height_magnet(self):
    """get the height of the hole magnets

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    Hmag: float
        height of the 2 Magnets [m]

    """

    # magnet_0 and magnet_1 have the same height
    Hmag = self.H2

    return Hmag
