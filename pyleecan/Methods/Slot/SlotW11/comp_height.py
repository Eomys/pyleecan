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
    if self.is_cstt_tooth:
        # Compute W1 and W2 to match W3 tooth constraint
        self._comp_W()

    Rbo = self.get_Rbo()

    if self.is_outwards():
        point_dict = self._comp_point_coordinate()
        line_dict = dict()
        Z6 = point_dict["Z6"]
        Z7 = point_dict["Z7"]

        Ndisc = 200

        line_dict["6-7"] = Arc1(
            Z6, Z7, 1 * self.R1, is_trigo_direction=self.is_outwards()
        )
        surf = self.get_surface()

        point_list = surf.discretize(Ndisc)

        point_list = array(point_list)

        return max(abs(point_list)) - Rbo

    else:
        # Computation of the arc height
        alpha = self.comp_angle_opening() / 2
        Harc = float(Rbo * (1 - cos(alpha)))
        return self.H0 + self.get_H1() + self.H2 + Harc
