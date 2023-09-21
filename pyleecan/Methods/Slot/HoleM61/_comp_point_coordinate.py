from numpy import exp, pi, cos, sin, tan, angle, sqrt
from ....Functions.Geometry.inter_line_circle import inter_line_circle


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM61
        A HoleM61 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    # comp point coordinate (in complex)

    Z1 = (Rbo - self.H0) + 1j * self.W0 / 2
    Z2 = Z1 + self.H1

    Zc6 = (Rbo - self.H0) + 1j * (Rbo - self.H0)

    Z6 = Zc6 - 1j * self.W3 / sqrt(2)

    Zc3 = (Rbo - self.H0 + self.H1) + 1j * (Rbo - self.H0 + self.H1)

    Z3 = Zc3 - 1j * (self.W3 / 2 + self.H1) / cos(pi / 4)

    # point on line Z5, Z6
    Zc5 = Z6 + 1j * self.H1 + (self.H1 * tan(pi / 4))

    # radius Rbo - H2
    Zint5 = inter_line_circle(Z6, Zc5, Rbo - self.H2)
    # Select the point with Re(Z) > 0 and Im(z) >0
    if Zint5[0].real > 0 and Zint5[0].imag > 0:
        Z5 = Zint5[0]
    else:
        Z5 = Zint5[1]

    # point on line Z3, Z4
    Zc4 = Z3 + 1j * self.H1 + self.H1 * tan(pi / 4)

    # radius Rbo - H2
    Zint4 = inter_line_circle(Z3, Zc4, Rbo - self.H2)
    # Select the point with Re(Z) > 0 and Im(z) >0
    if Zint4[0].real > 0 and Zint4[0].imag > 0:
        Z4 = Zint4[0]
    else:
        Z4 = Zint4[1]

    # draw magnet
    Zm1 = Z1
    Zm2 = Z2
    Zm3 = Z2 + 1j * self.W1
    Zm4 = Z1 + 1j * self.W1

    Zcm1 = (Z3 + Z4) / 2
    Zcm2 = Zcm1 - cos(pi / 4) * self.H1 + 1j * sin(pi / 4) * self.H1

    Zm5 = Zcm1 - (self.W2 / 2) * sin(pi / 4) - 1j * (self.W2 / 2) * cos(pi / 4)
    Zm6 = Zcm1 + (self.W2 / 2) * sin(pi / 4) + 1j * (self.W2 / 2) * cos(pi / 4)
    Zm7 = Zcm2 + (self.W2 / 2) * sin(pi / 4) + 1j * (self.W2 / 2) * cos(pi / 4)
    Zm8 = Zcm2 - (self.W2 / 2) * sin(pi / 4) - 1j * (self.W2 / 2) * cos(pi / 4)

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z6
    point_dict["ZM1"] = Zm1
    point_dict["ZM2"] = Zm2
    point_dict["ZM3"] = Zm3
    point_dict["ZM4"] = Zm4
    point_dict["ZM5"] = Zm5
    point_dict["ZM6"] = Zm6
    point_dict["ZM7"] = Zm7
    point_dict["ZM8"] = Zm8

    # Draw the right hole by symmetry
    point_dict["Z7"] = Z1.conjugate()
    point_dict["Z8"] = Z2.conjugate()
    point_dict["Z9"] = Z3.conjugate()
    point_dict["Z10"] = Z4.conjugate()
    point_dict["Z11"] = Z5.conjugate()
    point_dict["Z12"] = Z6.conjugate()
    point_dict["ZM9"] = Zm1.conjugate()
    point_dict["ZM10"] = Zm2.conjugate()
    point_dict["ZM11"] = Zm3.conjugate()
    point_dict["ZM12"] = Zm4.conjugate()
    point_dict["ZM13"] = Zm5.conjugate()
    point_dict["ZM14"] = Zm6.conjugate()
    point_dict["ZM15"] = Zm7.conjugate()
    point_dict["ZM16"] = Zm8.conjugate()

    return point_dict
