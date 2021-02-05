# -*- coding: utf-8 -*-
from numpy import exp
from ....Methods.Geometry.Arc3 import AngleRotationArc3Error


def rotate(self, angle):
    """Rotation of the Arc3 of angle

    Parameters
    ----------
    self : Arc3
        An Arc3 Object

    angle : float
        the angle of rotation [rad]


    Returns
    -------
    None
    """
    if not isinstance(angle, float) and not isinstance(angle, int):
        raise AngleRotationArc3Error("The angle must be a float or int ")

    # check if Arc3 is correct"
    self.check()

    # Modification from the rotation  of the object
    self.begin = self.begin * exp(1j * angle)
    self.end = self.end * exp(1j * angle)
