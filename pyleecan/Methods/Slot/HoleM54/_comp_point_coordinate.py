from numpy import pi, exp


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM54
        A HoleM54 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rext = self.get_Rext()

    # Compute point coordinates
    Zc0 = Rext - self.H0 + self.R1
    Z0 = Rext - self.H0
    Z1 = (self.R1 * exp(1j * (-pi + self.W0 / 2))) + Zc0
    Z2 = (self.R1 * exp(1j * (pi - self.W0 / 2))) + Zc0
    Z4 = ((self.R1 + self.H1) * exp(1j * (-pi + self.W0 / 2))) + Zc0
    Z3 = ((self.R1 + self.H1) * exp(1j * (pi - self.W0 / 2))) + Zc0

    point_dict = dict()
    point_dict["Z0"] = Z0
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Zc0"] = Zc0

    return point_dict
