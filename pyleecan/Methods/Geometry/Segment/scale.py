def scale(self, scale_factor):
    """Scale the coordinates of the begin/end

    Parameters
    ----------
    self : Segment
        A Segment Object
    scale_factor : float
        the Scale factor [-]

    Returns
    -------
    None
    """

    self.begin = self.begin * scale_factor
    self.end = self.end * scale_factor
