# -*- coding: utf-8 -*-
from ....Classes.Hole import Hole


def comp_radius_mid_yoke(self):
    """Compute the Lamination middle of the yoke radius

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    Ry: float
        middle of the yoke radius [m]

    """

    Rmin = self.Rext
    Rmax = self.Rint
    for hole in self.hole:
        if type(hole) is not Hole:
            (Rmin_hole, Rmax_hole) = hole.comp_radius()
            Rmin = min(Rmin, Rmin_hole)
            Rmax = max(Rmax, Rmax_hole)
    if self.is_internal:
        return (self.Rint + Rmin) / 2
    else:
        return (self.Rext + Rmax) / 2
