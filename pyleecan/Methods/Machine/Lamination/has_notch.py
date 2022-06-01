def has_notch(self, is_bore):
    """Check if notches are set on the requested radius

    Parameters
    ----------
    self : Lamination
        A Lamination object
    is_bore : bool
        True check notch on bore radius, else on yoke

    Returns
    -------
    has_notch : bool
        True if notches are set on the requested radius
    """

    if self.notch is None or len(self.notch) == 0:
        return False

    has_notch = any([notch.notch_shape.is_bore for notch in self.notch])
    if is_bore:
        return has_notch
    else:
        return not has_notch
