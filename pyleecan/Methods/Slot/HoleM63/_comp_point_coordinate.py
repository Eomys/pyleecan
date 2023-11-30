from numpy import sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM63
        A HoleM63 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()
    point_dict = dict()
    # comp point coordinate (in complex)

    if self.top_flat:
        Z6 = Rbo - self.H1 - 1j * self.W0 / 2
        Z7 = Rbo - self.H1 + 1j * self.W0 / 2
        Z5 = Z6 - self.H0
        Z8 = Z7 - self.H0
        point_dict["Z1"] = Z5
        point_dict["Z2"] = Z6
        point_dict["Z3"] = Z7
        point_dict["Z4"] = Z8
    else:
        Zc1 = ((Rbo - self.H1) ** 2) - ((self.W0 / 2) ** 2)
        Zc = sqrt(Zc1)
        Z3 = Zc + 1j * self.W0 / 2
        Z2 = Zc - 1j * self.W0 / 2
        Z4 = Z3 - self.H0
        Z1 = Z2 - self.H0
        point_dict["Z1"] = Z1
        point_dict["Z2"] = Z2
        point_dict["Z3"] = Z3
        point_dict["Z4"] = Z4

    return point_dict
