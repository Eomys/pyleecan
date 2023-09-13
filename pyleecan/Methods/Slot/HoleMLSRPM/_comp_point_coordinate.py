from numpy import exp, arcsin, tan, cos, sqrt, sin, pi


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleMLSRPM
        A HoleMLSRPM object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """
    Rbo = self.get_Rbo()
    # Z1
    delta1 = arcsin((self.R1 + self.W2) / (self.R1 + self.R3))
    alpha1 = self.W1 - delta1
    Z1 = self.R3 * exp(-1j * alpha1)

    # Zc1
    Zc1 = (self.R3 + self.R1) * exp(-1j * alpha1)
    xc1 = (self.R3 + self.R1) * cos(alpha1)
    yc1 = -(self.R3 + self.R1) * sin(alpha1)

    # Z2
    x2 = (-1 / tan(self.W1) * xc1 + yc1 - self.W2 / cos(self.W1)) / -(
        tan(self.W1) + 1 / tan(self.W1)
    )
    y2 = -tan(self.W1) * x2 + self.W2 / cos(self.W1)
    Z2 = x2 + 1j * y2

    # Z3
    a3 = 1 + tan(self.W1) ** 2
    b3 = -2 * tan(self.W1) * self.W2 / cos(self.W1)
    c3 = (self.W2 / cos(self.W1)) ** 2 - self.R2**2

    x3 = (-b3 + sqrt(b3**2 - 4 * a3 * c3)) / (2 * a3)
    y3 = -tan(self.W1) * x3 + self.W2 / cos(self.W1)
    Z3 = x3 + 1j * y3
    # Z5
    x5 = Rbo - self.H1
    y5 = -self.W0 / 2
    Z5 = x5 + 1j * y5
    # Zc2
    xc2 = Rbo - self.H1 - self.R1
    yc2 = -self.W0 / 2
    Zc2 = xc2 + 1j * yc2
    # Z4
    a4 = (xc2 - x3) ** 2 - self.R1**2
    b4 = 2 * (xc2 - x3) * (y3 - yc2)
    c4 = (y3 - yc2) ** 2 - self.R1**2
    alpha2 = (-b4 - sqrt(b4**2 - 4 * a4 * c4)) / (2 * a4)
    x4 = (xc2 / alpha2 + yc2 + alpha2 * x3 - y3) / (alpha2 + 1 / alpha2)
    y4 = alpha2 * (x4 - x3) + y3
    Z4 = x4 + 1j * y4
    Zw1 = self.R2 * exp(1j * self.W1)
    Zw2 = Zw1 + self.W2 * exp(1j * -(pi / 2 - self.W1))
    # symmetry
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    Z9 = Z2.conjugate()
    Z10 = Z1.conjugate()

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
    point_dict["Zc1"] = Zc1
    point_dict["Zc2"] = Zc2
    point_dict["Zw1"] = Zw1
    point_dict["Zw2"] = Zw2
    return point_dict
