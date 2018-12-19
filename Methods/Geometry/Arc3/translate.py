# -*- coding: utf-8 -*-
def translate(self, Zt):
    """Translate the Arc3 object with

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Zt : complex
        Complex value for translation


    Returns
    -------
    None

    """
    if (
        not isinstance(Zt, complex)
        and not isinstance(Zt, int)
        and not isinstance(Zt, float)
    ):
        raise PointTranslateArc3Error(
            "The point must be a complex number or int or float"
        )

    # check if the Arc3 is correct
    self.check()

    # Modification from the translation of Arc3
    self.begin = self.begin + Zt
    self.end = self.end + Zt


class PointTranslateArc3Error(Exception):
    """ """

    pass
