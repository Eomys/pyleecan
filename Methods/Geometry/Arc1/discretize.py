# -*- coding: utf-8 -*-

from numpy import angle as np_angle, exp, linspace

from pyleecan.Methods.Machine import ARC_NPOINT_D


def discretize(self, nb_point=ARC_NPOINT_D):
    """Return the discretize version of the Arc.
    Begin and end are always returned

    Parameters
    ----------
    self : Arc1
        The Arc1 object to discretize
    nb_point :
        Number of points to add to discretize the arc (Default value = ARC_NPOINT_D)

    Returns
    -------
    list_point: list
        list of complex coordinate of the points

    Raises
    ------
    NbPointArc1DError
        nb_point must be an integer >=0
    """

    # Check that the Arc is correct
    self.check()
    if not isinstance(nb_point, int):
        raise NbPointArc1DError("discretize : nb_point must be an integer")
    if nb_point < 0:
        raise NbPointArc1DError("nb_point must be >=0")

    # We use the complex representation of the point
    z1 = self.begin
    z2 = self.end
    zc = self.get_center()

    # Geometric transformation : center is the origin, angle(begin) = 0
    Zstart = (z1 - zc) * exp(-1j * np_angle(z1 - zc))
    Zend = (z2 - zc) * exp(-1j * np_angle(z1 - zc))

    # Generation of the point by rotation
    if self.is_trigo_direction:
        sign = 1
    else:
        sign = -1
    t = linspace(0, self.get_angle(), nb_point + 2)
    list_point = Zstart * exp(1j * t)

    # Geometric transformation : return to the main axis
    list_point = list_point * exp(1j * np_angle(z1 - zc)) + zc

    return list_point


class NbPointArc1DError(Exception):
    """ """

    pass
