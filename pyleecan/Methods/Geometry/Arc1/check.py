# -*- coding: utf-8 -*-
from ....Methods.Geometry.Arc1 import *


def check(self):
    """assert that the arc is correct (begin != end; radius !=0)

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    None

    Raises
    ------
    PointArc1Error
        The beginning point and the ending point of an Arc1
        can't be the same
    RadiusArc1Error
        An Arc1 can't have a null radius

    """

    if self.begin == self.end or (abs(self.begin) == 0 and abs(self.end) == 0):
        raise PointArc1Error(
            "The beginning point and the ending "
            + "point of an Arc1 can't be "
            + "the same"
        )
    if self.radius == 0:
        raise RadiusArc1Error("An Arc1 can't have a null radius")
