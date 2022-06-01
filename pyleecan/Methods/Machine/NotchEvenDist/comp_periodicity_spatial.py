def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the notch

    Parameters
    ----------
    self : NotchEvenDist
        A NotchEvenDist object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the notch
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    return self.notch_shape.Zs, False
