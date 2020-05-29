# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Jan 09 16:49:24 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from pyleecan.Classes.HoleMag import HoleMag
from pyleecan.Functions.matlab.gen_m_code import edit_line_if_not_None


def _to_m_file(self, lines, is_stator):
    """Convert a Slot object into a m file

    Parameters
    ----------
    self :
        A Slot object
    lines :
        Dictionary [Matlab name] = comment
    is_stator :
        Adapt the code to the Lamination type

    Returns
    -------
    list
        lines: needed to export the lamination

    """

    lines = HoleMag._to_m_file(self, lines, is_stator)

    lines = edit_line_if_not_None("Input.Geometry.Wmag", self.W4, lines)
    lines = edit_line_if_not_None("Input.Geometry.Hmag", self.H2, lines)
    lines = edit_line_if_not_None("Input.Geometry.type_shape_magnet", 20, lines)

    return lines
