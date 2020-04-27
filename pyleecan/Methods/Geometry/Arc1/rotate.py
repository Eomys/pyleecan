# -*- coding: utf-8 -*-
from numpy import exp


def rotate(self, angle):
    """Rotation of the Arc1 of <angle> rad with 0 as the center

    Parameters
    ----------
    self : Arc1
        An Arc1 Object

    angle : float
        the angle of rotation [rad]

    Returns
    -------
    None
    """
    if not isinstance(angle, float) and not isinstance(angle, int):
        raise AngleRotationArc1Error("The angle must be a float or int ")

    # check if Arc1 is correct"
    self.check()

    # Modification from the rotation  of the object
    self.begin = self.begin * exp(1j * angle)
    self.end = self.end * exp(1j * angle)


class AngleRotationArc1Error(Exception):
    """ """

    pass
