# -*- coding: utf-8 -*-

from numpy import exp, pi, tan, arctan, sin, sqrt, arcsin


def comp_surface(self):
    """Compute the surface of the Hole

    Parameters
    ----------
    self : HoleM62
        A HoleM62 object

    Returns
    -------
    S: float
        Surface of the Hole. [m**2]

    """
    Rbo = self.get_Rbo()
    if self.W0_is_rad:  # Polar Arc
        return (
            self.W0 * (Rbo - self.H1) ** 2 / 2
            - self.W0 * (Rbo - self.H1 - self.H0) ** 2 / 2
        )

    else:  # Parallel side
        Rbo = self.get_Rbo()
        # Top surface
        alpha = 2 * arcsin((self.W0 / 2) / (Rbo - self.H1))
        Stop = ((Rbo - self.H1) ** 2) * (alpha - sin(alpha)) / 2

        # Bottom surface
        point_dict = self._comp_point_coordinate()
        Z1 = point_dict["Z1"]
        R1 = abs(Z1)
        alpha = 2 * arcsin((self.W0 / 2) / R1)
        Sbot = R1 ** 2 * (alpha - sin(alpha)) / 2

        return self.H0 * self.W0 + Stop - Sbot
