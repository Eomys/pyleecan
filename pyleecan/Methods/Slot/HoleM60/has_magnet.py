def has_magnet(self):
    """Return if the Hole has magnets

    Parameters
    ----------
    self : HoleM60
        A HoleM60 object

    Returns
    -------
    has_magnet : bool
        True if the magnets are not None
    """

    return self.magnet_0 is not None or self.magnet_1 is not None
