from numpy import sqrt


def _comp_R0(self):
    """Compute the radius of the circle

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    R0 : float
        Radius of the circle [m]
    """

    # R0 is the radius of the circle
    # Pythagore in Triangle: Center, Z2, middle(Z1,Z2)
    # R0**2 = (W0/2)**2 + (H0-R0)**2

    return ((self.W0 / 2) ** 2 + self.H0 ** 2) / (2 * self.H0)
