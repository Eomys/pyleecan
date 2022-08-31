from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

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
    Z11 = point_dict["Z11"]
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
    line_dict["1-2"] = Arc1(Z1, Z2, self.R1)
    line_dict["2-3"] = Segment(Z2, Z3)
    line_dict["3-4"] = Segment(Z3, Z4)
    line_dict["4-5"] = Segment(Z4, Z5)
    line_dict["5-6"] = Segment(Z5, Z6)
    line_dict["6-7"] = Segment(Z6, Z7)
    line_dict["7-8"] = Segment(Z7, Z8)
    line_dict["8-9"] = Segment(Z8, Z9)
    line_dict["9-10"] = Segment(Z9, Z10)
    line_dict["10-11"] = Arc1(Z10, Z11, self.R1)
    line_dict["11-1"] = Arc1(Z11, Z1, -self.get_Rbo(), is_trigo_direction=False)
    # Winding lines
    line_dict["w3-w4"] = Segment(Zw3, Zw4)
    line_dict["w4-w1"] = Segment(Zw4, Zw1)
    line_dict["w1-w2"] = Segment(Zw1, Zw2)
    line_dict["w2-w3"] = Segment(Zw2, Zw3)

    line_dict["w3s-w4s"] = Segment(Zw3s, Zw4s)
    line_dict["w4s-w1s"] = Segment(Zw4s, Zw1s)
    line_dict["w1s-w2s"] = Segment(Zw1s, Zw2s)
    line_dict["w2s-w3s"] = Segment(Zw2s, Zw3s)
    # For opening surface (first winding)
    line_dict["4-w1"] = Segment(Z4, Zw1)
    line_dict["w2-5"] = Segment(Zw2, Z5)
    line_dict["3-w4"] = Segment(Z3, Zw4)
    line_dict["w3-6"] = Segment(Zw3, Z6)
    line_dict["w1-w4"] = Segment(Zw1, Zw4)
    line_dict["w4-w3"] = Segment(Zw4, Zw3)
    line_dict["w3-w2"] = Segment(Zw3, Zw2)
    # For opening surface (first winding)
    line_dict["7-w2s"] = Segment(Z7, Zw2s)
    line_dict["w1s-8"] = Segment(Zw1s, Z8)
    line_dict["6-w3s"] = Segment(Z6, Zw3s)
    line_dict["w4s-9"] = Segment(Zw4s, Z9)
    return line_dict
