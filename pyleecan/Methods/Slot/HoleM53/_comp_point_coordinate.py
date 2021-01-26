from numpy import cos, exp, sin
from ....Functions.Geometry.inter_line_circle import inter_line_circle
from ....Methods.Slot.HoleM53 import Slot53InterError


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

    Z7 = Rext - self.H0 - 1j * self.W1 / 2
    Z6 = Z7 - 1j * (self.H2 - self.H3) * cos(self.W4)
    Z8 = Z7 + (self.H2 - self.H3) * sin(self.W4)

    # Compute the coordinate in the ref of Z6 with rotation -W4
    Z5 = self.W2 * exp(-1j * self.W4) + Z6
    Z4 = (self.W2 - 1j * self.H3) * exp(-1j * self.W4) + Z6
    Z3 = (self.W2 + self.W3 - 1j * self.H3) * exp(-1j * self.W4) + Z6
    Z2 = (self.W2 + self.W3) * exp(-1j * self.W4) + Z6
    Z9 = (self.W2 + 1j * (self.H2 - self.H3)) * exp(-1j * self.W4) + Z6
    Z10 = (self.W2 + self.W3 + 1j * (self.H2 - self.H3)) * exp(-1j * self.W4) + Z6

    # Z1 and Z11 are defined as intersection between line and circle
    Zlist = inter_line_circle(Z8, Z10, Rext - self.H1)
    if len(Zlist) == 2 and Zlist[0].imag < 0 and Zlist[0].real > 0:
        Z11 = Zlist[0]
    elif len(Zlist) == 2 and Zlist[1].imag < 0 and Zlist[1].real > 0:
        Z11 = Zlist[1]
    else:
        raise Slot53InterError("ERROR: Slot 53, Can't find Z11 coordinates")

    Zlist = inter_line_circle(Z2, Z6, Rext - self.H1)
    if len(Zlist) == 2 and Zlist[0].imag < 0 and Zlist[0].real > 0:
        Z1 = Zlist[0]
    elif len(Zlist) == 2 and Zlist[1].imag < 0 and Zlist[1].real > 0:
        Z1 = Zlist[1]
    else:
        raise Slot53InterError("ERROR: Slot 53, Can't find Z1 coordinates")

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
    point_dict["Z1s"] = Z1.conjugate()
    point_dict["Z2s"] = Z2.conjugate()
    point_dict["Z3s"] = Z3.conjugate()
    point_dict["Z4s"] = Z4.conjugate()
    point_dict["Z5s"] = Z5.conjugate()
    point_dict["Z6s"] = Z6.conjugate()
    point_dict["Z7s"] = Z7.conjugate()
    point_dict["Z8s"] = Z8.conjugate()
    point_dict["Z9s"] = Z9.conjugate()
    point_dict["Z10s"] = Z10.conjugate()
    point_dict["Z11s"] = Z11.conjugate()
    return point_dict
