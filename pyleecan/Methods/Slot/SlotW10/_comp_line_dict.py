from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

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
    Z9 = point_dict["Z9"]
    Z10 = point_dict["Z10"]

    # Creation of curve
    line_dict = dict()
    if self.H0 > 0:
        line_dict["1-2"] = Segment(Z1, Z2)
    else:
        line_dict["1-2"] = None

    if self.H1 > 0 and self.W1 >= self.W0:
        line_dict["2-3"] = Segment(Z2, Z3)
    else:
        line_dict["2-3"] = None

    if self.W1 > self.W0:
        line_dict["3-4"] = Segment(Z3, Z4)
    else:
        line_dict["3-4"] = None

    line_dict["4-5"] = Segment(Z4, Z5)

    if self.W2 > 0:
        line_dict["5-6"] = Segment(Z5, Z6)
    else:
        line_dict["5-6"] = None

    line_dict["6-7"] = Segment(Z6, Z7)

    if self.W1 > self.W0:
        line_dict["7-8"] = Segment(Z7, Z8)
    else:
        line_dict["7-8"] = None

    if self.H1 > 0 and self.W1 >= self.W0:
        line_dict["8-9"] = Segment(Z8, Z9)
    else:
        line_dict["8-9"] = None

    if self.H0 > 0:
        line_dict["9-10"] = Segment(Z9, Z10)
    else:
        line_dict["9-10"] = None

    # Closing Arc (Rbo)
    line_dict["10-1"] = Arc1(Z10, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Closing Active part
    line_dict["4-7"] = Segment(Z4, Z7)
    line_dict["7-4"] = Segment(Z7, Z4)
    return line_dict
