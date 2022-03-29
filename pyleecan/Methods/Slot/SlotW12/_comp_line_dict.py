from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    line_dict: dict
        Dictionnary of the slot lines (key: line name, value: line object)
    """

    if self.is_outwards():
        rot_sign = True
    else:  # inward slot
        rot_sign = False

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
    line_dict["1-2"] = Segment(Z1, Z2)

    if self.R1 > 0:  # R1=0 => Z2==Z3
        line_dict["2-3"] = Arc3(Z2, Z3, rot_sign)
    else:
        line_dict["2-3"] = None

    if self.H1 > 0:  # H1=0 => Z3==Z4
        line_dict["3-4"] = Segment(Z3, Z4)
    else:
        line_dict["3-4"] = None

    line_dict["4-5"] = Arc3(Z4, Z5, rot_sign)

    if self.H1 > 0:  # H1=0 => Z5==Z6
        line_dict["5-6"] = Segment(Z5, Z6)
    else:
        line_dict["5-6"] = None

    if self.R1 > 0:  # R1=0 => Z6==Z7
        line_dict["6-7"] = Arc3(Z6, Z7, rot_sign)
    else:
        line_dict["6-7"] = None

    line_dict["7-8"] = Segment(Z7, Z8)

    # Closing Arc
    line_dict["8-1"] = Arc1(Z8, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Closing Active part
    line_dict["3-6"] = Segment(Z3, Z6)
    line_dict["6-3"] = Segment(Z6, Z3)

    return line_dict
