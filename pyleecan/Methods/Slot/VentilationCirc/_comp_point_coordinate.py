from numpy import arcsin, exp, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Hole.

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    Z1 = (self.H0 - self.D0 / 2) * exp(1j * self.Alpha0)
    Z2 = (self.H0 + self.D0 / 2) * exp(1j * self.Alpha0)
    Zc = (self.H0) * exp(1j * self.Alpha0)

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Zc"] = Zc
    return point_dict
