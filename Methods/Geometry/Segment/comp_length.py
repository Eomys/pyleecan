# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Segment.comp_length
Computation of Segment length method
@date Created on Fri Dec 05 11:00:08 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_length(self):
    """Compute the length of the line

    Parameters
    ----------
    self : Segment
        A Segment object

    Returns
    -------
    length: float
        lenght of the line [m]

    Raises
    ------
    PointSegmentError
        Call Segment.check()

    """

    self.check()

    z1 = self.begin
    z2 = self.end

    return float(abs(z2 - z1))
