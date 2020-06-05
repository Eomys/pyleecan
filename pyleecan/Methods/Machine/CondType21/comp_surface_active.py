# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType21
        A CondType21 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    Sact = self.Hbar * self.Wbar

    return Sact
