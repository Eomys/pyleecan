# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc1.comp_radius
Computation of Arc1 radius method 
@date Created on 12:47 31.07.2019
@author sebastian_g
"""


def comp_radius(self):
    """Compute the Radius of the Arc1 (for unification with other arc objects)

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    radius: float
        radius of the arc
    """

    self.check()

    return self.radius  # Radius of the arc
