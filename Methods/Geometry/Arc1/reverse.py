def reverse(self):
    """Reverse the begin and end point of the Line

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    """

    end = self.end
    self.end = self.begin
    self.begin = end
    self.radius = -self.radius
