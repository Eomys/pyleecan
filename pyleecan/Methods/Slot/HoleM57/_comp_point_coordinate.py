from numpy import arcsin, cos, exp, angle, pi, sin, tan, array
from pyleecan.Functions.Geometry.inter_line_line import inter_line_line


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """
    Rext = self.get_Rext()

    # "Tooth" angle (P1',0,P1)
    alpha_T = 2 * arcsin(self.W3 / (2 * (Rext - self.H1)))
    # magnet pole pitch angle (Z1,0,Z1')
    alpha_S = (2 * pi / self.Zh) - alpha_T
    # Angle (P1,P1',P4') and (P5',P4', )
    alpha = (pi - self.W0) / 2
    # Half slot pitch
    hssp = pi / self.Zh

    Z1 = (Rext - self.H1) * exp(-1j * alpha_S / 2)
    x11 = 2 * sin(alpha_S / 2) * (Rext - self.H1)  # Distance from P1 to P1'
    # In rect triangle P4, P1, perp (P1,P1') with P4
    H = tan(alpha) * (x11 / 2 - self.W1 / 2)
    Z4 = Z1.real - H - 1j * self.W1 / 2

    x45 = self.H2 / cos(alpha)  # distance from P4 to P5
    Z5 = Z4 - x45

    # Get coordinates of "random" points on (P5,P8) and (P1,P8)
    # In ref P4 center and P1 on X+ axis
    Z58 = (self.W4 - 1j * self.H2) * exp(1j * angle(Z1 - Z4)) + Z4
    # In the tooth ref
    Z18 = (Rext - self.H1 - self.H2 + 1j * self.W3 / 2) * exp(-1j * hssp)
    Z8 = inter_line_line(Z5, Z58, Z1, Z18)[0]

    # In ref "b" P4 center and P1 on X+ axis
    Z8b = (Z8 - Z4) * exp(-1j * angle(Z1 - Z4))
    Z9 = (Z8b + 1j * self.H2) * exp(1j * angle(Z1 - Z4)) + Z4
    Z2 = (Z8b + 1j * self.H2 - self.W2) * exp(1j * angle(Z1 - Z4)) + Z4
    Z3 = (Z8b + 1j * self.H2 - self.W2 - self.W4) * exp(1j * angle(Z1 - Z4)) + Z4
    Z7 = (Z8b - self.W2) * exp(1j * angle(Z1 - Z4)) + Z4
    Z6 = (Z8b - self.W2 - self.W4) * exp(1j * angle(Z1 - Z4)) + Z4

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z6
    point_dict["Z7"] = Z7
    point_dict["Z8"] = Z8
    point_dict["Z9"] = Z9

    # Symmetry
    point_dict["Z1s"] = Z1.conjugate()
    point_dict["Z2s"] = Z2.conjugate()
    point_dict["Z3s"] = Z3.conjugate()
    point_dict["Z4s"] = Z4.conjugate()
    point_dict["Z5s"] = Z5.conjugate()
    point_dict["Z6s"] = Z6.conjugate()
    point_dict["Z7s"] = Z7.conjugate()
    point_dict["Z8s"] = Z8.conjugate()
    point_dict["Z9s"] = Z9.conjugate()
    point_dict["Zc0"] = inter_line_line(Z3, Z2, point_dict["Z3s"], point_dict["Z2s"])[0]
    return point_dict
