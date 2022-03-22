def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType13
        A CondType13 object

    Returns
    -------
    W: float
        Width of the conductor [m]

    """

    return (2 * self.Wins_wire + self.Wwire) * self.Nwppc_tan
