from numpy import angle, arcsin, exp, tan
from ....Methods import ParentMissingError


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : MagnetType11
        A MagnetType11 object

    Returns
    -------
    point_list: list
        A list of 6 complex coordinates

    """
    if self.parent is not None:
        (Z1, Z2) = self.parent.get_point_bottom()
        H0 = self.parent.H0
        W0 = self.parent.W0
    else:
        raise ParentMissingError(
            "Error: The magnet object is not inside a " + "slot object"
        )

    # comp point coordinate (in complex)
    if W0 > self.Wmag:  # The magnet is smaller than the slot => center the mag
        Z1 = Z1 * exp(1j * (W0 - self.Wmag) / 2)
        Z2 = Z2 * exp(-1j * (W0 - self.Wmag) / 2)

    Rbot = abs(Z1)
    if self.is_outwards():
        Rtop = Rbot - self.Hmag
        Rslot = Rbot - H0
        Zref = Rbot - self.Hmag / 2
    else:
        Rtop = Rbot + self.Hmag
        Rslot = Rbot + H0
        Zref = Rbot + self.Hmag / 2

    Z3 = Rtop * exp(1j * angle(Z1))
    Zs3 = Rslot * exp(1j * angle(Z1))
    Z4 = Rtop * exp(1j * angle(Z2))
    Zs4 = Rslot * exp(1j * angle(Z2))

    return [Z1, Z2, Z3, Zs3, Zs4, Z4, Zref]
