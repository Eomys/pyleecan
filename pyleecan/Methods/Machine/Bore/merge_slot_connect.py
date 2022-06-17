from numpy import pi, exp

from ....Functions.Geometry.cut_lines_between_angle import cut_lines_between_angles
from ....Classes.Segment import Segment


def merge_slot_connect(self, radius_desc_list, prop_dict, sym):
    """Merge the Bore shape with notches/slot on the bore/yoke
    Connect method: Add lines between radius and notch/slot
    (To use when the radius shape have circular part matchine the radius
    or when radius lines are bellow normal radius)

    Parameters
    ----------
    radius_desc_list : list
        List of dict to describe the bore/yoke radius
    prop_dict : dict
        Property dictionary to apply on the radius lines (not on slot/notch)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    line_list : list
        List of lines needed to draw the radius
    """

    # Get all Radius lines (0 to 2*pi)
    radius_lines = self.get_bore_line()

    # Update begin and end angle if Radius (next step already cut lines)
    if sym != 1 and radius_desc_list[0]["label"] == "Radius":
        radius_desc_list[0]["begin_angle"] = 0
    if sym != 1 and radius_desc_list[-1]["label"] == "Radius":
        radius_desc_list[-1]["end_angle"] = 2 * pi / sym

    # Replace Arc radius from desc by lines from shape
    for desc_dict in radius_desc_list:
        if desc_dict["label"] == "Radius":
            desc_dict["lines"] = cut_lines_between_angles(
                radius_lines, desc_dict["begin_angle"], desc_dict["end_angle"]
            )

    # If slot/notch are coliding with sym lines => Cut
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

    # Apply merge strategy on slot/notch
    line_list = list()
    for ii, desc_dict in enumerate(radius_desc_list):
        if desc_dict["label"] == "Radius":
            # Add prop_dict on all the Radius Lines
            if prop_dict is not None:
                for line in desc_dict["lines"]:
                    if line.prop_dict is None:
                        line.prop_dict = dict()
                    line.prop_dict.update(prop_dict)
            line_list.extend(desc_dict["lines"])
        else:  # Connect and add notch lines
            if len(line_list) > 0:
                # Connect Radius to slot/notch by Segment (if needed)
                if (
                    abs(line_list[-1].get_end() - desc_dict["lines"][0].get_begin())
                    > 1e-6
                ):
                    line_list.append(
                        Segment(
                            line_list[-1].get_end(), desc_dict["lines"][0].get_begin()
                        )
                    )
            line_list.extend(desc_dict["lines"])
            # Connect slot/notch to next radius
            if (
                abs(
                    radius_desc_list[ii + 1]["lines"][0].get_begin()
                    - desc_dict["lines"][-1].get_end()
                )
                > 1e-6
            ):
                line_list.append(
                    Segment(
                        desc_dict["lines"][-1].get_end(),
                        radius_desc_list[ii + 1]["lines"][0].get_begin(),
                    )
                )
    return line_list
