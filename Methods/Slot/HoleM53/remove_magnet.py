# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Nov 29 17:26:43 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def remove_magnet(self):
    """Remove the magnet (set to None) of the Hole

    Parameters
    ----------
    self : HoleM53
        a HoleM53 object
    """

    self.magnet_0 = None
    self.magnet_1 = None
