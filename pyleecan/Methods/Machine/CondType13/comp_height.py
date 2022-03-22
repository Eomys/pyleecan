def comp_height(self):
    """Compute the height of the conductor

    Parameters
    ----------
    self : CondType13
        A CondType13 object

    Returns
    -------
    H: float
        Height of the conductor [m]

    """

    return (2 * self.Wins_wire + self.Wwire) * self.Nwppc_rad
