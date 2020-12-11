# -*- coding: utf-8 -*-

from numpy import arcsin
from ....Methods import ParentMissingError


def comp_angle_opening(self):
    """Compute the opening angle of the magnet at the lamination bore radius

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    alpha_mag: float
        Magnet opening angle [rad]

    """

    if self.parent is not None:
        Z1, _ = self.parent.get_point_bottom()
        return 2 * arcsin(self.Wmag / (2 * abs(Z1)))
    else:
        raise ParentMissingError(
            "Error: The magnet object is not inside a " + "slot object"
        )
