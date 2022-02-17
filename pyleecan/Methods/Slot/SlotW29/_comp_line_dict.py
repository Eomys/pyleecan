from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

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
    Z12 = point_dict["Z12"]

    # Creation of curve
    line_dict = dict()
    if self.H0 > 0:
        line_dict["1-2"] = Segment(Z1, Z2)
    line_dict["1-2"] = Segment(Z2, Z3)
    if self.H1 > 0:
        line_dict["1-2"] = Segment(Z3, Z4)
    line_dict["1-2"] = Segment(Z4, Z5)
    line_dict["1-2"] = Segment(Z5, Z6)
    line_dict["1-2"] = Segment(Z6, Z7)
    line_dict["1-2"] = Segment(Z7, Z8)
    line_dict["1-2"] = Segment(Z8, Z9)
    if self.H1 > 0:
        line_dict["1-2"] = Segment(Z9, Z10)
    line_dict["1-2"] = Segment(Z10, Z11)
    if self.H0 > 0:
        line_dict["1-2"] = Segment(Z11, Z12)

    # Closing Arc (Rbo)
    line_dict["8-1"] = Arc1(Z8, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Closing Active part
    line_dict["3-6"] = Segment(Z3, Z6)
    line_dict["6-3"] = Segment(Z6, Z3)

    return line_dict