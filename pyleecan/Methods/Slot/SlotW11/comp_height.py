# -*- coding: utf-8 -*-

from numpy import cos, exp, arcsin, array
from ....Classes.Arc1 import Arc1


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    if self.is_cstt_tooth and (self.W1 is None or self.W2 is None):
        # Compute W1 and W2 to match W3 tooth constraint
        self._comp_W()

    Rbo = self.get_Rbo()

    if self.is_outwards():
        if self.R1 * 2 == self.W2:
            # Computation of the arc height
            alpha = self.comp_angle_opening() / 2
            Harc = float(Rbo * (1 - cos(alpha)))
            return self.H0 + self.get_H1() + self.H2 - Harc

        else:
            line_dict = self._comp_line_dict()
            Arc = line_dict["6-7"]
            Ndisc = 200
            point_list = Arc.discretize(Ndisc)
            point_list = array(point_list)
            return max(abs(point_list)) - Rbo

    else:
        # Computation of the arc height
        alpha = self.comp_angle_opening() / 2
        Harc = float(Rbo * (1 - cos(alpha)))
        return self.H0 + self.get_H1() + self.H2 + Harc
