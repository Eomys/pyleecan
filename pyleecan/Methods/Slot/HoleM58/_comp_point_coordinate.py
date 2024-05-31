from numpy import sqrt, exp


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

    Z0 = Rext - self.H0
    Z2 = Z0 + 1j * (self.W0 / 2)
    Z1 = Z2 - 1j * self.W2
    Z12 = Z1 - 1j * self.W1
    Z11 = Z2 - 1j * self.W0
    Z5 = Z2 - self.H2
    Z6 = Z5 - 1j * self.W2
    Z7 = Z6 - 1j * self.W1
    Z8 = Z5 - 1j * self.W0

    Zc1 = (Rext - self.H1 - self.R0) * exp(1j * self.W3 / 2)

    # Z3 is the tangent point of the circle for (Z3,Z2)
    # (X3 - X2) * (X3 - Xc) + (Y3 - Y2) * (Y3 - Yc)
    # Z3 is on the circle
    # (X3 - Xc) ** 2 + (Y3 - Yc) ** 2 - R0 ** 2
    R0 = self.R0
    X2 = Z2.real
    Y2 = Z2.imag
    Xc = Zc1.real
    Yc = Zc1.imag
    # Solved with Sympy
    X3 = (
        R0**2 * X2
        - R0**2 * Xc
        - R0
        * Y2
        * sqrt(-(R0**2) + X2**2 - 2 * X2 * Xc + Xc**2 + Y2**2 - 2 * Y2 * Yc + Yc**2)
        + R0
        * Yc
        * sqrt(-(R0**2) + X2**2 - 2 * X2 * Xc + Xc**2 + Y2**2 - 2 * Y2 * Yc + Yc**2)
        + X2**2 * Xc
        - 2 * X2 * Xc**2
        + Xc**3
        + Xc * Y2**2
        - 2 * Xc * Y2 * Yc
        + Xc * Yc**2
    ) / (X2**2 - 2 * X2 * Xc + Xc**2 + Y2**2 - 2 * Y2 * Yc + Yc**2)
    Y3 = (
        R0**2 * Y2
        - R0**2 * Yc
        + R0
        * (X2 - Xc)
        * sqrt(-(R0**2) + X2**2 - 2 * X2 * Xc + Xc**2 + Y2**2 - 2 * Y2 * Yc + Yc**2)
        + X2**2 * Yc
        - 2 * X2 * Xc * Yc
        + Xc**2 * Yc
        + Y2**2 * Yc
        - 2 * Y2 * Yc**2
        + Yc**3
    ) / (X2**2 - 2 * X2 * Xc + Xc**2 + Y2**2 - 2 * Y2 * Yc + Yc**2)
    Z3 = X3 + 1j * Y3

    # Same for Z4
    X5 = Z5.real
    Y5 = Z5.imag
    X4 = (
        R0**2 * X5
        - R0**2 * Xc
        + R0
        * Y5
        * sqrt(-(R0**2) + X5**2 - 2 * X5 * Xc + Xc**2 + Y5**2 - 2 * Y5 * Yc + Yc**2)
        - R0
        * Yc
        * sqrt(-(R0**2) + X5**2 - 2 * X5 * Xc + Xc**2 + Y5**2 - 2 * Y5 * Yc + Yc**2)
        + X5**2 * Xc
        - 2 * X5 * Xc**2
        + Xc**3
        + Xc * Y5**2
        - 2 * Xc * Y5 * Yc
        + Xc * Yc**2
    ) / (X5**2 - 2 * X5 * Xc + Xc**2 + Y5**2 - 2 * Y5 * Yc + Yc**2)
    Y4 = (
        R0**2 * Y5
        - R0**2 * Yc
        - R0
        * (X5 - Xc)
        * sqrt(-(R0**2) + X5**2 - 2 * X5 * Xc + Xc**2 + Y5**2 - 2 * Y5 * Yc + Yc**2)
        + X5**2 * Yc
        - 2 * X5 * Xc * Yc
        + Xc**2 * Yc
        + Y5**2 * Yc
        - 2 * Y5 * Yc**2
        + Yc**3
    ) / (X5**2 - 2 * X5 * Xc + Xc**2 + Y5**2 - 2 * Y5 * Yc + Yc**2)
    Z4 = X4 + 1j * Y4

    Z9 = Z4.conjugate()
    Z10 = Z3.conjugate()
    Zc2 = Zc1.conjugate()

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
    point_dict["Zc1"] = Zc1
    point_dict["Zc2"] = Zc2

    return point_dict
