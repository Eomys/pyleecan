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

    # notch_shape.is_bore = None => Default is True
    if is_bore:
        return any([notch.notch_shape.is_bore in [True, None] for notch in self.notch])
    else:
        return any([notch.notch_shape.is_bore == False for notch in self.notch])
