from numpy import gcd


def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : lamination
        A lamination object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    if hasattr(self, "get_Zs") and hasattr(self, "get_pole_pair_number"):
        Zs = self.get_Zs()
        p = self.get_pole_pair_number()

        per = int(gcd(Zs, p))

        if per == 1:
            is_aper = bool(Zs % 2 == 0)
        else:
            is_aper = bool(Zs / p % 2 == 0)

    else:
        per = None
        is_aper = False

    return per, is_aper
