def has_magnet(self):
    """Return if LamSlot has magnets

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    has_magnet : bool
        True if LamSlot has magnets
    """

    return (
        hasattr(self, "magnet")
        or hasattr(self, "magnet_north")
        or hasattr(self, "magnet_south")
    )
