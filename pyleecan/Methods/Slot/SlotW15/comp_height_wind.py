# -*- coding: utf-8 -*-


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """
    return self.H1 + self.H2
