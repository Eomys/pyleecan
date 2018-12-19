# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Segment.get_middle
Compute the coordinate of the middle of a Segment method
@date Created on Wed May 04 11:07:56 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def get_middle(self):
    """Return the point at the middle of the Segment

    Parameters
    ----------
    self : Segment
        A Segment object

    Returns
    -------
    Zmid: complex
        Complex coordinates of the middle of the Segment
    """

    Z1 = self.begin
    Z2 = self.end

    Zmid = (Z1 + Z2) / 2.0
    # Return (0,0) if the point is too close from 0
    if abs(Zmid) < 1e-6:
        Zmid = 0
    return Zmid
