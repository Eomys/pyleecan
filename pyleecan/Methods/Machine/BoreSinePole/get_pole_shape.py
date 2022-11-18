from ....Methods import ParentMissingError
from numpy import arccos, cos, sin


def get_pole_shape(self, phi):
    """Return the complex coordinates of the point at phi

    Parameters
    ----------
    self : BoreSinePole
        A BoreSinePole object
    phi : float
        Angle where to compute the point [rad]

    Returns
    -------
    Z : complex
        Coordinates of the requested point
    """

    if self.parent is not None:
        Rbo = self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")

    # limit phi to valid values
    phi_max = arccos(self.delta_d / (self.delta_d + Rbo)) / self.k
    phi = max(-phi_max, phi)
    phi = min(phi_max, phi)

    # compute the point on the bore radius arc
    delta = self.delta_d / cos(phi * self.k)
    r = Rbo + self.delta_d - delta
    x = r * cos(2 * phi / self.N)
    y = r * sin(2 * phi / self.N)

    return x + 1j * y
