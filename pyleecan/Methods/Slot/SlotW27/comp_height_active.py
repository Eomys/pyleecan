# -*- coding: utf-8 -*-


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H1 + self.H2
