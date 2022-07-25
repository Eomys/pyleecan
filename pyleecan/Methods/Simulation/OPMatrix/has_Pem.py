def has_Pem(self):
    """Check if the Power column is set

    Parameters
    ----------
    self : OPMatrix
        OPMatrix object

    Returns
    -------
    has_Pem : bool
        True if the Power column is set
    """

    return self.Pem_av_ref is not None
