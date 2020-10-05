# -*- coding: utf-8 -*-
from ....Functions.Winding.comp_wind_periodicity import comp_wind_periodicity


def comp_periodicity(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    per : int
        Number of periodicities of the lamination
    is_antiper : bool
        True if an anti-periodicity is possible after the periodicities
    """

    sym_a, is_antisym_a = comp_wind_periodicity(self.winding.comp_connection_mat())

    if is_antisym_a:
        sym_a /= 2

    return (int(sym_a), is_antisym_a, sym_a, is_antisym_a)
