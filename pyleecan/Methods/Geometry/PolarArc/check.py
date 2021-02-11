from ....Methods.Geometry.PolarArc import *


def check(self):
    """check if the PolarArc object is correct

    Parameters
    ----------
    self : PolarArc
        a PolarArc Object

    Returns
    -------
    None

    Raises
    ------
    AnglePolarArcError
        The angle of a polar arc must be different to 0

    """
    if self.angle == 0:
        raise AnglePolarArcError("The angle of a polar arc must be different to 0")
