# -*- coding: utf-8 -*-


def get_pole_pair_number(self):
    """Return the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    if self.winding is not None:
        return self.winding.p
    else:
        return None
