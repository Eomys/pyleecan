# -*-- coding: utf-8 -*
from numpy import angle, exp

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def get_lines(self):
    """return the list of lines that delimits the PolarArc

    Parameters
    ----------
    self : PolarArc
        a PolarArc object

    Returns
    -------
    line_list: list
        List of line need to draw the slot (2 Segment + 2 Arc1)
    """
    # check if the PolarArc is correct
    self.check()

    Z_ref = self.point_ref
    center = Z_ref * exp(-1j * angle(Z_ref))
    H = self.height
    A = self.angle
    # the points of the PolarArc
    Z2 = (center - (H / 2)) * exp(1j * (-(A / 2))) * exp(1j * angle(Z_ref))
    Z3 = (center + (H / 2)) * exp(1j * (-(A / 2))) * exp(1j * angle(Z_ref))
    Z4 = (center + (H / 2)) * exp(1j * (A / 2)) * exp(1j * angle(Z_ref))
    Z1 = (center - (H / 2)) * exp(1j * (A / 2)) * exp(1j * angle(Z_ref))

    # Lines that delimit the PolarArc
    line1 = Arc1(Z1, Z2, -abs(Z1))
    line2 = Segment(Z2, Z3)
    line3 = Arc1(Z3, Z4, abs(Z3))
    line4 = Segment(Z4, Z1)

    return [line1, line2, line3, line4]
