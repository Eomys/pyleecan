def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H2 - self.H3
