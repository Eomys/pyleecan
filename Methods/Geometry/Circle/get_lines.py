# -*- coding: utf-8 -*-
from pyleecan.Classes.Arc3 import Arc3


def get_lines(self):
    """Get the lines needed to draw the surface (2 Arc3)

    Parameters
    ----------
    self : Circle
        A circle Object

    Returns
    -------
    line_list: list
        Two arcs to draw the circle

    """
    # check if the circle is correct
    self.check()
    begin = self.center + self.radius
    end = self.center - self.radius
    # first half-circle
    line1 = Arc3(begin, end, True, label=self.line_label)
    # second half-circle
    line2 = Arc3(end, begin, True, label=self.line_label)
    return [line1, line2]
