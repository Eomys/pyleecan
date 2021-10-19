# -*- coding: utf-8 -*-


def comp_periodicity(self, p=None):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

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

    per_a, is_antiper_a = self.get_Zs(), False
    per_a, is_antiper_a = self.comp_periodicity_duct_spatial(per_a, is_antiper_a)

    per_t, is_antiper_t = self.get_Zs(), False

    return per_a, is_antiper_a, per_t, is_antiper_t
