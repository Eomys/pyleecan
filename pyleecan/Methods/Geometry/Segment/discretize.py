# -*- coding: utf-8 -*-
from numpy import linspace

from ....Methods.Machine import LINE_NPOINT_D
from ....Methods.Geometry.Segment import NbPointSegmentDError


def discretize(self, nb_point=LINE_NPOINT_D):
    """Return the discretize version of the Segment.
    Begin and end are always returned

    Parameters
    ----------
    self : Segment
        A Segment object
    nb_point : int
        Number of points to add to discretize the line (Default value = LINE_NPOINT_D)

    Returns
    -------
    list_point: list
        List of complex coordinate of the points

    Raises
    ------
    NbPointSegmentDError
        nb_point must be an integer >=
    """

    self.check()
    if not isinstance(nb_point, int):
        raise NbPointSegmentDError("discretize : nb_point must be an integer")
    if nb_point < 0:
        raise NbPointSegmentDError("nb_point must be >=0")

    # t start by 0 (begin) and end by 1 (end)
    # len(t) = nb_point +2 : begin + end + nb_point between
    t = linspace(0, 1, nb_point + 2)

    # We use the complex representation of the point
    z1 = self.begin
    z2 = self.end

    # Generate the points with the parametric representation of the line
    return z1 - (z1 - z2) * t
