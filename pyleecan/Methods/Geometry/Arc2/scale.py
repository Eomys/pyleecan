def scale(self, scale_factor):
    """Scale the coordinates of the begin/end

    Parameters
    ----------
    self : Arc2
        An Arc2 Object
    scale_factor : float
        the Scale factor [-]

    Returns
    -------
    None
    """

    self.begin = self.begin * scale_factor
