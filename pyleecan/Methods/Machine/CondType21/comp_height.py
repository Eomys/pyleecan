# -*- coding: utf-8 -*-


def comp_height(self):
    """Compute the height of the conductor

    Parameters
    ----------
    self : CondType21
        A CondType21 object

    Returns
    -------
    H: float
        Height of the conductor (with insulation) [m]

    """

    return self.Hbar + 2 * self.Wins
