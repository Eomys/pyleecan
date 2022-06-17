# -*- coding: utf-8 -*-
from numpy import exp
from ....Methods.Geometry.Segment import AngleRotationSegmentError


def rotate(self, angle):
    """Rotation of the Segment of angle

    Parameters
    ----------
    self : Segment
        An Segment Object

    angle : float
        the angle of rotation [rad]

    Returns
    -------
    None

    """
    if not isinstance(angle, float) and not isinstance(angle, int):
        raise AngleRotationSegmentError("The angle must be a float or int ")

    # check if Segment is correct"
    self.check()

    # Modification from the rotation of the object
    self.begin = self.begin * exp(1j * angle)
    self.end = self.end * exp(1j * angle)
