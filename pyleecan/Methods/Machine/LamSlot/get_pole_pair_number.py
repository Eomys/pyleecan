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

    return self.slot.Zs // 2
