from numpy import angle, arcsin, arctan, cos, exp, pi, sin, sqrt

from ....Methods.Slot.SlotW30 import S30InnerError
from ....Functions.Geometry.inter_line_line import inter_line_line
from ....Functions.Geometry.inter_line_circle import inter_line_circle
from ....Classes.Arc1 import Arc1


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW30
        A SlotW30 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z12|| = W0
    alpha = arcsin(self.W0 / (2 * Rbo))
    hsp = pi / self.Zs  # Half slot pitch

    Z0 = Rbo * exp(1j * 0)
    Z12 = Z0 * exp(1j * alpha)
    if self.is_outwards():
        Z11 = Z12 + self.H0

        Zp1 = Rbo * exp(1j * hsp)
        Zp2 = 2 * Rbo * exp(1j * hsp)
        Zp1 = Zp1 * exp(-1j * hsp) - (self.W3 / 2) * 1j
        Zp2 = Zp2 * exp(-1j * hsp) - (self.W3 / 2) * 1j

        Zp1 = Zp1 * exp(1j * hsp)
        Zp2 = Zp2 * exp(1j * hsp)

        Zp3 = Z12.real + self.H0 + self.H1
        Zp4 = Z12.real + self.H0 + self.H1 + 1j

        Zc1 = inter_line_line(Zp1, Zp2, Zp3, Zp4)

        if self.R2 == 0:
            Z80 = Zc1[0] * exp(-1j * hsp) - (self.W3 / 2) * 1j
            Z80 = exp(1j * hsp) * Z80
            Zc = Z80
        else:
            Z8 = Zc1[0] * exp(-1j * hsp) - self.R2
            Z8 = exp(1j * hsp) * Z8

            Z7 = Zc1[0] - self.R2 * 1j
            Zc3 = Arc1(Z7, Z8, self.R2).get_center()

        Zc = exp(-1j * hsp) * Z8
        Zc = Zc - 1
        Zc = Zc * exp(1j * hsp)

        Zp6 = Z11 + 1j
        Zc2 = inter_line_line(Z8, Zc, Z11, Zp6)

        if self.R1 == 0:
            Z100 = Zc2[0] * exp(-1j * hsp) - (self.W3 / 2) * 1j
            Z100 = exp(1j * hsp) * Z100

        else:
            Z9 = Zc2[0] * exp(-1j * hsp) + self.R1
            Z10 = Zc2[0] - self.R1 * 1j

            Z9 = exp(1j * hsp) * Z9
            Zc4 = Arc1(Z9, Z10, self.R1).get_center()

    # is internal
    else:
        Z11 = Z12 - self.H0

        Zp1 = Rbo * exp(1j * hsp)
        Zp2 = 2 * Rbo * exp(1j * hsp)
        Zp1 = Zp1 * exp(-1j * hsp) - (self.W3 / 2) * 1j
        Zp2 = Zp2 * exp(-1j * hsp) - (self.W3 / 2) * 1j

        Zp1 = Zp1 * exp(1j * hsp)
        Zp2 = Zp2 * exp(1j * hsp)

        Zp3 = Z12.real - self.H0 - self.H1
        Zp4 = Z12.real - self.H0 - self.H1 + 1j

        Zc1 = inter_line_line(Zp1, Zp2, Zp3, Zp4)

        if self.R2 == 0:
            Z80 = Zc1[0] * exp(-1j * hsp) - (self.W3 / 2) * 1j
            Z80 = exp(1j * hsp) * Z80
            Zc = Z80

        else:
            Z8 = Zc1[0] * exp(-1j * hsp) + self.R2
            Z8 = exp(1j * hsp) * Z8

            Z7 = Zc1[0] - self.R2 * 1j
            Zc3 = Arc1(Z7, Z8, self.R2).get_center()

            Zc = exp(-1j * hsp) * Z8
            Zc = Zc + 1
            Zc = Zc * exp(1j * hsp)
            Zc3 = Arc1(Z8, Z7, self.R2).get_center()

        Zp6 = Z11 + 1j
        Zc2 = inter_line_line(Z8, Zc, Z11, Zp6)

        if self.R1 == 0:
            Z100 = Zc2[0] * exp(-1j * hsp) - (self.W3 / 2) * 1j
            Z100 = exp(1j * hsp) * Z100

        else:
            Z9 = Zc2[0] * exp(-1j * hsp) - self.R1
            Z10 = Zc2[0] - self.R1 * 1j
            Z9 = exp(1j * hsp) * Z9
            Zc4 = Arc1(Z10, Z9, self.R1).get_center()

    point_dict = dict()
    # symetry
    point_dict["Z12"] = Z12
    point_dict["Z11"] = Z11
    point_dict["Z2"] = Z11.conjugate()
    point_dict["Z1"] = Z12.conjugate()

    if self.R1 != 0:
        point_dict["Z10"] = Z10
        point_dict["Z9"] = Z9
        point_dict["Z4"] = Z9.conjugate()
        point_dict["Z3"] = Z10.conjugate()
        point_dict["Zc4"] = Zc4
        point_dict["Zc1"] = Zc4.conjugate()

    else:
        point_dict["Z100"] = Z100
        point_dict["Z40"] = Z100.conjugate()

    if self.R2 != 0:
        point_dict["Z8"] = Z8
        point_dict["Z7"] = Z7
        point_dict["Z6"] = Z7.conjugate()
        point_dict["Z5"] = Z8.conjugate()
        point_dict["Zc3"] = Zc3
        point_dict["Zc2"] = Zc3.conjugate()

    else:
        point_dict["Z80"] = Z80
        point_dict["Z60"] = Z7.conjugate()

    return point_dict
