# -*- coding: utf-8 -*-
"""@package Functions.get_height_magnet
Getter for magnet height of the HoleM50
@date Created on Fri Apr 12 12:05:00 2019
@author sebastian_g
@todo unittest it
"""


def get_height_magnet(self):
    """get the height of the hole magnets

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    Hmag: float
        height of the 2 Magnets [m]

    """

    # magnet_0 and magnet_1 have the same height
    Hmag = self.H3

    return Hmag
