# -*- coding: utf-8 -*-
"""@package Methods.Machine.MagnetType10.comp_volume
Compute the Magnet volume method
@date Created on Wed Dec 17 14:56:19 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_volume(self):
    """Compute the Magnet volume (by analytical computation)

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    V: float
        Magnet volume [m**3]

    """

    return self.comp_surface() * self.Lmag
