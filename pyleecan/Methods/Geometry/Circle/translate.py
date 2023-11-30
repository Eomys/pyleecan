from ....Methods.Geometry.Circle import PointTranslateCircleError


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

    if Zt == 0:
        return  # Nothing to do

    # check if the Circle is correct
    self.check()

    # Modification from the translation of Circle
    if self.point_ref is not None:
        self.point_ref = self.point_ref + Zt
    self.center = self.center + Zt
