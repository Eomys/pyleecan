# -*- coding: utf-8 -*-

from numpy import pi
from ....Functions.Winding.comp_wind_sym import comp_wind_sym


def comp_sym(self):
    """Compute the symmetry factor of the lamination

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    sym : int
        Number of symmetries of the Lamination
    is_antisym : bool
        True if an anti-symmetry is possible after the symmetries
    """

    sym, is_antisym = comp_wind_sym(self.winding.comp_connection_mat())
    if is_antisym:
        sym /= 2
    return (int(sym), is_antisym)
