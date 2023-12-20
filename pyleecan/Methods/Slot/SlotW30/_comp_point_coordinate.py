from numpy import arcsin, exp, pi
from ....Functions.Geometry.inter_line_line import inter_line_line
from ....Functions.Geometry.inter_line_circle import inter_line_circle


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

        if self.R2 == 0:
            Zc1 = inter_line_line(Zp1, Zp2, Zp3, Zp4)
            Z80 = Zc1[0]

        else:
            ZR1 = Rbo * exp(1j * hsp)
            ZR2 = 2 * Rbo * exp(1j * hsp)
            ZR1 = ZR1 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R2 * 1j
            ZR2 = ZR2 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R2 * 1j

            ZR1 = ZR1 * exp(1j * hsp)
            ZR2 = ZR2 * exp(1j * hsp)

            ZR3 = Z12.real + self.H0 + self.H1 - self.R2
            ZR4 = Z12.real + self.H0 + self.H1 - self.R2 + 1j

            ZcenterR2 = inter_line_line(ZR2, ZR1, ZR3, ZR4)

            Z8 = inter_line_circle(Zp1, Zp2, self.R2, ZcenterR2[0])
            Z7 = inter_line_circle(Zp3, Zp4 + 1j, self.R2, ZcenterR2[0])

            # we can have approximation, but we want a line tangent. So we can approximate coordinate center of cercle at 10e-6
            if len(Z8) == 0:
                Z8 = inter_line_circle(Zp1, Zp2, self.R2, ZcenterR2[0] + 1e-6 * 1j)

            if len(Z7) == 0:
                Z7 = inter_line_circle(Zp3, Zp4 + 1j, self.R2, ZcenterR2[0] + 1e-6)

            Z8 = Z8[0]
            Z7 = Z7[0]
            Zc3 = ZcenterR2[0]

        Zp5 = Z11
        Zp6 = Z11 + 1j

        if self.R1 == 0:
            Zc2 = inter_line_line(Zp5, Zp6, Zp1, Zp2)
            Z100 = Zc2[0]

        else:
            Zt1 = Rbo * exp(1j * hsp)
            Zt2 = 2 * Rbo * exp(1j * hsp)
            Zt1 = Zt1 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R1 * 1j
            Zt2 = Zt2 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R1 * 1j

            Zt1 = Zt1 * exp(1j * hsp)
            Zt2 = Zt2 * exp(1j * hsp)

            Zt3 = Z12.real + self.H0 + self.R1
            Zt4 = Z12.real + self.H0 + self.R1 + 1j

            ZcenterR1 = inter_line_line(Zt2, Zt1, Zt3, Zt4)

            Z9 = inter_line_circle(Zp1, Zp2, self.R1, ZcenterR1[0])
            Z10 = inter_line_circle(Zp5, Zp6, self.R1, ZcenterR1[0])

            # we can have approximation, but we want a line tangent. So we can approximate coordinate center of cercle at 10e-6
            if len(Z9) == 0:
                Z9 = inter_line_circle(Zp1, Zp2, self.R1, ZcenterR1[0] + 1e-6 * 1j)

            if len(Z10) == 0:
                Z10 = inter_line_circle(Zp5, Zp6, self.R1, ZcenterR1[0] - 1e-6)

            Z9 = Z9[0]
            Z10 = Z10[0]
            Zc4 = ZcenterR1[0]

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

        if self.R2 == 0:
            Zc1 = inter_line_line(Zp1, Zp2, Zp3, Zp4)
            Z80 = Zc1[0]

        else:
            ZR1 = Rbo * exp(1j * hsp)
            ZR2 = 2 * Rbo * exp(1j * hsp)
            ZR1 = ZR1 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R2 * 1j
            ZR2 = ZR2 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R2 * 1j

            ZR1 = ZR1 * exp(1j * hsp)
            ZR2 = ZR2 * exp(1j * hsp)

            ZR3 = Z12.real - self.H0 - self.H1 + self.R2
            ZR4 = Z12.real - self.H0 - self.H1 + self.R2 + 1j

            ZcenterR2 = inter_line_line(ZR2, ZR1, ZR3, ZR4)

            Z8 = inter_line_circle(Zp1, Zp2, self.R2, ZcenterR2[0])
            Z7 = inter_line_circle(Zp3, Zp4 + 1j, self.R2, ZcenterR2[0])

            # we can have approximation, but we want a line tangent. So we can approximate coordinate center of cercle at 10e-6
            if len(Z8) == 0:
                Z8 = inter_line_circle(Zp1, Zp2, self.R2, ZcenterR2[0] + 1e-6 * 1j)

            if len(Z7) == 0:
                Z7 = inter_line_circle(Zp3, Zp4 + 1j, self.R2, ZcenterR2[0] - 1e-6)

            Z8 = Z8[0]
            Z7 = Z7[0]
            Zc3 = ZcenterR2[0]

        Zp5 = Z11
        Zp6 = Z11 + 1j

        if self.R1 == 0:
            Zc2 = inter_line_line(Zp5, Zp6, Zp1, Zp2)
            Z100 = Zc2[0]

        else:
            Zt1 = Rbo * exp(1j * hsp)
            Zt2 = 2 * Rbo * exp(1j * hsp)
            Zt1 = Zt1 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R1 * 1j
            Zt2 = Zt2 * exp(-1j * hsp) - (self.W3 / 2) * 1j - self.R1 * 1j

            Zt1 = Zt1 * exp(1j * hsp)
            Zt2 = Zt2 * exp(1j * hsp)

            Zt3 = Z12.real - self.H0 - self.R1
            Zt4 = Z12.real - self.H0 - self.R1 + 1j

            ZcenterR1 = inter_line_line(Zt2, Zt1, Zt3, Zt4)

            Z9 = inter_line_circle(Zp1, Zp2, self.R1, ZcenterR1[0])
            Z10 = inter_line_circle(Zp5, Zp6, self.R1, ZcenterR1[0])

            # we can have approximation, but we want a line tangent. So we can approximate coordinate center of cercle at 10e-6
            if len(Z9) == 0:
                Z9 = inter_line_circle(Zp1, Zp2, self.R1, ZcenterR1[0] + 1e-6 * 1j)

            if len(Z10) == 0:
                Z10 = inter_line_circle(Zp5, Zp6, self.R1, ZcenterR1[0] + 1e-6)

            Z9 = Z9[0]
            Z10 = Z10[0]
            Zc4 = ZcenterR1[0]

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
        point_dict["Z60"] = Z80.conjugate()

    return point_dict
