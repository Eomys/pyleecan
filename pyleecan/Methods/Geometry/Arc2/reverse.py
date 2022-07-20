def reverse(self):
    """Reverse the begin and end point of the Line

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Returns
    -------
    """

    self.begin = self.get_end()
    self.angle = -self.angle
