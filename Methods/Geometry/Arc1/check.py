# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc1.check
Check Arc1 method
@date Created on Fri Dec 05 13:33:05 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


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


class PointArc1Error(Exception):
    """ """

    pass


class RadiusArc1Error(Exception):
    """ """

    pass
