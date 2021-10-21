# -*- coding: utf-8 -*-
from ....Classes.Winding import Winding
from ....Classes.Conductor import Conductor


def comp_periodicity(self, p=None):
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

    # Angular periodicity
    if self.winding is not None and self.winding.conductor is not None:
        per_a, is_antiper_a = self.winding.get_periodicity()
    else:
        per_a, is_antiper_a = 1, False
    if is_antiper_a:
        per_a = int(per_a / 2)
    per_a, is_antiper_a = self.comp_periodicity_duct_spatial(per_a, is_antiper_a)

    # Time periodicity
    per_t, is_antiper_t = per_a, is_antiper_a

    return int(per_a), bool(is_antiper_a), int(per_t), bool(is_antiper_t)
