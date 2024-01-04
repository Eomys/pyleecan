from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object

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

    Zw1 = point_dict["Zw1"]
    Zw2 = point_dict["Zw2"]

    Zw1s = point_dict["Zw1s"]
    Zw2s = point_dict["Zw2s"]

    # Creation of curve
    line_dict = dict()
    line_dict["1-2"] = Segment(Z1, Z2)
    line_dict["2-3"] = Segment(Z2, Z3)
    line_dict["3-4"] = Segment(Z3, Z4)
    line_dict["4-5"] = Segment(Z4, Z5)
    line_dict["5-6"] = Segment(Z5, Z6)
    line_dict["6-7"] = Segment(Z6, Z7)
    line_dict["7-8"] = Segment(Z7, Z8)

    # Winding lines
    line_dict["w1-2"] = Segment(Zw1, Z2)
    line_dict["2-w1"] = Segment(Z2, Zw1)
    line_dict["4-w2"] = Segment(Z4, Zw2)
    line_dict["w2-w1"] = Segment(Zw2, Zw1)
    line_dict["w1-w2"] = Segment(Zw1, Zw2)

    line_dict["w2s-5"] = Segment(Zw2s, Z5)
    line_dict["7-w1s"] = Segment(Z7, Zw1s)
    line_dict["w1s-w2s"] = Segment(Zw1s, Zw2s)

    line_dict["w1s-7"] = Segment(Zw1s, Z7)

    line_dict["w2s-w1s"] = Segment(Zw2s, Zw1s)
    line_dict["w2-w2s"] = Segment(Zw2, Zw2s)

    line_dict["7-2"] = Segment(Z7, Z2)
    line_dict["2-7"] = Segment(Z2, Z7)

    line_dict["8-1"] = Arc1(Z8, Z1, -abs(Z8), is_trigo_direction=False)

    if self.H2 == 0:
        line_dict["7w-2w"] = Arc1(Z7, Z2, -abs(Z7), is_trigo_direction=False)

    return line_dict
