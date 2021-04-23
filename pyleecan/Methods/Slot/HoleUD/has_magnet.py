def has_magnet(self):
    """Return if the Hole has magnets

    Parameters
    ----------
    self : HoleUD
        A HoleUD object

    Returns
    -------
    has_magnet : bool
        True if the magnets are not None
    """

    has_mag = False
    if self.magnet_dict is None:
        self.magnet_dict = dict()
        return False
    for value in self.magnet_dict.values():
        if value is not None:
            has_mag = True
    return has_mag
