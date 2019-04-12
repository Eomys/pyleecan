# -*- coding: utf-8 -*-
"""@package Functions.get_height_magnet
Getter for magnet height of the HoleM51
@date Created on Fri Apr 12 12:05:00 2019
@author sebastian_g
@todo unittest it
"""


def get_height_magnet(self):
    """get the height of the hole magnets

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    Hmag: float
        height of the 3 Magnets [m]

    """

    # magnet_0 and magnet_1 and magnet_2 have the same height
    Hmag = self.H2

    return Hmag
