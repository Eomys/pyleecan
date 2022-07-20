def has_slot(self, is_bore=True):
    """Return if the lamination has slot on the requested radius
    (notches not taken into account, cf has_notch)

    Parameters
    ----------
    self : Lamination
        A Lamination object
    is_bore : bool
        True check if there are slots on the bore, else yoke

    Returns
    -------
    has_slot : bool
        True if the lamination has slot on the requested radius
    """

    return False
