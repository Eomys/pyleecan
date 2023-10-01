def has_magnet(self):
    """Return if the Hole has magnets

    Parameters
    ----------
    self : HoleM61
        A HoleM61 object

    Returns
    -------
    has_magnet : bool
        True if the magnets are not None
    """

    return (
        self.magnet_0 is not None
        or self.magnet_1 is not None
        or self.magnet_2 is not None
        or self.magnet_3 is not None
    )
