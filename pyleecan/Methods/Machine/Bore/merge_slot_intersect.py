from numpy import pi, exp, angle

from ....Functions.Geometry.cut_lines_between_angle import cut_lines_between_angles
from ....Classes.Segment import Segment

DEBUG = False


def merge_slot_intersect(self, radius_desc_list, prop_dict, sym):
    """Merge the Bore shape with notches/slot on the bore/yoke
    Intersect method: cut lines of notch/slot to make the radius end match notch/slot begin
    technically reduice slot/notch height without changing yoke height

    Parameters
    ----------
    radius_desc_list : list
        List of dict to describe the bore/yoke radius (without bore shape, with notches)
    prop_dict : dict
        Property dictionary to apply on the radius lines (not on slot/notch)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    line_list : list
        List of lines needed to draw the radius
    """
    # Get all Radius lines (0 to 2*pi), i.e. the bore shape without notches
    bore_shape = self.get_bore_line()

    if DEBUG:
        _debug_plot(radius_desc_list, bore_shape, title="Original lines")

    # limit begin and end angles
    if sym != 1:
        if radius_desc_list[0]["label"] == "Radius":
            radius_desc_list[0]["begin_angle"] = 0
        if radius_desc_list[-1]["label"] == "Radius":
            radius_desc_list[-1]["end_angle"] = 2 * pi / sym

    # search intersection of each notch with bore shape -> cut notch
    for ii, desc_dict in enumerate(radius_desc_list):
        if desc_dict["label"] != "Radius":
            lines = [line for line in desc_dict["lines"]]
            # forward search for 1. cut
            found = False
            while lines and not found:
                for bore in bore_shape:
                    intersect = lines[0].intersect_obj(bore)
                    if intersect:
                        lines[0].split_point(intersect[0], is_begin=False)
                        found = True
                        break
                if not found:
                    lines.pop(0)

            # backward search for 2nd cut
            found = False
            while lines and not found:
                for bore in bore_shape:
                    intersect = lines[-1].intersect_obj(bore)
                    if intersect:
                        lines[-1].split_point(intersect[0], is_begin=True)
                        found = True
                        break
                if not found:
                    lines.pop(-1)

            desc_dict["lines"] = lines

    if DEBUG:
        _debug_plot(radius_desc_list, bore_shape, title="... after cutting notches")

    # fix radius_desc_list in case notches are cut out by bore shape completely
    # TODO print warning
    idx = [ii for ii, desc in enumerate(radius_desc_list) if not desc["lines"]]

    # correct previous and next segments begin and end angles first ...
    siz = len(radius_desc_list)
    for ii in idx:
        if sym != 1 and ii == 0:
            radius_desc_list[1]["begin_angle"] = 0
        elif sym != 1 and ii == (siz - 1):
            radius_desc_list[-2]["end_angle"] = 2 * pi / sym
        else:
            previous_segment = radius_desc_list[ii - 1]
            next_segment = radius_desc_list[(ii + 1) % siz]
            # begin and end of cut out notch on round bore shape
            begin = previous_segment["end_angle"] % (2 * pi)
            end = next_segment["begin_angle"] % (2 * pi)
            if begin <= end:
                ang = (begin + end) / 2
            else:  # zero crossing of angle
                ang = ((begin + end + 2 * pi) / 2) % (2 * pi)
            next_segment["begin_angle"] = ang
            previous_segment["end_angle"] = ang

    # ... then remove cut out notches
    for ii in idx[::-1]:
        radius_desc_list.pop(ii)

    # replace round bore segments by actual bore shape
    siz = len(radius_desc_list)
    for ii, desc_dict in enumerate(radius_desc_list):
        if desc_dict["label"] == "Radius":
            previous_segment = radius_desc_list[ii - 1]
            if previous_segment["label"] == "Radius":
                begin = desc_dict["begin_angle"]
            else:
                begin = angle(previous_segment["lines"][-1].get_end())

            next_segment = radius_desc_list[(ii + 1) % siz]
            if next_segment["label"] == "Radius":
                end = desc_dict["end_angle"]
            else:
                end = angle(next_segment["lines"][0].get_begin())

            desc_dict["lines"] = cut_lines_between_angles(bore_shape, begin, end)

    if DEBUG:
        _debug_plot(radius_desc_list, bore_shape, title="Merged (before sym. cutting)")

    # If notches are crossing sym lines => Cut
    if sym != 1:
        begin = 0
        end = 2 * pi / sym
        # Cut first desc (if needed)
        if radius_desc_list[0]["begin_angle"] < 0:
            lines = cut_lines_between_angles(radius_desc_list[0]["lines"], begin, end)
            radius_desc_list[0]["begin_angle"] = begin
            radius_desc_list[0]["lines"] = lines
        # Cut last desc (if needed)
        if radius_desc_list[-1]["end_angle"] > 2 * pi / sym:
            lines = cut_lines_between_angles(radius_desc_list[-1]["lines"], begin, end)
            radius_desc_list[-1]["end_angle"] = end
            radius_desc_list[-1]["lines"] = lines

    if DEBUG:
        _debug_plot(radius_desc_list, bore_shape, title="Merged completely")

    line_list = [line for desc_list in radius_desc_list for line in desc_list["lines"]]

    # Apply properties
    if prop_dict is not None:
        for line in line_list:
            if line.prop_dict is None:
                line.prop_dict = dict()
            line.prop_dict.update(prop_dict)

    return line_list


def _debug_plot(radius_desc_list, bore_shape=list(), title=""):
    """Helper function for debugging"""
    kwargs = dict(color="b", linewidth="1", linestyle="-")
    fig, ax = None, None
    for desc in radius_desc_list:
        for line in desc["lines"]:
            fig, ax = line.plot(fig=fig, ax=ax, **kwargs)

    kwargs = dict(color="gray", linewidth="1", linestyle="-.")
    for line in bore_shape:
        fig, ax = line.plot(fig=fig, ax=ax, **kwargs)

    ax.axis("equal")
    ax.set(title=title)
    fig.show()
