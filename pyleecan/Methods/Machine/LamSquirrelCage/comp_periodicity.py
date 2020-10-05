# -*- coding: utf-8 -*-


def comp_sym(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    per : int
        Number of periodicities of the lamination
    is_antiper : bool
        True if an anti-periodicity is possible after the periodicities
    """

    return self.slot.Zs, False, self.slot.Zs, False
