# -*- coding: utf-8 -*-


def comp_number_phase_eq(self):
    """Compute the equivalent number of phase

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    qb: float
        Number of winding phase
    """

    return float(self.winding.qs)
