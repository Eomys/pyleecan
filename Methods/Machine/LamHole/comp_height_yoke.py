# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotMag.comp_height
Lamination with Magnets computation of yoke height method
@date Created on Tue Jan 20 10:01:53 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height_yoke(self):
    """Compute the yoke height

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    Hy: float
        yoke height [m]

    """

    if self.is_internal:
        R = self.Rext
    else:
        R = self.Rint

    # The yoke is define the greater cylinder without holes
    for hole in self.hole:
        (Rmin, Rmax) = hole.comp_radius()
        if self.is_internal:
            R = min(R, Rmin)
        else:
            R = max(R, Rmax)

    if self.is_internal:
        return R - self.Rint
    else:
        return self.Rext - R
