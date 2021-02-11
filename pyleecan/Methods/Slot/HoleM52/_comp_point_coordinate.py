from numpy import exp, pi, cos, sin, tan
from ....Functions.Geometry.inter_line_circle import inter_line_circle


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rext = self.get_Rext()

    alpha1 = self.comp_alpha()
    Z1 = (Rext - self.H0) * exp(1j * alpha1 / 2)
    Z9 = (Rext - self.H0) * exp(-1j * alpha1 / 2)

    Z0 = (Z1 + Z9) / 2
    Z5 = Z0 - self.H1

    Z4 = Z5 + 1j * self.W0 / 2
    Z6 = Z4.conjugate()

    Z3 = Z4 + self.H2
    Z7 = Z3.conjugate()

    W1 = self.comp_W1()
    Z2 = Z3 + 1j * W1
    Z8 = Z2.conjugate()

    Z11 = Z3 + (self.H1 - self.H2)
    Z10 = Z7 + (self.H1 - self.H2)

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

    return point_dict
