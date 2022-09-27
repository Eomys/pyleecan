from math import gcd


def comp_periodicity_duct_spatial(self, per_a, is_antiper_a):
    """Compute the periodity of the axial cooling ducts

    Parameters
    ----------
    self : Lamination
        A Lamination object
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities

    Returns
    -------
    per_a : int
        Spatial periodicity of the lamination including ducts
    is_antiper_a : bool
        Spatial antiperidicity of the lamination including ducts
    """

    # No duct => no impact on sym
    if self.axial_vent in [None, list()]:
        self.axial_vent = list()
        return per_a, is_antiper_a

    # Compute duct periodicity
    per_d = self.axial_vent[0].Zh
    for duct in self.axial_vent[1:]:
        per_d = int(gcd(per_d, duct.Zh))

    # "Merge" lamination and duct periodicity
    if is_antiper_a:
        per = int(gcd(per_d, per_a * 2))
        if per == per_a * 2:  # No impact of vent
            pass
        elif per == per_a:  # Anti per removed
            is_antiper_a = False
        elif per_a % per == 0:
            per_a = per
            is_antiper_a = False
        elif per % 2 == 0:
            per_a = int(per / 2)
            is_antiper_a = True
        else:
            per_a = per
            is_antiper_a = False
    else:
        per_a = int(gcd(per_d, per_a))

    # if hasattr(self, "get_Zs") and hasattr(self, "get_pole_pair_number"):
    #     Zs = self.get_Zs()
    #     p = self.get_pole_pair_number()
    #     if per_a == 1:
    #         is_antiper_a = bool(Zs % 2 == 0)
    #     else:
    #         is_antiper_a = bool(Zs / p % 2 == 0)

    return per_a, is_antiper_a
