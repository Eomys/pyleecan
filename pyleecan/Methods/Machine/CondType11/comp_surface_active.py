# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    Sact = self.Hwire * self.Wwire * self.Nwppc_tan * self.Nwppc_rad

    return Sact
