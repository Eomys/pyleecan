# -*- coding: utf-8 -*-
def translate(self, Zt):
    """Translate the Segment object

    Parameters
    ----------
    self : Segment
        An Segment object

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
        raise PointTranslateSegmentError(
            "The point must be a complex number or int or float"
        )

    # check if the Segment is correct
    self.check()

    # Modification from the translation of Segment
    self.begin = self.begin + Zt
    self.end = self.end + Zt


class PointTranslateSegmentError(Exception):
    """ """

    pass
