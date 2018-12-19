# -*- coding: utf-8 -*-
"""@package Methods.Machine.Frame.comp_surface
Frame computation the surface methods
@date Created on Thu Jan 29 13:20:03 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_surface(self):
    """Compute the surface of the Frame

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    Sfra: float
        Surface of the Frame [m**2]

    """

    # Surface of the external disk
    S_ext = (self.Rext ** 2) * pi
    # Surface of the internal disk
    S_int = (self.Rint ** 2) * pi

    return S_ext - S_int
