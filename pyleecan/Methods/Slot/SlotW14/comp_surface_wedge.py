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
    # Selection type Wedge
    if self.wedge_type == 0:
        return self.comp_surface_opening()

    if self.wedge_type == 1:
        H1 = self.get_H1()
        point_dict = self._comp_point_coordinate()
        Z7 = point_dict["Z7"]
        W1 = abs(Z7.imag) * 2

        return (W1 + self.W0) * H1 / 2
