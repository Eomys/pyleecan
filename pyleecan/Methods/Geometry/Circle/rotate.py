# -*- coding: utf-8 -*-
from numpy import exp
from ....Methods.Geometry.Circle import AngleRotationCircleError


def rotate(self, angle):
    """Rotation of the Circle of angle

    Parameters
    ----------
    self : Circle
        An Circle Object

    angle : float
        the angle of rotation [rad]

    Returns
    -------
    None

    Raises
    -------
    AngleRotationCircleError
        The angle must be a float or int
    """
    if not isinstance(angle, float) and not isinstance(angle, int):
        raise AngleRotationCircleError("The angle must be a float or int ")

    if angle == 0:
        return  # Nothing to do
    # check if Circle is correct"
    self.check()

    # Modification of the object from the rotation
    self.center = self.center * exp(1j * angle)
    if self.point_ref is not None:
        self.point_ref = self.point_ref * exp(1j * angle)
