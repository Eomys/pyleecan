# -*- coding: utf-8 -*-


def get_pole_pair_number(self):
    """Return the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    p = self.winding.p

    for hole in self.hole:
        assert hole.Zh / 2 == p

    return p
