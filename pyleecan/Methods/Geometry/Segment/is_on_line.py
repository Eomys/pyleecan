# -*- coding: utf-8 -*-


def is_on_line(self, Z):
    """Check if a point defined by its complex coordinate is on the segment

    Parameters
    ----------
    self : Segment
        A Segment object
    Z : complex
        Complex coordinate of the point

    Returns
    -------
    is_on_line : bool
        True if the point is on the segment
    """

    Z1 = self.begin
    Z2 = self.end
    Z3 = Z
    # Check if the points are aligned
    Z12 = Z1 - Z2
    Z13 = Z1 - Z3
    if abs(Z12.real * Z13.imag - Z12.imag * Z13.real) < 1e-10:
        K13 = Z12.real * Z13.real + Z12.imag * Z13.imag
        K12 = Z12.real * Z12.real + Z12.imag * Z12.imag
        eps = 1e-12
        if K13 >= -eps and K13 <= K12 + eps:
            return True
    return False
