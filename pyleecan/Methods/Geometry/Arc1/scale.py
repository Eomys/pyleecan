def scale(self, scale_factor):
    """Scale the coordinates of the begin/end

    Parameters
    ----------
    self : Arc1
        An Arc1 Object
    scale_factor : float
        the Scale factor [-]

    Returns
    -------
    None
    """

    self.begin = self.begin * scale_factor
    self.end = self.end * scale_factor
    self.radius = self.radius * scale_factor
