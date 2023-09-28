def comp_inductance(self):
    """Return the enforced end winding inductance

    Parameters
    ----------
    self: EndWinding
        A EndWinding object

    Returns
    -------
    Lew : float
        end winding inductance [H]
    """

    return self.Lew_enforced
