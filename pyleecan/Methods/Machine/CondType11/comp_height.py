# -*- coding: utf-8 -*-


def comp_height(self):
    """Compute the height of the conductor

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    H: float
        Height of the conductor [m]

    """

    return (2 * self.Wins_wire + self.Hwire) * self.Nwppc_rad
