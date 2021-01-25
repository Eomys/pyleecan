from numpy import exp, pi, cos, sin, tan
from ....Functions.Geometry.inter_line_circle import inter_line_circle


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rext = self.get_Rext()

    # comp point coordinate (in complex)
    alpha = self.comp_alpha()

    Wslot = 2 * sin(self.W1 / 2) * (Rext - self.H1)
    L = 0.5 * (Wslot - self.W0) / cos(alpha)  # ||P2,P5||

    # Center of the hole
    Z0 = Rext - self.H0
    Z2 = Z0 + 1j * self.W0 / 2
    Z25 = Z0 - 1j * self.W0 / 2
    Z15 = Z25 - self.H2
    Z1 = Z2 - 1j * self.W2
    Z26 = Z1 - 1j * self.W3
    Z12 = Z2 - self.H2
    Z13 = Z12 - 1j * self.W2
    Z14 = Z13 - 1j * self.W3
    Z11 = Z12 + 1j * tan(alpha / 2) * self.H2
    Z16 = Z15 - 1j * tan(alpha / 2) * self.H2

    # Draw the left side with center P2, and X axis =(P2,P5), Y axis=(P2,P10)
    Z3 = self.W4 * exp(1j * (pi / 2 - alpha)) + Z2
    Z4 = (self.W4 + self.W5) * exp(1j * (pi / 2 - alpha)) + Z2
    Z5 = (Rext - self.H1) * exp(1j * self.W1 / 2)
    Z10 = (1j * self.H2) * exp(1j * (pi / 2 - alpha)) + Z2
    Z9 = (1j * self.H2 + self.W4) * exp(1j * (pi / 2 - alpha)) + Z2
    Z8 = (1j * self.H2 + self.W4 + self.W5) * exp(1j * (pi / 2 - alpha)) + Z2
    Z7 = (1j * self.H2 + L) * exp(1j * (pi / 2 - alpha)) + Z2

    # Draw the right side with center P25, X axis (P25,P23), Y axis(P25,P17)
    Z24 = self.W6 * exp(-1j * (pi / 2 - alpha)) + Z25
    Z23 = (self.W6 + self.W7) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z22 = (Rext - self.H1) * exp(-1j * self.W1 / 2)
    Z17 = (-1j * self.H2) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z18 = (-1j * self.H2 + self.W6) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z19 = (-1j * self.H2 + self.W6 + self.W7) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z20 = (-1j * self.H2 + L) * exp(-1j * (pi / 2 - alpha)) + Z25

    # Z6 is the intersection of the line [Z7,Z10] and Circle centre
    # (0,0) radius Rext - H1
    Zint = inter_line_circle(Z7, Z10, Rext - self.H1)

    # Select the point with Re(Z) > 0
    if Zint[0].real > 0:
        Z6 = Zint[0]
    else:
        Z6 = Zint[1]
    Z21 = Z6.conjugate()

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
    point_dict["Z10"] = Z10
    point_dict["Z11"] = Z11
    point_dict["Z12"] = Z12
    point_dict["Z13"] = Z13
    point_dict["Z14"] = Z14
    point_dict["Z15"] = Z15
    point_dict["Z16"] = Z16
    point_dict["Z17"] = Z17
    point_dict["Z18"] = Z18
    point_dict["Z19"] = Z19
    point_dict["Z20"] = Z20
    point_dict["Z21"] = Z21
    point_dict["Z22"] = Z22
    point_dict["Z23"] = Z23
    point_dict["Z24"] = Z24
    point_dict["Z25"] = Z25
    point_dict["Z26"] = Z26

    return point_dict
