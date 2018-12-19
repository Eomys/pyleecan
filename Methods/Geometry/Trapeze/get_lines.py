# -*-- coding: utf-8 -*
from numpy import angle, exp

from pyleecan.Classes.Segment import Segment


def get_lines(self):
    """Returns the Lines that delimit the Trapeze

    Parameters
    ----------
    self : Trapeze
        a Trapeze object


    Returns
    -------
    line_list : list
        list of 4 segments

    """
    # Check if the Trapeze is correct
    self.check()
    Z_ref = self.point_ref
    H = self.height
    W1 = self.W1
    W2 = self.W2

    # The 4 points of the Trapeze object
    Z1 = (complex(-H / 2, W1 / 2) * exp(1j * (angle(Z_ref)))) + Z_ref
    Z2 = (complex(-H / 2, -W1 / 2) * exp(1j * (angle(Z_ref)))) + Z_ref
    Z3 = (complex(H / 2, -W2 / 2) * exp(1j * (angle(Z_ref)))) + Z_ref
    Z4 = (complex(H / 2, W2 / 2) * exp(1j * (angle(Z_ref)))) + Z_ref

    # The lines that delimit the Trapeze
    line1 = Segment(Z1, Z2)
    line2 = Segment(Z2, Z3)
    line3 = Segment(Z3, Z4)
    line4 = Segment(Z4, Z1)

    return [line1, line2, line3, line4]
