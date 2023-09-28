from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    line_dict: dict
        Dictionnary of the slot lines (key: line name, value: line object)
    """

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]

    # Creation of curve
    line_dict = dict()
    if self.H0 > 0:
        line_dict["1-2"] = Segment(Z1, Z2)
    else:
        line_dict["1-2"] = None
    line_dict["2-3"] = Segment(Z2, Z3)
    line_dict["3-4"] = Segment(Z3, Z4)
    line_dict["4-5"] = Arc1(Z4, Z5, abs(Z5))
    line_dict["5-6"] = Segment(Z5, Z6)
    line_dict["6-7"] = Segment(Z6, Z7)
    if self.H0 > 0:
        line_dict["7-8"] = Segment(Z7, Z8)
    else:
        line_dict["7-8"] = None

    # Closing Arc (Rbo)
    line_dict["8-1"] = Arc1(Z8, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Closing Active part
    line_dict["3-6"] = Segment(Z3, Z6)
    line_dict["6-3"] = Segment(Z6, Z3)
    line_dict["7-2"] = Segment(Z7, Z2)

    return line_dict
