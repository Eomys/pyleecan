# -*- coding: utf-8 -*-
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import DRAW_PROP_LAB


def get_surface(self, is_simplified=False):
    """Returns the surface delimiting the slot

    Parameters
    ----------
    self : Slot
        A Slot object
    is_simplified : bool
        True to remove overlapping lines

    Returns
    -------
    surface: SurfLine
        A SurfLine object representing the slot

    """
    Rbo = self.get_Rbo()
    curve_list = self.build_geometry()

    # Remove line overlapping with bore/yoke lines
    if is_simplified:
        for line in curve_list:
            if line.prop_dict is None:
                line.prop_dict = dict()
            line.prop_dict[DRAW_PROP_LAB] = False

    # Add closing Arc
    Zbegin = curve_list[-1].get_end()
    Zend = curve_list[0].get_begin()
    curve_list.append(Arc1(Zbegin, Zend, -Rbo, is_trigo_direction=False))

    surf = SurfLine(line_list=curve_list, label="Slot")
    surf.comp_point_ref(is_set=True)
    return surf
