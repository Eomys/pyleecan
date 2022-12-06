def has_Tem(self):
    """Check if the Torque column is set

    Parameters
    ----------
    self : OPMatrix
        OPMatrix object

    Returns
    -------
    has_Tem : bool
        True if the Torque column is set
    """

    return self.Tem_av_ref is not None
