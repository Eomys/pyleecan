# -*-- coding: utf-8 -*
from numpy import exp


def rotate(self, angle):
    """Do the rotation of the PolarArc

    Parameters
    ----------
    self : PolarArc
        a PolarArc
    angle : float
        the angle for rotation [rad]

    Returns
    -------
    None
    """
    if angle == 0:
        return  # Nothing to do
    # check if the PolarArc is correct
    self.check()
    self.point_ref = self.point_ref * exp(1j * angle)
