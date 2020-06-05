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
    # check if the Trapeze is correct
    self.check()
    self.point_ref = self.point_ref * exp(1j * angle)
