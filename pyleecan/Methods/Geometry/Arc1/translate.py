from ....Methods.Geometry.Arc1 import PointTranslateArc1Error


def translate(self, Zt):
    """Translate the Arc1 object

    Parameters
    ----------
    self : Arc1
        An Arc1 object

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
        raise PointTranslateArc1Error(
            "The point must be a complex number or int or float"
        )

    # check if the Arc1 is correct
    self.check()

    # Modification from the translation of Arc1
    self.begin = self.begin + Zt
    self.end = self.end + Zt
