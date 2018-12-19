# -*- coding: utf-8 -*-
def check(self):
    """assert the Circle is correct (the radius > 0)

    Parameters
    ----------
    self : Circle
        A Circle object

    Returns
    -------
    None

    Raises
    ------
    RadiusCircleError
        The radius of a circle must be >=  0

    """
    if self.radius < 0:
        raise RadiusCircleError("The radius of a circle must be >= 0")


class RadiusCircleError(Exception):
    """ """

    pass
