def comp_length_endwinding(self):
    """Compute the Winding overhang length on one side for a half-turn[m]

    Parameters
    ----------
    self: Winding
        A Winding object
    Returns
    -------
    Lewout : float
        End-winding length on one side for a half-turn [m].
    """

    if self.end_winding is None:
        return self.Lewout
    else:
        return self.Lewout + self.end_winding.comp_length_endwinding()
