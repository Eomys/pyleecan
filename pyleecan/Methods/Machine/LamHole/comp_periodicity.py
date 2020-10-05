# -*- coding: utf-8 -*-


def comp_periodicity(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    per : int
        Number of periodicities of the lamination
    is_antiper : bool
        True if an anti-periodicity is possible after the periodicities
    """

    return self.get_pole_pair_number(), True, self.get_pole_pair_number(), True
