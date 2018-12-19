# -*- coding: utf-8 -*-
def translate(self, Zt):
    """Translate the Circle object

    Parameters
    ----------
    self : Circle
        An Circle object

    Zt : complex
        Complex value for translation


    Returns
    -------
    None

    Raises
    -------
    PointTranslateCircleError
        The point must be a complex number or int or float

    """
    if (
        not isinstance(Zt, complex)
        and not isinstance(Zt, int)
        and not isinstance(Zt, float)
    ):
        raise PointTranslateCircleError(
            "The point must be a complex number or int or float"
        )

    # check if the Circle is correct
    self.check()

    # Modification from the translation of Circle
    self.point_ref = self.point_ref + Zt
    self.center = self.center + Zt


class PointTranslateCircleError(Exception):
    """ """

    pass
