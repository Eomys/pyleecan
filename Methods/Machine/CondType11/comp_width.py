# -*- coding: utf-8 -*-


def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    W: float
        Width of the conductor [m]

    """

    return (2 * self.Wins_wire + self.Wwire) * self.Nwppc_tan
