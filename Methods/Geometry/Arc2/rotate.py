# -*- coding: utf-8 -*-
from numpy import exp


def rotate(self, angle):
    """Rotation of the Arc2 of angle

    Parameters
    ----------
    self : Arc2
        An Arc2 Object

    angle : float
        the angle of rotation [rad]

    Returns
    -------
    None
    """
    if not isinstance(angle, float) and not isinstance(angle, int):
        raise AngleRotationArc2Error("The angle must be a float or int")

    # check if Arc2 is correct"
    self.check()

    # Modification from the rotation  of the object
    self.begin = self.begin * exp(1j * angle)
    self.center = self.center * exp(1j * angle)


class AngleRotationArc2Error(Exception):
    """ """

    pass
