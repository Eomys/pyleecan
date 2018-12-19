"""
Created on 14 June. 2018

@author: franco_i
"""

from numpy import angle, arcsin, arctan, cos, exp, pi, sin, sqrt

from pyleecan.Methods.Slot.SlotW15 import S15InnerError


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    point_list: list
        A list of 12 Points

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z13|| = W0
    alpha = arcsin(self.W0 / (2 * Rbo))
    hsp = pi / self.Zs  # Half slot pitch

    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)
    if self.is_outwards():
        Z2 = Z0 + self.H0 + 1j * Z1.imag
        Z7 = Z0 + self.H0 + self.H1 + self.H2

        # Zc2, Z6 and (0,0) are align (tangent) => abs(Zc2)=Rbo+H0+H1+H2-R2
        # In tooth ref: Im(Zc2') = -W3/2 - R2
        A = Rbo + self.H0 + self.H1 + self.H2 - self.R2
        B = -self.W3 / 2 - self.R2
        xc2 = B * sin(-hsp) + sqrt(-B ** 2 + A ** 2) * cos(-hsp)
        yc2 = B * cos(-hsp) - sqrt(-B ** 2 + A ** 2) * sin(-hsp)
        Zc2 = xc2 + 1j * yc2
        Z5 = (Zc2 * exp(1j * -hsp) + self.R2 * 1j) * exp(1j * hsp)

        # Zc2, Z6 and (0,0) are align, |Zc2, Z6| = R2
        Z6 = (Zc2 * exp(1j * -angle(Zc2)) + self.R2) * exp(1j * angle(Zc2))

        # Real(Zc1) = Rbo+H0+H1
        # In tooth ref: Im(Zc1') = -W3/2 - R1
        xc1 = Rbo + self.H0 + self.H1
        yc1 = (-self.W3 / 2 - self.R1 - xc1 * sin(-hsp)) / cos(-hsp)
        Zc1 = xc1 + 1j * yc1
        Z4 = (Zc1 * exp(1j * -hsp) + self.R1 * 1j) * exp(1j * hsp)

        # Ref center at Zc1, (Z3,Z2) and (Z3,Zc1) are orthogonal
        # Z3 = R1*exp(1i*theta)
        # (R1*cos(theta)-x2)*R1*cos(theta)+(R1*sin(theta)-y2)*R1*sin(theta) = 0
        R1 = self.R1
        y2 = (Z2 - Zc1).imag
        x2 = (Z2 - Zc1).real
        theta = 2 * arctan((y2 - sqrt(-R1 ** 2 + x2 ** 2 + y2 ** 2)) / (R1 + x2))
        Z3 = R1 * exp(1j * theta) + Zc1
    else:
        raise S15InnerError("Slot Type 15 can't be used on inner lamination")

    # symetry
    Z8 = Z6.conjugate()
    Z9 = Z5.conjugate()
    Z10 = Z4.conjugate()
    Z11 = Z3.conjugate()
    Z12 = Z2.conjugate()
    Z13 = Z1.conjugate()
    return [Z13, Z12, Z11, Z10, Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]
