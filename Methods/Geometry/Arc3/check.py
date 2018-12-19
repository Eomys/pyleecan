# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc3.check
Check Arc3 method
@date Created on Tue Mar 01 10:18:09 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


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


class PointArc3Error(Exception):
    """ """

    pass
