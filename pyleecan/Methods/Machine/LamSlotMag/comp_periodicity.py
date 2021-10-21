# -*- coding: utf-8 -*-


def comp_periodicity(self, p):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

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

    # Angular periodicity
    per_a, is_antiper_a = p, True
    per_a, is_antiper_a = self.comp_periodicity_duct_spatial(per_a, is_antiper_a)

    # Time peridodicity
    per_t, is_antiper_t = p, True

    return per_a, is_antiper_a, per_t, is_antiper_t
