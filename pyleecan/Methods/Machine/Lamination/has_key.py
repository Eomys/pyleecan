def has_key(self):
    """Check if a there is key in the Lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    has_key : bool
        True if the Lamination has at least one key
    """

    if self.notch is None:
        return False
    return any([notch.has_key() for notch in self.notch])
