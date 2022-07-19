# -*- coding: utf-8 -*-


def comp_height_yoke(self):
    """Compute the yoke height

    Parameters
    ----------
    self : LamH
        A LamH object

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
    for hole in self.get_hole_list():
        (Rmin, Rmax) = hole.comp_radius()
        if self.is_internal:
            R = min(R, Rmin)
        else:
            R = max(R, Rmax)

    if self.is_internal:
        return R - self.Rint
    else:
        return self.Rext - R
