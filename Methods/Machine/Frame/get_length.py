# -*- coding: utf-8 -*-
"""@package Methods.Machine.Frame.get_length
Length dictionary method
@date Created on Mon Apr 04 14:17:17 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def get_length(self):
    """Return the length of the Frame

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    length: float
        Length of the frame

    """

    if self.comp_height_eq() > 0:
        return self.Lfra
    else:
        return 0
