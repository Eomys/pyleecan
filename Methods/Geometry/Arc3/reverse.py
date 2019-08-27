def reverse(self):
    """Reverse the begin and end point of the Line

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Returns
    -------
    """

    end = self.end
    self.end = self.begin
    self.begin = end
    self.is_trigo_direction = not self.is_trigo_direction
