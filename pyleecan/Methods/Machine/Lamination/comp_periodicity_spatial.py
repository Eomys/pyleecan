from attr import has
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

        per_a = int(gcd(Zs, p))

        # account for notches
        for notch in self.notch:
            per_a = int(gcd(notch.notch_shape.Zs, per_a))

        # account for bore
        if self.bore:
            if hasattr(self.bore, "N"):
                per_a = int(gcd(self.bore.N, per_a))
            else:
                per_a = 1

        if per_a == 1:
            is_antiper_a = bool(Zs % 2 == 0)
        else:
            is_antiper_a = bool(Zs / p % 2 == 0)

        # Account for duct periodicity
        per_a, is_antiper_a = self.comp_periodicity_duct_spatial(per_a, is_antiper_a)

    else:
        per_a = None
        is_antiper_a = False

    return per_a, is_antiper_a
