# -*- coding: utf-8 -*-


def comp_length(self):
    """Compute the length of the line

    Parameters
    ----------
    self : Segment
        A Segment object

    Returns
    -------
    length: float
        lenght of the line [m]

    Raises
    ------
    PointSegmentError
        Call Segment.check()

    """

    self.check()

    z1 = self.begin
    z2 = self.end

    return float(abs(z2 - z1))
