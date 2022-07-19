def has_slip(self):
    """Check if the slip column is set

    Parameters
    ----------
    self : OPMatrix
        OPMatrix object

    Returns
    -------
    has_slip : bool
        True if the slip_ref column is set
    """

    return self.slip_ref is not None
