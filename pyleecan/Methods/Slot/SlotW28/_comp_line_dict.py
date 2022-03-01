from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    line_dict: dict
        Dictionnary of the slot lines (key: line name, value: line object)
    """

    if self.is_outwards():
        rot_sign = 1  # Rotation direction for Arc1
    else:  # inward slot
        rot_sign = -1  # Rotation direction for Arc1
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
    line_dict["2-3"] = Arc1(Z2, Z3, rot_sign * self.R1, self.is_outwards())
    line_dict["3-4"] = Segment(Z3, Z4)
    line_dict["4-5"] = Arc3(Z4, Z5, self.is_outwards())
    line_dict["5-6"] = Segment(Z5, Z6)
    line_dict["6-7"] = Arc1(Z6, Z7, rot_sign * self.R1, self.is_outwards())
    if self.H0 > 0:
        line_dict["7-8"] = Segment(Z7, Z8)
    else:
        line_dict["7-8"] = None

    # Closing Arc (Rbo)
    line_dict["8-1"] = Arc1(Z8, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Closing Active part
    line_dict["2-7"] = Segment(Z2, Z7)
    line_dict["7-2"] = Segment(Z7, Z2)

    return line_dict
