# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.comp_total_length
Computation of the Lamination length (including radial ventilations duct) Methods
@date Created on Mon Jan 19 15:23:43 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_length(self):
    """Compure the total length of the Lamination (including radial
    ventilations duct)

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Lt: float
        Total Lenght of the Lamination [m]

    """
    if self.Nrvd is None or self.Wrvd is None:
        return self.L1
    else:
        return self.L1 + self.Nrvd * self.Wrvd
