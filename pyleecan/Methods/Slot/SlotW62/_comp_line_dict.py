from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW62
        A SlotW62 object

    Returns
    -------
    line_dict: dict
        Dictionnary of the slot lines (key: line name, value: line object)
    """

    Rbo = self.get_Rbo()
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
    Zw3 = point_dict["Zw3"]
    Zw4 = point_dict["Zw4"]

    Zw1s = point_dict["Zw1s"]
    Zw2s = point_dict["Zw2s"]
    Zw3s = point_dict["Zw3s"]
    Zw4s = point_dict["Zw4s"]

    # Creation of curve
    line_dict = dict()
    line_dict["1-2"] = Segment(Z1, Z2)
    if Z2 != Z3:
        line_dict["2-3"] = Segment(Z2, Z3)
    else:
        line_dict["2-3"] = None
    line_dict["3-4"] = Segment(Z3, Z4)
    line_dict["4-5"] = Arc1(Z4, Z5, abs(Z4))
    line_dict["5-6"] = Segment(Z5, Z6)
    if Z6 != Z7:
        line_dict["6-7"] = Segment(Z6, Z7)
    else:
        line_dict["6-7"] = None

    line_dict["7-8"] = Segment(Z7, Z8)
    line_dict["8-1"] = Arc1(Z8, Z1, -Rbo, is_trigo_direction=False)

    # Winding lines
    line_dict["w3-w4"] = Segment(Zw3, Zw4)
    line_dict["w4-w1"] = Segment(Zw4, Zw1)
    line_dict["w1-w2"] = Segment(Zw1, Zw2)
    line_dict["w2-w3"] = Segment(Zw2, Zw3)

    line_dict["w3s-w4s"] = Segment(Zw3s, Zw4s)
    line_dict["w4s-w1s"] = Segment(Zw4s, Zw1s)
    line_dict["w1s-w2s"] = Segment(Zw1s, Zw2s)
    line_dict["w2s-w3s"] = Segment(Zw2s, Zw3s)

    return line_dict
