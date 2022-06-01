from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    curve_list: list
        A list of 2 Segment and 1 Arc

    """

    [Z1, Z2, Z3, Z4] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.W1 > 0:
        curve_list.append(Arc1(Z2, Z3, abs(Z3)))
    curve_list.append(Segment(Z3, Z4))

    return curve_list
