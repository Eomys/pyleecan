# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Segment.check
Check Segment method
@date Created on Fri Dec 05 09:55:35 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def check(self):
    """assert that the line is correct (begin != end)

    Parameters
    ----------
    self : Segment
        A Segment object

    Returns
    -------
    None

    Raises
    ------
    PointSegmentError
        The beginning point and the ending point of an Segment
        can't be the same

    """
    if self.begin == self.end or (abs(self.begin) == 0 and abs(self.end) == 0):
        raise PointSegmentError(
            "The beginning point and the ending point of " "a Segment can't be the same"
        )


class PointSegmentError(Exception):
    """ """

    pass
