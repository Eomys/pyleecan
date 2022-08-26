from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    curve_list: list
        A list of 10 Segment

    """

    line_dict = self._comp_line_dict()

    # Creation of curve
    curve_list = [
        line_dict["1-2"],
        line_dict["2-3"],
        line_dict["3-4"],
        line_dict["4-5"],
        line_dict["5-6"],
        line_dict["6-7"],
        line_dict["7-8"],
        line_dict["8-9"],
        line_dict["9-10"],
    ]
    return [line for line in curve_list if line is not None]
