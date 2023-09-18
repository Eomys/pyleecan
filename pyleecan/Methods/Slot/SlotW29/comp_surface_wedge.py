# -*- coding: utf-8 -*-

from numpy import arcsin, cos, pi, sin


def comp_surface_wedge(self):
    """Compute the Slot wedge surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    S: float
        Slot wedge surface [m**2]

    """
    if hasattr(self, "wedge_type"):
        wedge_type = self.wedge_type
    else:
        wedge_type = 0

    # Selection type Wedge
    if wedge_type == 0:
        return self.comp_surface_opening()

    if wedge_type == 1:
        return (self.W1) * self.H1
