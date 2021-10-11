from numpy import arcsin, exp, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Hole.

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """

    Z1 = (self.H0 - 1j * self.W1 / 2) * exp(1j * self.Alpha0)
    Z2 = (self.H0 + self.D0 - 1j * self.W2 / 2) * exp(1j * self.Alpha0)
    Z3 = (self.H0 + self.D0 + 1j * self.W2 / 2) * exp(1j * self.Alpha0)
    Z4 = (self.H0 + 1j * self.W1 / 2) * exp(1j * self.Alpha0)
    ZM1 = (Z1 + Z4) / 2
    ZM2 = (Z2 + Z3) / 2
    Zc = (self.H0 + (self.D0 / 2)) * exp(1j * self.Alpha0)

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Zc"] = Zc
    point_dict["ZM1"] = ZM1
    point_dict["ZM2"] = ZM2
    return point_dict
