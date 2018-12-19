# -*- coding: utf-8 -*-
"""@package Methods.Machine.Frame.comp_volume
Frame computation the volume methods
@date Created on Thu Jan 29 13:20:03 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_volume(self):
    """Compute the volume of the Frame

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    Vfra: float
        Volume of the Frame [m**3]

    """

    Sfra = self.comp_surface()
    return Sfra * self.Lfra
