from numpy import pi, exp, angle

from ....Functions.Geometry.cut_lines_between_angle import cut_lines_between_angles
from ....Classes.Segment import Segment


def merge_slot_intersect(self, radius_desc_list, prop_dict, sym):
    """Merge the Bore shape with notches/slot on the bore/yoke
    Intersect method: cut lines of notch/slot to make the radius end match notch/slot begin
    technically reduice slot/notch height without changing yoke height

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
            for line in desc_dict["lines"]:
                if line.prop_dict is None:
                    line.prop_dict = dict()
                line.prop_dict.update(prop_dict)
            line_list.extend(desc_dict["lines"])
        else:  # Intersect and add slot/notch lines
            # Define First cutting line
            rad_line = radius_desc_list[ii - 1]["lines"][-1]
            # Find first line to intersect with cutting line
            for jj in range(len(desc_dict["lines"])):
                inter_list = desc_dict["lines"][jj].intersect_obj(
                    rad_line, is_on_line=True
                )
                if len(inter_list) > 0:
                    break
            if jj < len(desc_dict["lines"]):
                # Slot/notch was cut => Replace lines by cut ones
                desc_dict["lines"] = desc_dict["lines"][jj:]  # Keep all lines after cut
                # Update lines to start/end at cutting point
                desc_dict["lines"][0].split_point(inter_list[0], is_begin=False)
                rad_line.split_point(inter_list[0], is_begin=True)
            else:  # The slot is above the shape => Use shape lines
                desc_dict["lines"] = cut_lines_between_angles(
                    radius_lines, desc_dict["begin_angle"], desc_dict["end_angle"]
                )
                # Add prop_dict on all the Radius Lines
                for line in desc_dict["lines"]:
                    if line.prop_dict is None:
                        line.prop_dict = dict()
                    line.prop_dict.update(prop_dict)
                line_list.extend(desc_dict["lines"])
                continue  # No need to cut the other side
            # Second cut
            if ii != len(radius_desc_list) - 1:
                rad_line = radius_desc_list[ii + 1]["lines"][0]
            else:
                rad_line = radius_desc_list[0]["lines"][0]
            for jj in range(len(desc_dict["lines"])):
                inter_list = desc_dict["lines"][-(jj + 1)].intersect_obj(
                    rad_line, is_on_line=True
                )
                if len(inter_list) > 0:
                    break
            if jj < len(desc_dict["lines"]):
                # Slot/notch was cut => Replace lines by cut ones
                if jj != 0:  # Keep all the lines if last line is cut
                    desc_dict["lines"] = desc_dict["lines"][
                        :-jj
                    ]  # Keep all lines before cut
                # Update lines to start/end at cutting point
                desc_dict["lines"][-1].split_point(inter_list[0], is_begin=True)
                rad_line.split_point(inter_list[0], is_begin=False)
            line_list.extend(desc_dict["lines"])
    return line_list
