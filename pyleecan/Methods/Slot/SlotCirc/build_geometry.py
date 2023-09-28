from numpy import exp

from ....Classes.Arc1 import Arc1


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    curve_list: list
        A list of one Arc
    """

    line_dict = self._comp_line_dict()

    curve_list = [
        line_dict["1-M"],
        line_dict["M-2"],
    ]
    return [line for line in curve_list if line is not None]
