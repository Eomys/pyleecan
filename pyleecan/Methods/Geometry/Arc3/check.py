# -*- coding: utf-8 -*-
from ....Methods.Geometry.Arc3 import *


def check(self):
    """assert that the arc is correct (begin != end)

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Returns
    -------
    None

    Raises
    ------
    PointArc3Error
        The beginning point and the ending point of an Arc3
        can't be the same

    """

    if self.begin == self.end or (abs(self.begin) == 0 and abs(self.end) == 0):
        raise PointArc3Error(
            "The beginning point and the ending point of an " "Arc3 can't be the same"
        )
