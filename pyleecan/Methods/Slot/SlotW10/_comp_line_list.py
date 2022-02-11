from ....Classes.Segment import Segment
from ....Classes.Segment import Arc1


def _comp_line_list(self):
    """Define a list of the lines to draw the slot (bore to bore + closing arc)
    If a line has begin==end, it is replaced by "None" (list has always the same length)

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

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

    # Creation of curve
    line_list = list()
    if self.H0 > 0:
        line_list.append(Segment(Z1, Z2))
    else:
        line_list.append(None)

    if self.H1 > 0 and self.W1 > self.W0:
        line_list.append(Segment(Z2, Z3))
    else:
        line_list.append(None)

    if self.W1 > self.W0:
        line_list.append(Segment(Z3, Z4))
    else:
        line_list.append(None)

    line_list.append(Segment(Z4, Z5))

    if self.W2 > 0:
        line_list.append(Segment(Z5, Z6))
    else:
        line_list.append(None)

    line_list.append(Segment(Z6, Z7))

    if self.W1 > self.W0:
        line_list.append(Segment(Z7, Z8))
    else:
        line_list.append(None)

    if self.H1 > 0 and self.W1 > self.W0:
        line_list.append(Segment(Z8, Z9))
    else:
        line_list.append(None)

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
