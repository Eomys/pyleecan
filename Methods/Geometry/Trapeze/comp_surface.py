# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Trapeze.comp_surface
Compute the Trapeze surface method
@date Created on Thu Jul 27 13:51:43 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_surface(self):
    """Compute the Trapeze surface

    Parameters
    ----------
    self : Trapeze
        A Trapeze object

    Returns
    -------
    surf: float
        The Trapeze surface [m**2]

    """

    return self.height * (self.W2 + self.W1) / 2
