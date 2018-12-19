# -*- coding: utf-8 -*-
"""@package Methods.Machine.MagnetType12.comp_surface
Compute the Magnet surface method
@date Created on Wed Dec 17 15:33:08 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the Magnet surface (by numerical computation)

    Parameters
    ----------
    self : MagnetType12
        A MagnetType12 object

    Returns
    -------
    S: float
        Magnet surface [m**2]

    """

    surf = self.build_geometry()

    return surf[0].comp_surface()
