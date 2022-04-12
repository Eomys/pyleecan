# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3


def get_bore_line(self, sym=1, prop_dict=None):
    """

    Parameters
    ----------
    self : Lamination
        a Lamination object
    prop_dict : dict
        Property dictionary to apply on the lines

    Returns
    -------
    bore_line : list
        list of bore line

    """
    if self.bore:
        # TODO: sym != 1
        bore_lines = self.bore.get_bore_line(prop_dict=prop_dict)
    else:
        bore_lines = list()
        Rbo = self.get_Rbo()
        if sym == 1:
            arc1 = Arc3(begin=Rbo, end=-Rbo, is_trigo_direction=True)
            arc2 = Arc3(begin=-Rbo, end=Rbo, is_trigo_direction=True)
            bore_lines.append(arc1)
            bore_lines.append(arc2)
        else:
            rot = exp(1j * 2 * pi / sym)
            arc = Arc1(begin=Rbo, end=Rbo * rot, radius=Rbo, is_trigo_direction=True)
            bore_lines.append(arc)

        if prop_dict is not None:
            for line in bore_lines:
                line.prop_dict = prop_dict

    return bore_lines
