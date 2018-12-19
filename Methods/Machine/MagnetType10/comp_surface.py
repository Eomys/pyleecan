# -*- coding: utf-8 -*-
"""@package Methods.Machine.MagnetType10.comp_surface
Compute the Magnet surface method
@date Created on Wed Dec 17 14:56:19 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the Magnet surface (by analytical computation)

    Parameters
    ----------
    self : MagnetType10
        A MagnetType10 object

    Returns
    -------
    S: float
        Magnet surface [m**2]

    """

    return self.Hmag * self.Wmag
