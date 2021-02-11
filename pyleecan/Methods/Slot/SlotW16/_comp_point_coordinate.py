from numpy import arcsin, exp, pi, sqrt

from ....Methods.Slot.SlotW16 import S16OutterError
from ....Classes.Arc1 import Arc1


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW16
        A SlotW16 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """

    Rbo = self.get_Rbo()

    hsp = pi / self.Zs  # Half slot pitch

    if self.is_outwards():
        raise S16OutterError("Slot Type 16 can't be used on inner lamination")

    # ZXt => Complex coordinate in the tooth ref
    Z1 = Rbo * exp(-1j * self.W0 / 2)
    Z2 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)

    # Tooth angular width
    alphaT = 2 * arcsin(self.W3 * 0.5 / (Rbo - self.H0 - self.H2))
    Z5 = (Rbo - self.H0 - self.H2) * exp(-1j * (hsp - alphaT / 2))
    #  In the ref: O-tooth as axis
    # Z3 on cercle O => (x3t**2+y3t**2) = (Rbo-H0)**2
    # Zc on cercle O => (xct**2+yct**2) = (Rbo-H0-R1)**2
    # Z3 on cercle Zc => (xct-x3t)**2+(yct-y3t)**2 = R1**2
    # y4t = y5t = yct - R1
    # x4t = xct
    # O, Z3, Zc align => -y3t*xct+x3t*yct = 0
    Z5t = Z5 * exp(1j * hsp)
    y5t = Z5t.imag
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

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z5.conjugate()
    point_dict["Z7"] = Z4.conjugate()
    point_dict["Z8"] = Z3.conjugate()
    point_dict["Z9"] = Z2.conjugate()
    point_dict["Z10"] = Z1.conjugate()
    # Compute center
    A = Arc1(Z3, Z4, -self.R1, is_trigo_direction=False)
    point_dict["Zc1"] = A.get_center()
    point_dict["Zc2"] = point_dict["Zc1"].conjugate()
    return point_dict
