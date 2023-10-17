from numpy import arcsin, exp, pi, sqrt

from ....Methods.Slot.SlotW16 import S16OutterError
from ....Functions.Geometry.inter_circle_circle import inter_circle_circle


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
        raise S16OutterError("Slot Type 16 can't be used on outer lamination")

    # ZXt => Complex coordinate in the tooth ref
    Z1 = Rbo * exp(-1j * self.W0 / 2)
    Z2 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)

    # Tooth angular width

    alphaT = 2 * arcsin(self.W3 * 0.5 / (Rbo - self.H0 - self.H2))
    Z5 = (Rbo - self.H0 - self.H2) * exp(-1j * (hsp - alphaT / 2))
    R2 = Rbo - self.H0
    R3 = Rbo - self.H0 - self.R1

    #  In the ref: O-tooth as axis
    # Z3 on cercle O and radius R2 => (x3t**2+y3t**2) = R2**2
    # Zc on cercle O and radius R3 => (xct**2+yct**2) = R3**2
    # Z3 on cercle Zc => (xct-x3t)**2+(yct-y3t)**2 = R1**2
    # y4t = y5t = yct - R1
    # x4t = xct
    # O, Z3, Zc align => -y3t*xct+x3t*yct = 0

    y5t = -self.W3 / 2
    y4t = y5t
    yct = y5t - self.R1

    # xct = sqrt(R3**2-yct**2) and yct = y5t + R1

    xct = sqrt(R3 ** 2 - yct ** 2)
    x4t = xct
    Z4t = x4t + 1j * y4t
    Zct = xct + 1j * yct
    Z3t = inter_circle_circle(Zct, self.R1, 0, R2)[0]
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
    point_dict["Zc1"] = Zct * exp(-1j * hsp)
    point_dict["Zc2"] = point_dict["Zc1"].conjugate()

    return point_dict
