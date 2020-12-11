# -*- coding: utf-8 -*-
def translate(self, Zt):
    """Translate the Arc2 object with

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Zt : complex
        Complex coordinates value for translation

    Returns
    -------
    None
    """
    if (
        not isinstance(Zt, complex)
        and not isinstance(Zt, int)
        and not isinstance(Zt, float)
    ):
        raise PointTranslateArc2Error(
            "The point must be a complex number or int or float"
        )

    # check if the Arc2 is correct
    self.check()

    # Modification from the translation of Arc2
    self.begin = self.begin + Zt
    self.center = self.center + Zt


class PointTranslateArc2Error(Exception):
    """ """

    pass
