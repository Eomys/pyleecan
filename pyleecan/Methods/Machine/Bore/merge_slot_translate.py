from numpy import pi, exp, angle

from ....Functions.Geometry.cut_lines_between_angle import cut_lines_between_angles
from ....Classes.Segment import Segment

DEBUG = False


def merge_slot_translate(self, radius_desc_list, prop_dict, sym):
    """Merge the Bore shape with notches/slot on the bore/yoke
    Translate method: Translate lines of notch/slot to match the radius of the shape
    technically Keep the slot/notch height by reduicing the yoke height

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

    Rbo = self.parent.get_Rbo()

    if DEBUG:
        _debug_plot(radius_desc_list, bore_shape, title="Original lines")

    # limit begin and end angles
    if sym != 1:
        if radius_desc_list[0]["label"] == "Radius":
            radius_desc_list[0]["begin_angle"] = 0
        if radius_desc_list[-1]["label"] == "Radius":
            radius_desc_list[-1]["end_angle"] = 2 * pi / sym

    # search intersection of bore shape with mean opening angle of slots/notches ...
    # ... and translate notch to bore shape
    for ii, desc_dict in enumerate(radius_desc_list):
        if desc_dict["label"] != "Radius":
            lines = desc_dict["lines"]
            begin = desc_dict["begin_angle"] % (2 * pi)
            end = desc_dict["end_angle"] % (2 * pi)
            op = (begin + end) / 2
            if begin > end:
                op = ((begin + end + 2 * pi) / 2) % (2 * pi)
            R = 1 / 2 * abs(lines[0].get_begin() + lines[-1].get_end())
            Z = R * exp(1j * op)
            line = Segment(0, 2 * Rbo * exp(1j * op))  # be sure to cross bore shape
            found = False
            for bore in bore_shape:
                intersect = line.intersect_obj(bore)
                if intersect:
                    found = True
                    break
            if found:
                dZ = intersect[0] - Z
                for line in lines:
                    line.translate(dZ)

                # close gap between notch lines and round bore shape for next step
                line = Segment(lines[0].get_begin() - dZ, lines[0].get_begin())
                lines.insert(0, line)

                line = Segment(lines[-1].get_end(), lines[-1].get_end() - dZ)
                lines.append(line)
            else:
                self.get_logger().warning("Warning: Can't translate notch/slot.")

    if DEBUG:
        _debug_plot(radius_desc_list, bore_shape, title="translated lines (w/o gaps)")

    line_list = self.merge_slot_intersect(radius_desc_list, prop_dict, sym)

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
