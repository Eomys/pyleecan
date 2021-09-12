# -*- coding: utf-8 -*-
from numpy import gcd


def comp_periodicity(self, p):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    per_t : int
        Number of time periodicities of the lamination
    is_antiper_t : bool
        True if an time anti-periodicity is possible after the periodicities
    """
    Zs = self.get_Zs()

    per = gcd(Zs, p)

    if per == 1:
        is_aper = bool(Zs % 2 == 0)
    else:
        is_aper = bool(Zs / p % 2 == 0)

    return per, is_aper, per, is_aper
