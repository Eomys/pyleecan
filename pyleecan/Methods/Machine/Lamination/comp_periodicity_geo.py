def comp_periodicity_geo(self):
    """Compute the geometric periodicity factor of the lamination

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
        is_antiper_a = False

        # Account for duct periodicity
        per_a, is_antiper_a = self.comp_periodicity_duct_spatial(Zs, is_antiper_a)

    else:
        per_a = None
        is_antiper_a = False

    return per_a, is_antiper_a
