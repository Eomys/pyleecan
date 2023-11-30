# -*-- coding: utf-8 -*
from numpy import exp


def rotate(self, angle):
    """Rotate the surface

    Parameters
    ----------
    self : Trapeze
        a Trapeze Object

    angle : float
        angle for rotation [rad]


    Returns
    -------
    None
    """
    if angle == 0:
        return  # Nothing to do
    # check if the Trapeze is correct
    self.check()
    self.point_ref = self.point_ref * exp(1j * angle)
