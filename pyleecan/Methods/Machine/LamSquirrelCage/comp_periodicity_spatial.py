def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination over 2*pi
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    Zs = self.get_Zs()

    return Zs, bool(Zs % 2 == 0)
