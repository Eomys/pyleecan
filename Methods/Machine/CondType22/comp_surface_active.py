# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType22
        A CondType22 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    return self.Sbar
