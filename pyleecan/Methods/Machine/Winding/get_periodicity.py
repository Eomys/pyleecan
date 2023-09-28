def get_periodicity(self):
    """Computes the winding matrix (anti-)periodicity

    Parameters
    ----------
    self : Winding
        A Winding object

    Returns
    -------
    per_a: int
        Number of spatial periods of the winding
    is_aper_a: bool
        True if the winding is anti-periodic over space

    """

    if self.per_a is None or self.is_aper_a is None:
        self.per_a, self.is_aper_a = self.comp_periodicity()

    return self.per_a, self.is_aper_a
