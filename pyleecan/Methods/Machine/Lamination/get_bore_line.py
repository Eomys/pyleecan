# -*- coding: utf-8 -*-
from numpy import pi, exp, linspace

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Methods import NotImplementedYetError


def get_bore_line(self, alpha1, alpha2, prop_dict=None, ignore_notches=False):
    """

    Parameters
    ----------
    self : Lamination
        a Lamination object
    alpha1 : float
        Starting angle [rad]
    alpha2 : float
        Ending angle [rad]
    prop_dict : dict
        Property dictionary to apply on the lines

    Returns
    -------
    bore_line : list
        list of bore line

    """
    delta = alpha2 - alpha1

    if delta == 0:
        return []

    elif delta > 2 * pi:
        raise NotImplementedYetError(
            "Only angle smaller/equal to 2*pi are implemented."
        )
    else:
        # ignore_notches = 1
        if not self.notch or ignore_notches:
            Rbo = self.get_Rbo()
            Z1 = Rbo * exp(1j * alpha1)
            if delta == 2 * pi:
                Z2 = Rbo * exp(1j * (alpha1 + delta / 2))
                line1 = Arc3(
                    begin=Z1, end=Z2, is_trigo_direction=True, prop_dict=prop_dict
                )
                line2 = Arc3(
                    begin=Z2, end=Z1, is_trigo_direction=True, prop_dict=prop_dict
                )
                return [line1, line2]
            else:
                Z2 = Rbo * exp(1j * alpha2)
                return [Arc1(begin=Z1, end=Z2, radius=Rbo, prop_dict=prop_dict)]
        else:
            # === intermediate solution ========================================
            # no check for intersection of different notches
            line_list = self.notch[0].build_geometry(
                alpha1, alpha2, prop_dict=prop_dict
            )
            # === later =======================================================
            """
            bore_line = self.get_bore_line(alpha1, alpha2, ignore_notches=True)
            for notch in notch_shape:
                notch_line = notch.build_geometry()
                bore_line = build_intersect_geometry(bore_line, notch_line,
                                            inwards=True)
            """

            return line_list
