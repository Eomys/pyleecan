def reverse(self):
    """Reverse the begin and end point of the Line

    Parameters
    ----------
    self : Segment
        An Segment object

    Returns
    -------
    """

    end = self.end
    self.end = self.begin
    self.begin = end
