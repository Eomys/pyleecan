from numpy import exp, pi, cos, sin, tan, angle, sqrt
from ....Functions.Geometry.inter_line_circle import inter_line_circle


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM62
        A HoleM62 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()
    point_dict = dict()
    # comp point coordinate (in complex)
    if self.W0_is_rad:
        Z1 = (Rbo - self.H1 - self.H0) * exp(-1j * self.W0 / 2)
        Z2 = (Rbo - self.H1) * exp(-1j * self.W0 / 2)
        Z3 = (Rbo - self.H1) * exp(1j * self.W0 / 2)
        Z4 = (Rbo - self.H1 - self.H0) * exp(1j * self.W0 / 2)
        point_dict["Z1"] = Z1
        point_dict["Z2"] = Z2
        point_dict["Z3"] = Z3
        point_dict["Z4"] = Z4

    else:
        Zc1 = ((Rbo - self.H1) ** 2) - ((self.W0 / 2) ** 2)
        Zc = sqrt(Zc1)

        Z7 = Zc + 1j * self.W0 / 2
        Z6 = Zc - 1j * self.W0 / 2
        Z8 = Z7 - self.H0
        Z5 = Z6 - self.H0
        point_dict["Z1"] = Z5
        point_dict["Z2"] = Z6
        point_dict["Z3"] = Z7
        point_dict["Z4"] = Z8

    return point_dict
