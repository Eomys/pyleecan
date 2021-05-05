def scale(self, scale_factor):
    """Scale the coordinates of the lines

    Parameters
    ----------
    self : SurfLine
        A SurfLine Object
    scale_factor : float
        the Scale factor [-]

    Returns
    -------
    None
    """

    for line in self.line_list:
        line.scale(scale_factor)
    self.point_ref = self.point_ref * scale_factor
