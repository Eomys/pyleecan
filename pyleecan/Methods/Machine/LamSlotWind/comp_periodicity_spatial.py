from numpy import gcd


def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination over 2*pi
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """
    # get Lamination periodicity
    per_a, is_antiper_a = super(type(self), self).comp_periodicity_spatial()

    # Angular periodicity
    if self.winding is not None and self.winding.conductor is not None:
        per_a_w, is_antiper_a_w = self.winding.get_periodicity()
        per_a = int(gcd(per_a, per_a_w))
        is_antiper_a = is_antiper_a and is_antiper_a_w

    per_a, is_antiper_a = self.comp_periodicity_duct_spatial(per_a, is_antiper_a)

    return int(per_a), bool(is_antiper_a)
