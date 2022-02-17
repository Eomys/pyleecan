from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

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

    if self.is_outwards():
        rot_sign = 1  # Rotation direction for Arc1
    else:  # inward slot
        rot_sign = -1  # Rotation direction for Arc1

    # Creation of curve
    line_dict = dict()
    line_dict["1-2"] = Segment(Z1, Z2)
    if self.H1 > 0:
        line_dict["1-2"] = Arc1(
            Z2, Z3, rot_sign * self.R1, is_trigo_direction=self.is_outwards()
        )
        line_dict["1-2"] = Segment(Z3, Z4)
        line_dict["1-2"] = Arc3(Z4, Z5, self.is_outwards())
        line_dict["1-2"] = Segment(Z5, Z6)
        line_dict["1-2"] = Arc1(
            Z6, Z7, rot_sign * self.R1, is_trigo_direction=self.is_outwards()
        )
    elif self.H1 == 0:
        line_dict["1-2"] = Arc1(
            Z2, Z3, rot_sign * self.R1, is_trigo_direction=self.is_outwards()
        )
        line_dict["1-2"] = Arc3(Z3, Z6, self.is_outwards())
        line_dict["1-2"] = Arc1(
            Z6, Z7, rot_sign * self.R1, is_trigo_direction=self.is_outwards()
        )
    else:  # Should never be called
        raise Slot26_H1(Slot26_H1, "H1 can't be <0")

    line_dict["1-2"] = Segment(Z7, Z8)

    # Closing Arc (Rbo)
    line_dict["8-1"] = Arc1(Z8, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Closing Active part
    line_dict["3-6"] = Segment(Z3, Z6)
    line_dict["6-3"] = Segment(Z6, Z3)

    return line_dict