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
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    per_t : int
        Number of time periodicities of the lamination
    is_antiper_t : bool
        True if an time anti-periodicity is possible after the periodicities
    """

    sym_a, is_antisym_a = comp_wind_periodicity(self.winding.comp_connection_mat())

    if is_antisym_a:
        sym_a /= 2

    return (int(sym_a), is_antisym_a, sym_a, is_antisym_a)
