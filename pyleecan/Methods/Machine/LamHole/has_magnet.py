def has_magnet(self):
    """Return if any of the Holes have magnets

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    has_magnet : bool
        True if any of the Holes have magnets
    """

    has_mag = [hole.has_magnet() for hole in self.hole]
    return any(has_mag)
