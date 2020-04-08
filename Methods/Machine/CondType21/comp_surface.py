# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the surface of the conductor

    Parameters
    ----------
    self : CondType21
        A CondType21 object

    Returns
    -------
    S: float
        Surface of the conductor (with insulation) [m**2]

    """

    S = self.comp_height() * self.comp_width()

    return S
