from numpy import gcd


def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamHoleNS
        A LamHoleNS object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    per_a = self.get_pole_pair_number()
    is_antiper_a = False

    # Account for duct periodicity
    per_a, is_antiper_a = self.comp_periodicity_duct_spatial(per_a, is_antiper_a)

    return per_a, is_antiper_a
