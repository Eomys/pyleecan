# -*- coding: utf-8 -*-


def comp_sym(self):
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

    return self.slot.Zs, False, self.slot.Zs, False
