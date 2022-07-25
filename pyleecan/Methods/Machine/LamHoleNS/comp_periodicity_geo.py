def comp_periodicity_geo(self):
    """Compute the geometric periodicity factor of the lamination

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

    return self.comp_periodicity_spatial()
