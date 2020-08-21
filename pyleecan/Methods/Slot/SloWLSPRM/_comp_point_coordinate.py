from numpy import arcsin, exp, pi, sqrt, sin, cos


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotWLSPRM
        A SlotWLSPRM object

    Returns
    -------
    point_list: list
        A list of 10 Point

    """

    Rbo = self.get_Rbo()

    hsp = pi / self.Zs  # Half slot pitch

    # ZXt => Complex coordinate in the slot ref
    Z1 = (Rbo - self.H0 - self.H2) * exp(-1j * hsp)
    y2 = -(((Rbo - self.H0) * sin(hsp) * 2) - (self.W1 * cos(hsp) * 2)) / 2
    x2 = Rbo - self.H0
    Z2 = x2 + 1j * y2
    x3t = Rbo - self.H0
    y3t = self.W3 / 2
    Z3t = x3t + 1j * y3t
    Z3 = Z3t * exp(-1j * hsp)

    # Tooth angular width
    # alphaT = 2 * arcsin(self.W3 * 0.5 / (Rbo - self.H0 - self.H2))
    # Z5 = (Rbo - self.H0 - self.H2) * exp(-1j * (hsp - alphaT / 2))
    #  In the ref: O-tooth as axis
    # Z3 on cercle O => (x3t**2+y3t**2) = (Rbo-H0)**2
    # Zc on cercle O => (xct**2+yct**2) = (Rbo-H0-R1)**2
    # Z3 on cercle Zc => (xct-x3t)**2+(yct-y3t)**2 = R1**2
    # y4t = y5t = yct - R1
    # x4t = xct
    # O, Z3, Zc align => -y3t*xct+x3t*yct = 0

    xct = sqrt(
        self.H0 ** 2
        + 2 * self.H0 * self.R1
        - 2 * self.H0 * Rbo
        - 2 * self.R1 * Rbo
        - 2 * self.R1 * y5t
        + Rbo ** 2
        - y5t ** 2
    )
    x3t = (self.H0 - Rbo) * xct / (self.H0 + self.R1 - Rbo)
    x4t = sqrt((self.H0 - Rbo - y5t) * (self.H0 + 2 * self.R1 - Rbo + y5t))
    y3t = (self.H0 - Rbo) * (self.R1 + y5t) / (self.H0 + self.R1 - Rbo)
    y4t = y5t
    Z4t = x4t + 1j * y4t
    Z3t = x3t + 1j * y3t

    Z4 = Z4t * exp(-1j * hsp)
    Z3 = Z3t * exp(-1j * hsp)

    # symetry
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    Z9 = Z2.conjugate()
    Z10 = Z1.conjugate()

    return [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10]
