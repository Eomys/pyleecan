# -*- coding: utf-8 -*-


def comp_number_phase_eq(self):
    """Compute the equivalent number of phase

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    qb: float
        Zs/p
    """

    return self.slot.Zs / float(self.winding.p)
