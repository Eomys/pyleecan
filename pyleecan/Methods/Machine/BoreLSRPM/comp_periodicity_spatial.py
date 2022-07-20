def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the Bore

    Parameters
    ----------
    self : BoreLSRPM
        A BoreLSRPM object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the bore
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    return self.N, False
