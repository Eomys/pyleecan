def clean(self):
    """Clean the internal properties (wind_mat and periodicity)

    Parameters
    ----------
    self : Winding
        A Winding object
    """
    self.wind_mat = None
    self.per_a = None
    self.is_aper_a = None
