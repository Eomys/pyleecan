from ....Classes.Segment import Segment
from ....Classes.Segment import Arc1
from ....Classes.Segment import Arc3


def _comp_line_list(self):
    """Define a list of the lines to draw the slot (bore to bore + closing arc)
    If a line has begin=end, it is replaced by "None" (list has always the same length)

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    line_list: list
        Ordered list of lines to draw the slot
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

    if self.is_outwards():
        rot_sign = 1  # Rotation direction for Arc1
    else:  # inward slot
        rot_sign = -1  # Rotation direction for Arc1

    # Creation of curve
    line_list = list()
    if self.H0 > 0:
        line_list.append(Segment(Z1, Z2))
    else:
        line_list.append(None)

    line_list.append(Segment(Z2, Z3))
    line_list.append(Segment(Z3, Z4))

    if self.R1 * 2 < self.W2:
        line_list.append(
            Arc1(Z4, Z5, rot_sign * self.R1, is_trigo_direction=self.is_outwards())
        )
        line_list.append(Segment(Z5, Z6))
        line_list.append(
            Arc1(Z6, Z7, rot_sign * self.R1, is_trigo_direction=self.is_outwards())
        )
    else:
        line_list.append(None)
        line_list.append(Arc3(Z4, Z7, self.is_outwards()))
        line_list.append(None)

    line_list.append(Segment(Z7, Z8))
    line_list.append(Segment(Z8, Z9))

    if self.H0 > 0:
        line_list.append(Segment(Z9, Z10))
    else:
        line_list.append(None)

    # Closing Arc
    Rbo = self.get_Rbo()
    Zbegin = line_list[-1].get_end()
    Zend = line_list[0].get_begin()
    line_list.append(Arc1(Zbegin, Zend, -Rbo, is_trigo_direction=False))

    return line_list
