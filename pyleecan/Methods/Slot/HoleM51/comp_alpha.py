from numpy import arctan, cos, sin


def comp_alpha(self):
    """Compute the angle of the Hole (cf schematics)

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    alpha: float
        Angle of the Hole (cf schematics) [rad]

    """
    Rext = self.get_Rext()

    alpha = -arctan(
        2
        * (self.H0 - self.H1 * cos(0.5 * self.W1) + Rext * cos(0.5 * self.W1) - Rext)
        / (2.0 * self.H1 * sin(0.5 * self.W1) - 2 * Rext * sin(0.5 * self.W1) + self.W0)
    )

    return alpha
