def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination over 2*pi
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    return self.get_pole_pair_number(), True
