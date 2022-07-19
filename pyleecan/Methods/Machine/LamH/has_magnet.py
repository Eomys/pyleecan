def has_magnet(self):
    """Return if any of the Holes have magnets

    Parameters
    ----------
    self : LamH
        A LamH object

    Returns
    -------
    has_magnet : bool
        True if any of the Holes have magnets
    """

    has_mag = [hole.has_magnet() for hole in self.get_hole_list()]
    return any(has_mag)
