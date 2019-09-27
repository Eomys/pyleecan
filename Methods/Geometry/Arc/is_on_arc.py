# -*- coding: utf-8 -*-

from numpy import exp, pi, angle, abs as np_abs


def is_on_arc(self, Z):
    """Check is a point defined by its complex coordinate is on the arc

    Parameters
    ----------
    self : Arc
        An Arc object
    Z : complex
        Complex coordinate of the point

    Returns
    -------
    is_on_arc : bool
        True if the point is on the arc
    """

    Zc = self.get_center()
    R = self.comp_radius()

    # Check if on the circle
    if abs(np_abs(Z - Zc) - R) > 1e-6:
        return False

    # Check if point is begin or end
    begin = self.get_begin()
    end = self.get_end()
    if np_abs(Z - begin) < 1e-6:
        return True
    if np_abs(Z - end) < 1e-6:
        return True

    # Go to the coordinate system Zc as center, begin on X > 0 axis
    Ze = (end - Zc) * exp(-1j * angle(begin - Zc))
    Z = (Z - Zc) * exp(-1j * angle(begin - Zc))

    alpha = self.get_angle()
    Ae = angle(Ze) % (2 * pi)
    Az = angle(Z) % (2 * pi)
    if alpha > 0:  # Trigo direction
        if Ae > Az:
            return True
        return False
    # Clockwise direction
    if Az > Ae:
        return True
    return False
