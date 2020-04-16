# -*- coding: utf-8 -*-


def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType21
        A CondType21 object

    Returns
    -------
    W: float
        Width of the conductor (with insulation) [m]

    """

    return self.Wbar + 2 * self.Wins
