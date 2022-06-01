def comp_surface_active(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType13
        A CondType13 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    Sact = self.Wwire * self.Wwire * self.Nwppc_tan * self.Nwppc_rad

    return Sact
