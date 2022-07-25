# -*- coding: utf-8 -*-
from numpy import sqrt, abs as np_abs


def inter_line_circle(Z1, Z2, R, Zc=0):
    """INTER_LINE_CIRCLE find the intersection between a circle of center Zc
    and radius r with a line defined by two points

    Parameters
    ----------
    Z1 : complex
        Complex coordinate of a point on the line
    Z2 : complex
        Complex coordinate of another point on the line
    R : float
        Radius of the circle [m]
    Zc : complex
        Complex coordinate of the center

    Returns
    -------
    Zlist: list
        List of the complex coordinates of the intersection
    """
    # Set the coordinate system on the circle center
    if np_abs(Zc) > 1e-6:
        Z1 = Z1 - Zc
        Z2 = Z2 - Zc
    else:
        Zc = 0

    x1 = Z1.real
    y1 = Z1.imag
    x2 = Z2.real
    y2 = Z2.imag

    dx = x2 - x1
    dy = y2 - y1
    dr = sqrt(dx ** 2 + dy ** 2)
    D = x1 * y2 - x2 * y1

    delta = R ** 2 * dr ** 2 - D ** 2
    if delta < 0:  # 0 point
        return list()
    elif delta == 0:  # 1 point(tangent)
        return [(D * dy - 1j * D * dx) / dr ** 2 + Zc]

    else:  # 2 points
        if dy < 0:
            xs1 = (D * dy - dx * sqrt(delta)) / dr ** 2
            xs2 = (D * dy + dx * sqrt(delta)) / dr ** 2
        else:
            xs1 = (D * dy + dx * sqrt(delta)) / dr ** 2
            xs2 = (D * dy - dx * sqrt(delta)) / dr ** 2
        ys1 = (-D * dx + abs(dy) * sqrt(delta)) / dr ** 2
        ys2 = (-D * dx - abs(dy) * sqrt(delta)) / dr ** 2

        return [xs1 + 1j * ys1 + Zc, xs2 + 1j * ys2 + Zc]
