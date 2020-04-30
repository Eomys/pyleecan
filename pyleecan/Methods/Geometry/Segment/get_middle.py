# -*- coding: utf-8 -*-


def get_middle(self):
    """Return the point at the middle of the Segment

    Parameters
    ----------
    self : Segment
        A Segment object

    Returns
    -------
    Zmid: complex
        Complex coordinates of the middle of the Segment
    """

    Z1 = self.begin
    Z2 = self.end

    Zmid = (Z1 + Z2) / 2.0
    # Return (0,0) if the point is too close from 0
    if abs(Zmid) < 1e-6:
        Zmid = 0
    return Zmid
