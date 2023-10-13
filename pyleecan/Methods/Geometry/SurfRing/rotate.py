# -*- coding: utf-8 -*-

from numpy import exp


def rotate(self, angle):
    """Rotate the surface

    Parameters
    ----------
    self : SurfRing
        A SurfRing object

    angle : float
        the angle of rotation [rad]

    Returns
    -------
    None
    """
    if angle == 0:
        return  # Nothing to do
    # Check if the Surface is correct
    self.check()
    # rotation of every line in the Surface
    self.out_surf.rotate(angle)
    self.in_surf.rotate(angle)
    if self.point_ref is not None:
        self.point_ref = self.point_ref * exp(1j * angle)
