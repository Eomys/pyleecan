# -*- coding: utf-8 -*-


def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    W: float
        Width of the conductor [m]

    """

    if self.Wins_cond is None:
        if self.Nwppc == 1:
            Wins_wire = self.Wins_wire if self.Wins_wire is not None else 0
            width = self.Wwire + 2 * Wins_wire
        else:
            raise Exception("Conductor diameter not set")
    else:
        width = self.Wins_cond

    return width
