# -*- coding: utf-8 -*-
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.SurfLine import SurfLine


def get_surface(self):
    """Returns the surface delimiting the slot

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    surface: SurfLine
        A SurfLine object representing the slot

    """
    Rbo = self.get_Rbo()
    curve_list = self.build_geometry()
    Zbegin = curve_list[-1].get_end()
    Zend = curve_list[0].get_begin()
    curve_list.append(Arc1(Zbegin, Zend, -Rbo, is_trigo_direction=False))

    return SurfLine(line_list=curve_list, label="Slot")
