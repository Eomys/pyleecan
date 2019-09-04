# -*- coding: utf-8 -*-
"""@package get_surface
@date Created on juil. 02 11:03 2018
@author franco_i
"""
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Methods import ParentMissingError
from numpy import exp, pi


def get_surface_tooth(self):
    """Returns the surface delimiting the tooth (including yoke part)

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    surface: SurfLine
        A SurfLine object representing the slot

    """

    if self.parent is not None:
        Ryoke = self.parent.get_Ryoke()
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")

    curve_list = list()
    # tooth lines
    top_list = self.build_geometry_half_tooth(is_top=True)
    bot_list = self.build_geometry_half_tooth(is_top=False)
    # Yoke lines
    Z1 = Ryoke * exp(1j * pi / self.Zs)
    Z2 = Ryoke * exp(-1j * pi / self.Zs)
    curve_list.append(Segment(top_list[-1].get_end(), Z1, label="Tooth_Yoke_Side"))
    if Ryoke > 0:
        curve_list.append(Arc1(Z1, Z2, -Ryoke, label="Tooth_Yoke_Arc"))
    curve_list.append(Segment(Z2, bot_list[0].get_begin(), label="Tooth_Yoke_Side"))
    # Second half of the tooth
    curve_list.extend(bot_list)
    curve_list.extend(top_list)

    return SurfLine(line_list=curve_list, label="Tooth")
