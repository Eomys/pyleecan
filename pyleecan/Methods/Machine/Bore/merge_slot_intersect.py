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

    # fig, ax = None, None
    # for desc in radius_desc_list:
    #     fig, ax = _plot_lines(desc['lines'], fig=fig, ax=ax, color="b")
    # fig, ax = _plot_lines(radius_lines, fig=fig, ax=ax, color="gray")
    # ax.axis('equal')
    # fig.show()


    # Update begin and end angle if Radius (next step already cut lines)
    if sym != 1 and radius_desc_list[0]["label"] == "Radius":
        radius_desc_list[0]["begin_angle"] = 0
    if sym != 1 and radius_desc_list[-1]["label"] == "Radius":
        radius_desc_list[-1]["end_angle"] = 2 * pi / sym

    # Replace Arc radius from desc by lines from shape
    for ii, desc_dict in enumerate(radius_desc_list):
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
        else:  # Intersect and add slot/notch lines
            # fig, ax = _plot_lines(desc_dict['lines'], is_show=True)
            # Define First cutting line
            # rad_line = radius_desc_list[ii - 1]["lines"][-1]
            op = desc_dict["end_angle"] - desc_dict["begin_angle"]
            if not (ii == 0 and sym != 1):  # No first cut for first notch on Ox
                rad_line_list = cut_lines_between_angles(
                    radius_lines,
                    desc_dict["begin_angle"] - op / 4,
                    desc_dict["begin_angle"] + op / 4,
                )
                # Find first intersection between any line in rad_line_list 
                # and any line in desc_dict["lines"]
                for cutting_line in rad_line_list[::-1]:
                    for jj, line in enumerate(desc_dict["lines"]):
                        inter_list = line.intersect_obj(cutting_line, is_on_line=True)
                        if inter_list:
                            break  
                    if inter_list:
                        break

                # fig, ax = _plot_lines(desc_dict['lines'], is_show=False)
                # fig, ax = _plot_lines([rad_line_list[-1]], color="r", fig=fig, ax=ax, is_show=True)
                # fig, ax = _plot_lines([cutting_line], color="b", fig=fig, ax=ax, is_show=False)
                # fig, ax = _plot_lines(line_list, color="g", linestyle="-.", fig=fig, ax=ax, is_show=True)

                if inter_list:
                    # slot/notch was cut => replace slot/notch lines by cut ones, i.e.
                    # keep all lines after the cut and update to start at cutting point
                    desc_dict["lines"] = desc_dict["lines"][jj:]  
                    desc_dict["lines"][0].split_point(inter_list[0], is_begin=False)
                    if len(line_list) == 0:  # Slot/notch on Ox
                        radius_desc_list[-1]["lines"][-1].split_point(
                            inter_list[0], is_begin=True
                        )
                    else:
                        line_list[-1].split_point(inter_list[0], is_begin=True)
                else:  # the slot is above the bore shape => use bore shape lines
                    desc_dict["lines"] = cut_lines_between_angles(
                        radius_lines, desc_dict["begin_angle"], desc_dict["end_angle"]
                    )
                    # Add prop_dict on all the Radius Lines
                    if prop_dict is not None:
                        for line in desc_dict["lines"]:
                            if line.prop_dict is None:
                                line.prop_dict = dict()
                            line.prop_dict.update(prop_dict)
                    line_list.extend(desc_dict["lines"])
                    # fig, ax = _plot_lines(radius_lines)
                    # fig, ax = _plot_lines(desc_dict["lines"], fig=fig, ax=ax, color="b")
                    # fig, ax = _plot_lines([rad_line_list[-1]], fig=fig, ax=ax, color="r")
                    # fig, ax = _plot_point(rad_line_list[-1].get_begin(), fig=fig, ax=ax, color="r", marker=".")
                    # fig, ax = _plot_point(rad_line_list[-1].get_end(), fig=fig, ax=ax, color="r", marker=".", is_show=True)
                    continue  # No need to cut the other side

            # Second cut
            if not (ii == len(radius_desc_list) - 1 and sym != 1):
                # No second cut for notch on sym line
                rad_line_list = cut_lines_between_angles(
                    radius_lines,
                    desc_dict["end_angle"] - op / 4,
                    desc_dict["end_angle"] + op / 4,
                )

                for cutting_line in rad_line_list:
                    for jj, line in enumerate(desc_dict["lines"][::-1]):
                        inter_list = line.intersect_obj(cutting_line, is_on_line=True)
                        if inter_list:
                            break  
                    if inter_list:
                        break

                if inter_list:
                    # Slot/notch was cut => Replace lines by cut ones
                    if jj != 0: # Keep all the lines if last line is cut
                        # keep all lines before cut
                        desc_dict["lines"] = desc_dict["lines"][:-jj]  
                    # update lines to end at cutting point
                    desc_dict["lines"][-1].split_point(inter_list[0], is_begin=True)
                    radius_desc_list[ii + 1]["lines"][0].split_point(
                        inter_list[0], is_begin=False
                    )
            # Add slot/notch lines to final list
            line_list.extend(desc_dict["lines"])
    return line_list


def _plot_lines(
        lines, color="k", linestyle="-", linewidth=1, fig=None, ax=None, is_show=False
        ):
    
    # fig, ax = None, None
    for line in lines:
        fig, ax = line.plot(
            fig=fig, ax=ax, color=color, linewidth=linewidth, linestyle=linestyle
            )

    if is_show:
        ax.axis('equal')
        fig.show()

    return fig, ax

def _plot_point(
        point, color="k", marker="o", markersize=10, fig=None, ax=None, is_show=False
        ):
    
    ax.plot(point.real, point.imag, marker=marker, markersize=markersize, color=color)

    if is_show:
        ax.axis('equal')
        fig.show()

    return fig, ax
