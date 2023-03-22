# -*- coding: utf-8 -*-

from numpy import pi, exp, angle


def get_angle(self, is_deg=False):
    """Return the angle of the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object
    is_deg: bool
        True to convert to degree

    Returns
    -------
    angle: float
        Angle of the arc
    """
    # Go to center ref with begin on the X > 0 axis
    Zc = self.get_center()
    Z2 = (self.end - Zc) * exp(-1j * angle(self.begin - Zc))

    if Z2.imag > 0 and self.is_trigo_direction:
        alpha = angle(Z2)
    elif Z2.imag > 0 and not self.is_trigo_direction:
        alpha = -(2 * pi - angle(Z2))
    elif Z2.imag < 0 and self.is_trigo_direction:
        alpha = 2 * pi - abs(angle(Z2))
    elif Z2.imag < 0 and not self.is_trigo_direction:
        alpha = angle(Z2)
    elif Z2.imag == 0 and self.is_trigo_direction:
        alpha = abs(angle(Z2))
    elif Z2.imag == 0 and not self.is_trigo_direction:
        alpha = -abs(angle(Z2))
    else:
        alpha = 0

    if is_deg:
        return alpha * 180 / pi
    else:
        return alpha
