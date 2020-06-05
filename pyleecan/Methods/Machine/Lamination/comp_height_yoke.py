# -*- coding: utf-8 -*-


def comp_height_yoke(self):
    """Compute the yoke height

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Hy: float
        yoke height [m]

    """
    return self.Rext - self.Rint
