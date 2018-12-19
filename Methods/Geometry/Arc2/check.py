# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc2.check
Check Arc2 method
@date Created on Mon Dec 08 13:20:16 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from numpy import pi


def check(self):
    """assert that the arc is correct (begin != center)

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Returns
    -------
    None

    Raises
    ------
    PointArc2Error
        The beginning point and the ending point of an Arc2
        can't be the same
    AngleArc2Error
        An Arc2 can't have a null opening angle
    """

    if self.begin == self.center or (abs(self.begin) == 0 and abs(self.center) == 0):
        raise PointArc2Error
        ("The beginning point and the center of an Arc2 can't be the same")
    if self.angle == 0:
        raise AngleArc2Error("An arc can't have a null opening angle")
    if self.angle == 2 * pi:
        raise AngleArc2Error("You can't draw a circle with an Arc2")


class PointArc2Error(Exception):
    """ """

    pass


class AngleArc2Error(Exception):
    """ """

    pass
