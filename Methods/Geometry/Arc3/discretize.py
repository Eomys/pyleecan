# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc3.discretize
Discretize an Arc3 method
@date Created on Tue Mar 01 10:15:26 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import angle as np_angle, exp, linspace, pi

from pyleecan.Methods.Machine import ARC_NPOINT_D


def discretize(self, nb_point=ARC_NPOINT_D):
    """Return the discretize version of the Arc.
    Begin and end are always return

    Parameters
    ----------
    self : Arc3
        An Arc3 object
    nb_point : int
        Number of points to add to discretize the arc (Default value = ARC_NPOINT_D)

    Returns
    -------
    list_point: list
        list of complex coordinate of the points

    Raises
    ------
    NbPointArc1DError
        nb_point must be an integer >=0
    """

    # Check that the Arc is correct
    self.check()
    if not isinstance(nb_point, int):
        raise NbPointArc3DError("discretize : nb_point must be an integer")
    if nb_point < 0:
        raise NbPointArc3DError("nb_point must be >=0")

    # We use the complex representation of the point
    z1 = self.begin
    zc = self.get_center()
    R = self.comp_radius()

    # Generation of the point by rotation
    if self.is_trigo_direction:  # Top
        t = linspace(0, pi, nb_point + 2)
    else:  # Bottom
        t = linspace(0, -pi, nb_point + 2)
    list_point = R * exp(1j * t)

    # Geometric transformation : return to the main axis
    list_point = list_point * exp(1j * np_angle(z1 - zc)) + zc

    return list_point


class NbPointArc3DError(Exception):
    """ """

    pass
