# -*- coding: utf-8 -*-
from ....Functions.Geometry.inter_line_line import find_line_eq
from numpy import sqrt


def comp_distance(self, Z):
    """Compute the distance of a point to the Segment

    Parameters
    ----------
    self : Segment
        A Segment object
    Z : complex
        Complex coordinate of the point

    Returns
    -------
    D : float
        distance of a point to the Segment
    """

    Z1 = self.begin
    Z2 = self.end
    Z3 = Z
    if self.is_on_line(Z=Z):
        return 0
    # Check if the points are aligned
    Z12 = Z1 - Z2
    Z13 = Z1 - Z3
    if Z12.real * Z13.imag - Z12.imag * Z13.real == 0:
        return min(abs(Z1 - Z3), abs(Z2 - Z3))
    # point not aligned
    (A, B, C) = find_line_eq(Z1, Z2)
    return (abs(A * Z3.real + B * Z3.imag - C)) / sqrt(A ** 2 + B ** 2)
