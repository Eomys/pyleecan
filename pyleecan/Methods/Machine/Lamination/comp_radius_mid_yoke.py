# -*- coding: utf-8 -*-


def comp_radius_mid_yoke(self):
    """Compute the Lamination middle of the yoke radius

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Ry: float
        middle of the yoke radius [m]

    """

    return (self.Rext + self.Rint) / 2
