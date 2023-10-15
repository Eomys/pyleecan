def has_magnet(self):
    """Return if the Hole has magnets

    Parameters
    ----------
    self : HoleM63
        A HoleM63 object

    Returns
    -------
    has_magnet : bool
        True if the magnets are not None
    """

    return self.magnet_0 is not None
