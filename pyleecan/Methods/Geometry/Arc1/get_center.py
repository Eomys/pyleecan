# -*- coding: utf-8 -*-
from numpy import abs as np_abs, angle as np_angle, exp, sqrt


def get_center(self):
    """Return the center of the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    Zc: complex
        Complex coordinates of the center of the Arc1
    """

    self.check()

    # The center is on the bisection of [begin, end]
    z1 = self.begin
    z2 = self.end
    R = self.radius
    D12 = np_abs(z2 - z1)  # length of segment [begin,end]

    # Centre at the middle of begin and end (distance(Z1, Z2) = diameter )
    if np_abs(D12 - np_abs(2 * R)) < 1e-6:
        Zc = (z2 + z1) / 2.0
    else:
        # In the coordinate system begin on center and end on X > 0 axis
        if R > 0:  # Center is above the segment
            Zc = D12 / 2 + 1j * sqrt(R ** 2 - (D12 / 2) ** 2)
        else:
            Zc = D12 / 2 - 1j * sqrt(R ** 2 - (D12 / 2) ** 2)
        # Go back to the original coordinate system
        Zc = Zc * exp(1j * np_angle(z2 - z1)) + z1

    # Return (0,0) if the point is too close from 0
    if np_abs(Zc) < 1e-6:
        Zc = 0

    return Zc
