# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3


def build_radius_lines(self, is_bore, sym=1, is_reversed=False, prop_dict=None):
    """Create the lines need to draw the selected radius of the Lamination

    Parameters
    ----------
    self : Lamination
        a Lamination object
    is_bore : bool
        True generate lines of bore, else yoke
    is_reversed : bool
        True to return the lines in clockwise oder (reverse begin and end), False trigo
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    prop_dict : dict
        Property dictionary to apply on the radius lines (not on slot/notch)

    Returns
    -------
    radius_lines : list
        list of bore/yoke lines
    """
    # For readibitlity
    is_notch = self.has_notch(is_bore=is_bore)
    is_slot = self.has_slot(is_bore=is_bore)
    if is_bore:
        R = self.get_Rbo()
        is_shape = self.bore is not None
        shape_obj = self.bore
    else:
        R = self.get_Ryoke()
        is_shape = self.yoke is not None
        shape_obj = self.yoke

    if not is_shape:  # Arc or Slot/Notch only
        radius_desc_list = self.build_radius_desc(is_bore=is_bore, sym=sym)
        # Cut lines for sym
        if sym != 1:
            # Cut first desc (if needed)
            if radius_desc_list[0]["begin_angle"] < 0:
                lines = list()
                for line in radius_desc_list[0]["lines"]:
                    top_split_list, _ = line.split_line(0, 1)
                    lines.extend(top_split_list)
                radius_desc_list[0]["begin_angle"] = 0
                radius_desc_list[0]["lines"] = lines
            # Cut last desc (if needed)
            if radius_desc_list[-1]["end_angle"] > 2 * pi / sym:
                lines = list()
                for line in radius_desc_list[-1]["lines"]:
                    _, bot_split_list = line.split_line(0, exp(1j * 2 * pi / sym))
                    lines.extend(bot_split_list)
                radius_desc_list[-1]["end_angle"] = 2 * pi / sym
                radius_desc_list[-1]["lines"] = lines
        # Extract the line list
        radius_lines = list()
        for desc_dict in radius_desc_list:
            # Apply prop_dict on Radius only
            if prop_dict is not None and desc_dict["label"] == "Radius":
                for line in desc_dict["lines"]:
                    if line.prop_dict is None:
                        line.prop_dict = dict()
                    line.prop_dict.update(prop_dict)
            radius_lines.extend(desc_dict["lines"])

    elif is_shape and not is_notch and not is_slot:
        # Bore/Yoke shape only
        radius_lines = shape_obj.get_bore_line()
        if sym > 1:  # Ox cut
            lines = list()
            for line in radius_lines:
                top_split_list, _ = line.split_line(0, 1)
                lines.extend(top_split_list)
            radius_lines = lines
        if sym > 2:
            lines = list()
            for line in radius_lines:
                _, bot_split_list = line.split_line(0, exp(1j * 2 * pi / sym))
                lines.extend(bot_split_list)
            radius_lines = lines
        # Only radius lines => prop_dict on all lines
        if prop_dict is not None:
            for line in radius_lines:
                if line.prop_dict is None:
                    line.prop_dict = dict()
                line.prop_dict.update(prop_dict)
    else:  # Bore/Yoke shape to merge with slot/notch
        radius_desc_list = self.build_radius_desc(is_bore=is_bore, sym=sym)
        radius_lines = shape_obj.merge_slot(
            radius_desc_list, prop_dict=prop_dict, sym=sym
        )

    # Reverse the lines
    if is_reversed:
        radius_lines = radius_lines[::-1]
        for line in radius_lines:
            line.reverse()

    return radius_lines
