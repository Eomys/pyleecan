# -*- coding: utf-8 -*-


def get_pole_pair_number(self):
    """Return the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    return self.hole[0].Zh // 2
