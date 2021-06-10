# -*- coding: utf-8 -*-


def comp_periodicity(self, p=None):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSlotMulti
        A LamSlotMulti object

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
    is_aper = False

    return Zs, is_aper, Zs, is_aper
