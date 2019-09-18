# -*- coding: utf-8 -*-
"""@package inter_line_line
@date Created on aug 08 09:58 2018
@author pierre_b
"""


def inter_line_line(Z1, Z2, Z3, Z4):
    """INTER_LINE_LINE find the intersection between two lines defined by two
    complex

    Parameters
    ----------
    Z1 : complex
        Complex coordinate of a point on the first line
    Z2 : complex
        Complex coordinate of another point on the first line
    Z3 : complex
        Complex coordinate of a point on the second line
    Z4 : complex
        Complex coordinate of another point on the second line

    Returns
    -------
        Zlist: list
            List of the complex coordinates of the intersection
            return [Z1, Z2] if the 4 points are aligned
    """

    # Check if the points are aligned
    Z12 = Z1 - Z2
    Z13 = Z1 - Z3
    Z14 = Z1 - Z4
    if (
        Z12.real * Z13.imag - Z12.imag * Z13.real == 0
        and Z12.real * Z14.imag - Z12.imag * Z14.real == 0
    ):
        return [Z1, Z2]

    # Compute the line equation
    (A1, B1, C1) = find_line_eq(Z1, Z2)
    (A2, B2, C2) = find_line_eq(Z3, Z4)
    # Compute the intersection
    D = A1 * B2 - B1 * A2
    Dx = C1 * B2 - B1 * C2
    Dy = A1 * C2 - C1 * A2
    if D != 0:
        x = Dx / D
        y = Dy / D
        return [x + 1j * y]
    else:
        return []


def find_line_eq(Z1, Z2):
    """Find the line equation (Ax+By=C)

    Parameters
    ----------
    Z1 : complex
        Complex coordinate of a point on the line
    Z2 : complex
         Complex coordinate of another point on the line

    Returns
    -------
    A, B, C : (float, float, float)
        Line equation parameters
    """
    A = Z1.imag - Z2.imag
    B = Z2.real - Z1.real
    C = Z1.real * Z2.imag - Z2.real * Z1.imag
    return (A, B, -C)
