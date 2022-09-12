from ....Methods import ParentMissingError
from numpy import arccos, cos, sin


def get_pole_shape(self, phi):
    """Return the bore radius

    Parameters
    ----------
    phi : float
        angle corresponding to the bore radius

    Rbo : float
        radius of the inital bore

    delta_0 : float
        initial airgap width

    Returns
    -------
    r : float
        Bore radius
    """

    if self.parent is not None:
        Rbo = self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")

    # limit phi to valid values
    phi_max = arccos(self.delta_d / (self.delta_d + Rbo)) / self.k
    phi = max(-phi_max, phi)
    phi = min(phi_max, phi)

    # compute the bore radius
    delta = self.delta_d / cos(phi * self.k)
    r = Rbo + self.delta_d - delta
    x = r * cos(2 * phi / self.N)
    y = r * sin(2 * phi / self.N)

    return x + 1j * y
