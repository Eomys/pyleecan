from numpy import angle, arcsin, arctan, cos, exp, pi, sin, sqrt

from ....Methods.Slot.SlotW15 import S15InnerError


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z13|| = W0
    alpha = arcsin(self.W0 / (2 * Rbo))
    hsp = pi / self.Zs  # Half slot pitch

    Z0 = Rbo * exp(1j * 0)
    Z13 = Z0 * exp(1j * alpha)
    if self.is_outwards():
        Z12 = Z0 + self.H0 + 1j * Z13.imag
        Z7 = Z0 + self.H0 + self.H1 + self.H2

        # Zc3, Z8 and (0,0) are align (tangent) => abs(Zc3)=Rbo+H0+H1+H2-R2
        # In tooth ref: Im(Zc3') = -W3/2 - R2
        A = Rbo + self.H0 + self.H1 + self.H2 - self.R2
        B = -self.W3 / 2 - self.R2
        xc2 = B * sin(-hsp) + sqrt(-(B**2) + A**2) * cos(-hsp)
        yc2 = B * cos(-hsp) - sqrt(-(B**2) + A**2) * sin(-hsp)
        Zc3 = xc2 + 1j * yc2
        Z9 = (Zc3 * exp(1j * -hsp) + self.R2 * 1j) * exp(1j * hsp)

        # Zc3, Z8 and (0,0) are align, |Zc3, Z8| = R2
        Z8 = (Zc3 * exp(1j * -angle(Zc3)) + self.R2) * exp(1j * angle(Zc3))

        # Real(Zc4) = Rbo+H0+H1
        # In tooth ref: Im(Zc4') = -W3/2 - R1
        xc1 = Rbo + self.H0 + self.H1
        yc1 = (-self.W3 / 2 - self.R1 - xc1 * sin(-hsp)) / cos(-hsp)
        Zc4 = xc1 + 1j * yc1
        Z10 = (Zc4 * exp(1j * -hsp) + self.R1 * 1j) * exp(1j * hsp)

        # Ref center at Zc4, (Z11,Z12) and (Z11,Zc4) are orthogonal
        # Z11 = R1*exp(1i*theta)
        # (R1*cos(theta)-x2)*R1*cos(theta)+(R1*sin(theta)-y2)*R1*sin(theta) = 0
        R1 = self.R1
        y2 = (Z12 - Zc4).imag
        x2 = (Z12 - Zc4).real
        theta = 2 * arctan((y2 - sqrt(-(R1**2) + x2**2 + y2**2)) / (R1 + x2))
        Z11 = R1 * exp(1j * theta) + Zc4
    else:
        raise S15InnerError("Slot Type 15 can't be used on inner lamination")

    point_dict = dict()
    # symetry
    point_dict["Z13"] = Z13
    point_dict["Z12"] = Z12
    point_dict["Z11"] = Z11
    point_dict["Z10"] = Z10
    point_dict["Z9"] = Z9
    point_dict["Z8"] = Z8
    point_dict["Z7"] = Z7
    point_dict["Z6"] = Z8.conjugate()
    point_dict["Z5"] = Z9.conjugate()
    point_dict["Z4"] = Z10.conjugate()
    point_dict["Z3"] = Z11.conjugate()
    point_dict["Z2"] = Z12.conjugate()
    point_dict["Z1"] = Z13.conjugate()
    point_dict["Zc4"] = Zc4
    point_dict["Zc3"] = Zc3
    point_dict["Zc2"] = Zc3.conjugate()
    point_dict["Zc1"] = Zc4.conjugate()
    return point_dict
