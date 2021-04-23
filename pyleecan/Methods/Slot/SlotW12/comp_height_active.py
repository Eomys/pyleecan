# -*- coding: utf-8 -*-


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H1 + self.R2
